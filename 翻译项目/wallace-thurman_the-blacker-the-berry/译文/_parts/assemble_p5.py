# -*- coding: utf-8 -*-
"""Assemble part-5.zh-CN.md from source paragraphs + section translation files."""
import re, sys, io

BASE = r"C:\Users\HanTi\OneDrive\translate\翻译项目\wallace-thurman_the-blacker-the-berry"
SRC = BASE + r"\原文\part-5.md"
PARTS = [BASE + r"\译文\_parts\p5-s%d.zh.txt" % i for i in range(1, 6)]
OUT = BASE + r"\译文\part-5.zh-CN.md"
SECTIONS_END_AT = {26, 38, 45, 59}  # 1-based paragraph indices ending sections 1-4

# --- extract source paragraphs ---
lines = open(SRC, encoding="utf-8").read().split("\n")
paras = []
for ln in lines[4:]:  # skip header lines 1-4 (## Part / V / blank / Pyrrhic Victory)
    s = ln.strip()
    if not s or s == "---":
        continue
    paras.append(s)
print("source paragraphs:", len(paras))
assert len(paras) == 100, "unexpected paragraph count"

# --- parse translation part files ---
blocks = []  # (start, end, [zh paras])
for path in PARTS:
    cur = None  # (start, end, [zh paras])
    for raw in open(path, encoding="utf-8").read().split("\n"):
        line = raw.strip()
        if not line:
            continue
        m = re.fullmatch(r"(\d+)-(\d+)", line)
        if m:
            if cur:
                blocks.append(cur)
            cur = (int(m.group(1)), int(m.group(2)), [])
        else:
            assert cur is not None, "paragraph before any block header in %s" % path
            cur[2].append(line)
    if cur:
        blocks.append(cur)

# validate per-block paragraph counts
for start, end, zh in blocks:
    assert len(zh) == end - start + 1, (
        "block %d-%d has %d zh paras, need %d" % (start, end, len(zh), end - start + 1))

# --- validate coverage 1..100 in order ---
pos = 1
for start, end, zh in blocks:
    assert start == pos, "gap/overlap: expected start %d got %d" % (pos, start)
    pos = end + 1
assert pos == 101, "coverage ends at %d" % (pos - 1)
print("blocks:", len(blocks), "coverage 1..100 OK")

# --- emit ---
out = io.StringIO()
out.write("## Part V / 第五部\n\nPyrrhic Victory / 皮洛士式的胜利\n\n")
for bi, (start, end, zh) in enumerate(blocks):
    out.write("===Original===\n")
    out.write("\n\n".join(paras[start - 1:end]) + "\n\n")
    if end in SECTIONS_END_AT:
        out.write("---\n\n")
    out.write("===Chinese===\n")
    out.write("\n\n".join(zh) + "\n\n")
    if end in SECTIONS_END_AT and bi != len(blocks) - 1:
        out.write("---\n")
data = out.getvalue()
with open(OUT, "w", encoding="utf-8", newline="\n") as f:
    f.write(data)
print("written:", OUT, len(data.encode('utf-8')), "bytes")
