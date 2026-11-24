#!/usr/bin/env python3
"""Generate project scaffold file (translation_queue.csv) in true reading order.

排序优先级：
1. 存在 原书/*.epub → 按 OPF spine 顺序（复用 epub_to_md 的 spine 过滤与标题/kebab 规则；
   多卷 EPUB 按文件名 natural 序拼接卷）。spine 文件名与 原文/ 完全一致时直接采用；
   不一致时按 spine 对齐已匹配文件，剩余文件自然序追加并告警。
2. 无 EPUB → 改进版自然排序（支持罗马数字词；年份等数字不再把文件顶到全书最前）。
状态一律写 todo（脚手架阶段专用）。
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from epub_to_md import spine_entries

_ROMAN_RE = re.compile(r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$", re.IGNORECASE)
_ROMAN_VAL = {"i": 1, "v": 5, "x": 10, "l": 50, "c": 100, "d": 500, "m": 1000}


def _roman_value(s):
    total = 0
    prev = 0
    for ch in reversed(s.lower()):
        v = _ROMAN_VAL[ch]
        total = total - v if v < prev else total + v
        prev = max(prev, v)
    return total


def natural_key(name):
    """词元级自然排序：数字串与罗马数字词元按数值比较，单词按字典比较。
    dogfight-1973 落在 d 词区而非全书最前；part-i/part-ii 按 1/2 排。"""
    keys = []
    for tok in re.findall(r"\d+|[A-Za-z]+", name):
        if tok.isdigit():
            keys.append((0, int(tok), ""))
        elif _ROMAN_RE.match(tok):
            keys.append((0, _roman_value(tok), ""))
        else:
            keys.append((1, 0, tok.lower()))
    return keys or [(2, 0, "")]


def epub_reading_order(proj_dir, src_files):
    """EPUB spine 顺序 → 原文文件名列表。返回 (order, warn) 或 None（无 EPUB）。"""
    epub_dir = os.path.join(proj_dir, "原书")
    if not os.path.isdir(epub_dir):
        return None
    epubs = [f for f in sorted(os.listdir(epub_dir), key=natural_key) if f.endswith(".epub")]
    if not epubs:
        return None
    expected = []
    for ep in epubs:
        expected += [e["file"] for e in spine_entries(os.path.join(epub_dir, ep))]
    existing = set(src_files)
    order = [f for f in expected if f in existing]
    rest = sorted(set(src_files) - set(order), key=natural_key)
    warn = None
    if rest:
        warn = f"spine 未覆盖 {len(rest)} 个文件，已按自然序追加: {rest[:5]}{'…' if len(rest) > 5 else ''}"
    return order + rest, warn


def main():
    if len(sys.argv) != 2:
        print("Usage: gen_project_files.py <project_dir>")
        sys.exit(1)
    proj_dir = sys.argv[1]
    src_dir = os.path.join(proj_dir, '原文')
    files = [f for f in os.listdir(src_dir) if f.endswith('.md')]
    result = epub_reading_order(proj_dir, files)
    if result is None:
        order, warn = sorted(files, key=natural_key), None
    else:
        order, warn = result
    if warn:
        print(f"警告: {warn}")
    out_path = os.path.join(proj_dir, 'translation_queue.csv')
    with open(out_path, 'w', encoding='utf-8', newline='\n') as f:
        f.write('file,size_kb,status\n')
        for fn in order:
            size = os.path.getsize(os.path.join(src_dir, fn)) / 1024
            f.write(f'{fn},{size:.1f},todo\n')
    print(f"Wrote {out_path} with {len(order)} entries (reading order)")


if __name__ == '__main__':
    main()
