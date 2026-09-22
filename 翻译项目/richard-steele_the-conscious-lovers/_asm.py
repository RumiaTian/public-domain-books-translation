# -*- coding: utf-8 -*-
"""Temporary assembler: build paired bilingual md from source + zh data json.
Data json: {"title": "中文标题", "items": [ {"h": "中文", "src": "## EN heading"},
  {"r": [start,end], "zh": ["...", ...]} ]}
- r ranges are 1-based inclusive line ranges into 原文/<stem>.md
- zh list length must equal number of non-blank lines in the range
- blank positions in the source block are mirrored as blank lines in Chinese block
"""
import json
import os
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
stem = sys.argv[1]
src = open(os.path.join(BASE, '原文', stem + '.md'), encoding='utf-8').read()
src = src.replace('\r\n', '\n').replace('\r', '\n')
lines = src.split('\n')
while lines and lines[-1] == '':
    lines.pop()

data = json.load(open(os.path.join(BASE, '_zh_%s.json' % stem), encoding='utf-8'))

def is_heading(l):
    return l.lstrip().startswith('#')

assert lines and is_heading(lines[0]), 'first source line is not a heading: %r' % lines[0][:60]

out = [lines[0].rstrip() + ' / ' + data['title']]
covered = set()
last_pos = 0  # 0 = title line

for item in data['items']:
    if 'h' in item:
        want = item['src'].strip()
        idx = None
        for i in range(1, len(lines)):
            if i in covered or not lines[i].strip():
                continue
            if is_heading(lines[i]) and lines[i].strip() == want:
                idx = i
                break
        assert idx is not None, 'heading not found: %r' % want[:60]
        assert idx > last_pos, 'heading out of order: %r' % want[:60]
        covered.add(idx)
        last_pos = idx
        out.append('')
        out.append(lines[idx].rstrip() + ' / ' + item['h'])
    else:
        a, b = item['r']
        blk = lines[a - 1:b]
        assert blk, 'empty range %s' % item['r']
        assert not any(is_heading(l) for l in blk), 'heading inside block at %s' % item['r']
        assert a - 1 > last_pos, 'block out of order: %s' % item['r']
        last_pos = b - 1
        covered.update(range(a - 1, b))
        nonblank = [i for i, l in enumerate(blk) if l.strip()]
        zh = item['zh']
        assert len(nonblank) == len(zh), 'para mismatch r=%s en=%d zh=%d' % (
            item['r'], len(nonblank), len(zh))
        zhl = [''] * len(blk)
        for k, i in enumerate(nonblank):
            zhl[i] = zh[k]
        while blk and not blk[-1].strip():
            blk.pop(); zhl.pop()
        while blk and not blk[0].strip():
            blk.pop(0); zhl.pop(0)
        out.append('')
        out.append('===Original===')
        out.extend(blk)
        out.append('')
        out.append('===Chinese===')
        out.extend(zhl)

missed = [i for i in range(1, len(lines)) if lines[i].strip() and i not in covered]
assert not missed, 'uncovered non-blank lines: %r' % [(i + 1, lines[i][:50]) for i in missed[:5]]

txt = '\n'.join(out) + '\n'
dst = os.path.join(BASE, '译文', stem + '.zh-CN.md')
with open(dst, 'w', encoding='utf-8', newline='\n') as f:
    f.write(txt)
print('WROTE', dst, len(txt), 'chars,', txt.count('===Original==='), 'blocks')
