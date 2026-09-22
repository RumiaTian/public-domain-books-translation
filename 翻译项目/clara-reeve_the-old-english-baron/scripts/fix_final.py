#!/usr/bin/env python3
"""Properly fix the translation file structure by removing duplicates and re-adding missing translations."""
PATH = r'C:\Users\HanTi\OneDrive\translate\翻译项目\clara-reeve_the-old-english-baron\译文\the-old-english-baron_part1.zh-CN.md'

with open(PATH, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Problem analysis:
# Line 594 (idx 593): ===Original=== (Joseph farewell + first night Original)
# Line 655 (idx 654): ===Chinese=== (MISPLACED Chinese - translates aftermath)
# Lines 656-715: Chinese text for Baron aftermath + first night continuation
# Line 716 (idx 715): ===Original=== (dream sequence Original)
# Line 743 (idx 742): ===Original=== (DUPLICATE Baron section Original)
# Lines 744-812: Original text for Baron section
# Line 812 (idx 811): ===Chinese=== (DUPLICATE Chinese for Baron section)
# Lines 813-881: Chinese text for Baron section
# Line 881 (idx 880): ===Chinese=== (dream sequence Chinese)
# Lines 882-972: Chinese text for dream sequence
# Line 972 (idx 971): ===Chinese=== (DUPLICATE more Chinese for Baron section)
# Lines 973-1037: More Chinese text for Baron section
# Line 1037 (idx 1036): ===Original=== (Margery's confession)

# Fix strategy:
# 1. Remove the misplaced Chinese block (lines 655-715)
# 2. Remove the duplicate Baron Original block (lines 743-812)
# 3. Remove the duplicate Baron Chinese block (lines 812-881)
# 4. Remove the duplicate Baron Chinese continuation (lines 972-1037)
# 5. Keep: dream Original (716-742), dream Chinese (881-972)
# 6. Add the missing Chinese translation for the first night's Joseph farewell section

# Let's work with the content more carefully
# The key insight: block 11 (haunted room) had a huge Original block (lines 594-715)
# that contained BOTH the Joseph farewell AND the first night events.
# The Chinese for this was supposed to be the Chinese at lines 656-714,
# but it was incorrectly placed after the Baron's aftermath text.

# Actually, looking more carefully:
# - Lines 594-654 (Original): Joseph farewell + first night events (source 232-262)
# - Lines 655-715 (Chinese): This Chinese text is actually the translation of
#   source lines 230-231 (aftermath of trial) + source lines 232-262 (first night)
#   So it's the CORRECT Chinese for the first night section, just misplaced!

# Wait - let me re-examine. The Chinese at line 656 starts with:
# "埃德蒙退回自己的房间，奥斯瓦尔德则被勋爵留下来密谈"
# This translates source lines 230-231 (aftermath).
# But the Original at line 594 starts with the Joseph farewell (source 232+).

# So the Chinese at lines 656-715 actually translates:
# 1. Source lines 230-231 (Baron's aftermath - NOT in the Original at 594!)
# 2. Source lines 232-262 (first night - this IS in the Original at 594)

# This means:
# - The Original at line 594 needs its proper Chinese (source 232-262)
# - The Chinese at line 656 starts with source 230-231 content, which is EXTRA

# But actually, looking at block 11's script, it included the first night section
# with the Joseph farewell Chinese at the end. The script output has the correct
# Chinese for Joseph farewell at the END of block 11.

# Let me check what lines 696-714 contain (the last part of the misplaced Chinese)
for k in range(696, 716):
    print(f'{k+1}: {lines[k].rstrip()[:120]}')
