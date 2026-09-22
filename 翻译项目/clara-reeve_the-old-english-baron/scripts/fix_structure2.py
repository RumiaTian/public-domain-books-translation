#!/usr/bin/env python3
"""Fix the translation file structure properly."""
PATH = r'C:\Users\HanTi\OneDrive\translate\翻译项目\clara-reeve_the-old-english-baron\译文\the-old-english-baron_part1.zh-CN.md'

with open(PATH, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find all markers and their line numbers
markers = []
for i, line in enumerate(lines):
    s = line.strip()
    if s in ('===Original===', '===Chinese==='):
        markers.append((i, s))

# Print the full marker sequence for analysis
print("Full marker sequence:")
for idx, (ln, mt) in enumerate(markers):
    print(f"  {idx}: Line {ln+1}: {mt}")
