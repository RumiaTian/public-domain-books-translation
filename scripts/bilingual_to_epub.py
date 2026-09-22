#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
bilingual_to_epub.py — 把双语对照 md 转成 EPUB，译文用淡黄色背景区分。

用法:
    python3 bilingual_to_epub.py <输入.md> <输出.epub> [--title 标题] [--author 作者]

输入格式（唯一支持）:
    每个段落块用显式标记标注语言，标记独占一行，前后各三个等号：
        ===Original===
        English text
        ===Chinese===
        中文译文

    标题（#/##/###）合并写成一行「英文 / 中文」，不加块标记：
        ## Safety Instructions / 安全指令

输入契约见 prompts/通用翻译引擎.md 第五节。标记格式由标记直接声明语言，
不依赖交替结构，也不受译文块含大量英文运算符的影响。

原理:
    1. 状态机逐行扫描：===Original=== 块原样输出，===Chinese=== 块包进
       ::: {.translation} 围栏 div（pandoc 转成 <div class="translation">）。
       标题行作为游离内容，不进任何块、不加译文背景。
    2. pandoc 转 EPUB3，注入 CSS：译文淡黄底色，字体一律阅读器默认。

依赖: pandoc (命令行)
"""
import argparse
import os
import re
import subprocess
import sys
import tempfile

# 标记格式：独占一行的 ===Original=== 或 ===Chinese===（等号数≥3，大小写不敏感）
_MARKER_RE = re.compile(r'^={3,}\s*(original|chinese)\s*={0,}\s*$', re.IGNORECASE)
# 标题行：以 # 开头
_HEADING_RE = re.compile(r'^#{1,6}\s')


def process_markdown(md_text):
    """把标记格式的双语 md 转成 pandoc 可渲染的 md。

    状态机逐行扫描，三种段落类型：
    - Original 块：原样输出（原文无背景）
    - Chinese 块：包进 ::: {.translation} 围栏 div（译文淡黄背景）
    - 游离内容（标题等）：原样输出，不进任何块
    标题行会中断当前块，作为游离内容独立处理。
    """
    out = []
    buf = []         # 当前块的内容行
    cur_type = None  # 'original' | 'chinese' | None(游离)

    def flush():
        nonlocal buf, cur_type
        content = '\n'.join(buf).strip()
        if content:
            if cur_type == 'chinese':
                out.append('::: {.translation}')
                out.append('')
                out.append(content)
                out.append('')
                out.append(':::')
                out.append('')
            else:  # original 或游离，原样输出
                out.append(content)
                out.append('')
        buf = []
        cur_type = None

    for line in md_text.split('\n'):
        m = _MARKER_RE.match(line)
        if m:
            flush()
            cur_type = m.group(1).lower()
            continue
        # 标题行：结束当前块，标题作为游离内容
        if _HEADING_RE.match(line):
            flush()
            cur_type = None
        buf.append(line)
    flush()

    return '\n'.join(out)


EPUB_CSS = """
/* 译文：淡黄色背景 + 左边竖线，字体一律阅读器默认 */
div.translation {
    background-color: #FFF8DC;
    border-left: 3px solid #E0C36A;
    padding: 0.6em 0.9em;
    margin: 0.6em 0;
    page-break-inside: avoid;
}
/* 原文段无特殊样式，用阅读器默认字体 */
/* 代码块保持等宽字体 */
pre, code { font-family: monospace; }
"""


def build_epub(processed_md, css_path, out_epub, title, author):
    cmd = [
        'pandoc',
        # 关闭 yaml_metadata_block：部分文件开头有形似 YAML 的内容会被误判。
        '-f', 'markdown+pipe_tables+backtick_code_blocks+fenced_code_blocks-yaml_metadata_block',
        '-t', 'epub3',
        '--standalone',
        '--toc',
        '--css', css_path,
        '--metadata', f'title={title}',
        '--metadata', f'author={author}',
        '--metadata', 'lang=zh-CN',
        '-o', out_epub,
    ]
    result = subprocess.run(cmd, input=processed_md, capture_output=True, text=True)
    if result.returncode != 0:
        print('pandoc 出错:', result.stderr, file=sys.stderr)
        sys.exit(1)


def main():
    ap = argparse.ArgumentParser(description='双语 md 转 EPUB（译文淡黄背景）')
    ap.add_argument('input', help='输入 md 文件（===标记=== 格式）')
    ap.add_argument('output', help='输出 epub 文件')
    ap.add_argument('--title', default='双语对照', help='书名')
    ap.add_argument('--author', default='', help='作者')
    args = ap.parse_args()

    md_text = open(args.input, encoding='utf-8').read()
    processed = process_markdown(md_text)

    with tempfile.TemporaryDirectory() as tmp:
        css_path = os.path.join(tmp, 'style.css')
        open(css_path, 'w', encoding='utf-8').write(EPUB_CSS)
        build_epub(processed, css_path, args.output, args.title, args.author)

    print(f'已生成: {args.output}')


if __name__ == '__main__':
    main()
