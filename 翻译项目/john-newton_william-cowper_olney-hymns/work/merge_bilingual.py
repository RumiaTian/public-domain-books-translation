# -*- coding: utf-8 -*-
"""Merge source md + my numbered translations into bilingual .zh-CN.md.

Usage: python merge_bilingual.py <src.md> <mytrans.txt> <out.zh-CN.md>
mytrans format (in order): '@@H n <chinese heading>' or '@@B n' followed by
chinese block lines until the next @@ line. Unit numbering must match the
source split exactly (same algorithm as mk_manifest.py).
"""
import re, sys

src_path, tr_path, out_path = sys.argv[1], sys.argv[2], sys.argv[3]

# ---- split source (must mirror mk_manifest.py) ----
text = open(src_path, encoding='utf-8').read()
lines = text.split('\n')
units = []
cur = None
consumed = set()

def close():
    global cur
    if cur is not None:
        seg = lines[cur['idx'][0]:cur['idx'][1]]
        if any(l.strip() for l in seg):
            units.append(cur)
        cur = None

i = 0
while i < len(lines):
    line = lines[i]
    m = re.match(r'^(#{1,6})\s+(.*)$', line)
    if m:
        close()
        level = len(m.group(1))
        htext = m.group(2).strip()
        if htext == 'Book' and i + 1 < len(lines) and not lines[i+1].startswith('#') and lines[i+1].strip():
            htext = 'Book ' + lines[i+1].strip()
            consumed.add(i+1)
            i += 1
        units.append({'kind': 'H', 'level': level, 'en': htext})
        i += 1
        continue
    if i in consumed:
        i += 1
        continue
    if cur is None:
        cur = {'kind': 'B', 'idx': [i, i]}
    cur['idx'][1] = i + 1
    i += 1
close()

# ---- parse mytrans ----
trs = []  # list of (n, kind, payload lines)
n = kind = None
buf = []
def flush():
    global n, kind, buf
    if n is not None:
        while buf and not buf[0].strip():
            buf.pop(0)
        while buf and not buf[-1].strip():
            buf.pop()
        trs.append((n, kind, list(buf)))
    buf = []

for line in open(tr_path, encoding='utf-8').read().split('\n'):
    m = re.match(r'^@@(H|B)\s+(\d+)\s*(.*)$', line)
    if m:
        flush()
        kind = m.group(1)
        n = int(m.group(2))
        buf = []
        if kind == 'H':
            buf.append(m.group(3).strip())
        continue
    buf.append(line)
flush()

if len(trs) != len(units):
    print('FATAL: unit count mismatch src=%d trans=%d' % (len(units), len(trs)))
    sys.exit(2)

out = []
for u, (n, kind, payload) in zip(units, trs):
    if u['kind'] == 'H':
        if kind != 'H' or not payload or not payload[0].strip():
            print('FATAL: unit %d expected heading translation' % n)
            sys.exit(3)
        out.append('%s %s / %s' % ('#' * u['level'], u['en'], payload[0].strip()))
    else:
        if kind != 'B':
            print('FATAL: unit %d expected block translation' % n)
            sys.exit(4)
        if not payload:
            print('FATAL: unit %d empty block translation' % n)
            sys.exit(5)
        orig = lines[u['idx'][0]:u['idx'][1]]
        out.append('===Original===')
        out.extend(orig)
        out.append('===Chinese===')
        out.extend(payload)
    out.append('')
open(out_path, 'w', encoding='utf-8', newline='\n').write('\n'.join(out).rstrip('\n') + '\n')
print('OK units=%d -> %s' % (len(units), out_path))
