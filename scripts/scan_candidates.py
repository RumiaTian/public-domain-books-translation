#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/scan_candidates.py — 多批次定时任务候选书目分流与动态摸底工具

功能：
1. 【空间互斥分片】：通过确定性分片算法将全库书目严格划分为 N 个互斥池（默认 3 批次），保证各批次绝对不重叠。
2. 【运行时动态排他锁】：检测各项目的「认领.md」，锁定中的书目（锁龄 < 超时阈值）自动跳过。
3. 【断点与残留检测】：识别 doing 残留及译文落盘状态，指导断点恢复。
4. 【轻量优先排序】：按待译容量（todo_kb）升序排列，优先调度容易整本完结的轻量/中量作品。

用法：
    python scripts/scan_candidates.py --batch 1
    python scripts/scan_candidates.py --batch 2
    python scripts/scan_candidates.py --batch 3
    python scripts/scan_candidates.py --batch 1 --limit 5 --max-kb 300
"""

import argparse
import csv
import os
import sys
import time
import zlib

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJ_DIR = os.path.join(ROOT, "翻译项目")


def get_batch_assignment(proj_name, index, method="index", total_batches=3):
    if method == "crc32":
        return (zlib.crc32(proj_name.encode("utf-8")) % total_batches) + 1
    else:
        return (index % total_batches) + 1


def main():
    parser = argparse.ArgumentParser(description="多批次定时翻译任务书目分流与摸底")
    parser.add_argument("--batch", type=int, choices=[1, 2, 3, 0], default=0,
                        help="指定批次编号 (1, 2, 3，0 表示查看全局)")
    parser.add_argument("--total-batches", type=int, default=3, help="总批次数（默认 3）")
    parser.add_argument("--method", type=str, choices=["index", "crc32"], default="index",
                        help="分片算法：index（字典序下标模 3，最均衡）或 crc32（纯无状态哈希）")
    parser.add_argument("--limit", type=int, default=15, help="输出候选数量上限")
    parser.add_argument("--max-kb", type=float, default=None, help="仅筛选 todo_kb <= 阈值的书目")
    parser.add_argument("--lock-timeout-hours", type=float, default=48.0, help="锁超时判定小时数（默认 48h）")
    args = parser.parse_args()

    if not os.path.isdir(PROJ_DIR):
        print(f"错误：项目目录不存在：{PROJ_DIR}", file=sys.stderr)
        sys.exit(1)

    now = time.time()
    all_projs = sorted([d for d in os.listdir(PROJ_DIR) if os.path.isdir(os.path.join(PROJ_DIR, d))])

    locked_projects = {}   # proj -> (holder, age_h, is_expired)
    doing_items = []       # (proj, file, size_kb, zh_exists, batch_id)
    candidates = []        # (todo_kb, proj, todo_n, done_n, total_n, doing_n, batch_id)

    for idx, p in enumerate(all_projs):
        d = os.path.join(PROJ_DIR, p)
        q = os.path.join(d, "translation_queue.csv")
        if not os.path.isfile(q):
            continue

        proj_batch = get_batch_assignment(p, idx, method=args.method, total_batches=args.total_batches)

        # 检查认领锁
        lock_file = os.path.join(d, "认领.md")
        has_active_lock = False
        if os.path.isfile(lock_file):
            try:
                age_h = (now - os.path.getmtime(lock_file)) / 3600.0
                first_line = open(lock_file, "r", encoding="utf-8", errors="ignore").readline().strip()
                is_expired = age_h >= args.lock_timeout_hours
                locked_projects[p] = (first_line or "已上锁", round(age_h, 1), is_expired)
                if not is_expired:
                    has_active_lock = True
            except Exception:
                has_active_lock = True

        # 读取队列状态
        try:
            with open(q, "r", encoding="utf-8", errors="ignore") as f:
                rows = list(csv.DictReader(f))
        except Exception:
            continue

        todo_n = done_n = doing_n = 0
        todo_kb = 0.0
        for r in rows:
            st = r.get("status", "").strip()
            kb = float(r.get("size_kb") or 0)
            if st == "done":
                done_n += 1
            elif st == "doing":
                doing_n += 1
                fname = r.get("file", "")
                stem = fname[:-3] if fname.endswith(".md") else fname
                zh_path = os.path.join(d, "译文", f"{stem}.zh-CN.md")
                doing_items.append((p, fname, kb, os.path.isfile(zh_path), proj_batch))
            elif st == "todo":
                todo_n += 1
                todo_kb += kb

        if todo_n == 0 and doing_n == 0:
            continue

        # 候选人判定：必须属于目标批次（如果指定），且无活跃未过期锁
        if (args.batch == 0 or proj_batch == args.batch) and not has_active_lock:
            if todo_n > 0:
                if args.max_kb is None or todo_kb <= args.max_kb:
                    candidates.append((todo_kb, p, todo_n, done_n, len(rows), doing_n, proj_batch))

    target_desc = f"【批次 {args.batch}】" if args.batch > 0 else "【全局所有批次】"
    print(f"==================================================")
    print(f"  翻译流水线候选书目摸底分流报告  {target_desc}")
    print(f"==================================================")

    # 1. 活跃认领锁
    if locked_projects:
        print(f"\n🔒 [全库认领锁] 共 {len(locked_projects)} 本处于锁定状态：")
        for p, (holder, age_h, is_exp) in sorted(locked_projects.items()):
            exp_flag = "⚠️ 已超时(>48h可接管)" if is_exp else "🟢 活跃中"
            print(f"  - {p:<50} [{holder}] 锁龄: {age_h:4.1f}h ({exp_flag})")
    else:
        print("\n🔒 [全库认领锁] 当前全库无锁。")

    # 2. Doing 残留
    cur_batch_doings = [x for x in doing_items if (args.batch == 0 or x[4] == args.batch)]
    if cur_batch_doings:
        print(f"\n⚡ [DOING 断点残留] {target_desc} 发现 {len(cur_batch_doings)} 个在译章节：")
        for p, f, kb, zh_ex, pb in cur_batch_doings:
            status_txt = "译文已落盘(待卡点校验回填done)" if zh_ex else "译文缺失(需重译)"
            print(f"  - [批次{pb}] {p} -> {f} ({kb:.1f}KB) | {status_txt}")
    else:
        print(f"\n⚡ [DOING 断点残留] {target_desc} 无未完成的 doing 章节。")

    # 3. 待译候选清单
    candidates.sort(key=lambda x: (x[0], x[2]))  # 按 todo_kb 升序，篇目数升序
    print(f"\n📖 [待译候选清单] {target_desc} 共找到 {len(candidates)} 本待译书目（按容量升序排列）：")
    if not candidates:
        print("  (暂无符合条件的候选书目)")
    else:
        display_list = candidates[:args.limit]
        for rank, (tkb, p, tn, dn, tot, dgn, pb) in enumerate(display_list, 1):
            batch_tag = f"[批次{pb}] " if args.batch == 0 else ""
            print(f"  {rank:2d}. {batch_tag}{tkb:7.1f} KB | 待译: {tn:2d}/{tot:2d} 篇 (已译: {dn:2d}) | {p}")

        if len(candidates) > args.limit:
            print(f"  ... 另有 {len(candidates) - args.limit} 本书目未展开（可通过 --limit 参数调整显示数量）")

    # 4. 推荐行动指令
    if candidates:
        top_cand = candidates[0][1]
        print(f"\n💡 [调度指引] 建议该批次 Agent 首选认领：")
        print(f"  1. 创建锁：echo '批次{args.batch if args.batch>0 else candidates[0][6]}' > 翻译项目/{top_cand}/认领.md")
        print(f"  2. 启动该书翻译，并在完工后删除认领锁：rm -f 翻译项目/{top_cand}/认领.md")
    print(f"==================================================\n")


if __name__ == "__main__":
    main()
