# -*- coding: utf-8 -*-
"""Split source md into units (headings + blocks) and emit a readable manifest.

Usage: python mk_manifest.py <src.md> <manifest.txt>
Units are numbered 1..N sequentially. Headings whose text is exactly 'Book'
absorb the following line as continuation. Whitespace-only segments are dropped.
Manifest: '@@H n | <#level> <text>' or '@@B n' followed by cleaned block lines
(runs of >=3 whitespace-only lines collapse to a paragraph marker line).
"""
import re, sys

src_path, man_path = sys.argv[1], sys.argv[2]
text = open(src_path, encoding='utf-8').read()
lines = text.split('\n')

units = []  # each: dict(kind='H'/'B', level, en, idx=[start,end) source line indices)
cur = None  # current block dict
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

out = []
for n, u in enumerate(units, 1):
    if u['kind'] == 'H':
        out.append('@@H %d | %s %s' % (n, '#' * u['level'], u['en']))
    else:
        out.append('@@B %d' % n)
        seg = lines[u['idx'][0]:u['idx'][1]]
        run = 0
        emitted = False
        for l in seg:
            if not l.strip():
                run += 1
                continue
            if run >= 3 and emitted:
                out.append('¶')
            run = 0
            out.append(l.strip())
            emitted = True
    out.append('')
open(manan_path if False else man_path, 'w', encoding='utf-8', newline='\n').write('\n'.join(out) + '\n')
nb = sum(1 for u in units if u['kind'] == 'B')
nh = len(units) - nb
print('units=%d headings=%d blocks=%d manifest_lines=%d' % (len(units), nh, nb, len(out)))
