#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
epub_to_md.py — 从 Standard Ebooks 风格的 EPUB 中按 spine 顺序提取正文，每章一个 markdown 文件。

用法：
    python epub_to_md.py <epub文件> <输出目录>

规则（对齐 WORKFLOW.md 第 2 步）：
- 解压 epub，读 META-INF/container.xml 找到 OPF
- 按 OPF 的 spine 顺序处理 xhtml
- <h1>/<h2> → # / ##；<p> → 段落；<hr/> → ---；<em>/<i> → *x*；<strong>/<b> → **x**
- 去 HTML 实体、去缩进、跳过版权页/colophon/imprint/titlepage/halftitlepage/uncopyright/dedication(默认保留 dedication/preface 见 --front)
- 去除 epub:type 标记的 frontmatter（titlepage/imprint/colophon/uncopyright）等非正文
- 文件名用章节标题转 kebab-case；无标题的用 spine 序号
- 输出 UTF-8 不带 BOM
"""
import sys
import os
import re
import zipfile
import xml.etree.ElementTree as ET
from html import unescape

# Standard Ebooks 里需要跳过的 epub:type 关键词
SKIP_TYPES = {
    "titlepage", "halftitlepage", "colophon", "imprint", "uncopyright",
    "copyright-page", "frontmatter", "rearmatter", "publisher",
}
# 这些虽然属于 frontmatter 但内容可能是正文（前言/献词），默认保留
KEEP_FRONT = {"preface", "introduction", "foreword", "dedication", "prologue",
              "epigraph", "preamble", "acknowledgments", "note", "afterword"}


def kebab(s):
    s = unescape(s).strip()
    # 保留字母数字，其余转 -
    s = re.sub(r"[^A-Za-z0-9]+", "-", s).strip("-").lower()
    # Windows 路径上限 260：截断超长标题（如哈格德《克利奥帕特拉》整段式章名），重名由调用方 -n 去重
    if len(s) > 80:
        s = s[:80].rstrip("-")
    return s or "untitled"


def strip_ns(tag):
    return tag.split("}", 1)[-1] if "}" in tag else tag


def get_epub_types(el):
    """从元素及祖先的 epub:type 属性收集语义类型关键词。"""
    types = set()
    cur = el
    while cur is not None:
        t = cur.get("epub:type") or cur.get("{http://www.idpf.org/2007/ops}type")
        if t:
            types.update(t.split())
        cur = cur  # 只看自身（祖先判断单独在 parse 时做）
        break
    return types


def _render_table(el, lines, quote=False):
    """渲染 <table>（此前整表被丢弃）。
    - z3998:drama 对话表：每行 = 人物 td + 台词 td → 「**人物.** 台词」段落
    - 其它表（如诗歌对齐表）：逐行逐格渲染文本行
    """
    prefix = "> " if quote else ""
    etypes = get_epub_types(el)
    is_drama = "z3998:drama" in etypes or "drama" in etypes
    rows = [r for r in el.iter() if isinstance(r.tag, str) and strip_ns(r.tag) == "tr"]
    for r in rows:
        cells = [c for c in r if isinstance(c.tag, str) and strip_ns(c.tag) == "td"]
        if not cells:
            continue
        if is_drama and len(cells) >= 2:
            persona = _inline(cells[0]).strip()
            speeches = []
            for c in cells[1:]:
                for p in c.iter():
                    if isinstance(p.tag, str) and strip_ns(p.tag) == "p":
                        t = _inline(p).strip()
                        if t:
                            speeches.append(t)
                # td 直接文本（无 p 包裹）
                if not any(isinstance(x.tag, str) and strip_ns(x.tag) == "p" for x in c.iter()):
                    t = _inline(c).strip()
                    if t:
                        speeches.append(t)
            if speeches:
                if persona:
                    lines.append(prefix + "**" + persona + ".** " + speeches[0])
                else:
                    lines.append(prefix + speeches[0])
                for s in speeches[1:]:
                    lines.append(prefix + s)
        else:
            for c in cells:
                t = _inline(c).strip()
                t = re.sub(r"\s*\n\s*", "\n", t)
                if t:
                    for ln in t.split("\n"):
                        if ln.strip():
                            lines.append(prefix + ln.strip())


def render(el, lines):
    """递归把元素渲染为 markdown 行（列表形式），保留段落/标题/引用/列表结构。"""
    tag = strip_ns(el.tag)
    # 先看是否有 epub:type 标记需跳过
    etypes = get_epub_types(el)
    if etypes & SKIP_TYPES and not (etypes & KEEP_FRONT):
        return

    if tag == "hgroup":
        # 合并序号(h2) + 章名(p[epub:type=title]) 为一个 ## 标题
        ordinal = ""
        title = ""
        for c in el:
            if not isinstance(c.tag, str):
                continue
            ct = strip_ns(c.tag)
            ctypes = get_epub_types(c)
            txt = _inline(c).strip()
            if not txt:
                continue
            if ct in ("h1", "h2", "h3", "h4", "h5"):
                ordinal = txt
            elif ct == "p":
                if "z3998:title" in ctypes or "title" in ctypes or not title:
                    title = txt
                else:
                    # 普通段落不应出现在 hgroup，但容错
                    if not ordinal:
                        ordinal = txt
        combined = (ordinal + " " + title).strip() if (ordinal and title) else (title or ordinal)
        if combined:
            lines.append("## " + combined)
        return
    if tag in ("h1", "h2", "h3", "h4", "h5"):
        level = {"h1": 1, "h2": 2, "h3": 3, "h4": 4, "h5": 5}[tag]
        # 标题内 <br/> 会产生硬换行，导致标题被断成两行（第二行丢失 # 前缀）→ 折叠为空格
        txt = re.sub(r"\s*\n\s*", " ", inline_text(el))
        if txt.strip():
            lines.append("#" * level + " " + txt.strip())
        return
    if tag == "p":
        txt = inline_text(el)
        if txt.strip():
            lines.append(txt.strip())
        return
    if tag == "blockquote":
        lines.append("")  # 引用前空行
        # 引用内段落用 > 前缀
        for child in el:
            ctag = strip_ns(child.tag)
            if ctag == "p":
                txt = inline_text(child).strip()
                if txt:
                    lines.append("> " + txt)
            elif ctag == "footer":
                for cc in child:
                    if strip_ns(cc.tag) == "p":
                        txt = inline_text(cc).strip()
                        if txt:
                            lines.append("> " + txt)
            elif ctag == "cite":
                # 引用出处（此前被丢弃）：> — 出处
                txt = inline_text(child).strip()
                if txt:
                    lines.append("> — " + txt)
            elif ctag == "table":
                _render_table(child, lines, quote=True)
        lines.append("")
        return
    if tag == "table":
        _render_table(el, lines)
        return
    if tag == "hr":
        lines.append("---")
        return
    if tag in ("ul", "ol"):
        idx = 0
        for child in el:
            if strip_ns(child.tag) == "li":
                idx += 1
                txt = inline_text(child).strip()
                marker = f"{idx}. " if tag == "ol" else "- "
                if txt:
                    lines.append(marker + txt)
        return
    # 其它容器：递归子元素
    for child in el:
        render(child, lines)


def inline_text(el):
    """把元素内联文本渲染为 markdown 行内文本（处理 em/strong/br）。"""
    parts = []
    for node in el.iter():
        if node is el:
            continue
        if node.tag is ET.Comment:
            continue
        tag = strip_ns(node.tag) if isinstance(node.tag, str) else ""
        if tag == "br":
            parts.append("  \n")  # markdown 硬换行
            continue
    # 用递归方式更可靠
    return _inline(el)


def _inline(el):
    out = []
    if el.text:
        out.append(unescape(el.text))
    for child in el:
        if isinstance(child.tag, str):
            ctag = strip_ns(child.tag)
            if ctag == "br":
                out.append("  \n")
                if child.tail:
                    out.append(unescape(child.tail))
                continue
            inner = _inline(child)
            stripped = inner.strip()
            if ctag in ("em", "i"):
                if stripped:
                    out.append("*" + stripped + "*")
                else:
                    out.append(inner)
                if child.tail:
                    out.append(unescape(child.tail))
            elif ctag in ("strong", "b"):
                if stripped:
                    out.append("**" + stripped + "**")
                else:
                    out.append(inner)
                if child.tail:
                    out.append(unescape(child.tail))
            else:
                out.append(inner)
                if child.tail:
                    out.append(unescape(child.tail))
    return re.sub(r"[ \t]+", " ", "".join(out))


def clean_lines(lines):
    """合并多余空行、去掉首尾空白、按段落规整。"""
    out = []
    prev_blank = False
    for ln in lines:
        ln = ln.rstrip()
        is_blank = (ln == "")
        if is_blank and prev_blank:
            continue
        out.append(ln)
        prev_blank = is_blank
    # 去尾
    while out and out[-1] == "":
        out.pop()
    return out


def extract_chapter_title(root, default):
    """从章节提取标题（用于文件命名）。优先 <hgroup>/<h2>/<h1>。"""
    body = root.find(".//{http://www.w3.org/1999/xhtml}body")
    if body is not None:
        # 找第一个 h1/h2 或 hgroup 内 title
        for h in body.iter():
            if not isinstance(h.tag, str):
                continue
            tag = strip_ns(h.tag)
            if tag == "hgroup":
                # 取 hgroup 内 p[epub:type=title] 或 h2
                title_parts = []
                for c in h.iter():
                    if not isinstance(c.tag, str):
                        continue
                    ct = strip_ns(c.tag)
                    if ct in ("h1", "h2", "p"):
                        txt = _inline(c).strip()
                        if txt:
                            title_parts.append(txt)
                if title_parts:
                    return title_parts[-1]  # 用标题部分（通常第二行是章名）
            if tag in ("h1", "h2", "h3"):
                txt = _inline(h).strip()
                if txt:
                    return txt
    return default


def has_skipped_type(root):
    """检查 body 或 section 是否标记了需跳过的 epub:type。"""
    body = root.find(".//{http://www.w3.org/1999/xhtml}body")
    if body is None:
        return True
    # 检查 body 和直接子 section
    etypes_all = set()
    for el in [body] + list(body.iter()):
        et = el.get("epub:type") or el.get("{http://www.idpf.org/2007/ops}type")
        if et:
            etypes_all.update(et.split())
    if etypes_all & SKIP_TYPES:
        # 如果同时有 KEEP_FRONT，保留
        if etypes_all & KEEP_FRONT:
            return False
        return True
    return False


def emit_md(title, lines, out_dir, seen_titles, written):
    """按标题写一个 md 文件（kebab + 去重），并记入 written。"""
    base = kebab(title)
    n = seen_titles.get(base, 0) + 1
    seen_titles[base] = n
    fname = base if n == 1 else f"{base}-{n}"
    out_path = os.path.join(out_dir, fname + ".md")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines) + "\n")
    written.append((fname + ".md", len("\n".join(lines).encode("utf-8")) / 1024.0))


def extract_title_in(el):
    """从 article 等容器内提取标题（hgroup/h1/h2/h3 顺序），无则返回 None。"""
    for h in el.iter():
        if not isinstance(h.tag, str):
            continue
        tag = strip_ns(h.tag)
        if tag in ("h1", "h2", "h3"):
            txt = _inline(h).strip()
            if txt:
                return txt
    return None


def process_epub(epub_path, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    with zipfile.ZipFile(epub_path) as zf:
        names = zf.namelist()
        # 找 container.xml
        container = ET.fromstring(zf.read("META-INF/container.xml"))
        ns_c = {"c": "urn:oasis:names:tc:opendocument:xmlns:container"}
        opf_path = container.find(".//c:rootfile", ns_c).get("full-path")
        opf_dir = os.path.dirname(opf_path)
        opf = ET.fromstring(zf.read(opf_path))

        # 解析 manifest: id -> href
        manifest = {}
        for item in opf.iter():
            if strip_ns(item.tag) == "item":
                iid = item.get("id")
                href = item.get("href")
                media = item.get("media-type", "")
                if iid and href and "html" in media or media == "application/xhtml+xml":
                    manifest[iid] = (href, media)
        # spine 顺序
        spine_ids = []
        for item in opf.iter():
            if strip_ns(item.tag) == "itemref":
                idref = item.get("idref")
                if idref:
                    spine_ids.append(idref)

        written = []
        seen_titles = {}
        for sid in spine_ids:
            if sid not in manifest:
                continue
            href, media = manifest[sid]
            if "html" not in media and "xhtml" not in media and media != "application/xhtml+xml":
                continue
            full = os.path.normpath(os.path.join(opf_dir, href)).replace("\\", "/")
            try:
                content = zf.read(full)
            except KeyError:
                continue
            try:
                root = ET.fromstring(content)
            except ET.ParseError as e:
                sys.stderr.write(f"解析失败 {full}: {e}\n")
                continue
            # 跳过非正文
            if has_skipped_type(root):
                continue
            default_title = os.path.splitext(os.path.basename(href))[0]
            title = extract_chapter_title(root, default_title)
            # 渲染
            body = root.find(".//{http://www.w3.org/1999/xhtml}body")
            if body is None:
                continue
            # 诗集/短篇集常把全部篇目放同一 xhtml：每篇一个 <article>。
            # 多 article 时逐篇渲染输出（一篇一个 md），避免只取第一个截断全书。
            arts = [c for c in body.iter() if isinstance(c.tag, str) and strip_ns(c.tag) == "article"]
            if len(arts) > 1:
                for art in arts:
                    art_title = extract_title_in(art) or title
                    art_lines = []
                    for child in art:
                        render(child, art_lines)
                    art_lines = clean_lines(art_lines)
                    if not art_lines:
                        continue
                    emit_md(art_title, art_lines, out_dir, seen_titles, written)
                continue
            lines = []
            # 直接遍历 body 下的顶层 article/section/p 等
            # 优先找 article（Standard Ebooks 短篇/章节容器：h3 标题 + 若干 section 分节），
            # 其内部 section 会经 render 递归完整渲染；只取第一个 section 会截断多节篇章
            target = arts[0] if arts else None
            if target is None:
                for c in body.iter():
                    if isinstance(c.tag, str) and strip_ns(c.tag) == "section":
                        target = c
                        break
            if target is None:
                target = body
            for child in target:
                render(child, lines)
            lines = clean_lines(lines)
            if not lines:
                continue
            emit_md(title, lines, out_dir, seen_titles, written)
        return written


def main():
    if len(sys.argv) != 3:
        sys.stderr.write("用法: python epub_to_md.py <epub文件> <输出目录>\n")
        sys.exit(2)
    epub_path, out_dir = sys.argv[1], sys.argv[2]
    if not os.path.isfile(epub_path):
        sys.stderr.write(f"找不到 epub: {epub_path}\n")
        sys.exit(2)
    written = process_epub(epub_path, out_dir)
    for fname, size in written:
        print(f"{fname}\t{size:.1f}KB")


if __name__ == "__main__":
    main()
