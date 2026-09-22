#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
package_finished_books.py — 全自动打包已完成翻译的书籍为标准双语 EPUB。

特性：
1. 质量门禁：仅对已完成翻译（todo==0, doing==0, total>0）的书目打包；
2. 防乱序机制：严格遵循 translation_queue.csv 行物理顺序合并章节；
3. 元数据抽取：智能提取中文书名与作者信息，生成规范的 <中文书名>.epub；
4. 排版样式：注入双语对照样式（中文译文淡黄底色高亮容器），字体自适应；
5. 多进程并发：支持多核并发打包，海量书目极速完成。
"""
import argparse
import concurrent.futures
import csv
import os
import re
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECTS_DIR = os.path.join(ROOT, "翻译项目")

manual_zh_titles = {
    "alexander-mackenzie_journals": "亚历山大·麦肯齐探险日志",
    "anthony-trollope_short-fiction": "安东尼·特罗洛普短篇小说集",
    "calvin-coolidge_the-autobiography-of-calvin-coolidge": "柯立芝自传",
    "edward-whymper_scrambles-amongst-the-alps-in-the-years-1860-69": "阿尔卑斯攀登记",
    "frederik-pohl_short-fiction": "弗雷德里克·波尔短篇小说集",
    "geronimo_geronimos-story-of-his-life": "杰罗尼莫自述生平",
    "manly-wade-wellman_short-fiction": "曼利·韦德·威尔曼短篇小说集",
}

# 标记格式：独占一行的 ===Original=== 或 ===Chinese===
_MARKER_RE = re.compile(r"^={3,}\s*(original|chinese)\s*={0,}\s*$", re.IGNORECASE)
_HEADING_RE = re.compile(r"^#{1,6}\s")

EPUB_CSS = """
/* 译文：淡黄色背景 + 左边竖线，字体一律阅读器默认 */
div.translation {
    background-color: #FFF8DC;
    border-left: 3px solid #E0C36A;
    padding: 0.6em 0.9em;
    margin: 0.6em 0;
    page-break-inside: avoid;
}
pre, code { font-family: monospace; }
"""


def process_markdown(md_text):
    """将 ===Original=== / ===Chinese=== 块转换为 Pandoc 围栏 div"""
    out = []
    buf = []
    cur_type = None

    def flush():
        nonlocal buf, cur_type
        content = "\n".join(buf).strip()
        if content:
            if cur_type == "chinese":
                out.append("::: {.translation}")
                out.append("")
                out.append(content)
                out.append("")
                out.append(":::")
                out.append("")
            else:
                out.append(content)
                out.append("")
        buf = []
        cur_type = None

    for line in md_text.split("\n"):
        m = _MARKER_RE.match(line)
        if m:
            flush()
            cur_type = m.group(1).lower()
            continue
        if _HEADING_RE.match(line):
            flush()
            cur_type = None
        buf.append(line)
    flush()
    return "\n".join(out)


def extract_metadata(pname, pdir):
    """提取书目中文名称与作者"""
    orig_epub_dir = os.path.join(pdir, "原书")
    raw_epubs = (
        [f for f in os.listdir(orig_epub_dir) if f.endswith(".epub")]
        if os.path.exists(orig_epub_dir)
        else []
    )
    raw_title, raw_author = "", ""
    if raw_epubs:
        try:
            with zipfile.ZipFile(os.path.join(orig_epub_dir, raw_epubs[0])) as z:
                opf = [n for n in z.namelist() if n.endswith(".opf")][0]
                tree = ET.fromstring(z.read(opf))
                ns = {"dc": "http://purl.org/dc/elements/1.1/"}
                t_node = tree.find(".//dc:title", ns)
                c_node = tree.find(".//dc:creator", ns)
                if t_node is not None and t_node.text:
                    raw_title = t_node.text.strip()
                if c_node is not None and c_node.text:
                    raw_author = c_node.text.strip()
        except Exception:
            pass

    zh_title = manual_zh_titles.get(pname, "")
    rev_path = os.path.join(pdir, "审核报告.md")
    if not zh_title and os.path.exists(rev_path):
        try:
            with open(rev_path, "r", encoding="utf-8") as f:
                for line in f:
                    m = re.search(r"#\s*审[核校]报告[：:]\s*《([^》]+)》", line)
                    if m:
                        zh_title = m.group(1).strip()
                        break
        except Exception:
            pass

    pm_path = os.path.join(pdir, "项目说明.md")
    author = raw_author
    if os.path.exists(pm_path):
        try:
            with open(pm_path, "r", encoding="utf-8") as f:
                pm_txt = f.read()
            if not zh_title:
                m = re.search(r"#\s*项目说明[：:]\s*《([^》]+)》", pm_txt)
                if m:
                    zh_title = m.group(1).strip()
            if not zh_title:
                m = re.search(r"#\s*项目说明[（\(]([^）\)]+)[）\)]", pm_txt)
                if m:
                    zh_title = m.group(1).strip()
            if not zh_title:
                m = re.search(r"-\s*\*\*项目名称\*\*：.*?《([^》]+)》", pm_txt)
                if m:
                    zh_title = m.group(1).strip()
            if not zh_title:
                m = re.search(r"《([^》\n]{2,30})》", pm_txt[:400])
                if m:
                    zh_title = m.group(1).strip()

            if not author:
                m_a = re.search(r"-\s*\*\*(?:原作者|作者)\*\*：([^\n]+)", pm_txt)
                if m_a:
                    author = m_a.group(1).strip()
        except Exception:
            pass

    if not zh_title:
        zh_title = raw_title or pname

    if not author:
        author = pname.split("_")[0].replace("-", " ").title()

    clean_filename = re.sub(r'[\\/*?:"<>|]', "", zh_title).strip()
    if not clean_filename or clean_filename in (".", ".."):
        clean_filename = pname

    return {
        "title": zh_title,
        "author": author,
        "filename": f"{clean_filename}.epub",
    }


def assemble_chapters(pname, pdir):
    """按照 translation_queue.csv 行物理顺序合并所有章节译文"""
    csv_path = os.path.join(pdir, "translation_queue.csv")
    if not os.path.exists(csv_path):
        return None, "未找到 translation_queue.csv"

    rows = []
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            rows.append(r)

    if not rows:
        return None, "translation_queue.csv 为空"

    # 门禁检查：所有行必须均为 done
    not_done = [r["file"] for r in rows if r.get("status") != "done"]
    if not_done:
        return None, f"存在未完成章节 ({len(not_done)} 篇未 done)"

    chapters_content = []
    for r in rows:
        f_orig = r.get("file", "").strip()
        stem = os.path.splitext(f_orig)[0]

        cand1 = os.path.join(pdir, "译文", f"{stem}.zh-CN.md")
        cand2 = os.path.join(pdir, "译文", f"{f_orig}.zh-CN.md")
        cand3 = os.path.join(pdir, "译文", f_orig)

        chosen = None
        for c in (cand1, cand2, cand3):
            if os.path.isfile(c):
                chosen = c
                break

        if chosen:
            with open(chosen, "r", encoding="utf-8") as f:
                content = f.read().strip()
                if content:
                    chapters_content.append(content)
        else:
            # 容错：个别分片仅为卷名或题献，原分章可能直接放在原文目录
            orig_file = os.path.join(pdir, "原文", f_orig)
            if os.path.isfile(orig_file):
                with open(orig_file, "r", encoding="utf-8") as f:
                    content = f.read().strip()
                    if content:
                        chapters_content.append(content)

    if not chapters_content:
        return None, "未能收集到任何章节内容"

    all_md = "\n\n".join(chapters_content)
    return all_md, None


def package_project(pname, force=False):
    """打包单个项目为 EPUB"""
    pdir = os.path.join(PROJECTS_DIR, pname)
    if not os.path.isdir(pdir):
        return False, pname, "目录不存在"

    # 检查是否已存在 EPUB
    existing_epubs = [f for f in os.listdir(pdir) if f.endswith(".epub")]
    if existing_epubs and not force:
        return True, pname, f"已存在 EPUB: {existing_epubs[0]} (跳过)"

    meta = extract_metadata(pname, pdir)
    all_md, err = assemble_chapters(pname, pdir)
    if err:
        return False, pname, err

    # 写入合并全量文件 翻译项目/<项目名>/译文/<项目名>.all.zh-CN.md
    trans_dir = os.path.join(pdir, "译文")
    os.makedirs(trans_dir, exist_ok=True)
    all_md_path = os.path.join(trans_dir, f"{pname}.all.zh-CN.md")
    with open(all_md_path, "w", encoding="utf-8") as f:
        f.write(all_md)

    processed_md = process_markdown(all_md)
    out_epub = os.path.join(pdir, meta["filename"])

    with tempfile.TemporaryDirectory() as tmp:
        css_path = os.path.join(tmp, "style.css")
        with open(css_path, "w", encoding="utf-8") as f:
            f.write(EPUB_CSS)

        cmd = [
            "pandoc",
            "-f",
            "markdown+pipe_tables+backtick_code_blocks+fenced_code_blocks-yaml_metadata_block",
            "-t",
            "epub3",
            "--standalone",
            "--toc",
            "--css",
            css_path,
            "--metadata",
            f"title={meta['title']}",
            "--metadata",
            f"author={meta['author']}",
            "--metadata",
            "lang=zh-CN",
            "-o",
            out_epub,
        ]

        res = subprocess.run(
            cmd, input=processed_md, capture_output=True, text=True
        )
        if res.returncode != 0:
            return False, pname, f"Pandoc 编译错误: {res.stderr[:200]}"

    if not os.path.isfile(out_epub) or not zipfile.is_zipfile(out_epub):
        return False, pname, "生成的 EPUB 文件损坏或不存在"

    size_kb = os.path.getsize(out_epub) / 1024
    return True, pname, f"打包成功: 《{meta['title']}》 -> {meta['filename']} ({size_kb:.1f}KB)"


def get_finished_projects():
    """扫描所有翻译完成且已准备好打包的项目"""
    candidates = []
    for pname in sorted(os.listdir(PROJECTS_DIR)):
        pdir = os.path.join(PROJECTS_DIR, pname)
        if not os.path.isdir(pdir):
            continue
        csv_path = os.path.join(pdir, "translation_queue.csv")
        if not os.path.exists(csv_path):
            continue
        try:
            with open(csv_path, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                rows = list(reader)
            if rows and all(r.get("status") == "done" for r in rows):
                candidates.append(pname)
        except Exception:
            continue
    return candidates


def main():
    parser = argparse.ArgumentParser(
        description="全自动打包已完成翻译的书籍为标准双语 EPUB"
    )
    parser.add_argument("--project", help="指定打包的单个项目名称")
    parser.add_argument("--all-finished", action="store_true", help="打包所有已翻译完成的书籍")
    parser.add_argument("--force", action="store_true", help="强制重新打包已存在 EPUB 的项目")
    parser.add_argument(
        "--workers",
        type=int,
        default=min(8, os.cpu_count() or 4),
        help="并发打包进程数 (默认: CPU 核心数或 8)",
    )

    args = parser.parse_args()

    # 校验 pandoc 是否已安装
    try:
        subprocess.run(["pandoc", "--version"], capture_output=True, check=True)
    except Exception:
        print("❌ 错误: 系统未安装 pandoc，无法编译 EPUB！", file=sys.stderr)
        sys.exit(1)

    if args.project:
        ok, pname, msg = package_project(args.project, force=args.force)
        if ok:
            print(f"✅ {pname}: {msg}")
        else:
            print(f"❌ {pname}: {msg}", file=sys.stderr)
            sys.exit(1)
        return

    if args.all_finished:
        finished = get_finished_projects()
        print(f"🔍 扫描到已 100% 翻译完成的项目共 {len(finished)} 部")

        to_build = []
        for pname in finished:
            pdir = os.path.join(PROJECTS_DIR, pname)
            has_epub = any(f.endswith(".epub") for f in os.listdir(pdir))
            if not has_epub or args.force:
                to_build.append(pname)

        print(f"📦 其中待打包项目共 {len(to_build)} 部 (已跳过 {len(finished) - len(to_build)} 部已有产物)")
        if not to_build:
            print("🎉 所有已完成书籍均已打包完成，无需操作。")
            return

        success_cnt = 0
        fail_cnt = 0

        with concurrent.futures.ProcessPoolExecutor(max_workers=args.workers) as executor:
            future_to_proj = {
                executor.submit(package_project, pname, args.force): pname
                for pname in to_build
            }

            total = len(to_build)
            done_idx = 0
            for future in concurrent.futures.as_completed(future_to_proj):
                done_idx += 1
                ok, pname, msg = future.result()
                if ok:
                    success_cnt += 1
                    print(f"[{done_idx}/{total}] ✅ {msg}")
                else:
                    fail_cnt += 1
                    print(f"[{done_idx}/{total}] ❌ {pname}: {msg}", file=sys.stderr)

        print("\n" + "=" * 50)
        print(f"📊 打包完成统计: 成功 {success_cnt} 部，失败 {fail_cnt} 部。")
        print("=" * 50)
        if fail_cnt > 0:
            sys.exit(1)
        return

    parser.print_help()


if __name__ == "__main__":
    main()
