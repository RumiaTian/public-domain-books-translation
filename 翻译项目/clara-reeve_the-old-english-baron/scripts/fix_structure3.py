#!/usr/bin/env python3
"""Comprehensive fix for the translation file structure."""
PATH = r'C:\Users\HanTi\OneDrive\translate\翻译项目\clara-reeve_the-old-english-baron\译文\the-old-english-baron_part1.zh-CN.md'

with open(PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Problem 1: The Chinese block at line 655 (after "Joseph withdrew...")
# translates lines 230-231 (aftermath). This Chinese block should NOT be here.
# Instead, the Original at line 716 (dream sequence) should be preceded by
# the Baron's Original section (lines 271-304).
#
# Problem 2: The fix script inserted a duplicate Baron Original+Chinese block.
# We need to remove the duplicates and restructure properly.

# Step 1: Remove the Chinese block that starts at line 655
# (lines 655-715 are Chinese text that should be removed from this position)
# The Chinese text translates source lines 230-231, which is part of block 12
# that should have been paired with its Original counterpart.

# Let's find the exact boundaries
lines = content.split('\n')

# Find key markers
markers = []
for i, line in enumerate(lines):
    s = line.strip()
    if s in ('===Original===', '===Chinese==='):
        markers.append((i, s))

# Build a list of problematic markers to fix
# The issues are:
# - marker at index 49 (line 655): ===Chinese=== without preceding ===Original===
# - marker at index 51 (line 743): duplicate ===Original=== (Baron section)
# - marker at index 53 (line 881): duplicate ===Chinese=== (Baron section Chinese)
# - marker at index 54 (line 972): duplicate ===Chinese=== (Baron section Chinese continued)

# Strategy: Remove the inserted duplicate content entirely and restructure

# Find the start of the problematic section:
# After Joseph's last words (marker 48 at line 594), the content should be:
# Original (Joseph's farewell + first night) -> Chinese (same)
# Then Original (Baron's plan) -> Chinese (same)
# Then Original (dream sequence) -> Chinese (same)

# Current broken structure:
# Marker 48: Line 594: ===Original=== (Joseph's farewell + first night - this is a HUGE block)
# Marker 49: Line 655: ===Chinese=== (Joseph's Chinese farewell - but this starts a Chinese block that translates the Baron's aftermath, NOT the first night!)
# ... Chinese text until line 715 ...
# Marker 50: Line 716: ===Original=== (dream sequence)
# Marker 51: Line 743: ===Original=== (DUPLICATE Baron section)
# ... Original text until line 811 ...
# Marker 52: Line 812: ===Chinese=== (Baron section Chinese - this is the first of the duplicate Chinese)
# ... Chinese text until line 880 ...
# Marker 53: Line 881: ===Chinese=== (dream sequence Chinese)
# ... Chinese text until line 971 ...
# Marker 54: Line 972: ===Chinese=== (DUPLICATE Baron section Chinese)
# ... Chinese text until line 1036 ...
# Marker 55: Line 1037: ===Original=== (Margery's confession)

# The fix: Remove the inserted duplicate Original+Chinese blocks (lines 743-971)
# and instead restructure the section properly.

# Let's identify exact line ranges for the content to keep vs remove

# Find line 743 (the start of the inserted duplicate Original)
dup_orig_start = None
dup_chinese_end = None
for i, line in enumerate(lines):
    if i == 742 and line.strip() == '===Original===':  # line 743 (0-indexed: 742)
        dup_orig_start = i
        break

# Find line 972 (end of duplicate Chinese)
for i, line in enumerate(lines):
    if i == 971 and line.strip() == '===Chinese===':  # line 972 (0-indexed: 971)
        dup_chinese_end = i
        break

print(f"Duplicate Original starts at line {dup_orig_start+1}")
print(f"Duplicate Chinese ends at line {dup_chinese_end+1}")

# Find the start of the correct Chinese for the dream sequence (line 881)
correct_dream_chinese = None
for i, line in enumerate(lines):
    if i == 880 and line.strip() == '===':  # line 881
        correct_dream_chinese = i
        break

print(f"Correct dream Chinese starts at line {correct_dream_chinese+1}")

# The approach: We need to restructure lines 655-972
# 1. Remove lines 655-714 (the misplaced Chinese text about Baron's aftermath)
# 2. Remove lines 743-880 (the duplicate Original block)
# 3. Keep lines 716-742 (dream Original) and its correct Chinese at 881+
# 4. Remove lines 972-1036 (duplicate Chinese about Baron's aftermath)

# Actually, a cleaner approach: rebuild the section from lines 655 to 1036

# Extract the text sections we need:
# A. From the first night section (lines 594-654): Original about Joseph's farewell
#    This is marker 48 (line 594): ===Original===
#    The Chinese at marker 49 (line 655) is NOT its translation - it's misplaced

# B. The dream sequence Original (lines 716-742)
# C. The dream sequence Chinese (lines 881-971)
# D. The Baron section Original (lines 743-811) - DUPLICATE, remove
# E. The Baron section Chinese (lines 812-880) - DUPLICATE, remove
# F. The Baron aftermath Chinese (lines 972-1036) - DUPLICATE, remove

# Let me check what's actually at each section more carefully
print("\n--- Line 594 content ---")
print(lines[593][:100])
print("\n--- Line 655 content ---")
print(lines[654][:100])
print("\n--- Line 716 content ---")
print(lines[715][:100])
print("\n--- Line 743 content ---")
print(lines[742][:100])
print("\n--- Line 812 content ---")
print(lines[811][:100])
print("\n--- Line 881 content ---")
print(lines[880][:100])
print("\n--- Line 972 content ---")
print(lines[971][:100])
print("\n--- Line 1037 content ---")
print(lines[1036][:100])
