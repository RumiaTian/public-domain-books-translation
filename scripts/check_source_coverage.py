# -*- coding: utf-8 -*-
"""原文素材完整性核对（阶段三辅助工具）

用途：把项目 原文/*.md 与 原书/*.epub 的正文逐段比对，找出 **原文素材相对 epub 缺失的段落**
（阶段三实战发现的缺陷类型：多小节故事只抽出第一节、诗行/短段遗漏等；译文会同步缺译）。

判定：归一化（去标点/空白/变音符、统一引号破折号）后，epub 每段做"是否存在于 原文 md 全文"包含判定。
     仅报告长度 ≥ --min-chars 的段落（默认 60；诗集/含诗行的书建议 25，但噪声会上升）。

用法：
  python scripts/check_source_coverage.py <项目名> [<项目名> ...] [--min-chars 25]
输出：每个项目的检查段数 / 缺失段数 / 缺失段落样例（含 epub 文件名）。

已知局限：
  * 短段落（诗行、舞台提示）会被长度阈值滤掉——诗行缺失请用 --min-chars 25 复跑；
  * 若项目 原文 来自与 epub 不同的版本/选品（选集、选诗），缺失数会偏高且不代表缺陷，
    需人工核对是否为"选集差异"。
"""
import zipfile, re, os, sys, glob, html, posixpath, unicodedata

ROOT = r'C:\Users\HanTi\OneDrive\translate\翻译项目'


def norm(s):
    s = html.unescape(s)
    s = s.replace('æ', 'ae').replace('Æ', 'AE').replace('œ', 'oe').replace('Œ', 'OE')
    s = unicodedata.normalize('NFKD', s)
    s = ''.join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r'[^0-9A-Za-z\u4e00-\u9fff]', '', s)
    return s.lower()


def epub_paras(epub_path):
    paras = []
    with zipfile.ZipFile(epub_path) as z:
        cont = z.read('META-INF/container.xml').decode('utf-8', 'ignore')
        m = re.search(r'full-path="([^"]+\.opf)"', cont)
        if not m:
            return paras
        opf_path = m.group(1)
        base = os.path.dirname(opf_path)
        opf = z.read(opf_path).decode('utf-8', 'ignore')
        manifest = {}
        for mm in re.finditer(r'<item\b[^>]*>', opf):
            tag = mm.group(0)
            idm = re.search(r'id="([^"]+)"', tag)
            hm = re.search(r'href="([^"]+)"', tag)
            if idm and hm:
                manifest[idm.group(1)] = hm.group(1)
        order = []
        for sm in re.finditer(r'<itemref\b[^>]*>', opf):
            idm = re.search(r'idref="([^"]+)"', sm.group(0))
            if idm and idm.group(1) in manifest:
                order.append(manifest[idm.group(1)])
        skip = ('titlepage', 'imprint', 'colophon', 'uncopyright', 'halftitlepage', 'cover', 'toc', 'nav')
        for href in order:
            if any(p in skip for p in re.split(r'[/\\._-]', href.lower())):
                continue
            full = posixpath.join(base, href) if base else href
            try:
                txt = z.read(full).decode('utf-8', 'ignore')
            except KeyError:
                continue
            txt = re.sub(r'<(script|style)[^>]*>.*?</\1>', ' ', txt, flags=re.S | re.I)
            txt = re.sub(r'</(p|div|h1|h2|h3|h4|h5|li|blockquote|td|tr)>', '\n', txt, flags=re.I)
            txt = re.sub(r'<br\s*/?>', '\n', txt, flags=re.I)
            txt = re.sub(r'<[^>]+>', '', txt)
            for line in txt.split('\n'):
                line = html.unescape(line).strip()
                if line:
                    paras.append((href, line))
    return paras


def check(book, min_chars):
    pdir = os.path.join(ROOT, book)
    eps = glob.glob(os.path.join(pdir, '原书', '*.epub'))
    if not eps:
        print("### %s  <NO EPUB>" % book)
        return
    md_norm = norm('\n'.join(open(f, encoding='utf-8', errors='ignore').read()
                             for f in sorted(glob.glob(os.path.join(pdir, '原文', '*.md')))))
    paras = epub_paras(eps[0])
    missing = []
    checked = 0
    for href, line in paras:
        n = norm(line)
        if len(n) < min_chars:
            continue
        checked += 1
        if n not in md_norm:
            missing.append((href, line))
    print("### %s  检查 %d 段 (阈值%d), 缺失 %d 段" % (book, checked, min_chars, len(missing)))
    for href, line in missing[:12]:
        print("   [%s] %s" % (os.path.basename(href), line[:150]))


if __name__ == '__main__':
    argv = sys.argv[1:]
    min_chars = 60
    if '--min-chars' in argv:
        i = argv.index('--min-chars')
        min_chars = int(argv[i + 1])
        argv = argv[:i] + argv[i + 2:]
    for book in argv:
        check(book, min_chars)
