#!/usr/bin/env python3
"""Generate project scaffold files (translation_queue.csv) for a project.
Reads 原文/*.md, writes translation_queue.csv sorted by natural chapter order.
"""
import sys
import os
import re

def natural_key(name):
    """Sort 1-1, 1-2, 2-1, chapter-1, chapter-2, etc. in reading order."""
    # extract all number groups
    nums = re.findall(r'\d+', name)
    return [int(n) for n in nums] if nums else [9999]

def main():
    if len(sys.argv) != 2:
        print("Usage: gen_queue.py <project_dir>")
        sys.exit(1)
    proj_dir = sys.argv[1]
    src_dir = os.path.join(proj_dir, '原文')
    files = sorted([f for f in os.listdir(src_dir) if f.endswith('.md')], key=natural_key)
    out_path = os.path.join(proj_dir, 'translation_queue.csv')
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('file,size_kb,status\n')
        for fn in files:
            size = os.path.getsize(os.path.join(src_dir, fn)) / 1024
            f.write(f'{fn},{size:.1f},todo\n')
    print(f"Wrote {out_path} with {len(files)} entries")

if __name__ == '__main__':
    main()
