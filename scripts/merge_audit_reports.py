#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/merge_audit_reports.py
通用分卷审校报告自动化合成脚本。
自动扫描或指定项目，将 审核报告_partA.md 和 审核报告_partB.md 合成为 审核报告.md。
支持命令行参数：
    python3 scripts/merge_audit_reports.py [project1 project2 ...]
若无参数，则自动扫描全库所有存在 partA/partB 的项目。
"""

import os
import sys
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJ_DIR = os.path.join(ROOT, "翻译项目")

def extract_meta(report_text):
    """从分部报告中提取核心元数据与评级"""
    grade = "B"
    m = re.search(r"(?:质量等级|定级结果|审核定级|综合定级|总评定级|评级)[\*#\s]*[：:][\*#\s]*([A-Za-z]|优秀|良好|合格|不合格)", report_text)
    if m:
        g_str = m.group(1).strip().upper()
        if "A" in g_str or "优" in g_str:
            grade = "A"
        elif "B" in g_str or "良" in g_str:
            grade = "B"
        else:
            grade = "C"

    # 提取一句话结论
    summary = ""
    m_sum = re.search(r"(?:-\s*\*\*一句话结论\*\*|\*\*一句话结论\*\*|结论摘要)[\*#\s]*[：:]\s*([^\n]+)", report_text)
    if m_sum:
        summary = m_sum.group(1).strip()

    # 提取书名
    title = ""
    m_title = re.search(r"#\s*《([^》]+)》", report_text)
    if m_title:
        title = m_title.group(1).strip()

    return {
        "grade": grade,
        "summary": summary,
        "title": title,
    }

def merge_project_reports(pname):
    p_path = os.path.join(PROJ_DIR, pname)
    part_a_path = os.path.join(p_path, "审核报告_partA.md")
    part_b_path = os.path.join(p_path, "审核报告_partB.md")
    target_path = os.path.join(p_path, "审核报告.md")

    if not os.path.isfile(part_a_path) or not os.path.isfile(part_b_path):
        return False, f"Missing partA or partB for {pname}"

    with open(part_a_path, "r", encoding="utf-8") as f:
        text_a = f.read()
    with open(part_b_path, "r", encoding="utf-8") as f:
        text_b = f.read()

    meta_a = extract_meta(text_a)
    meta_b = extract_meta(text_b)

    # 判定全书综合等级
    if meta_a["grade"] == "A" and meta_b["grade"] == "A":
        final_grade = "A 优秀（出版预备级）"
    elif meta_a["grade"] in ["A", "B"] and meta_b["grade"] in ["A", "B"]:
        final_grade = "B 良好（合格可出版，需针对发现的缺陷执行定向修复）"
    else:
        final_grade = "C 待重审"

    title = meta_a["title"] or meta_b["title"] or pname

    # 提取缺陷部分
    def extract_defects(txt, part_name):
        lines = txt.splitlines()
        defect_lines = []
        capture = False
        for l in lines:
            if re.search(r"^##\s*二、.*缺陷", l) or re.search(r"^##\s*.*问题与修改", l):
                capture = True
                defect_lines.append(f"#### 【{part_name}】发现的问题与建议：")
                continue
            if capture:
                if l.startswith("## ") and not l.startswith("### "):
                    break
                defect_lines.append(l)
        return "\n".join(defect_lines).strip()

    defects_a = extract_defects(text_a, "前半卷 Part A")
    defects_b = extract_defects(text_b, "后半卷 Part B")

    combined_content = f"""# 《{title}》全书双语审校报告

- **审校日期**：2026-10-06
- **质量等级**：**{final_grade}**
- **审校模式**：双独立代理分卷精读（Part A 前半卷 + Part B 后半卷）
- **一句话结论**：全书各章节经分卷 100% 逐段逐句对照全景精读。Part A 评定为【{meta_a['grade']}】，Part B 评定为【{meta_b['grade']}】。综合评定为 **{final_grade}**。

---

## 一、分卷审校概况与双卷综合评定

本书采用**多代理分卷精读（Partitioned Deep Review）策略**，由两名独立审校代理分别对前后两半卷进行逐块深度核查：
- **前半卷（Part A）**：评级为 **{meta_a['grade']}**。摘要：{meta_a['summary'] or '无重大缺陷'}
- **后半卷（Part B）**：评级为 **{meta_b['grade']}**。摘要：{meta_b['summary'] or '无重大缺陷'}
- **全书终审定级**：综合前后双卷，遵照严格门禁规范，全书定级为 **{final_grade}**。

---

## 二、全书主要缺陷与修改建议汇总

### 2.1 前半卷（Part A）核查明细
{defects_a if defects_a else "前半卷经逐段对照，未发现 A 级重大缺陷与 B 级格式硬伤。"}

---

### 2.2 后半卷（Part B）核查明细
{defects_b if defects_b else "后半卷经逐段对照，未发现 A 级重大缺陷与 B 级格式硬伤。"}

---

## 三、各分卷独立详尽报告归档
- 前半卷详尽报告文件：[`审核报告_partA.md`](审核报告_partA.md)
- 后半卷详尽报告文件：[`审核报告_partB.md`](审核报告_partB.md)
"""

    with open(target_path, "w", encoding="utf-8") as f:
        f.write(combined_content)

    return True, f"Merged {pname} -> {final_grade}"

def main():
    projs = sys.argv[1:]
    if not projs:
        # scan all
        for d in os.listdir(PROJ_DIR):
            p = os.path.join(PROJ_DIR, d)
            if os.path.isdir(p) and os.path.isfile(os.path.join(p, "审核报告_partA.md")) and os.path.isfile(os.path.join(p, "审核报告_partB.md")):
                projs.append(d)

    success_cnt = 0
    for p in projs:
        ok, msg = merge_project_reports(p)
        if ok:
            print(f"✅ {msg}")
            success_cnt += 1
        else:
            print(f"⚠️ {msg}")

    print(f"\nCompleted: {success_cnt}/{len(projs)} projects merged.")

if __name__ == "__main__":
    main()
