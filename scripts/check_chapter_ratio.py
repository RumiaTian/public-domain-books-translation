# -*- coding: utf-8 -*-
"""逐章译率筛查（阶段三辅助工具）

用途：抓「整章（或大段）未译但素材完整、块对自洽、台账标 done」这类隐蔽缺陷
（判例：h-c-mcneile_the-black-gang chapter-14，原 35,984B/149 段，译文仅 4,090B/3 块对）。

方法：对每章分别统计
  * 原文：`原文/<章>.md` 的拉丁字母数
  * 译文：`译文/<章>.zh-CN.md` 中 `===Chinese===` 块内的汉字数
  比值 = 汉字数 / 拉丁字母数（正常中译本约 0.30–0.75；未译章会跌到 0.1 以下）

用法：
  python scripts/check_chapter_ratio.py <项目名> [<项目名> ...] [--min-ratio 0.20] [--all-in 列表文件]
"""
import re, os, sys, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJ = os.path.join(ROOT, '翻译项目')


def zh_blocks(text):
    return [m.group(1) for m in re.finditer(r'===Chinese===\n(.*?)(?====Original===|\Z)', text, re.S)]


def check(book, min_ratio=0.20, quiet=False):
    pdir = os.path.join(PROJ, book)
    srcs = sorted(glob.glob(os.path.join(pdir, '原文', '*.md')))
    if not srcs:
        print('### %s  <无原文>' % book); return []
    rows = []
    for s in srcs:
        base = os.path.basename(s)
        zp = os.path.join(pdir, '译文', base.replace('.md', '.zh-CN.md'))
        en_src = open(s, encoding='utf-8', errors='ignore').read()
        n_lat = len(re.findall(r'[A-Za-z]', en_src))
        if not os.path.exists(zp):
            rows.append((base, n_lat, None, 0.0)); continue
        t = open(zp, encoding='utf-8', errors='ignore').read()
        n_zh = sum(len(re.findall(r'[\u4e00-\u9fff]', b)) for b in zh_blocks(t))
        ratio = n_zh / n_lat if n_lat else 0.0
        rows.append((base, n_lat, n_zh, ratio))
    low = [r for r in rows if r[2] is not None and r[3] < min_ratio]
    miss = [r for r in rows if r[2] is None]
    flag = '  ★★%d章偏低' % len(low) if low else ''
    print('### %-58s %3d章 译率中位=%.2f%s%s' % (
        book, len(rows),
        sorted(r[3] for r in rows if r[2] is not None)[len(rows) // 2] if rows else 0,
        flag, '  ★%d章无译文' % len(miss) if miss else ''))
    if not quiet:
        for b, nl, nz, ra in sorted(rows, key=lambda x: x[3])[:8]:
            mark = '  <<<' if ra < min_ratio else ''
            print('      %-46s 原文%7d字母  译文%7d汉字  比%.2f%s' % (b, nl, nz or 0, ra, mark))
    return low


if __name__ == '__main__':
    argv = sys.argv[1:]
    min_ratio = 0.20
    if '--min-ratio' in argv:
        i = argv.index('--min-ratio'); min_ratio = float(argv[i + 1]); argv = argv[:i] + argv[i + 2:]
    if argv and argv[0] == '--all-in':
        books = [l.strip() for l in open(argv[1], encoding='utf-8') if l.strip()]
        quiet = True
    else:
        books = argv; quiet = False
    for b in books:
        check(b, min_ratio, quiet)
