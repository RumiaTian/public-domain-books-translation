#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""一键刷新 README.md 中的 647 部书目索引与实时翻译/审校状态表。"""
import os
import re
import sys
import xml.etree.ElementTree as ET
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
import refresh_progress

manual_zh_titles = {
    "alexander-mackenzie_journals": "亚历山大·麦肯齐探险日志",
    "anthony-trollope_short-fiction": "安东尼·特罗洛普短篇小说集",
    "calvin-coolidge_the-autobiography-of-calvin-coolidge": "柯立芝自传",
    "edward-whymper_scrambles-amongst-the-alps-in-the-years-1860-69": "阿尔卑斯攀登记",
    "frederik-pohl_short-fiction": "弗雷德里克·波尔短篇小说集",
    "geronimo_geronimos-story-of-his-life": "杰罗尼莫自述生平",
    "manly-wade-wellman_short-fiction": "曼利·韦德·威尔曼短篇小说集",
}


def clean_cell(text, max_len=180):
    if not text:
        return "-"
    text = text.replace("|", "/").replace("\n", " ").replace("\r", " ")
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) > max_len:
        text = text[: max_len - 3] + "..."
    return text


def generate_index_table(projects, reviews):
    rows = []
    for p in projects:
        pname = p["name"]

        # 1. 翻译与审校状态
        trans_dir_link = f"翻译项目/{pname}/译文"
        if p["total"] == 0:
            t_str = "空项目"
        elif p["todo"] == 0 and p["doing"] == 0:
            if p.get("epub_files"):
                epub_rel = f"翻译项目/{pname}/{p['epub_files'][0][0]}"
                t_str = f"[✅ 100%]({trans_dir_link}) · [📦 下载]({epub_rel})"
            else:
                t_str = f"[✅ 100%]({trans_dir_link})"
        elif p["done"] > 0:
            rate = p["done_kb"] / p["tot_kb"] * 100 if p["tot_kb"] else 0
            t_str = f"[🟡 {rate:.1f}%]({trans_dir_link})"
        else:
            t_str = f"⚪ 待译 ({p['total']}篇)"

        rev_info = reviews.get(pname)
        rev_file_link = f"翻译项目/{pname}/审核报告.md"
        if p["has_review_file"] or (rev_info and rev_info.get("status") == "已完成"):
            grade_m = re.search(r"([A-D])\s*(优秀|良好|需关注|严重)", rev_info["summary"]) if rev_info else None
            grade_txt = f"已审({grade_m.group(1)})" if grade_m else "已审"
            r_str = f"[{grade_txt}]({rev_file_link})"
        elif rev_info and rev_info.get("status") == "审核中":
            r_str = "审核中"
        elif p["todo"] == 0 and p["doing"] == 0 and p["total"] > 0:
            r_str = "⏳ 待审"
        else:
            r_str = "—"

        status_cell = f"{t_str} · {r_str}" if r_str != "—" else t_str

        # 2. EPUB 原文与作者
        epub_dir = os.path.join(ROOT, "翻译项目", pname, "原书")
        epubs = [f for f in os.listdir(epub_dir) if f.endswith(".epub")] if os.path.exists(epub_dir) else []
        title, author, orig_desc = "", "", ""
        if epubs:
            try:
                with zipfile.ZipFile(os.path.join(epub_dir, epubs[0])) as z:
                    opf = [n for n in z.namelist() if n.endswith(".opf")][0]
                    tree = ET.fromstring(z.read(opf))
                    ns = {"dc": "http://purl.org/dc/elements/1.1/"}
                    t_node = tree.find(".//dc:title", ns)
                    c_node = tree.find(".//dc:creator", ns)
                    d_node = tree.find(".//dc:description", ns)
                    title = t_node.text.strip() if t_node is not None and t_node.text else pname
                    author = c_node.text.strip() if c_node is not None and c_node.text else ""
                    if d_node is not None and d_node.text:
                        txt = re.sub(r"<[^>]+>", "", d_node.text)
                        orig_desc = txt
            except Exception:
                title = pname

        # 3. 中文标题与描述
        zh_title = manual_zh_titles.get(pname, "")
        if not zh_title:
            rev_path = os.path.join(ROOT, "翻译项目", pname, "审核报告.md")
            if os.path.exists(rev_path):
                with open(rev_path, encoding="utf-8") as f:
                    for line in f:
                        m = re.search(r"#\s*审[核校]报告[：:]\s*《([^》]+)》", line)
                        if m:
                            zh_title = m.group(1).strip()
                            break

        pm_path = os.path.join(ROOT, "翻译项目", pname, "项目说明.md")
        zh_desc = ""
        if os.path.exists(pm_path):
            with open(pm_path, encoding="utf-8") as f:
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
                m = re.search(r"《([^》\n]{2,30})》", pm_txt[:300])
                if m:
                    zh_title = m.group(1).strip()

            m_desc = re.search(r"-\s*\*\*内容简述\*\*：([^\n]+)", pm_txt)
            if m_desc:
                zh_desc = m_desc.group(1).strip()
            else:
                m_bq = re.search(r"# 项目说明[^\n]*\n\n>\s*([^\n]+)", pm_txt)
                if m_bq:
                    zh_desc = m_bq.group(1).strip()

        if not zh_title:
            zh_title = title or pname

        book_cell = f"[{clean_cell(title or pname, 45)}](翻译项目/{pname}/)"
        rows.append(
            f"| {book_cell} | {clean_cell(author, 25)} | {clean_cell(zh_title, 25)} | {status_cell} | {clean_cell(zh_desc, 140)} | {clean_cell(orig_desc, 160)} |"
        )

    table_header = "| 书本 | 作者 | 中文 | 翻译/校审状态 | 中文介绍 | 书本身介绍 |\n|:---|:---|:---|:---|:---|:---|\n"
    return table_header + "\n".join(rows)


def refresh_readme():
    catalog = refresh_progress.load_catalog()
    projects = refresh_progress.scan_all_projects(catalog)
    reviews = refresh_progress.parse_existing_reviews()

    table_content = generate_index_table(projects, reviews)

    readme_path = os.path.join(ROOT, "README.md")
    if not os.path.isfile(readme_path):
        return

    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 替换表格部分
    pattern = re.compile(
        r"(## 📚 全量书目索引表[^\n]*\n\n[^\n]+\n\n)\| 书本 \| 作者.*?(?=\n---\n\n## ⚖️ 版权与开源许可)",
        re.DOTALL,
    )

    if pattern.search(content):
        new_content = pattern.sub(r"\g<1>" + table_content, content)
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(">>> README.md 索引表格刷新成功！")
    else:
        print("⚠️ 未匹配到 README 表格替换区间，保持原样。")


if __name__ == "__main__":
    refresh_readme()
