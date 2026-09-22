#!/usr/bin/env python3
"""Rebuild the problematic section - v2 with fixed markers."""
PATH = r'C:\Users\HanTi\OneDrive\translate\翻译项目\clara-reeve_the-old-english-baron\译文\the-old-english-baron_part1.zh-CN.md'

with open(PATH, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# The current file has these issues after rebuild:
# 1. Lines 594 and 656: consecutive ===Original=== (first night Original + Baron aftermath Original)
# 2. Lines 730-731: consecutive ===Chinese=== (dream Chinese block has extra marker)
# 3. Lines 892-893: consecutive ===Chinese=== (Baron plan Chinese block has extra marker)

# Fix: Remove the extra markers at lines 656, 731, 893

# Line 656 (0-indexed: 655): Extra ===Original=== marker
# This is the Baron aftermath Original that was inserted between first night Original
# and first night Chinese. It should be removed because the Baron aftermath is now
# part of the first night's context.

# Lines 730-731 (0-indexed: 729-730): Extra ===Chinese===
# Line 730 is a duplicate of line 731.

# Lines 892-893 (0-indexed: 891-892): Extra ===Chinese===
# Line 892 is a duplicate of line 893.

# Strategy: Remove lines at indices 655, 729, 891 (the duplicate markers)
# But removing lines changes indices, so I need to do it in reverse order.

indices_to_remove = sorted([655, 729, 891], reverse=True)
for idx in indices_to_remove:
    print(f"Removing line {idx+1}: [{lines[idx].strip()[:60]}]")
    del lines[idx]

# Write the fixed file
with open(PATH, 'w', encoding='utf-8') as f:
    f.writelines(lines)

print(f"Fixed file written. Total lines: {len(lines)}")
