#!/usr/bin/env python3
"""Extract a play epub (table-based dialogue) into clean markdown.

Converts <table><tr><td>persona</td><td>line</td></tr></table> into:
**Persona**: line

Usage: python scripts/extract_play.py <extracted_dir> <project_name> <chapter_list_file>
"""
import sys
import os
import re
from html import unescape


def clean_inline(html):
    """Convert inline tags to markdown."""
    # bold persona names
    html = re.sub(r'<b[^>]*epub:type="[^"]*z3998:persona[^"]*"[^>]*>(.*?)</b>', r'**\1**', html, flags=re.DOTALL)
    # stage directions (italic)
    html = re.sub(r'<i[^>]*epub:type="[^"]*z3998:stage-direction[^"]*"[^>]*>(.*?)</i>', r'*（\1）*', html, flags=re.DOTALL)
    # generic em/italic
    html = re.sub(r'<i[^>]*>(.*?)</i>', r'*\1*', html, flags=re.DOTALL)
    html = re.sub(r'<em[^>]*>(.*?)</em>', r'*\1*', html, flags=re.DOTALL)
    # generic bold
    html = re.sub(r'<b[^>]*>(.*?)</b>', r'**\1**', html, flags=re.DOTALL)
    html = re.sub(r'<strong[^>]*>(.*?)</strong>', r'**\1**', html, flags=re.DOTALL)
    # br
    html = re.sub(r'<br\s*/?>', '\n', html)
    # drop links (footnote refs)
    html = re.sub(r'<a[^>]*>.*?</a>', '', html, flags=re.DOTALL)
    return html


def convert_play_chapter(xhtml_path):
    with open(xhtml_path, encoding='utf-8') as f:
        content = f.read()
    # extract body
    body_match = re.search(r'<body[^>]*>(.*)</body>', content, re.DOTALL)
    if not body_match:
        return ''
    body = body_match.group(1)
    # remove section/article wrappers but keep content
    out_lines = []

    # First, handle the heading (hgroup/h1/h2)
    # Find all top-level structural blocks in order

    # Split body by tables and other block elements, process each
    # Strategy: process the body sequentially

    # Extract hgroup headings first (they appear before content)
    def replace_hgroup(m):
        inner = m.group(1)
        # collect text of h1/h2/p inside
        texts = re.findall(r'<h[12][^>]*>(.*?)</h[12]>', inner, re.DOTALL)
        texts = [re.sub(r'<[^>]+>', ' ', t) for t in texts]
        texts = [re.sub(r'\s+', ' ', t).strip() for t in texts]
        texts = [unescape(t) for t in texts if t.strip()]
        if texts:
            return '\n\n## ' + ' '.join(texts) + '\n\n'
        return ''

    body = re.sub(r'<hgroup[^>]*>(.*?)</hgroup>', replace_hgroup, body, flags=re.DOTALL)

    # Now handle single h1/h2
    def replace_h(m):
        tag = m.group(1)
        inner = re.sub(r'<[^>]+>', ' ', m.group(2))
        inner = unescape(inner)
        inner = re.sub(r'\s+', ' ', inner).strip()
        if inner:
            return f'\n\n## {inner}\n\n'
        return ''
    body = re.sub(r'<(h[12])[^>]*>(.*?)</\1>', replace_h, body, flags=re.DOTALL)
    def replace_h3(m):
        inner = re.sub(r'<[^>]+>', ' ', m.group(1))
        inner = unescape(inner)
        inner = re.sub(r'\s+', ' ', inner).strip()
        return f'\n\n### {inner}\n\n' if inner else ''
    body = re.sub(r'<h3[^>]*>(.*?)</h3>', replace_h3, body, flags=re.DOTALL)

    # Process tables: each row -> **persona**: line
    def replace_table(m):
        table_html = m.group(1)
        rows = re.findall(r'<tr[^>]*>(.*?)</tr>', table_html, re.DOTALL)
        result = []
        for row in rows:
            tds = re.findall(r'<td[^>]*>(.*?)</td>', row, re.DOTALL)
            if len(tds) >= 2:
                persona = re.sub(r'<[^>]+>', '', tds[0]).strip()
                persona = unescape(persona)
                line = clean_inline(tds[1]).strip()
                line = re.sub(r'<[^>]+>', '', line)
                line = unescape(line)
                line = re.sub(r'\s+', ' ', line).strip()
                if persona and line:
                    result.append(f'**{persona}**：{line}')
                elif line:
                    result.append(line)
        return '\n\n' + '\n\n'.join(result) + '\n\n' if result else ''

    body = re.sub(r'<table[^>]*>(.*?)</table>', replace_table, body, flags=re.DOTALL)

    # Process paragraphs (stage description prose)
    def replace_p(m):
        inner = clean_inline(m.group(1))
        inner = re.sub(r'<[^>]+>', '', inner)
        inner = unescape(inner).strip()
        inner = re.sub(r'\s+', ' ', inner)
        return f'\n\n{inner}' if inner else ''
    body = re.sub(r'<p[^>]*>(.*?)</p>', replace_p, body, flags=re.DOTALL)

    # blockquotes (epigraphs)
    def replace_bq(m):
        inner = clean_inline(m.group(1))
        inner = re.sub(r'<[^>]+>', '', inner).strip()
        inner = unescape(inner)
        lines = inner.split('\n')
        return '\n\n' + '\n'.join('> ' + ln if ln.strip() else '' for ln in lines)
    body = re.sub(r'<blockquote[^>]*>(.*?)</blockquote>', replace_bq, body, flags=re.DOTALL)

    # hr
    body = re.sub(r'<hr\s*/?>', '\n\n---\n\n', body)

    # strip remaining tags
    body = re.sub(r'<[^>]+>', '', body)
    body = unescape(body)

    # normalize whitespace
    body = re.sub(r'\n{3,}', '\n\n', body)
    return body.strip() + '\n'


def main():
    if len(sys.argv) != 4:
        print("Usage: extract_play.py <extracted_dir> <project_name> <chapter_list_file>")
        sys.exit(1)
    extracted_dir, project_name, chapter_list = sys.argv[1], sys.argv[2], sys.argv[3]
    text_dir = os.path.join(extracted_dir, 'epub', 'text')
    out_dir = os.path.join('翻译项目', project_name, '原文')
    os.makedirs(out_dir, exist_ok=True)
    with open(chapter_list, encoding='utf-8') as f:
        entries = [ln.strip() for ln in f if ln.strip() and not ln.startswith('#')]
    total = 0
    for ln in entries:
        parts = ln.split(',')
        if len(parts) != 2:
            continue
        spine_file, out_base = parts[0].strip(), parts[1].strip()
        src = os.path.join(text_dir, spine_file)
        if not os.path.exists(src):
            print(f"MISSING: {src}")
            continue
        md = convert_play_chapter(src)
        out_path = os.path.join(out_dir, out_base + '.md')
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(md)
        size_kb = os.path.getsize(out_path) / 1024
        print(f"  {out_base}.md  {size_kb:.1f}KB")
        total += 1
    print(f"Done: {total} files -> {out_dir}")


if __name__ == '__main__':
    main()
