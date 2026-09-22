#!/usr/bin/env python3
"""Audit translation markdown files for James Weldon Johnson poetry.

The script follows the 9‑item checklist in `3_审核WORKFLOW.md` but implements a
light‑weight, read‑only analysis:

* Detect empty Chinese blocks (A‑level missing translation)
* Detect obvious semantic mismatch by checking for English words left in the Chinese block (B‑level).
* Detect numeric mismatch by simple pattern comparison (A/B‑level).
* Count total blocks and report summary statistics.

The results are written to `审核报告.md` in the project root.
"""

import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent
TRANSLATION_DIR = PROJECT_ROOT / "译文"
REPORT_PATH = PROJECT_ROOT / "审核报告.md"

def is_english_word(text: str) -> bool:
    # Simple heuristic: contains ASCII letters and spaces, no Chinese characters
    return bool(re.search(r"[A-Za-z]", text)) and not bool(re.search(r"[\u4e00-\u9fff]", text))

def extract_blocks(content: str):
    # Split on ===Original=== and ===Chinese=== markers
    # Returns list of (orig, trans) tuples
    blocks = []
    parts = content.split("===Original===")
    for part in parts[1:]:  # first split before first marker may be empty
        # part starts with original block then maybe ===Chinese===
        if "===Chinese===" not in part:
            continue
        orig, rest = part.split("===Chinese===", 1)
        # Chinese block ends at next ===Original=== or end of file
        if "===Original===" in rest:
            trans, _ = rest.split("===Original===", 1)
        else:
            trans = rest
        blocks.append((orig.strip(), trans.strip()))
    return blocks

def analyze_file(filepath: Path):
    text = filepath.read_text(encoding="utf-8")
    blocks = extract_blocks(text)
    issues = []
    for idx, (orig, trans) in enumerate(blocks, start=1):
        # A‑level: missing translation (empty or only whitespace)
        if not trans:
            issues.append((idx, "Missing translation", "A"))
            continue
        # B‑level: leftover English words
        if is_english_word(trans):
            issues.append((idx, "English residue", "B"))
        # Simple numeric check: compare numbers in both blocks
        orig_nums = re.findall(r"\d+", orig)
        trans_nums = re.findall(r"\d+", trans)
        if orig_nums != trans_nums:
            issues.append((idx, "Numeric mismatch", "A"))
    return issues, len(blocks)

def main():
    all_files = list(TRANSLATION_DIR.rglob("*.zh-CN.md"))
    total_files = len(all_files)
    total_blocks = 0
    total_issues = []
    per_file_summary = []
    for f in all_files:
        issues, block_cnt = analyze_file(f)
        total_blocks += block_cnt
        if issues:
            total_issues.extend([(f, *iss) for iss in issues])
        a_cnt = sum(1 for _, _, sev in issues if sev == "A")
        b_cnt = sum(1 for _, _, sev in issues if sev == "B")
        c_cnt = sum(1 for _, _, sev in issues if sev == "C")
        per_file_summary.append((f.relative_to(PROJECT_ROOT), block_cnt, a_cnt, b_cnt, c_cnt))
    with REPORT_PATH.open("w", encoding="utf-8") as out:
        out.write("# 审核报告\n\n")
        out.write(f"**处理文件数**: {total_files}\n\n")
        out.write(f"**块总数**: {total_blocks}\n\n")
        out.write("## 每文件问题概览\n\n")
        out.write("| 文件 | 块数 | A 级 | B 级 | C 级 |\n")
        out.write("|---|---|---|---|---|\n")
        for rel, blk, a, b, c in per_file_summary:
            out.write(f"| {rel} | {blk} | {a} | {b} | {c} |\n")
        out.write("\n## 详细问题列表\n\n")
        out.write("| 文件 | 块号 | 问题类型 | 严重级别 |\n")
        out.write("|---|---|---|---|\n")
        for file_path, blk_idx, issue, sev in total_issues:
            out.write(f"| {file_path.relative_to(PROJECT_ROOT)} | {blk_idx} | {issue} | {sev} |\n")
        out.write("\n*报告自动生成，未进行人工校对。*\n")

if __name__ == "__main__":
    main()
