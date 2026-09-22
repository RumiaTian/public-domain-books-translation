#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""兼容入口：刷新根 Plan.md 与 translation_queue.csv。
直接调用统一总控脚本 scripts/refresh_progress.py。

用法：
  python scripts/refresh_plan.py --snapshot "2026-08-25，批次..." \
      --log-date 2026-08-25 --log-event "每日批次" --log-done "+6" \
      --log-notes "备注文本" [--no-rebuild]
"""
import sys
import subprocess
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TARGET = os.path.join(ROOT, "scripts", "refresh_progress.py")

def main():
    args = [sys.executable, TARGET]
    i = 1
    while i < len(sys.argv):
        arg = sys.argv[i]
        if arg == "--no-rebuild":
            args.append("--no-rebuild-csv")
        else:
            args.append(arg)
        i += 1
    
    ret = subprocess.run(args)
    sys.exit(ret.returncode)

if __name__ == "__main__":
    main()
