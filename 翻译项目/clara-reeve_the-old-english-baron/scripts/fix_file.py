#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fix the translation file by removing duplicate ===Chinese=== markers."""
import re

path = r'C:\Users\HanTi\OneDrive\translate\翻译项目\clara-reeve_the-old-english-baron\译文\the-old-english-baron_part3.zh-CN.md'

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove duplicate consecutive ===Chinese=== lines
# Pattern: ===Chinese===\n===Chinese===  -> ===Chinese===
content = re.sub(r'(===Chinese===\n)===Chinese===\n', r'\1', content)

# Also remove any ===Chinese=== that appears right after ===Original===
# Pattern: ===Original===\n===Chinese===\n -> ===Original===\n
# (This shouldn't happen but just in case)
content = re.sub(r'===Original===\n===Chinese===\n', '===Original===\n', content)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

# Verify
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

orig_count = content.count('===Original===')
chinese_count = content.count('===Chinese===')
print(f'After fix: Original blocks: {orig_count}, Chinese blocks: {chinese_count}')
print(f'File size: {len(content)} chars, {content.count(chr(10))} lines')

# Check first few markers
lines = content.split('\n')
for i, line in enumerate(lines):
    if '===' in line and ('Original' in line or 'Chinese' in line):
        print(f'Line {i+1}: {line}')
        if i > 60:
            break
