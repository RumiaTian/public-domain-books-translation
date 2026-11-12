#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/translate_chapter_genai.py — 单章节单次调用 Gemini API 翻译驱动脚本
适配《世界骗术》(p-t-barnum_the-humbugs-of-the-world) 及同类公版书项目。

特性：
1. 块对照切片（<=2400字符/块，段落/句子边界兜底，与 translate_mcp 严格一致）
2. 动态精准术语提取（从项目的术语表.md匹配本章命中的词条）
3. 单次请求完整章节长输出（纯中文块 [TRANS_01]..[N]，节省50% Token）
4. 本地自动化拼装与 check_bilingual.py 闭环校验
5. 自动维护 translation_queue.csv 状态
"""

import argparse
import csv
import json
import os
import re
import subprocess
import sys
import time

try:
    from google import genai
    from google.genai import types
except ImportError:
    # 尝试在备用 venv 中重试导入
    sys.stderr.write("提示: 请使用安装了 google-genai 的 python 环境运行本脚本 (如 ~/.venvs/gemini/bin/python)\n")
    sys.exit(1)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJ_DIR = os.path.join(ROOT, "翻译项目")
CHECKER = os.path.join(ROOT, "scripts", "check_bilingual.py")

MAX_BLOCK_CHARS = 2400
_HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")
_SENT_RE = re.compile(r"[^.!?。！？…]*[.!?。！？…]+[”’)」』]*", re.S)


def shatter(text):
    if len(text) <= MAX_BLOCK_CHARS:
        return [text]
    sents, last = [], 0
    for m in _SENT_RE.finditer(text):
        sents.append(text[last:m.end()])
        last = m.end()
    if last < len(text):
        sents.append(text[last:])
    pieces, cur = [], ""
    for s in sents:
        if len(s) > MAX_BLOCK_CHARS:
            if cur:
                pieces.append(cur)
                cur = ""
            for j in range(0, len(s), MAX_BLOCK_CHARS):
                pieces.append(s[j:j + MAX_BLOCK_CHARS])
            continue
        if cur and len(cur) + len(s) > MAX_BLOCK_CHARS:
            pieces.append(cur)
            cur = s
        else:
            cur += s
    if cur:
        pieces.append(cur)
    return pieces


def split_blocks(src_text):
    lines = src_text.split("\n")
    blocks = []
    cur_paras = []
    cur_len = 0
    cur_heading = None

    def close():
        nonlocal cur_paras, cur_len, cur_heading
        body = "\n\n".join(cur_paras).strip()
        if cur_heading or body:
            blocks.append({"heading": cur_heading, "text": body})
        cur_paras, cur_len, cur_heading = [], 0, None

    para = []

    def flush_para():
        nonlocal para, cur_len
        text = "\n".join(para).strip()
        para = []
        if not text:
            return
        for piece in shatter(text):
            add_len = len(piece) + 2
            if cur_paras and cur_len + add_len > MAX_BLOCK_CHARS:
                close()
            cur_paras.append(piece)
            cur_len += add_len

    for line in lines:
        m = _HEADING_RE.match(line)
        if m:
            flush_para()
            if cur_paras or cur_heading:
                close()
            cur_heading = line.rstrip()
            continue
        if not line.strip():
            flush_para()
            continue
        para.append(line.rstrip())
    flush_para()
    close()
    for i, b in enumerate(blocks, 1):
        b["i"] = i
    return blocks


def parse_glossary(glossary_path, src_text):
    if not os.path.isfile(glossary_path):
        return []
    terms = []
    in_fixed_terms = False
    with open(glossary_path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            line = line.strip()
            if line.startswith("## 定名术语"):
                in_fixed_terms = True
                continue
            elif line.startswith("## ") and in_fixed_terms:
                in_fixed_terms = False
                continue

            if not in_fixed_terms:
                continue

            if not line.startswith("|") or line.count("|") < 2:
                continue
            cells = [c.strip() for c in line.strip("|").split("|")]
            src = cells[0].strip("`*- ")
            tgt = cells[1].strip("`*- ") if len(cells) > 1 else ""
            if not src or len(src) < 2 or set(src) <= set("-— "):
                continue
            if src in ("原文", "---", "源词") or tgt in ("译法", "---"):
                continue
            # 单词边界或子串匹配
            pattern = r"\b" + re.escape(src) + r"\b" if re.search(r"^\w+$", src) else re.escape(src)
            if re.search(pattern, src_text, re.IGNORECASE):
                terms.append((src, tgt))
    return terms


def get_project_metadata(pdir):
    desc_path = os.path.join(pdir, "项目说明.md")
    title = os.path.basename(pdir)
    desc = ""
    domain_guide = "- 目标语言：忠实、典雅、流畅的现代中文；句式自然拆分，消除机器翻译腔。\n- 遵循学术规范与文学通行译名。"
    if os.path.isfile(desc_path):
        with open(desc_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
        for line in content.splitlines():
            if line.startswith("# 项目说明："):
                title = line.replace("# 项目说明：", "").strip("《》 \t")
                break
            elif line.startswith("# "):
                title = line.lstrip("# \t")
                break
        m_desc = re.search(r"^>\s*(.+)$", content, re.MULTILINE)
        if m_desc:
            desc = m_desc.group(1).strip()
        m_dom = re.search(r"prompts/(\S+?\.md)", content)
        if m_dom:
            dom_file = os.path.join(ROOT, "prompts", m_dom.group(1))
            if os.path.isfile(dom_file):
                with open(dom_file, "r", encoding="utf-8", errors="ignore") as df:
                    d_lines = [l.strip() for l in df.read().splitlines() if l.strip() and not l.startswith("#")]
                    if d_lines:
                        domain_guide = "\n".join(d_lines[:15])
    return title, desc, domain_guide


def build_prompt(book_title, book_desc, domain_guide, fname, blocks, matched_terms, prev_tail=""):
    total_blocks = len(blocks)
    terms_md = ""
    if matched_terms:
        terms_lines = ["| 英文源词 | 强制中文定名 |", "|---|---|"]
        for s, t in matched_terms:
            terms_lines.append(f"| {s} | {t} |")
        terms_md = "\n".join(terms_lines)
    else:
        terms_md = "无特定术语约束，保持通用学术/文学严肃定名。"

    prev_context_block = ""
    if prev_tail:
        prev_context_block = f"""
## 前章结尾参考（仅供语流与口吻衔接，绝对切勿翻译此段）：
\"\"\"
{prev_tail}
\"\"\"
"""

    blocks_payload = []
    for b in blocks:
        i = b["i"]
        h = b["heading"]
        t = b["text"]
        tag = f"[BLOCK_{i:02d}:HEADING]" if h else f"[BLOCK_{i:02d}]"
        content_parts = []
        if h:
            content_parts.append(h)
        if t:
            content_parts.append(t)
        blocks_payload.append(f"{tag}\n" + "\n\n".join(content_parts))

    blocks_str = "\n\n".join(blocks_payload)

    prompt = f"""你是一位精通英语文学与学术文献的顶级翻译专家。你正在翻译著作《{book_title}》。
【作品背景】：{book_desc}
当前章节文件：`{fname}`。

# 文风与领域规范
{domain_guide}

{prev_context_block}

# 强制术语表（本章命中）
{terms_md}

# 核心输出契约（必须 100% 严格遵守，违反判定为任务失败）：
1. **纯净译文输出**：
   - 严禁在输出中重复英文原文！不要输出任何寒暄、前言或总结说明。
2. **块级 1:1 严格对齐**：
   - 本章共有【{total_blocks}】个块，编号从 `[BLOCK_01]` 至 `[BLOCK_{total_blocks:02d}]`。
   - 你的输出必须依次包含从 `[TRANS_01]` 到 `[TRANS_{total_blocks:02d}]` 的每一个块。
   - 每个块以 `[TRANS_XX]` 独占一行开始，其后紧接该块的纯中文译文。
3. **标题块格式**：
   - 若块标有 `:HEADING`，第一行输出对应的纯中文标题（不要加 `#`，也不要带英文）。
   - 若该块标题下方还包含正文内容，请务必在第一行标题后另起新行，完整翻译并输出该块的所有正文内容，绝不可遗漏正文！
4. **数字与事实锚点**：
   - 原文中的所有阿拉伯数字、时间、金额、年份、度量衡必须准确对应，不增不减。
5. **严禁省略**：
   - 绝对不可使用“……”“（中间略）”等方式跳过任何段落。

---

# 输入待译内容（共 {total_blocks} 块）：

{blocks_str}
"""
    return prompt


def parse_model_response(resp_text, total_blocks):
    # 提取 [TRANS_01] 或 [TRANS_1] 格式
    pattern = re.compile(r"^\[TRANS_(\d+)\]\s*$", re.MULTILINE)
    matches = list(pattern.finditer(resp_text))
    if not matches:
        # 兼容不带括号的情况
        pattern = re.compile(r"^TRANS_(\d+)[:：]?\s*$", re.MULTILINE)
        matches = list(pattern.finditer(resp_text))

    if not matches:
        return None, "模型回复未找到任何 [TRANS_XX] 块标记"

    trans_map = {}
    for idx, m in enumerate(matches):
        block_num = int(m.group(1))
        start_pos = m.end()
        end_pos = matches[idx + 1].start() if idx + 1 < len(matches) else len(resp_text)
        block_text = resp_text[start_pos:end_pos].strip()
        trans_map[block_num] = block_text

    missing = [i for i in range(1, total_blocks + 1) if i not in trans_map]
    if missing:
        return None, f"块编号缺失，缺少以下块: {missing}"

    return trans_map, "OK"


def assemble_bilingual(blocks, trans_map):
    out = []
    for b in blocks:
        i = b["i"]
        h = b["heading"]
        t = b["text"]
        zh = trans_map.get(i, "").strip()

        if h:
            # 标题处理：如果 trans 有多行，第一行视为标题中文
            zh_lines = [l.strip() for l in zh.split("\n") if l.strip()]
            zh_title = zh_lines[0].lstrip("#").strip() if zh_lines else ""
            zh_body = "\n\n".join(zh_lines[1:]).strip() if len(zh_lines) > 1 else ""
            out.append(f"{h} / {zh_title}")
            if t or zh_body:
                if t and not zh_body:
                    zh_body = zh_title
                out.append(f"===Original===\n\n{t}\n\n===Chinese===\n\n{zh_body}")
        else:
            out.append(f"===Original===\n\n{t}\n\n===Chinese===\n\n{zh}")

    return "\n\n".join(out).strip() + "\n"


def run_checker(zh_path):
    cmd = [sys.executable, CHECKER, zh_path]
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    out = (r.stdout or "") + (r.stderr or "")
    struct_ok = ("标记成对: 满足" in out) and ("标题合并格式: 满足" in out)
    return struct_ok, out


def update_queue_status(pdir, fname, status):
    q_path = os.path.join(pdir, "translation_queue.csv")
    if not os.path.isfile(q_path):
        return
    rows = []
    with open(q_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)
    updated = False
    for r in rows:
        if r and r[0].strip() == fname:
            r[2] = status
            updated = True
            break
    if updated:
        tmp = q_path + ".tmp"
        with open(tmp, "w", encoding="utf-8", newline="\n") as f:
            csv.writer(f).writerows(rows)
        os.replace(tmp, q_path)


def translate_chapter(project_name, fname, client, model="gemini-3.8-flash", dry_run=False):
    pdir = os.path.join(PROJ_DIR, project_name)
    src_file = os.path.join(pdir, "原文", fname)
    if not os.path.isfile(src_file):
        print(f"[-] 原文文件不存在: {src_file}")
        return False

    with open(src_file, "r", encoding="utf-8", errors="ignore") as f:
        src_text = f.read()

    blocks = split_blocks(src_text)
    if not blocks:
        print(f"[-] 文件内容为空: {fname}")
        return False

    # 提取术语
    glossary_path = os.path.join(pdir, "术语表.md")
    matched_terms = parse_glossary(glossary_path, src_text)

    # 提取前章末尾
    stem = fname[:-3] if fname.endswith(".md") else fname
    prev_tail = ""
    # 查找上一篇 done 的译文末尾
    q_path = os.path.join(pdir, "translation_queue.csv")
    if os.path.isfile(q_path):
        with open(q_path, "r", encoding="utf-8") as f:
            q_rows = list(csv.DictReader(f))
        for idx, row in enumerate(q_rows):
            if row.get("file") == fname and idx > 0:
                prev_file = q_rows[idx - 1].get("file")
                prev_stem = prev_file[:-3] if prev_file.endswith(".md") else prev_file
                prev_zh = os.path.join(pdir, "译文", f"{prev_stem}.zh-CN.md")
                if os.path.isfile(prev_zh):
                    with open(prev_zh, "r", encoding="utf-8", errors="ignore") as pf:
                        p_content = pf.read().strip()
                        prev_tail = p_content[-500:]
                break

    title, desc, domain_guide = get_project_metadata(pdir)
    prompt = build_prompt(title, desc, domain_guide, fname, blocks, matched_terms, prev_tail)

    if dry_run:
        print(f"[DRY-RUN] 章节: {fname} | 块数: {len(blocks)} | 命中术语: {len(matched_terms)}")
        print("Prompt 预览 (前 800 字符):")
        print(prompt[:800])
        return True

    print(f"[*] 开始翻译 {fname} (共 {len(blocks)} 块, 命中 {len(matched_terms)} 术语)...")
    response = None
    elapsed = 0.0
    for attempt in range(2):
        t0 = time.time()
        try:
            response = client.models.generate_content(
                model=model,
                contents=prompt,
            )
            elapsed = time.time() - t0
            break
        except Exception as e:
            print(f"[-] 第 {attempt+1} 次 API 调用异常: {e}")
            if attempt == 0:
                print("[*] 等待 2 秒后进行第 2 次重试...")
                time.sleep(2)
            else:
                return False
    resp_text = response.text or ""
    print(f"[+] API 回复耗时: {elapsed:.1f}s, 输出长度: {len(resp_text)} 字符")

    trans_map, err = parse_model_response(resp_text, len(blocks))
    if not trans_map:
        print(f"[-] 解析译文失败: {err}")
        return False

    bilingual_md = assemble_bilingual(blocks, trans_map)
    zh_dir = os.path.join(pdir, "译文")
    os.makedirs(zh_dir, exist_ok=True)
    out_zh_file = os.path.join(zh_dir, f"{stem}.zh-CN.md")
    with open(out_zh_file, "w", encoding="utf-8", newline="\n") as f:
        f.write(bilingual_md)

    struct_ok, report = run_checker(out_zh_file)
    if not struct_ok:
        print(f"[-] 校验未通过 ({out_zh_file}):")
        for line in report.splitlines()[:15]:
            print("    " + line)
        return False

    update_queue_status(pdir, fname, "done")
    print(f"[SUCCESS] {fname} 校验通过并已标记 done -> {out_zh_file}")
    return True


def main():
    parser = argparse.ArgumentParser(description="单章节单次调用 Gemini API 翻译工具")
    parser.add_argument("--project", default="p-t-barnum_the-humbugs-of-the-world", help="项目名称")
    parser.add_argument("--file", default=None, help="指定章节文件名 (如 i.md)")
    parser.add_argument("--all", action="store_true", help="连续处理所有 todo 章节")
    parser.add_argument("--model", default="gemini-3.8-flash", help="模型名称")
    parser.add_argument("--api-key", default="tian233", help="API Key")
    parser.add_argument("--base-url", default="http://10.38.1.94:8989", help="代理基础 URL")
    parser.add_argument("--dry-run", action="store_true", help="演练模式，不实际调用 API")
    args = parser.parse_args()

    client = None
    if not args.dry_run:
        client = genai.Client(
            api_key=args.api_key,
            http_options={
                "api_version": "v1beta",
                "base_url": args.base_url,
            },
        )

    pdir = os.path.join(PROJ_DIR, args.project)
    q_path = os.path.join(pdir, "translation_queue.csv")
    if not os.path.isfile(q_path):
        print(f"[-] 找不到项目队列: {q_path}")
        sys.exit(1)

    if args.file:
        files = [args.file]
    else:
        with open(q_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            files = [r["file"] for r in reader if r.get("status") == "todo"]

    if not files:
        print("[*] 没有需要翻译的 todo 章节！")
        return

    print(f"[*] 待翻译篇数: {len(files)}")
    for f in files:
        ok = translate_chapter(args.project, f, client, model=args.model, dry_run=args.dry_run)
        if not ok:
            print(f"[-] 章节 {f} 处理中断")
            sys.exit(1)
        if not args.all:
            break


if __name__ == "__main__":
    main()
