#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
mcp_worker.py — translate_mcp 的轻量 CLI 包装，方便在命令行或子代理中直接驱动 MCP 工具流
支持跨调用保持相同的 worker 身份，实现锁重入
"""
import sys
import os
import json
import uuid

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "mcp"))
import translate_mcp

SESSION_ID_FILE = os.path.join(ROOT, ".mcp_worker_session_id")

def get_session_id():
    env_sid = os.environ.get("MCP_WORKER_ID")
    if env_sid:
        return env_sid
    if os.path.exists(SESSION_ID_FILE):
        with open(SESSION_ID_FILE, "r", encoding="utf-8") as f:
            sid = f.read().strip()
            if sid:
                return sid
    sid = uuid.uuid4().hex[:8]
    with open(SESSION_ID_FILE, "w", encoding="utf-8") as f:
        f.write(sid)
    return sid

def clear_session():
    if os.path.exists(SESSION_ID_FILE):
        os.remove(SESSION_ID_FILE)

# 注入固定的 worker session ID 保持一书一主锁重入
worker_id = get_session_id()
translate_mcp._SELF_ID = worker_id

def main():
    if len(sys.argv) < 2:
        print("Usage: mcp_worker.py [batch_begin|claim|pack|get|submit|clear] ...")
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "batch_begin":
        batch_id = int(sys.argv[2]) if len(sys.argv) > 2 else 1
        res = translate_mcp.tool_batch_begin(batch_id)
        print(res)

    elif cmd == "claim":
        project = sys.argv[2]
        res = translate_mcp.tool_claim_task(project)
        print(res)

    elif cmd == "pack":
        project = sys.argv[2]
        fname = sys.argv[3]
        res = translate_mcp.tool_context_pack(project, fname)
        print(res)

    elif cmd == "get":
        project = sys.argv[2]
        fname = sys.argv[3]
        res = translate_mcp.tool_get_blocks(project, fname)
        print(res)

    elif cmd == "submit":
        project = sys.argv[2]
        fname = sys.argv[3]
        blocks_file = sys.argv[4]
        with open(blocks_file, "r", encoding="utf-8") as f:
            blocks = json.load(f)
        res = translate_mcp.tool_submit_translation(project, fname, blocks)
        print(res)

    elif cmd == "clear":
        clear_session()
        print("Worker session ID cleared.")

    else:
        print(f"Unknown command: {cmd}")
        sys.exit(1)

if __name__ == "__main__":
    main()
