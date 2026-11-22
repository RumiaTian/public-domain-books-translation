#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/batch_translate_runner.py — 自动化调度与执行批量翻译
严格遵循两级规范：
1. 逐章调用 scripts/translate_chapter_genai.py 进行翻译与 check_bilingual 校验；
2. 异常自动重试 1 次，若依然失败则跳过推进下一篇；
3. 阶段性归档（每完成 batch_size 篇，默认 6~8 篇）：
   - 追加记录到 Plan.md
   - 执行阶段性 Git 提交
4. 全书收尾：
   - 当队列全为 done 时，删除认领.md，刷新 refresh_progress.py，提交最终代码。
"""

import argparse
import csv
import os
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJ_DIR = os.path.join(ROOT, "翻译项目")
GENAI_PY = os.path.join(ROOT, "scripts", "translate_chapter_genai.py")
REFRESH_PY = os.path.join(ROOT, "scripts", "refresh_progress.py")


def run_cmd(cmd):
    p = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=ROOT)
    return p.returncode, p.stdout.strip(), p.stderr.strip()


def get_queue_status(pdir):
    q_path = os.path.join(pdir, "translation_queue.csv")
    if not os.path.isfile(q_path):
        return []
    with open(q_path, "r", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def append_plan_log(pdir, completed_records):
    if not completed_records:
        return
    plan_path = os.path.join(pdir, "Plan.md")
    if not os.path.isfile(plan_path):
        return

    today = time.strftime("%Y-%m-%d")
    new_lines = []
    for fn, res, note in completed_records:
        clean_note = note.replace("\n", " ").replace("\r", " ").strip()
        new_lines.append(f"| {today} | {fn} | {res} | {clean_note} |")

    with open(plan_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 在日志表后追加
    updated_content = content.rstrip() + "\n" + "\n".join(new_lines) + "\n"
    with open(plan_path, "w", encoding="utf-8") as f:
        f.write(updated_content)
    print(f"[+] 已向 Plan.md 追加 {len(completed_records)} 条进度记录")


def git_commit_batch(project, count):
    pdir_rel = f"翻译项目/{project}"
    run_cmd(f'git add "{pdir_rel}"')
    msg = f"feat(translation): {project} 推进进度 (完成 {count} 篇)"
    rc, out, err = run_cmd(f'git commit -m "{msg}"')
    if rc == 0:
        print(f"[+] Git 提交成功: {msg}")
    else:
        print(f"[-] Git 提交输出: {out or err}")


def finalize_book(project):
    print("\n================== 全书收尾阶段 ==================")
    pdir = os.path.join(PROJ_DIR, project)
    # 1. 删除认领锁
    claim_path = os.path.join(pdir, "认领.md")
    if os.path.isfile(claim_path):
        os.remove(claim_path)
        print(f"[+] 已删除认领锁: {claim_path}")

    # 2. 刷新总控看板
    print("[*] 正在刷新总控看板...")
    rc, out, err = run_cmd(f'"{sys.executable}" "{REFRESH_PY}"')
    print(out)
    if err:
        print(f"[-] 看板刷新 stderr: {err}")

    # 3. 提交最终代码
    run_cmd(f'git add .')
    msg = f"feat(translation): {project} 全书双语翻译竣工与看板刷新"
    rc, out, err = run_cmd(f'git commit -m "{msg}"')
    print(f"[+] 最终代码提交: {msg}")
    print("==================================================")


FATAL_ERROR_PATTERNS = (
    "Cookie 认证失败",
    "Session transition failed",
    "accounts.google.com",
    "ConnectionRefusedError",
    "401 UNAUTHENTICATED",
)


def is_fatal_global_error(msg):
    return any(pat in msg for pat in FATAL_ERROR_PATTERNS)


def main():
    parser = argparse.ArgumentParser(description="批量翻译调度 Runner")
    parser.add_argument("--project", required=True, help="项目名称")
    parser.add_argument("--model", default="gemini-3.8-flash", help="模型名称")
    parser.add_argument("--batch-size", type=int, default=8, help="每批次篇数 (到达后自动归档提交，0表示无限制全量)")
    parser.add_argument("--max-total", type=int, default=0, help="最多处理总篇数 (0表示处理所有todo)")
    parser.add_argument("--min-interval", type=float, default=60.0, help="相邻两次 API 调用最小间隔秒数 (默认 60s)")
    parser.add_argument("--max-retries", type=int, default=1, help="单章最大重试次数 (默认 1 次，即最多共尝试 2 次)")
    args = parser.parse_args()

    pdir = os.path.join(PROJ_DIR, args.project)
    if not os.path.isdir(pdir):
        print(f"[-] 项目目录不存在: {pdir}")
        sys.exit(1)

    python_bin = sys.executable

    batch_done = []
    total_processed = 0
    failed_files = set()
    last_call_start = 0.0
    aborted_reason = None

    while True:
        rows = get_queue_status(pdir)
        all_todos = [r["file"] for r in rows if r.get("status") == "todo"]
        todos = [f for f in all_todos if f not in failed_files]
        dones = [r["file"] for r in rows if r.get("status") == "done"]

        print(f"\n[*] 状态概览: todo={len(all_todos)} (可调度={len(todos)}), done={len(dones)}, total={len(rows)}", flush=True)

        if not todos:
            if batch_done:
                append_plan_log(pdir, batch_done)
                git_commit_batch(args.project, len(batch_done))
                batch_done = []
            if not all_todos:
                print("[+] 所有章节已全部翻译完成 (todo=0)！")
                finalize_book(args.project)
            else:
                print(f"[!] 剩余 {len(all_todos)} 篇异常跳过未完成: {all_todos}")
            break

        if args.max_total > 0 and total_processed >= args.max_total:
            print(f"[*] 已达到最大处理上限 {args.max_total} 篇，停止当前批次。")
            if batch_done:
                append_plan_log(pdir, batch_done)
                git_commit_batch(args.project, len(batch_done))
            break

        target_file = todos[0]
        print(f"\n>>> [{total_processed + 1}] 开始处理: {target_file} (剩余待译: {len(todos)})", flush=True)

        success = False
        err_msg = ""
        max_attempts = 1 + max(0, args.max_retries)
        for attempt in range(max_attempts):
            if last_call_start > 0 and args.min_interval > 0:
                elapsed_since_last = time.time() - last_call_start
                wait_sec = args.min_interval - elapsed_since_last
                if wait_sec > 0:
                    print(f"[*] 遵守频控 ({args.min_interval:.0f}s/次)，等待 {wait_sec:.1f}s 后发起请求...", flush=True)
                    time.sleep(wait_sec)

            if attempt > 0:
                print(f"[*] 对 {target_file} 进行第 {attempt + 1} 次尝试...", flush=True)

            last_call_start = time.time()
            cmd = [
                python_bin,
                GENAI_PY,
                "--project",
                args.project,
                "--model",
                args.model,
                "--file",
                target_file,
            ]
            p = subprocess.run(cmd, capture_output=True, text=True, cwd=ROOT)
            stdout = p.stdout.strip()
            stderr = p.stderr.strip()
            print(stdout, flush=True)
            if stderr:
                print(f"[stderr] {stderr}", flush=True)

            if p.returncode == 0 and "[SUCCESS]" in stdout:
                success = True
                break
            else:
                err_msg = f"{stdout}\n{stderr}".strip() or "未知异常"
                if is_fatal_global_error(err_msg):
                    aborted_reason = f"检测到全局认证/连接阻断，立即熔断停止: {err_msg[:200]}"
                    break

        if aborted_reason:
            print(f"\n[!] {aborted_reason}", flush=True)
            batch_done.append((target_file, "中断", f"全局熔断: {err_msg[:80]}"))
            if batch_done:
                append_plan_log(pdir, batch_done)
                git_commit_batch(args.project, len(batch_done))
                batch_done = []
            break

        if success:
            batch_done.append((target_file, "成功", "check_bilingual 校验通过，标记 done"))
            total_processed += 1
        else:
            print(f"[-] 章节 {target_file} 尝试 {max_attempts} 次均失败，跳过该章节。原因: {err_msg[:200]}", flush=True)
            batch_done.append((target_file, "失败", f"异常跳过: {err_msg[:80]}"))
            failed_files.add(target_file)
            total_processed += 1

        # 阶段性归档检查
        if args.batch_size > 0 and len(batch_done) >= args.batch_size:
            print(f"\n[***] 达到批次阶段性归档阈值 ({len(batch_done)} 篇)，执行 Plan.md 归档与 Git 提交...")
            append_plan_log(pdir, batch_done)
            git_commit_batch(args.project, len(batch_done))
            batch_done = []

    print(f"\n[✓] Runner 运行结束。本次运行共处理 {total_processed} 篇。")


if __name__ == "__main__":
    main()
