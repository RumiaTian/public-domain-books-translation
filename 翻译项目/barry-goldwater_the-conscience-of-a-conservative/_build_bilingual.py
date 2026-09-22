# -*- coding: utf-8 -*-
"""临时构建器：源文段落 + 中文译文载荷 -> 双语对照 md。
用法: python _build_bilingual.py <src> <payload> <dst> [start] [end] [append|new]
payload 格式：首块 "H\t<中文标题>"，之后各块以只含 %%% 的行分隔，依次对应段落。
append 模式用于长文续段（不再输出标题）；new 模式从头输出（含标题）。"""
import io
import sys

src, payload_path, dst = sys.argv[1], sys.argv[2], sys.argv[3]
start = int(sys.argv[4]) if len(sys.argv) > 4 else 0
end = int(sys.argv[5]) if len(sys.argv) > 5 else None
mode = sys.argv[6] if len(sys.argv) > 6 else 'new'

lines = io.open(src, encoding='utf-8').read().split('\n')
heading = next(l for l in lines if l.startswith('#'))
paras = [l for l in lines if l.strip() and not l.startswith('#')]

raw = io.open(payload_path, encoding='utf-8').read().split('\n')
blocks, cur = [], []
for l in raw:
    if l.strip() == '%%%':
        blocks.append('\n'.join(cur).strip('\n'))
        cur = []
    else:
        cur.append(l)
blocks.append('\n'.join(cur).strip('\n'))

head_block = blocks[0]
assert head_block.startswith('H\t'), 'payload 首块须为 "H\t<中文标题>"'
head_zh = head_block[2:].strip()
zh_paras = blocks[1:]
seg_src = paras[start:end]
seg_zh = zh_paras[start:end]
assert len(seg_src) == len(seg_zh), '段落数不匹配: src=%d zh=%d' % (len(seg_src), len(seg_zh))

parts = []
if mode == 'new':
    parts.append('%s / %s' % (heading, head_zh))
for i in range(len(seg_src)):
    parts.append('===Original===\n%s\n\n===Chinese===\n%s' % (seg_src[i], seg_zh[i]))
new_text = '\n\n'.join(parts) + '\n'

if mode == 'append':
    old = io.open(dst, encoding='utf-8').read().rstrip('\n')
    io.open(dst, 'w', encoding='utf-8', newline='').write(old + '\n\n' + new_text)
else:
    io.open(dst, 'w', encoding='utf-8', newline='').write(new_text)

n_pairs = len(seg_src)
total_pairs = (new_text.count('===Original===') + (io.open(dst, encoding='utf-8').read().count('===Original===') if mode == 'append' else 0)) if mode == 'append' else new_text.count('===Original===')
print('built %s: 本次块对=%d, 文件总块对=%d, 源文段落总数=%d' % (dst, n_pairs, io.open(dst, encoding='utf-8').read().count('===Original==='), len(paras)))
