# -*- coding: utf-8 -*-
"""审核门禁盘点（阶段三辅助工具）

按 3_审核WORKFLOW.md 的门禁条件扫描全库，列出可审且尚无 审核报告.md 的项目（按原文体积升序）：
  1) 项目 translation_queue.csv 全部 done；2) 译文/*.zh-CN.md 数 ≥ done 数；
  3) 项目说明.md / 术语表.md / 原文/ / 译文/ 齐备；4) 无既有 审核报告.md；5) 项目 CSV 亦全 done。

用法：python scripts/gate_scan_review.py [--top N]
"""
import csv, os, glob, sys, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJ = os.path.join(ROOT, '翻译项目')


def scan():
    with open(os.path.join(ROOT, 'translation_queue.csv'), encoding='utf-8-sig') as f:
        rows = list(csv.DictReader(f))
    by_proj = collections.OrderedDict()
    for r in rows:
        p = r['project'].strip()
        by_proj.setdefault(p, []).append(r)
    eligible = []
    for p, rs in by_proj.items():
        pdir = os.path.join(PROJ, p)
        if not os.path.isdir(pdir):
            continue
        n_done = sum(1 for r in rs if (r.get('status') or '').strip().lower() == 'done')
        if n_done == 0:
            continue
        if any((r.get('status') or '').strip().lower() != 'done' for r in rs):
            continue
        zh = glob.glob(os.path.join(pdir, '译文', '*.zh-CN.md'))
        if len(zh) < n_done:
            continue
        if not all(os.path.exists(os.path.join(pdir, x)) for x in ('项目说明.md', '术语表.md', '原文', '译文')):
            continue
        if os.path.exists(os.path.join(pdir, '审核报告.md')):
            continue
        pcsv = os.path.join(pdir, 'translation_queue.csv')
        if os.path.exists(pcsv):
            with open(pcsv, encoding='utf-8-sig') as f:
                prows = list(csv.DictReader(f))
            if any((r.get('status') or '').strip().lower() != 'done' for r in prows):
                continue
        size = sum(float(r['size_kb']) for r in rs if (r.get('size_kb') or '').strip())
        extra = len(zh) - n_done
        eligible.append((size, p, n_done, len(rs), extra))
    eligible.sort()
    return eligible


if __name__ == '__main__':
    top = 25
    if '--top' in sys.argv:
        top = int(sys.argv[sys.argv.index('--top') + 1])
    el = scan()
    print("=== 可审池（升序）共 %d 本 ===" % len(el))
    for i, (size, p, n_done, n_files, extra) in enumerate(el[:top], 1):
        flag = " [译文多%d个文件]" % extra if extra else ""
        print("%2d. %7.1fKB  %-55s done=%d rows=%d%s" % (i, size, p, n_done, n_files, flag))
