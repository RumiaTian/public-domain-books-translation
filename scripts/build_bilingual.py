#!/usr/bin/env python3
"""主模型直译拼装脚本：源文(每行一段) + 纯中文译文(每行一段) -> 双语对照文件。

用法: python scripts/build_bilingual.py <源文.md> <中文译文.txt> <输出.zh-CN.md>
规则:
- 源文与译文行数必须一致, 逐行对应
- 标题行(源文以 # 开头): 译文行以 # 开头(层级任意, 只取文本), 合并输出 "#... EN / ZH"
- 分隔线(源文行 == '---'): 译文行必须也是 '---', 做成对称块
- 普通段: ===Original===/===Chinese=== 成对块
- 输出 UTF-8 无 BOM, LF 行尾; 原文行原样保留(CRLF 统一转 LF, 隐形字符保留)
"""
import sys

def main():
    src_path, zh_path, out_path = sys.argv[1], sys.argv[2], sys.argv[3]
    with open(src_path, 'rb') as f:
        src_lines = [l.decode('utf-8').rstrip('\r\n') for l in f.readlines()]
    with open(zh_path, 'rb') as f:
        zh_lines = [l.decode('utf-8').rstrip('\r\n') for l in f.readlines()]

    if len(src_lines) != len(zh_lines):
        print(f"ERROR: 行数不一致 源文={len(src_lines)} 译文={len(zh_lines)}")
        sys.exit(1)

    out = []
    for i, (en, zh) in enumerate(zip(src_lines, zh_lines)):
        if en.startswith('#'):
            if not zh.startswith('#'):
                print(f"ERROR: 第{i+1}行源文是标题但译文不是标题: {zh[:30]}")
                sys.exit(1)
            zh_text = zh.lstrip('#').strip()
            out.append(f"{en} / {zh_text}")
        elif en.strip() == '---':
            if zh.strip() != '---':
                print(f"ERROR: 第{i+1}行源文是分隔线但译文不是: {zh[:30]}")
                sys.exit(1)
            out.append("===Original===\n---\n\n===Chinese===\n---")
        else:
            if not en.strip():
                if zh.strip():
                    print(f"ERROR: 第{i+1}行源文为空但译文非空")
                    sys.exit(1)
                out.append("")
                continue
            if not zh.strip():
                print(f"ERROR: 第{i+1}行译文为空: {en[:50]}")
                sys.exit(1)
            out.append(f"===Original===\n{en}\n\n===Chinese===\n{zh}")

    text = "\n\n".join(out) + "\n"
    text = text.replace('\n\n\n\n', '\n\n\n')
    with open(out_path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(text)
    n_pairs = sum(1 for en in src_lines if en.strip() and not en.startswith('#') and en.strip() != '---')
    print(f"OK: {len(src_lines)} 行, {n_pairs} 对普通块, 标题 "
          f"{sum(1 for l in src_lines if l.startswith('#'))} 个 -> {out_path}")

if __name__ == '__main__':
    main()
