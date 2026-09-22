#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""全生命周期进度总控统一工具 (refresh_progress.py)

一键并发扫描全库项目：
1. 统计四大阶段全生命周期状态：
   - 阶段 1：下载与选品（1499 本全量库状态、中译本排查结果与原书 EPUB 链接）
   - 阶段 2：翻译执行（647 本精选项目的完成率、章节数、KB 与译文目录链接）
   - 阶段 3：独立审核（审核报告.md、质量等级与审核报告链接）
   - 阶段 4：出版打包（双语 EPUB 产物、体积与 EPUB 文件链接）
2. 重建根 translation_queue.csv；
3. 生成并刷新根 Plan.md（包含全局四阶段概览、全生命周期主表、审校明细、EPUB 打包汇总与运行日志）。

用法：
  python scripts/refresh_progress.py
  python scripts/refresh_progress.py --snapshot "2026-08-25，全生命周期统一总控" \
      --log-date 2026-08-25 --log-event "四阶段体系整合" --log-done "+0" \
      --log-notes "统一 Plan.md 呈现下载、翻译、审核、打包全生命周期与结果文件"
"""
import argparse
import csv
import json
import os
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJ_DIR = os.path.join(ROOT, "翻译项目")
ROOT_CSV = os.path.join(ROOT, "translation_queue.csv")
PLAN_MD = os.path.join(ROOT, "Plan.md")
REVIEW_MD = os.path.join(ROOT, "审核记录.md")
EPUB_MD = os.path.join(ROOT, "EPUB打包汇总.md")

HOME_DL = os.path.expanduser("~/Downloads")
EPUB_POOL_DIR = os.path.join(HOME_DL, "1499_books_epub")
CATALOG_JSON = os.path.join(EPUB_POOL_DIR, "archive_scripts", "catalog.json")


def natural_key(name):
    nums = re.findall(r"\d+", name)
    return [int(n) for n in nums] if nums else [9999]


def load_catalog():
    """加载 1499 本全量图书元数据"""
    catalog_map = {}
    if os.path.isfile(CATALOG_JSON):
        try:
            with open(CATALOG_JSON, "r", encoding="utf-8") as f:
                data = json.load(f)
                books = data.get("books", [])
                for b in books:
                    fn = b.get("file", "")
                    stem = Path(fn).stem if fn else ""
                    if stem:
                        catalog_map[stem] = {
                            "title": b.get("title", stem),
                            "authors": ", ".join(b.get("authors", [])) or "未知",
                            "file": fn,
                            "url": b.get("url", ""),
                        }
        except Exception:
            pass
    return catalog_map


def parse_existing_reviews():
    """从 审核记录.md 或 Plan.md 中提取历史审核记录字典，并自动补全各项目的 审核报告.md"""
    reviews = {}
    sources = [REVIEW_MD, PLAN_MD]
    for src in sources:
        if not os.path.isfile(src):
            continue
        try:
            with open(src, "r", encoding="utf-8") as f:
                content = f.read()
            for line in content.splitlines():
                parts = [p.strip() for p in line.split("|")]
                if len(parts) >= 11 and parts[1].isdigit():
                    pname = parts[2].strip("`")
                    if pname not in reviews:
                        reviews[pname] = {
                            "raw_kb": parts[3],
                            "chapters": parts[4],
                            "tokens": parts[5],
                            "agents": parts[6],
                            "status": parts[7],
                            "date": parts[8],
                            "report": parts[9],
                            "summary": parts[10],
                        }
        except Exception:
            pass

    # 自动扫描翻译项目目录下的 审核报告.md 兜底补全
    if os.path.isdir(PROJ_DIR):
        for d in sorted(os.listdir(PROJ_DIR)):
            if d in reviews or d.startswith("_"):
                continue
            rp = os.path.join(PROJ_DIR, d, "审核报告.md")
            if not os.path.isfile(rp):
                continue
            try:
                with open(rp, "r", encoding="utf-8") as f:
                    txt = f.read()
                m_date = re.search(r"审校日期[*：:\s]+([0-9]{4}-[0-9]{2}-[0-9]{2})", txt)
                date = m_date.group(1) if m_date else "-"

                m_grade = re.search(r"(?:质量等级|综合评级)[*：:\s]+([^\n\r]+)", txt)
                grade = m_grade.group(1).replace("*", "").strip() if m_grade else "-"

                m_sum = re.search(r"一句话结论[*：:\s]+([^\n\r]+)", txt)
                summary = m_sum.group(1).replace("*", "").strip() if m_sum else ""
                if not summary:
                    m_sum2 = re.search(r"一句话结论[*：:\s]*\n+([^\n\r]+)", txt)
                    summary = m_sum2.group(1).replace("*", "").strip() if m_sum2 else ""

                comb_summary = f"{grade} | {summary}" if summary else grade

                csv_file = os.path.join(PROJ_DIR, d, "translation_queue.csv")
                tot_kb = 0.0
                chs = 0
                if os.path.isfile(csv_file):
                    with open(csv_file, "r", encoding="utf-8") as cf:
                        for r in csv.DictReader(cf):
                            chs += 1
                            try:
                                tot_kb += float(r.get("size_kb") or 0)
                            except Exception:
                                pass

                reviews[d] = {
                    "raw_kb": f"{tot_kb:.1f}",
                    "chapters": str(chs),
                    "tokens": "-",
                    "agents": "1",
                    "status": "已完成",
                    "date": date,
                    "report": f"[`审核报告.md`](翻译项目/{d}/审核报告.md)",
                    "summary": comb_summary,
                }
            except Exception:
                pass

    # 只保留本地实际存在 审核报告.md 的有效审校记录，杜绝幽灵/已删除记录残留
    valid_reviews = {}
    for pname, rinfo in reviews.items():
        if os.path.isfile(os.path.join(PROJ_DIR, pname, "审核报告.md")):
            # 如果 Plan.md 中的旧记录没有解析出 date/summary，尝试从本地文件补全
            if rinfo.get("date") == "-" or rinfo.get("summary") == "-":
                try:
                    rp = os.path.join(PROJ_DIR, pname, "审核报告.md")
                    with open(rp, "r", encoding="utf-8") as f:
                        txt = f.read()
                    m_date = re.search(r"审校日期[*：:\s]+([0-9]{4}-[0-9]{2}-[0-9]{2})", txt)
                    if m_date:
                        rinfo["date"] = m_date.group(1)
                    m_grade = re.search(r"(?:质量等级|综合评级)[*：:\s]+([^\n\r]+)", txt)
                    g = m_grade.group(1).replace("*", "").strip() if m_grade else ""
                    m_sum = re.search(r"一句话结论[*：:\s]+([^\n\r]+)", txt)
                    s = m_sum.group(1).replace("*", "").strip() if m_sum else ""
                    if not s:
                        m_sum2 = re.search(r"一句话结论[*：:\s]*\n+([^\n\r]+)", txt)
                        s = m_sum2.group(1).replace("*", "").strip() if m_sum2 else ""
                    if g or s:
                        rinfo["summary"] = f"{g} | {s}" if (g and s) else (g or s)
                except Exception:
                    pass
            valid_reviews[pname] = rinfo
    return valid_reviews


def parse_existing_epubs():
    """从 EPUB打包汇总.md 或 Plan.md 中提取 EPUB 打包元数据"""
    epubs = {}
    sources = [EPUB_MD, PLAN_MD]
    for src in sources:
        if not os.path.isfile(src):
            continue
        try:
            with open(src, "r", encoding="utf-8") as f:
                content = f.read()
            in_epub_section = (src == EPUB_MD)
            for line in content.splitlines():
                if "EPUB 双语出版打包明细" in line:
                    in_epub_section = True
                    continue
                if in_epub_section and line.startswith("## ") and "EPUB" not in line:
                    in_epub_section = False
                    continue
                if not in_epub_section:
                    continue
                parts = [p.strip() for p in line.split("|")]
                if (
                    len(parts) >= 7
                    and not parts[1].isdigit()
                    and not parts[1].startswith("书名")
                    and not parts[1].startswith("---")
                    and not parts[1].startswith(":")
                    and parts[1]
                ):
                    pname = parts[3].strip("`") if len(parts) > 3 else ""
                    if not pname or pname.startswith("http") or pname == "-":
                        path = parts[6] if len(parts) > 6 else parts[5]
                        m = re.search(r"翻译项目/([^/]+)/", path)
                        pname = m.group(1).strip("`") if m else ""
                    if pname and pname not in epubs:
                        epubs[pname] = {
                            "title": parts[1],
                            "author": parts[2],
                            "size": parts[4] if len(parts) > 4 else parts[3],
                            "blocks": parts[5] if len(parts) > 5 else parts[4],
                            "path": parts[6] if len(parts) > 6 else parts[5],
                        }
        except Exception:
            pass
    return epubs


def extract_project_info(name, proj_path, catalog_map):
    """读取单项目的所有状态信息"""
    csv_path = os.path.join(proj_path, "translation_queue.csv")
    rows = []
    if os.path.isfile(csv_path):
        try:
            with open(csv_path, "r", encoding="utf-8") as f:
                rdr = csv.DictReader(f)
                for r in rdr:
                    rows.append(r)
        except Exception:
            pass

    rows.sort(key=lambda r: natural_key(r.get("file", "")))
    done = todo = doing = 0
    tot_kb = done_kb = 0.0
    for r in rows:
        st = (r.get("status") or "").strip().lower()
        try:
            kb = float(r.get("size_kb") or 0)
        except ValueError:
            kb = 0.0
        tot_kb += kb
        if st == "done":
            done += 1
            done_kb += kb
        elif st == "doing":
            doing += 1
        else:
            todo += 1

    has_review_file = os.path.isfile(os.path.join(proj_path, "审核报告.md"))
    has_spec = os.path.isfile(os.path.join(proj_path, "项目说明.md"))

    epub_files = []
    try:
        for f in os.listdir(proj_path):
            if f.endswith(".epub"):
                fp = os.path.join(proj_path, f)
                epub_files.append((f, os.path.getsize(fp) / 1024))
    except Exception:
        pass

    cat_meta = catalog_map.get(name, {})
    title = cat_meta.get("title", "")
    author = cat_meta.get("authors", "")

    # 如果 catalog 中无数据，从项目说明或审核报告中智能补全
    if not title:
        rev_path = os.path.join(proj_path, "审核报告.md")
        if os.path.isfile(rev_path):
            try:
                with open(rev_path, "r", encoding="utf-8") as f:
                    for l in f:
                        m = re.search(r"#\s*审[核校]报告[：:]\s*《([^》]+)》", l)
                        if m:
                            title = m.group(1).strip()
                            break
            except Exception:
                pass
    if not title:
        pm_path = os.path.join(proj_path, "项目说明.md")
        if os.path.isfile(pm_path):
            try:
                with open(pm_path, "r", encoding="utf-8") as f:
                    pm_txt = f.read()
                m = re.search(r"#\s*项目说明[：:]\s*《([^》]+)》", pm_txt)
                if m:
                    title = m.group(1).strip()
                if not title:
                    m = re.search(r"#\s*项目说明[（\(]([^）\)]+)[）\)]", pm_txt)
                    if m:
                        title = m.group(1).strip()
                if not title:
                    m = re.search(r"-\s*\*\*项目名称\*\*：.*?《([^》]+)》", pm_txt)
                    if m:
                        title = m.group(1).strip()
                if not title:
                    m = re.search(r"《([^》\n]{2,30})》", pm_txt[:400])
                    if m:
                        title = m.group(1).strip()
                if not author:
                    m_a = re.search(r"-\s*\*\*(?:原作者|作者)\*\*：([^\n]+)", pm_txt)
                    if m_a:
                        author = m_a.group(1).strip()
            except Exception:
                pass

    if not title:
        title = name
    if not author:
        author = name.split("_")[0].replace("-", " ").title()

    # 判断原书 EPUB 状态
    epub_filename = cat_meta.get("file", f"{name}.epub")
    pool_epub_path = os.path.join(EPUB_POOL_DIR, epub_filename)
    has_pool_epub = os.path.isfile(pool_epub_path)

    return {
        "name": name,
        "title": title,
        "author": author,
        "epub_filename": epub_filename,
        "has_pool_epub": has_pool_epub,
        "pool_epub_path": pool_epub_path,
        "rows": rows,
        "done": done,
        "todo": todo,
        "doing": doing,
        "total": len(rows),
        "tot_kb": tot_kb,
        "done_kb": done_kb,
        "has_review_file": has_review_file,
        "has_spec": has_spec,
        "epub_files": epub_files,
    }


def scan_all_projects(catalog_map):
    """并发扫描所有项目"""
    proj_names = sorted(
        [d for d in os.listdir(PROJ_DIR) if os.path.isdir(os.path.join(PROJ_DIR, d)) and not d.startswith("_")]
    )

    def worker(name):
        return extract_project_info(name, os.path.join(PROJ_DIR, name), catalog_map)

    with ThreadPoolExecutor(max_workers=32) as ex:
        results = list(ex.map(worker, proj_names))

    results.sort(key=lambda x: x["name"])
    return results


def rebuild_root_csv(projects):
    """根据各项目 CSV 重新生成根 translation_queue.csv"""
    total_rows = 0
    with open(ROOT_CSV, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["project", "file", "size_kb", "status"])
        for p in projects:
            for r in p["rows"]:
                try:
                    kb = float(r.get("size_kb") or 0)
                except ValueError:
                    kb = 0.0
                st = (r.get("status") or "todo").strip()
                w.writerow([p["name"], r.get("file", ""), f"{kb:.1f}", st])
                total_rows += 1
    return total_rows


def extract_existing_logs():
    """从已有的 Plan.md 中提取历史日志行"""
    logs = []
    if not os.path.isfile(PLAN_MD):
        return logs
    try:
        with open(PLAN_MD, "r", encoding="utf-8") as f:
            lines = f.readlines()
        in_log = False
        for line in lines:
            if "运行日志" in line and line.startswith("#"):
                in_log = True
                continue
            if in_log:
                if line.startswith("#") and "运行日志" not in line:
                    break
                s = line.strip()
                if s.startswith("|") and not s.startswith("| 日期") and not s.startswith("|:---") and not s.startswith("| ---"):
                    logs.append(s)
    except Exception:
        pass
    return logs


def generate_plan_markdown(projects, catalog_map, reviews_meta, epubs_meta, snapshot_title, log_entry=None):
    """生成全生命周期的根 Plan.md"""
    # 统计全局指标
    g_done = sum(p["done"] for p in projects)
    g_todo = sum(p["todo"] for p in projects)
    g_doing = sum(p["doing"] for p in projects)
    g_total_chapters = sum(p["total"] for p in projects)
    g_tot_kb = sum(p["tot_kb"] for p in projects)
    g_done_kb = sum(p["done_kb"] for p in projects)
    g_rate = (g_done_kb / g_tot_kb * 100) if g_tot_kb else 0.0

    p_100 = [p for p in projects if p["todo"] == 0 and p["doing"] == 0 and p["total"] > 0]
    p_doing = [p for p in projects if (p["doing"] > 0 or (p["done"] > 0 and p["todo"] > 0))]
    p_todo = [p for p in projects if p["done"] == 0 and p["doing"] == 0 and p["total"] > 0]

    reviewed_projects = [
        p for p in projects if p["has_review_file"] or (p["name"] in reviews_meta and reviews_meta[p["name"]]["status"] == "已完成")
    ]
    epub_projects = [p for p in projects if p["epub_files"] or p["name"] in epubs_meta]

    total_catalog_count = len(catalog_map) or 1499
    filtered_out_count = total_catalog_count - len(projects)

    lines = []
    lines.append("# 全生命周期进度总控 (Plan.md)")
    lines.append("")
    lines.append("> 本文件是**全生命周期进度总控看板**，整合 `阶段一：下载选品`、`阶段二：翻译执行`、`阶段三：独立审核`、`阶段四：出版打包` 与 `流水线全局运行日志`。")
    lines.append("> ")
    lines.append("> **权威源声明**：各项目单章状态权威源为 `翻译项目/<项目名>/translation_queue.csv`；根 `translation_queue.csv` 与本文件均为统一快照。")
    lines.append("")
    lines.append("---")
    lines.append("")

    # 1. 全局四阶段总览 Dashboard
    lines.append(f"## 📊 全局四阶段总览（快照：{snapshot_title}）")
    lines.append("")
    lines.append("| 流水线阶段 | 核心指标 / 覆盖书目 | 产物规模 / 推进比率 | 关键结果与存储位置 |")
    lines.append("|:---|:---:|:---:|:---|")
    lines.append(
        f"| **阶段一：下载与选品 (Download & Sourcing)** | 全量 **{total_catalog_count}** 本已 100% 下载封存 | **{len(projects)}** 本精选入库 / **{filtered_out_count}** 本已过滤(已有中译本) | 原书底库：1499 本全量封存 |"
    )
    lines.append(
        f"| **阶段二：翻译执行 (Translation)** | **{len(p_100)}** 完 / **{len(p_doing)}** 译 / **{len(p_todo)}** 待（共 {len(projects)} 本） | **{g_done}** / {g_total_chapters} 篇（**{g_done_kb:.1f}** / {g_tot_kb:.1f} KB）· **{g_rate:.1f}%** | 译文产物：`翻译项目/<项目>/译文/*.zh-CN.md` |"
    )
    lines.append(
        f"| **阶段三：独立审校 (Review & Audit)** | **{len(reviewed_projects)}** 本已审 / **{len(p_100) - len(reviewed_projects)}** 本待审 | 覆盖精读 **{len(reviewed_projects)}** 本（**{len(reviewed_projects)/len(p_100)*100 if p_100 else 0:.1f}%** 基于已译完） | 审核报告：`翻译项目/<项目>/审核报告.md` |"
    )
    lines.append(
        f"| **阶段四：出版打包 (EPUB Packaging)** | **{len(epub_projects)}** 本已打包 / **{len(p_100) - len(epub_projects)}** 本待打包 | 交付标准双语 EPUB **{len(epub_projects)}** 本（**{len(epub_projects)/len(p_100)*100 if p_100 else 0:.1f}%** 基于已译完） | 最终出版：`翻译项目/<项目>/<书名>.epub` |"
    )
    lines.append("")
    lines.append(
        f"> 📈 **全流程里程碑**：全量 **1499** 本原书已全部入库；精选 **{len(projects)}** 本无译本书目中，已有 **{len(p_100)}** 本译完，**{len(reviewed_projects)}** 本完成独立审校，**{len(epub_projects)}** 本完成双语 EPUB 出版打包。"
    )
    lines.append("")
    lines.append("---")
    lines.append("")

    # 2. 全生命周期书目主台账 (Master Lifecycle Ledger)
    lines.append(f"## 📚 {len(projects)} 本精选项目全生命周期主台账")
    lines.append("")
    lines.append("| # | 项目名 / 书名 | 阶段1: 下载 (原书EPUB) | 阶段2: 翻译 (译文产物) | 阶段3: 审校 (审核报告) | 阶段4: 打包 (双语EPUB) | 阶段摘要与结论 |")
    lines.append("|---|:---|:---:|:---:|:---:|:---:|:---|")

    idx = 1
    for p in projects:
        pname = p["name"]
        
        # 阶段 1: 下载
        dl_st = "✅ 已入库"

        # 阶段 2: 翻译
        trans_dir_link = f"翻译项目/{pname}/译文"
        if p["total"] == 0:
            trans_st = "空项目"
        elif p["todo"] == 0 and p["doing"] == 0:
            trans_st = f"[✅ **100%**]({trans_dir_link}) ({p['done']}篇)"
        elif p["done"] > 0:
            rate = p["done_kb"] / p["tot_kb"] * 100 if p["tot_kb"] else 0
            trans_st = f"[🟡 {rate:.1f}%]({trans_dir_link}) ({p['done']}/{p['total']})"
        else:
            trans_st = f"⚪ 待译 ({p['total']}篇)"

        # 阶段 3: 审校
        rev_info = reviews_meta.get(pname)
        rev_file_link = f"翻译项目/{pname}/审核报告.md"
        if p["has_review_file"] or (rev_info and rev_info.get("status") == "已完成"):
            grade_m = re.search(r"([A-D])\s*(优秀|良好|需关注|严重)", rev_info["summary"]) if rev_info else None
            grade_txt = f"✅ 已审({grade_m.group(1)})" if grade_m else "✅ 已审"
            rev_st = f"[{grade_txt}]({rev_file_link})"
        elif rev_info and rev_info.get("status") == "审核中":
            rev_st = "🟡 审核中"
        elif p["todo"] == 0 and p["doing"] == 0 and p["total"] > 0:
            rev_st = "⏳ 待审"
        else:
            rev_st = "—"

        # 阶段 4: 打包
        epub_info = epubs_meta.get(pname)
        if p["epub_files"]:
            ep_name, ep_size = p["epub_files"][0]
            epub_link = f"翻译项目/{pname}/{ep_name}"
            epub_st = f"[📦 {ep_size:.0f}KB]({epub_link})"
        elif epub_info:
            ep_path = epub_info.get("path", "")
            epub_link = ep_path
            epub_st = f"[📦 {epub_info.get('size', '已打包')}]({epub_link})"
        elif p["has_review_file"] or (rev_info and rev_info.get("status") == "已完成"):
            epub_st = "⏳ 待打包"
        else:
            epub_st = "—"

        # 摘要
        summary = ""
        if rev_info and rev_info.get("summary"):
            summary = rev_info["summary"]
            if len(summary) > 40:
                summary = summary[:38] + "…"
        elif p["todo"] == 0 and p["doing"] == 0 and p["total"] > 0:
            summary = "已译完待审"
        elif p["doing"] > 0:
            summary = f"翻译中 (done {p['done']}/{p['total']})"

        lines.append(
            f"| {idx} | `{pname}` | {dl_st} | {trans_st} | {rev_st} | {epub_st} | {summary} |"
        )
        idx += 1

    lines.append(
        f"| | **合计 ({len(projects)} 本精选)** | **100% 下载** | **{g_done}/{g_total_chapters} 篇 ({g_rate:.1f}%)** | **{len(reviewed_projects)} 本完成** | **{len(epub_projects)} 本完成** | 全流程四阶段闭环 |"
    )
    lines.append("")
    lines.append("---")
    lines.append("")

    # 3. 详细审校台账明细
    lines.append("## 🔍 独立审校台账明细")
    lines.append("")
    lines.append(
        "> 遵循 `3_审核WORKFLOW.md`，由独立审校子代理对译稿进行精读核查，执行 A/B/C 三级问题评定。只读评估，不修改译文。"
    )
    lines.append("")
    lines.append("| # | 项目 | 原文KB | 章数 | 输入Token(万) | 代理数 | 状态 | 审核日期 | 报告路径 | 结论与缺陷摘要 |")
    lines.append("|---|:---|---:|---:|---:|---:|:---:|:---:|:---|:---|")

    rev_list = []
    for pname, r in reviews_meta.items():
        try:
            rkb = float(r.get("raw_kb", 0))
        except ValueError:
            rkb = 0.0
        rev_list.append((pname, rkb, r))

    rev_list.sort(key=lambda x: x[1])
    for i, (pname, rkb, r) in enumerate(rev_list, 1):
        report_link = f"翻译项目/{pname}/审核报告.md"
        lines.append(
            f"| {i} | `{pname}` | {r.get('raw_kb', '-')} | {r.get('chapters', '-')} | {r.get('tokens', '-')} | {r.get('agents', '-')} | {r.get('status', '已完成')} | {r.get('date', '-')} | [`审核报告.md`]({report_link}) | {r.get('summary', '-')} |"
        )

    lines.append("")
    lines.append("---")
    lines.append("")

    # 4. EPUB 双语出版打包明细
    lines.append("## 📦 EPUB 双语出版打包明细")
    lines.append("")
    lines.append(
        "> 遵循 `4_打包WORKFLOW.md`，依据审核报告终校修复后，使用 `bilingual_to_epub.py` 经 Pandoc 编译构建输出。"
    )
    lines.append("")
    lines.append("| 书名 | 作者 | 项目目录 | EPUB 大小 | 块对数 | EPUB 产物路径 |")
    lines.append("|:---|:---|:---|---:|---:|:---|")

    all_epubs = dict(epubs_meta)
    for p in projects:
        if p.get("epub_files"):
            pname = p["name"]
            ep_file, ep_size = p["epub_files"][0]
            if pname not in all_epubs:
                all_epubs[pname] = {
                    "title": p.get("title", pname),
                    "author": p.get("author", "-"),
                    "size": f"{ep_size:.0f}KB",
                    "blocks": "-",
                    "filename": ep_file,
                }
            else:
                all_epubs[pname]["filename"] = ep_file
                if not all_epubs[pname].get("size") or all_epubs[pname]["size"] == "-":
                    all_epubs[pname]["size"] = f"{ep_size:.0f}KB"

    for pname, ep in sorted(all_epubs.items()):
        ep_file = ep.get("filename", f"{pname}.epub")
        epub_rel = f"翻译项目/{pname}/{ep_file}"
        lines.append(
            f"| {ep.get('title', '-')} | {ep.get('author', '-')} | `{pname}` | {ep.get('size', '-')} | {ep.get('blocks', '-')} | [`{ep_file}`]({epub_rel}) |"
        )

    lines.append("")
    lines.append("---")
    lines.append("")

    # 5. 流水线全局运行日志
    lines.append("## 📝 流水线全局运行日志")
    lines.append("")
    lines.append("> 记录下载选品、批次翻译、审校核验与 EPUB 打包的全局流水线运行事件。")
    lines.append("")
    lines.append("| 日期 | 事件 | 完成/变动 | 剩余 todo | doing | 详细备注 |")
    lines.append("|:---:|:---|:---:|:---:|:---:|:---|")

    existing_logs = extract_existing_logs()
    for log in existing_logs:
        lines.append(log)

    if log_entry:
        lines.append(log_entry)

    lines.append("")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="全生命周期进度总控统一工具")
    parser.add_argument("--snapshot", default=None, help="快照描述标签")
    parser.add_argument("--log-date", default=None, help="日志日期 (YYYY-MM-DD)")
    parser.add_argument("--log-event", default=None, help="日志事件名称")
    parser.add_argument("--log-done", default=None, help="完成篇数变化，如 +5 或 414")
    parser.add_argument("--log-notes", default=None, help="日志备注说明")
    parser.add_argument("--no-rebuild-csv", action="store_true", help="跳过重建根 translation_queue.csv")
    args = parser.parse_args()

    t0 = time.time()
    print(">>> 正在扫描全库项目生命周期状态...", flush=True)
    catalog_map = load_catalog()
    reviews_meta = parse_existing_reviews()
    epubs_meta = parse_existing_epubs()
    projects = scan_all_projects(catalog_map)
    print(f">>> 扫描完成：共 {len(projects)} 个精选项目，耗时 {time.time() - t0:.2f}s", flush=True)

    if not args.no_rebuild_csv:
        csv_rows = rebuild_root_csv(projects)
        print(f">>> 根 translation_queue.csv 已更新（共 {csv_rows} 行）", flush=True)

    snapshot_title = args.snapshot or time.strftime("%Y-%m-%d，全库生命周期总控")
    log_row = None
    if args.log_date and args.log_event:
        g_todo = sum(p["todo"] for p in projects)
        g_doing = sum(p["doing"] for p in projects)
        log_row = (
            f"| {args.log_date} | {args.log_event} | {args.log_done or '+0'} | "
            f"{g_todo} | {g_doing} | {args.log_notes or ''} |"
        )

    print(">>> 正在生成统一 Plan.md 四阶段总控看板...", flush=True)
    plan_content = generate_plan_markdown(
        projects, catalog_map, reviews_meta, epubs_meta, snapshot_title, log_row
    )

    with open(PLAN_MD, "w", encoding="utf-8", newline="\n") as f:
        f.write(plan_content)

    print(f">>> Plan.md 刷新成功！总耗时: {time.time() - t0:.2f}s", flush=True)


if __name__ == "__main__":
    main()
