#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
check_bilingual.py — 检查双语对照 md 是否符合 EPUB 生成契约，并启发式检测段落语义错配。

用法:
    python3 check_bilingual.py <输入.zh-CN.md>

格式（唯一支持）:
    块标记 ===Original=== / ===Chinese===，标题合并成「英文 / 中文」。

输出: 逐项报告结构契约符合情况，并列出可疑的语义错配供人工确认。
退出码: 有结构违规或可疑错配时非零，可用于翻译流程的自动卡点。

说明:
    结构契约可自动验证（见 prompts/通用翻译引擎.md 第五节）。
    语义契约（译文紧跟其原文、语义对应）无法纯自动判定，本工具用「原文段的显著数字
    是否出现在紧跟译文段」做启发式检测，输出可疑项供人工核对。数字、URL、年份等在翻译
    中通常原样保留，是较好的锚点；但译者可能改写（如 18→十八），故结果有噪声，需人工判断。
"""
import re
import sys

_MARKER_RE = re.compile(r'^={3,}\s*(original|chinese)\s*={0,}\s*$', re.IGNORECASE)
_HEADING_RE = re.compile(r'^#{1,6}\s')


def main():
    if len(sys.argv) != 2:
        print('用法: python3 check_bilingual.py <输入.zh-CN.md>', file=sys.stderr)
        sys.exit(2)
    path = sys.argv[1]
    md = open(path, encoding='utf-8').read()

    # 状态机提取标记序列
    markers = []  # [(type, content)]
    cur_type = None
    buf = []

    def flush():
        nonlocal buf, cur_type
        content = '\n'.join(buf).strip()
        if cur_type and content:
            markers.append((cur_type, content))
        buf = []
        cur_type = None

    for line in md.split('\n'):
        m = _MARKER_RE.match(line)
        if m:
            flush()
            cur_type = m.group(1).lower()
            continue
        # Only flush on headings when NOT inside a block (cur_type is None)
        if _HEADING_RE.match(line) and cur_type is None:
            flush()
        buf.append(line)
    flush()

    # ---- 结构契约 ----
    # 契约1: 标记成对（Original 后接 Chinese，不连续同标记）
    pair_violations = []
    for i in range(len(markers) - 1):
        if markers[i][0] == markers[i + 1][0]:
            pair_violations.append((i, markers[i][0], markers[i + 1][0]))

    # 配对提取相邻的 (original, chinese)
    pairs = []
    i = 0
    while i < len(markers) - 1:
        if markers[i][0] == 'original' and markers[i + 1][0] == 'chinese':
            pairs.append((markers[i][1], markers[i + 1][1]))
            i += 2
        else:
            i += 1

    # 标题格式检查：标题行应为「英文 / 中文」合并形式（含 / 分隔）
    title_warnings = []
    for line in md.split('\n'):
        if _HEADING_RE.match(line) and '/' not in line:
            title_warnings.append(line.strip()[:50])

    # ---- 语义错配启发式筛查 ----
    suspicious = []
    for en, zh in pairs:
        nums = set(re.findall(r'\b\d{2,}\b', en)) - {'2024', '2025', '2026'}
        if nums and not (nums & set(re.findall(r'\b\d{2,}\b', zh))):
            suspicious.append((en[:40].replace('\n', ' '), zh[:30].replace('\n', ' '), sorted(nums)))

    # ---- 报告 ----
    print(f'文件: {path}')
    print(f'标记块总数: {len(markers)}（Original/Chinese 各应半数）')
    print()
    print('结构契约:')
    if pair_violations:
        print(f'  标记成对: 违反，连续同标记 {len(pair_violations)} 处')
        for idx, a, b in pair_violations[:5]:
            print(f'    [{idx}]->[{idx+1}] {a} 紧跟 {b}')
    else:
        print(f'  标记成对: 满足（{len(pairs)} 对 Original/Chinese）')
    if title_warnings:
        print(f'  标题合并格式: 警告，{len(title_warnings)} 个标题无 "/" 分隔（可能未合并英中）')
        for t in title_warnings[:3]:
            print(f'    "{t}"')
    else:
        print(f'  标题合并格式: 满足')
    print()
    print(f'语义契约（启发式检测，需人工确认）:')
    print(f'  可疑段落错配: {len(suspicious)} 处')
    if suspicious:
        print('  （原文有显著数字但紧跟译文无对应，可能错配；也可能是译者改写数字）')
        for en, zh_t, nums in suspicious[:20]:
            print(f'    原文:{en}... | 译文:{zh_t}... | 锚点数字:{nums}')
        if len(suspicious) > 20:
            print(f'    ...还有 {len(suspicious) - 20} 处未显示')

    struct_ok = not pair_violations and not title_warnings
    sys.exit(0 if (struct_ok and not suspicious) else 1)


if __name__ == '__main__':
    main()
