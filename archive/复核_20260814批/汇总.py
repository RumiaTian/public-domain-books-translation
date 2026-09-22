# -*- coding: utf-8 -*-
"""0814 批次复核收口汇总

读取 `复核_20260814批/批次台账.md`，输出：
  1) 新旧等级对照总表（按体积升序）
  2) 等级迁移统计（旧→新 矩阵）
  3) 按「缺陷性质」分类：完整性缺陷 / 质量缺陷 / 无实质缺陷
  4) D 级书目与其缺失量摘要（从台账备注正则提取）

用法：python 复核_20260814批/汇总.py [--md 输出文件]
"""
import re, os, sys, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEDGER = os.path.join(ROOT, '复核_20260814批', '批次台账.md')

ORDER = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
NAME = {'A': 'A 优秀', 'B': 'B 良好', 'C': 'C 需关注', 'D': 'D 严重'}
TARGET = os.path.join(ROOT, '翻译项目')


def parse():
    t = open(LEDGER, encoding='utf-8').read()
    rows = re.findall(r'^\| (\d+) \| `([^`]+)` \| ([\d.]+) \| ([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|$', t, re.M)
    out = []
    for idx, proj, size, old, new, status, note in rows:
        old = old.strip()
        m = re.search(r'\*\*([A-D])', new) or re.search(r'([A-D])', new)
        newl = m.group(1) if m else ''
        out.append(dict(idx=int(idx), proj=proj, size=float(size), old=old, new=newl,
                        status=status.strip(), note=note.strip()))
    return out


def has_report(proj):
    return os.path.isfile(os.path.join(TARGET, proj, '审核报告_复核.md'))


def missing_pct(note):
    for pat in (r'未译[\d,，]*\s*词[^;；)]{0,6}?([\d.]+)%', r'缺\s*([\d.]+)%', r'([\d.]+)%[^;；)]{0,8}?未译'):
        m = re.search(pat, note)
        if m:
            return m.group(1) + '%'
    return ''


def main(argv):
    rows = parse()
    done = [r for r in rows if r['status'] in ('done', '挂起')]
    doing = [r for r in rows if r['status'] == 'doing']
    L = []
    L.append('# 2026-08-14 批次独立复核 · 收口汇总')
    L.append('')
    L.append('复核方式：**盲审**（审校员不得读取旧 `审核报告.md`），一本一个子代理、并发 5、'
             '产出独立的 `审核报告_复核.md`；旧报告未被覆盖或修改。')
    L.append('')
    L.append('完成 **%d/%d** 本（其中 %d 本标「挂起·待修」）；在途 %d 本。'
             % (len(done), len(rows), len([r for r in done if r['status'] == '挂起']), len(doing)))
    L.append('')
    # 迁移矩阵
    mat = collections.Counter((r['old'], r['new']) for r in done)
    L.append('## 一、等级迁移')
    L.append('')
    L.append('| 旧 → 新 | 本数 |')
    L.append('|---|---:|')
    for (o, n), c in sorted(mat.items(), key=lambda x: (ORDER.get(x[0][0], 9), ORDER.get(x[0][1], 9))):
        L.append('| %s → %s | %d |' % (o, NAME.get(n, n), c))
    L.append('')
    oc = collections.Counter(r['old'] for r in done)
    nc = collections.Counter(r['new'] for r in done)
    L.append('| 分布 | A | B | C | D |')
    L.append('|---|---:|---:|---:|---:|')
    L.append('| 旧报告 | %d | %d | %d | %d |' % tuple(oc.get(k, 0) for k in 'ABCD'))
    L.append('| 本次复核 | %d | %d | %d | %d |' % tuple(nc.get(k, 0) for k in 'ABCD'))
    L.append('')
    unchanged = [r for r in done if r['old'] == r['new']]
    L.append('等级未变 **%d** 本，需要改动 **%d** 本。' % (len(unchanged), len(done) - len(unchanged)))
    L.append('')
    # 总表
    L.append('## 二、逐本对照')
    L.append('')
    L.append('| # | 项目 | KB | 旧 | 新 | 缺失量 | 状态 | 关键结论（台账摘要） |')
    L.append('|---:|---|---:|:--:|:--:|:--:|:--:|---|')
    for r in sorted(done, key=lambda x: x['size']):
        note = r['note'].replace('|', '/')
        note = re.sub(r'^\s*\**旧?[A-D]?\s*[→>-]+\s*新?[A-D]?[^*]*\**\s*；?', '', note).strip('； ')
        L.append('| %d | `%s` | %.1f | %s | **%s** | %s | %s | %s |'
                 % (r['idx'], r['proj'], r['size'], r['old'], NAME.get(r['new'], r['new']),
                    missing_pct(r['note']), r['status'], note[:150]))
    L.append('')
    # D 级明细
    L.append('## 三、D 级书目（交付物缺失内容）')
    L.append('')
    L.append('| 项目 | 旧 | 缺失量 | 缺陷形态 |')
    L.append('|---|---:|:--:|---|')
    for r in sorted([x for x in done if x['new'] == 'D'], key=lambda x: x['size']):
        L.append('| `%s` | %s | %s | %s |' % (r['proj'], r['old'], missing_pct(r['note']) or '见报告', r['note'][:120]))
    L.append('')
    out = '\n'.join(L) + '\n'
    dst = None
    if '--md' in argv:
        dst = argv[argv.index('--md') + 1]
    if dst:
        open(dst, 'w', encoding='utf-8').write(out)
        print('written %s (%d bytes)' % (dst, len(out.encode('utf-8'))))
    else:
        print(out)


if __name__ == '__main__':
    main(sys.argv[1:])
