#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""写项目 CSV（唯一事务源）。根 translation_queue.csv 为快照，由 refresh_progress.py 统一重建，此处不写。
用法: python scripts/set_status.py <project> <todo|doing|done> <file1> [file2 ...]"""
import csv, sys, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def main():
    proj, st, files = sys.argv[1], sys.argv[2], set(sys.argv[3:])
    pq = os.path.join(ROOT, '翻译项目', proj, 'translation_queue.csv')
    rows = []
    with open(pq, encoding='utf-8') as f:
        r = csv.DictReader(f); cols = r.fieldnames
        for row in r:
            if row['file'] in files: row['status'] = st
            rows.append(row)
    with open(pq, 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=cols, lineterminator='\n'); w.writeheader(); w.writerows(rows)
    print(f'{proj}: {len(files)} files -> {st}')

if __name__ == '__main__':
    main()
