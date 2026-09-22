# -*- coding: utf-8 -*-
"""epub spine 阅读序提取（阶段三辅助工具）

用途：当项目文件名为字母序（无编号/kebab 篇题）或字符串序有陷阱时，从 原书/*.epub 提取
      spine 权威阅读序与 NCX 目录标题，用于核定简报的阅读顺序、核对 原文 文件是否齐备。

用法：python scripts/epub_spine.py <项目名> [<项目名> ...]
"""
import zipfile, re, sys, os, glob, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJ = os.path.join(ROOT, '翻译项目')


def is_boilerplate(href, skip=('titlepage', 'imprint', 'colophon', 'uncopyright',
                               'halftitlepage', 'cover', 'toc', 'nav')):
    """按「路径/文件名分段」判定版式页，避免子串误伤（navy-day.xhtml 曾被子串 'nav' 误跳）。"""
    return any(p in skip for p in re.split(r'[/\\._-]', href.lower()))


def spine_order(epub_path):
    with zipfile.ZipFile(epub_path) as z:
        cont = z.read('META-INF/container.xml').decode('utf-8', 'ignore')
        m = re.search(r'full-path="([^"]+\.opf)"', cont)
        if not m:
            return [], {}
        opf_path = m.group(1)
        opf = z.read(opf_path).decode('utf-8', 'ignore')
        base = os.path.dirname(opf_path)
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
        titles = {}
        for name in z.namelist():
            if name.endswith('.ncx'):
                ncx = z.read(name).decode('utf-8', 'ignore')
                for nm in re.finditer(r'<navPoint\b.*?</navPoint>', ncx, re.S):
                    blk = nm.group(0)
                    tm = re.search(r'<text>(.*?)</text>', blk, re.S)
                    cm = re.search(r'src="([^"#]+)', blk)
                    if tm and cm:
                        titles.setdefault(cm.group(1), html.unescape(tm.group(1).strip()))
        _ = base
        return order, titles


def main(argv):
    for p in argv:
        d = os.path.join(PROJ, p, '原书')
        eps = glob.glob(os.path.join(d, '*.epub'))
        if not eps:
            print("### %s  <NO EPUB>" % p)
            continue
        order, titles = spine_order(eps[0])
        skip = ('titlepage', 'imprint', 'colophon', 'uncopyright', 'halftitlepage', 'cover', 'toc', 'nav')
        content = [h for h in order if not is_boilerplate(h, skip)]
        print("### %s  (spine content %d, total spine %d)" % (p, len(content), len(order)))
        for h in content:
            nm = os.path.basename(h).rsplit('.', 1)[0]
            t = titles.get(h, '')
            print("   %-52s | %s" % (nm, t))


if __name__ == '__main__':
    main(sys.argv[1:])
