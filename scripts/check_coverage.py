#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
check_coverage.py — 检查译文是否覆盖原文的每一段（防整段漏译）。

原理：把原文按非空段落切分，对每个原文段，在译文的 ===Original=== 块集合里
找一个最相似的（基于词/token 重叠率）。重叠率低于阈值则报告为可疑漏译。

用法:
    python3 check_coverage.py <原文.md> <译文.zh-CN.md>

退出码: 有可疑漏译（重叠率<阈值）时非零。
"""
import re
import sys
from difflib import SequenceMatcher

MARKER_RE = re.compile(r'^={3,}\s*(original|chinese)\s*={0,}\s*$', re.IGNORECASE)


def extract_original_blocks(trans_path):
    """从译文里抽出所有 ===Original=== 块的文本，合并成一个大字符串。"""
    md = open(trans_path, encoding='utf-8').read()
    blocks = []
    cur_type = None
    buf = []
    for line in md.split('\n'):
        m = MARKER_RE.match(line)
        if m:
            if cur_type == 'original':
                blocks.append('\n'.join(buf).strip())
            cur_type = m.group(1).lower()
            buf = []
            continue
        # 跳过标题行（不进 original 块内容会影响段落，但其实标题不含正文，留着也无妨）
        buf.append(line)
    if cur_type == 'original':
        blocks.append('\n'.join(buf).strip())
    return blocks


def tokenize(s):
    """粗略分词：英文按单词、中文按字符，去标点和空白。"""
    s = re.sub(r'[\s\.,;:!?\'"`\(\)\[\]\{\}<>\-—–…·、。，；：！？""''（）【】《》\n\r\t]', '', s)
    return s.lower()


def split_paragraphs(src_path):
    """原文按空行分段，去掉标题行和纯分隔符行。"""
    md = open(src_path, encoding='utf-8').read()
    paras = []
    for chunk in re.split(r'\n\s*\n', md):
        chunk = chunk.strip()
        if not chunk:
            continue
        # 跳过标题行 / 分隔线
        lines = [ln for ln in chunk.split('\n')
                 if not ln.strip().startswith('#')
                 and ln.strip() not in ('---',)]
        cleaned = '\n'.join(lines).strip()
        if cleaned:
            paras.append(cleaned)
    return paras


def main():
    if len(sys.argv) != 3:
        print('用法: python3 check_coverage.py <原文.md> <译文.zh-CN.md>', file=sys.stderr)
        sys.exit(2)
    src_path, trans_path = sys.argv[1], sys.argv[2]
    paras = split_paragraphs(src_path)
    blocks = extract_original_blocks(trans_path)

    # 把所有 original 块拼起来作为匹配池
    pool = '\n\n'.join(blocks)
    pool_tok = tokenize(pool)

    threshold = 0.55  # 重叠率阈值
    suspicious = []
    for i, p in enumerate(paras):
        p_tok = tokenize(p)
        if len(p_tok) < 8:
            continue  # 太短的段（如单行对话标记）跳过
        # 用 SequenceMatcher 算 ratio（基于字符序列）
        ratio = SequenceMatcher(None, p_tok, pool_tok).ratio()
        # ratio 在 pool 远大于 p 时会被稀释，改用覆盖率：p 中连续片段有多少出现在 pool
        # 用更直接的：把 p 切成 20-gram，看多少出现在 pool
        gram = 20
        if len(p_tok) >= gram:
            grams = [p_tok[i:i+gram] for i in range(0, len(p_tok)-gram+1, max(1, gram//2))]
            hits = sum(1 for g in grams if g in pool_tok)
            cov = hits / len(grams)
        else:
            cov = 1.0 if p_tok in pool_tok else 0.0
        if cov < threshold:
            suspicious.append((i, cov, p[:70].replace('\n', ' ')))

    print(f'文件: {trans_path}')
    print(f'原文段落数: {len(paras)}, 译文 Original 块数: {len(blocks)}')
    print(f'可疑漏译段（覆盖率 < {threshold}）: {len(suspicious)} 处')
    for idx, cov, preview in suspicious[:30]:
        print(f'  [段{idx}] 覆盖率{cov:.2f} | {preview}...')
    if len(suspicious) > 30:
        print(f'  ...还有 {len(suspicious)-30} 处未显示')
    sys.exit(1 if suspicious else 0)


if __name__ == '__main__':
    main()
