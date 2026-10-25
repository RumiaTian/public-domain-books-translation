#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
translate_mcp.py — 阶段二翻译执行 MCP 服务器（方案 C：省 token 层 + 续接层）

零第三方依赖：stdio 上按行交换 JSON-RPC 2.0（MCP 协议核心子集）。
设计文档见 MCP方案对比.md。

工具:
  batch_begin(batch_id, dry_run)             幂等续跑入口 + doing 残留回收
  claim_task(project)                        章节认领（互斥）+ 书级锁心跳
  context_pack(project, file)                命中术语 + 风格摘要 + 黄金样本 + 前章末尾
  get_blocks(project, file)                  原文分块（标题与正文分离）
  submit_translation(project, file, blocks)  服务端拼装双语 + 卡点校验 + 状态回填

地面真相 = 文件（不引入独立状态文件）:
  - 项目 translation_queue.csv 的 todo/doing/done
  - 翻译项目/<书>/认领.md 书级锁（mtime 超 48h 过期，语义同 scan_candidates.py）
  - 译文/<stem>.zh-CN.md 是否落盘、check_bilingual.py 是否通过
分区算法与 scan_candidates.py 完全一致: sorted(项目目录) 下标 % TOTAL_BATCHES + 1（冻结）。
服务器不内嵌任何 LLM 调用。
"""
import csv
import json
import os
import re
import subprocess
import sys
import time
from contextlib import contextmanager

try:
    import msvcrt

    def _lock_handle(f):
        f.seek(0)
        msvcrt.locking(f.fileno(), msvcrt.LK_LOCK, 1)

    def _unlock_handle(f):
        f.seek(0)
        msvcrt.locking(f.fileno(), msvcrt.LK_UNLCK, 1)
except ImportError:  # 非 Windows 平台退化为无锁
    def _lock_handle(f):
        pass

    def _unlock_handle(f):
        pass

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJ_DIR = os.path.join(ROOT, "翻译项目")
CHECKER = os.path.join(ROOT, "scripts", "check_bilingual.py")
LOCK_DIR = os.path.join(os.path.expanduser("~"), ".translate_mcp_locks")  # 跨进程队列锁集中存放，不污染仓库
_MCP_DIR = os.path.dirname(os.path.abspath(__file__))
BLOCKLIST_FILE = os.path.join(_MCP_DIR, "拦截清单.txt")   # 1301 内容拦截回避书目（一行一书名，# 注释）
ACTIVITY_LOG = os.path.join(_MCP_DIR, "活动日志.txt")     # 工具活动足迹：worker 暴毙时供调度会话定位卡住的书

TOTAL_BATCHES = 3        # 红线：与 scan_candidates.py 默认一致，冻结
LOCK_TIMEOUT_H = 48.0    # 认领.md 锁超时（小时）
ACTIVE_GRACE_H = 4.0     # MCP 锁活跃宽限：锁龄小于此值视为"该书有主"（活 worker 每次 claim/submit 都会刷锁）；同批次窗口间隔≥8h，取 4h 不阻塞任何接管路径
MAX_BLOCK_CHARS = 2400   # get_blocks 单块目标上限（贴近既有译文「几百字数段一块」粒度）
PACK_STYLE_LINES = 45    # context_pack：领域配置摘要行数
PACK_ENGINE_LINES = 35   # context_pack：通用引擎摘要行数
PACK_GOLDEN_LINES = 35   # context_pack：黄金样本节选行数
PACK_PREV_TAIL = 700     # context_pack：前章译文末尾字符数
GLOSSARY_MAX = 150       # context_pack：命中词条上限
BACKFILL_CHECK_LIMIT = 30  # batch_begin 单次跑校验器的 doing 回填上限

_HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")


class ToolError(Exception):
    pass


# ---------- 基础 IO ----------

def _safe_component(name):
    if not name or "/" in name or "\\" in name or ".." in name or name.startswith("."):
        raise ToolError(f"非法名称: {name!r}")
    return name


def _proj_path(project):
    _safe_component(project)
    p = os.path.join(PROJ_DIR, project)
    if not os.path.isdir(p):
        raise ToolError(f"项目不存在: {project}")
    return p


@contextmanager
def _queue_lock(project):
    """项目队列的跨进程读-改-写锁"""
    os.makedirs(LOCK_DIR, exist_ok=True)
    lp = os.path.join(LOCK_DIR, _safe_component(project) + ".lock")
    with open(lp, "a+b") as lf:
        _lock_handle(lf)
        try:
            yield
        finally:
            _unlock_handle(lf)


def _read_queue(project):
    q = os.path.join(_proj_path(project), "translation_queue.csv")
    if not os.path.isfile(q):
        raise ToolError(f"缺少队列文件: {project}/translation_queue.csv")
    with open(q, "r", encoding="utf-8", errors="ignore", newline="") as f:
        reader = csv.reader(f)
        rows = list(reader)
    if not rows:
        raise ToolError(f"队列为空: {project}")
    return q, rows


def _write_queue(q, rows):
    tmp = q + ".mcp.tmp"
    with open(tmp, "w", encoding="utf-8", newline="") as f:
        csv.writer(f, lineterminator="\n").writerows(rows)
    os.replace(tmp, q)


def _row_status(row):
    # 列顺序 file,size_kb,status
    return row[2].strip() if len(row) >= 3 else ""


def _set_row_status(rows, fname, status):
    for row in rows:
        if row and row[0].strip() == fname:
            row[2] = status
            return True
    return False


def _zh_path(project, fname):
    stem = fname[:-3] if fname.endswith(".md") else fname
    return os.path.join(PROJ_DIR, project, "译文", f"{stem}.zh-CN.md")


def _src_path(project, fname):
    return os.path.join(PROJ_DIR, project, "原文", fname)


def _read_text(path, limit=None):
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read() if limit is None else f.read(limit)


def _lock_path(project):
    return os.path.join(PROJ_DIR, project, "认领.md")


def _holder_is_mcp(holder):
    """认领.md 首行形如「translate-mcp <id> | 时间戳」（旧格式无 id），按前缀判定持有者"""
    return holder.split("|")[0].strip().startswith("translate-mcp")


def _holder_self(holder):
    """锁是否由当前 MCP 进程持有（owner 重入自己的书）"""
    return holder.split("|")[0].strip() == "translate-mcp " + _SELF_ID


def _lock_info(project):
    """返回 (exists, holder, age_h, expired)"""
    lp = _lock_path(project)
    if not os.path.isfile(lp):
        return False, "", 0.0, False
    age_h = (time.time() - os.path.getmtime(lp)) / 3600.0
    holder = _read_text(lp, 120).splitlines()[0].strip() if os.path.getsize(lp) else ""
    return True, holder, age_h, age_h >= LOCK_TIMEOUT_H


_SELF_ID = __import__("uuid").uuid4().hex[:8]  # 每个 MCP 服务进程唯一：锁持有者身份，自己可重入自己的锁


def _touch_lock(project, holder=None):
    lp = _lock_path(project)
    with open(lp, "w", encoding="utf-8", newline="") as f:
        f.write(f"{holder or ('translate-mcp ' + _SELF_ID)} | {time.strftime('%Y-%m-%d %H:%M:%S')}\n")


def _run_checker(path):
    """跑 check_bilingual.py，返回 (struct_ok, report_text)"""
    try:
        r = subprocess.run(
            [sys.executable, CHECKER, path],
            capture_output=True, encoding="utf-8", errors="replace", timeout=120,
            cwd=ROOT,
        )
        out = (r.stdout or "") + (r.stderr or "")
    except Exception as e:  # 校验器跑不起来按未通过处理
        return False, f"校验器执行失败: {e}"
    struct_ok = ("标记成对: 满足" in out) and ("标题合并格式: 满足" in out)
    return struct_ok, out


# ---------- 分块（get_blocks 与 submit 共用，必须确定性一致） ----------

_SENT_RE = re.compile(r"[^.!?。！？…]*[.!?。！？…]+[”’)」』]*", re.S)


def _shatter(text):
    """超长段落（无空行分隔的整段）按句子边界切成 ≤MAX_BLOCK_CHARS 的片段。
    单句仍超限时按字符硬切，保证块上限永远成立（ii-2 类源文实测需要）。"""
    if len(text) <= MAX_BLOCK_CHARS:
        return [text]
    sents, last = [], 0
    for m in _SENT_RE.finditer(text):
        sents.append(text[last:m.end()])
        last = m.end()
    if last < len(text):
        sents.append(text[last:])
    pieces, cur = [], ""
    for s in sents:
        if len(s) > MAX_BLOCK_CHARS:
            if cur:
                pieces.append(cur)
                cur = ""
            for j in range(0, len(s), MAX_BLOCK_CHARS):
                pieces.append(s[j:j + MAX_BLOCK_CHARS])
            continue
        if cur and len(cur) + len(s) > MAX_BLOCK_CHARS:
            pieces.append(cur)
            cur = s
        else:
            cur += s
    if cur:
        pieces.append(cur)
    return pieces


def _split_blocks(src_text):
    """按标题切节、按空行打包成 ≤MAX_BLOCK_CHARS 的块；超长段落句子级兜底。
    返回 [{i, heading(原始行或None), text(正文)}]"""
    lines = src_text.split("\n")
    blocks = []
    cur_paras = []          # 当前块内的段落
    cur_len = 0
    cur_heading = None      # 当前块所属标题行（原始行，含 #）

    def close():
        nonlocal cur_paras, cur_len, cur_heading
        body = "\n\n".join(cur_paras).strip()
        if cur_heading or body:
            blocks.append({"heading": cur_heading, "text": body})
        cur_paras, cur_len, cur_heading = [], 0, None

    para = []

    def flush_para():
        nonlocal para, cur_len
        text = "\n".join(para).strip()
        para = []
        if not text:
            return
        for piece in _shatter(text):
            add_len = len(piece) + 2
            if cur_paras and cur_len + add_len > MAX_BLOCK_CHARS:
                close()
            cur_paras.append(piece)
            cur_len += add_len

    for line in lines:
        m = _HEADING_RE.match(line)
        if m:
            flush_para()
            if cur_paras or cur_heading:
                close()
            cur_heading = line.rstrip()
            continue
        if not line.strip():
            flush_para()
            continue
        para.append(line.rstrip())
    flush_para()
    close()
    for i, b in enumerate(blocks, 1):
        b["i"] = i
    return blocks


_PAIR_ORIG_RE = re.compile(r"^={3,}\s*original\s*={0,}\s*$", re.IGNORECASE)
_PAIR_ZH_RE = re.compile(r"^={3,}\s*chinese\s*={0,}\s*$", re.IGNORECASE)


def _parse_existing_pairs(path):
    """解析已落盘双语文件 → (pairs, titles)。
    pairs: [(original, chinese)]（仅完整成对块）；titles: 按出现顺序的已合并标题中文部分。"""
    if not os.path.isfile(path):
        return [], []
    markers, cur_type, buf = [], None, []
    titles = []
    for line in _read_text(path).split("\n"):
        if _PAIR_ORIG_RE.match(line):
            if cur_type and buf:
                markers.append((cur_type, "\n".join(buf).strip()))
            cur_type, buf = "original", []
        elif _PAIR_ZH_RE.match(line):
            if cur_type and buf:
                markers.append((cur_type, "\n".join(buf).strip()))
            cur_type, buf = "chinese", []
        elif cur_type:
            buf.append(line)
        else:
            m = _HEADING_RE.match(line)
            if m and "/" in line:
                titles.append(m.group(2).split("/", 1)[1].strip())
    if cur_type and buf:
        markers.append((cur_type, "\n".join(buf).strip()))
    pairs = []
    i = 0
    while i < len(markers) - 1:
        if markers[i][0] == "original" and markers[i + 1][0] == "chinese":
            pairs.append((markers[i][1], markers[i + 1][1]))
            i += 2
        else:
            i += 1
    return pairs, titles


def _valid_prefix(src_blocks, pairs):
    """既有译文与当前原文按序比对，返回可复用的完整块数（原文不一致即截断）。"""
    valid = 0
    for b in src_blocks:
        if valid < len(pairs) and pairs[valid][0] == b["text"] and pairs[valid][1]:
            valid += 1
        else:
            break
    return valid


# ---------- 工具实现 ----------

def _load_blocklist():
    if not os.path.isfile(BLOCKLIST_FILE):
        return []
    out = []
    for ln in _read_text(BLOCKLIST_FILE).splitlines():
        s = ln.strip()
        if s and not s.startswith("#"):
            out.append(s)
    return out


def _log_activity(tool, project, fname=""):
    try:
        with open(ACTIVITY_LOG, "a", encoding="utf-8") as f:
            f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')}|{tool}|{project}|{fname}\n")
    except OSError:
        pass


def tool_batch_begin(batch_id, dry_run=False):
    if batch_id not in (0, 1, 2, 3):
        raise ToolError("batch_id 取值 1/2/3（0=只读全局总览）")
    blocklist = _load_blocklist()
    all_dirs = sorted(d for d in os.listdir(PROJ_DIR) if os.path.isdir(os.path.join(PROJ_DIR, d)))
    retry_queue, backfilled, pending_next = [], [], []
    candidates = []
    checked = 0
    for idx, name in enumerate(all_dirs):
        b = idx % TOTAL_BATCHES + 1
        q = os.path.join(PROJ_DIR, name, "translation_queue.csv")
        if not os.path.isfile(q):
            continue
        try:
            _, rows = _read_queue(name)
        except ToolError:
            continue
        lock_exists, holder, age_h, expired = _lock_info(name)
        changed = False
        # 残留回收：只动本批次、且无活跃外部锁的项目；粒度到块（锁内读改写）；拦截书目冻结不动（防经重试队列回流）；
        # 活跃 MCP 锁（<2h 心跳）= 并行 worker 正在做，冻结不动（防误重置在译章节）
        if batch_id != 0 and b == batch_id and name not in blocklist and not (lock_exists and not expired and not _holder_is_mcp(holder)) and not (lock_exists and not expired and _holder_is_mcp(holder) and age_h < ACTIVE_GRACE_H):
            with _queue_lock(name):
                try:
                    _, rows = _read_queue(name)
                except ToolError:
                    rows = []
                if rows:
                    for row in rows:
                        if not row or _row_status(row) != "doing":
                            continue
                        fname = row[0].strip()
                        zh = _zh_path(name, fname)
                        srcf = _src_path(name, fname)
                        if os.path.isfile(zh) and os.path.isfile(srcf):
                            sblocks = _split_blocks(_read_text(srcf))
                            pairs, _t = _parse_existing_pairs(zh)
                            valid = _valid_prefix(sblocks, pairs)
                            if sblocks and valid == len(sblocks):
                                # 全部块已译：卡点校验后回填 done
                                if checked < BACKFILL_CHECK_LIMIT:
                                    checked += 1
                                    ok, _ = _run_checker(zh)
                                    if ok:
                                        if not dry_run:
                                            _set_row_status(rows, fname, "done")
                                            changed = True
                                        backfilled.append(f"{name}/{fname}")
                                        continue
                                pending_next.append(f"{name}/{fname}")
                                continue
                            if valid > 0:
                                # 块级断点：已有译文保留在盘，下一窗口补剩余块
                                retry_queue.append(f"{name}/{fname}(断点:已译{valid}/{len(sblocks)}块)")
                                continue
                            # 无可复用块：整章重投
                        if not dry_run:
                            _set_row_status(rows, fname, "todo")
                            changed = True
                        retry_queue.append(f"{name}/{fname}")
                    if changed:
                        _write_queue(q, rows)
                    # 回收动过本书 = 持有者已死，MCP 幽灵锁一并清除（防候选池被排除 48h）
                    if changed and not dry_run and lock_exists and not expired and _holder_is_mcp(holder):
                        try:
                            os.remove(_lock_path(name))
                        except OSError:
                            pass
        # 候选统计（回收后重算）
        todo_n = sum(1 for r in rows if r and _row_status(r) == "todo")
        done_n = sum(1 for r in rows if r and _row_status(r) == "done")
        doing_n = sum(1 for r in rows if r and _row_status(r) == "doing")
        if todo_n == 0 and doing_n == 0:
            continue
        if (batch_id == 0 or b == batch_id) and not (lock_exists and not expired) and name not in blocklist:
            todo_kb = 0.0
            for r in rows:
                if r and _row_status(r) == "todo":
                    try:
                        todo_kb += float(r[1] or 0)
                    except ValueError:
                        pass
            candidates.append((todo_kb, name, todo_n, done_n, len(rows) - 1))
    candidates.sort(key=lambda x: (x[0], x[2]))
    bp_cnt = sum(1 for x in retry_queue if "断点" in x)
    lines = [f"批次 {batch_id} 续跑清单（dry_run={str(dry_run).lower()}；分区 index%{TOTAL_BATCHES}，参数冻结）"]
    lines.append(f"回收: 回填done {len(backfilled)} 章 | 块级断点续译 {bp_cnt} 章 | 整章重投 {len(retry_queue) - bp_cnt} 章 | 待下轮回收 {len(pending_next)} 章")
    if retry_queue:
        lines.append("[重试队列·本批最优先] " + "; ".join(retry_queue[:8]) + ("…" if len(retry_queue) > 8 else ""))
    if backfilled:
        lines.append("[已回填done] " + "; ".join(backfilled[:8]) + ("…" if len(backfilled) > 8 else ""))
    lines.append(f"[候选·todo_kb升序·共{len(candidates)}本·显示前12]")
    if blocklist:
        lines.append(f"[内容拦截回避 {len(blocklist)} 本·见 mcp/拦截清单.txt] " + "; ".join(blocklist[:5]) + ("…" if len(blocklist) > 5 else ""))
    for rank, (tkb, name, tn, dn, tot) in enumerate(candidates[:12], 1):
        lines.append(f" {rank:2d}. {tkb:7.1f}KB 待译{tn:3d}/{tot:3d} 已译{dn:3d} | {name}")
    if candidates:
        lines.append(f"[建议首选] {candidates[0][1]} —— 调用 claim_task(\"{candidates[0][1]}\") 认领")
    else:
        lines.append("[候选] 本批次无待译书目")
    return "\n".join(lines)


def tool_claim_task(project):
    _proj_path(project)
    if project in _load_blocklist():
        raise ToolError(f"{project} 在 mcp/拦截清单.txt 中（1301 回避），请从候选单另选；人工核查后删除该行即可解冻")
    _log_activity("claim", project)
    lock_exists, holder, age_h, expired = _lock_info(project)
    if lock_exists and not expired and not _holder_is_mcp(holder):
        raise ToolError(f"{project} 被外部锁持有({holder}，{age_h:.1f}h)，未超 {LOCK_TIMEOUT_H}h 不可接管")
    if lock_exists and not expired and _holder_is_mcp(holder) and age_h < ACTIVE_GRACE_H and not _holder_self(holder):
        raise ToolError(f"{project} 正被另一 worker 活跃持有（锁龄 {age_h * 60:.0f} 分钟 < {ACTIVE_GRACE_H}h，一书一主），请换候选单下一本")
    with _queue_lock(project):
        q, rows = _read_queue(project)
        target = None
        for row in rows[1:]:
            if row and _row_status(row) == "todo":
                target = row[0].strip()
                break
        if target is None:
            return f"{project}: 无 todo 章节（全书完成或状态异常），请换下一本"
        _set_row_status(rows, target, "doing")
        _write_queue(q, rows)
        size_kb = next((r[1] for r in rows[1:] if r and r[0].strip() == target), "?")
        todo_left = sum(1 for r in rows[1:] if r and _row_status(r) == "todo")
    _touch_lock(project)
    return json.dumps({
        "claimed": target,
        "size_kb": size_kb,
        "todo_left": todo_left,
        "lock": "认领.md 已刷新（48h TTL）",
        "next": f'读取原文用 get_blocks("{project}", "{target}")，配套 context_pack("{project}", "{target}")',
    }, ensure_ascii=False)


def _parse_glossary(path):
    """解析术语表 markdown 表格 → [(源词, 定名)]"""
    if not os.path.isfile(path):
        return []
    terms = []
    for line in _read_text(path).splitlines():
        line = line.strip()
        if not line.startswith("|") or line.count("|") < 2:
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        src_term = cells[0].strip("`*- ")
        target = cells[1].strip("`*- ") if len(cells) > 1 else ""
        if not src_term or len(src_term) < 2 or set(src_term) <= set("-— "):
            continue
        if re.fullmatch(r"[:\-—\s]+", src_term):
            continue
        terms.append((src_term, target))
    return terms


def tool_context_pack(project, fname):
    _safe_component(fname)
    _log_activity("context_pack", project, fname)
    src_path = _src_path(project, fname)
    if not os.path.isfile(src_path):
        raise ToolError(f"原文不存在: {project}/原文/{fname}")
    src = _read_text(src_path)
    pdir = _proj_path(project)
    out = []

    # 领域配置摘要
    domain_file = None
    desc_path = os.path.join(pdir, "项目说明.md")
    if os.path.isfile(desc_path):
        m = re.search(r"prompts/(\S+?\.md)", _read_text(desc_path, 4000))
        if m:
            domain_file = os.path.join(ROOT, "prompts", m.group(1))
    if domain_file and os.path.isfile(domain_file):
        out.append("【领域配置·摘要】")
        out.extend(_read_text(domain_file, 8000).splitlines()[:PACK_STYLE_LINES])
    else:
        out.append("【领域配置·摘要】未找到，按小说文学通用规范执行")

    # 术语命中
    terms = _parse_glossary(os.path.join(pdir, "术语表.md"))
    hits = []
    for src_term, target in terms:
        if re.fullmatch(r"[A-Za-z0-9 .'\-]+", src_term):
            if re.search(r"(?<![A-Za-z0-9])" + re.escape(src_term) + r"(?![A-Za-z0-9])", src):
                hits.append((src_term, target))
        elif src_term in src:
            hits.append((src_term, target))
        if len(hits) >= GLOSSARY_MAX:
            break
    out.append(f"\n【术语表·本章命中 {len(hits)} 条】（硬约束；首现标「中文（English）」）")
    for s, t in hits:
        out.append(f"- {s} → {t or '（待定名）'}")

    # 黄金样本（译文目录里最小的一篇）
    zh_dir = os.path.join(pdir, "译文")
    golden = None
    if os.path.isdir(zh_dir):
        cands = [f for f in os.listdir(zh_dir) if f.endswith(".zh-CN.md")]
        if cands:
            golden = min(cands, key=lambda f: os.path.getsize(os.path.join(zh_dir, f)))
    if golden:
        out.append(f"\n【黄金样本节选·{golden}】")
        out.extend(_read_text(os.path.join(zh_dir, golden), 9000).splitlines()[:PACK_GOLDEN_LINES])

    # 前章末尾
    src_dir = os.path.join(pdir, "原文")
    if os.path.isdir(src_dir):
        files = sorted(f for f in os.listdir(src_dir) if f.endswith(".md"))
        if fname in files and files.index(fname) > 0:
            prev = files[files.index(fname) - 1]
            prev_zh = _zh_path(project, prev)
            tail_file = prev_zh if os.path.isfile(prev_zh) else os.path.join(src_dir, prev)
            if os.path.isfile(tail_file):
                tail = _read_text(tail_file).strip()[-PACK_PREV_TAIL:]
                out.append(f"\n【前章末尾衔接·{'译文' if os.path.isfile(prev_zh) else '原文'}·{prev}】")
                out.append(tail)

    # 本章标题清单
    heads = [ln.rstrip() for ln in src.splitlines() if _HEADING_RE.match(ln)]
    if heads:
        out.append("\n【本章标题（翻译时合并为「英文 / 中文」单行）】")
        out.extend("- " + h for h in heads)
    return "\n".join(out)


def tool_get_blocks(project, fname):
    _safe_component(fname)
    _log_activity("get_blocks", project, fname)
    src_path = _src_path(project, fname)
    if not os.path.isfile(src_path):
        raise ToolError(f"原文不存在: {project}/原文/{fname}")
    src = _read_text(src_path)
    blocks = _split_blocks(src)
    pairs, _t = _parse_existing_pairs(_zh_path(project, fname))
    valid = _valid_prefix(blocks, pairs)
    remaining = [b["i"] for b in blocks if b["i"] > valid]
    payload = {
        "file": fname,
        "total_chars": len(src),
        "translated_blocks": valid,
        "remaining_blocks": remaining,
        "hint": "块级断点续译：只翻 remaining_blocks 中的块；含 heading 的块需提供 title_zh（纯中文标题，不带#）；已译块服务端自动保留，可用 submit_translation 只提交剩余块",
        "blocks": [
            {"i": b["i"], "heading": b["heading"], "translated": b["i"] <= valid,
             "chars": len(b["text"]), "text": b["text"]}
            for b in blocks
        ],
    }
    return json.dumps(payload, ensure_ascii=False)


def tool_submit_translation(project, fname, blocks):
    _safe_component(fname)
    _log_activity("submit", project, fname)
    _touch_lock(project)  # 提交即心跳：维持"一书一主"的活跃锁
    src_path = _src_path(project, fname)
    if not os.path.isfile(src_path):
        raise ToolError(f"原文不存在: {project}/原文/{fname}")
    if not isinstance(blocks, dict) or not blocks:
        raise ToolError("blocks 须为 {块号: {chinese: 正文, title_zh: 中文标题?}} 非空对象；允许只提交部分块（按序前缀），服务端自动合并既有译文")
    src_blocks = _split_blocks(_read_text(src_path))
    # 合并既有部分译文（前缀对齐 + 原文比对，防原文变更后错位复用）
    zh_path = _zh_path(project, fname)
    pairs, old_titles = _parse_existing_pairs(zh_path)
    valid = _valid_prefix(src_blocks, pairs)
    zh_map, title_map = {}, {}
    ti = 0
    for b in src_blocks[:valid]:
        zh_map[b["i"]] = pairs[b["i"] - 1][1]
        if b["heading"]:
            title_map[b["i"]] = old_titles[ti] if ti < len(old_titles) else ""
            ti += 1
    # 应用本次提交（同号覆盖旧译）
    for b in src_blocks:
        key = str(b["i"])
        if key not in blocks:
            continue
        item = blocks[key]
        if not isinstance(item, dict) or not item.get("chinese", "").strip():
            raise ToolError(f"第 {b['i']} 块的 chinese 译文为空")
        zh_map[b["i"]] = item["chinese"].strip()
        title_zh = (item.get("title_zh") or "").strip().lstrip("#").strip()
        if b["heading"]:
            if not title_zh and not title_map.get(b["i"]):
                raise ToolError(f"第 {b['i']} 块含标题 {b['heading']!r}，必须提供 title_zh")
            if title_zh:
                title_map[b["i"]] = title_zh
    # 只落盘连续覆盖的前缀块（保证块序完整、可被断点复用）
    parts, covered = [], 0
    for b in src_blocks:
        if b["i"] not in zh_map:
            break
        if b["heading"]:
            parts.append(f"{b['heading']} / {title_map.get(b['i'], '')}")
        parts.append("===Original===\n\n" + b["text"] + "\n\n===Chinese===\n\n" + zh_map[b["i"]] + "\n")
        covered += 1
    if covered == 0:
        raise ToolError("没有任何可落盘的完整块")
    os.makedirs(os.path.dirname(zh_path), exist_ok=True)
    with open(zh_path, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(parts).rstrip() + "\n")
    q, rows = None, None
    stem = fname[:-3] if fname.endswith(".md") else fname
    csv_name = f"{stem}.md"
    if covered < len(src_blocks):
        # 块级断点：部分落盘，保持 doing，不回填、不判 done
        with _queue_lock(project):
            q, rows = _read_queue(project)
            _set_row_status(rows, csv_name, "doing")
            _write_queue(q, rows)
        held = [b["i"] for b in src_blocks[covered:] if b["i"] in zh_map]
        msg = (f"PARTIAL: {covered}/{len(src_blocks)} 块已落盘 {zh_path}（CSV 保持 doing）\n"
               f"剩余块: {[b['i'] for b in src_blocks[covered:]]}\n"
               f"续译: 重新 get_blocks 会标记已译块，补齐剩余块后再次 submit_translation")
        if held:
            msg += f"\n注意: 块 {held} 已提交但因前缀未连续暂未落盘，下次提交请包含它们"
        return msg
    struct_ok, report = _run_checker(zh_path)
    suspicious = [ln for ln in report.splitlines() if ln.strip().startswith("原文:")]
    if struct_ok:
        with _queue_lock(project):
            q, rows = _read_queue(project)
            _set_row_status(rows, csv_name, "done")
            _write_queue(q, rows)
            book_done = not any(
                r and _row_status(r) in ("todo", "doing") for r in rows[1:]
            )
        # 整书收官：清掉本书 MCP 认领锁，避免换书后残留 48h 幽灵锁
        if book_done:
            lock_exists, holder, _age, expired = _lock_info(project)
            if lock_exists and (expired or _holder_is_mcp(holder)):
                try:
                    os.remove(_lock_path(project))
                except OSError:
                    pass
        msg = f"PASS: {zh_path}（{covered} 块，校验通过，CSV 已回填 done）"
        if book_done:
            msg += "；本书 todo 清零，认领锁已清除"
        if suspicious:
            msg += f"\n数字锚点提示（多为误报，供人工抽查）: {len(suspicious)} 处，前5: " + " | ".join(s.strip()[:60] for s in suspicious[:5])
        return msg
    # 结构违规：不回填 done，返回错误行供按行修复后重新 submit（幂等覆盖）
    errs = [ln for ln in report.splitlines() if ln.strip() and not ln.startswith("文件:")][:20]
    return "FAIL(结构契约未过，未回填 done；修复后重新 submit_translation 即可覆盖):\n" + "\n".join(errs)


# ---------- MCP stdio 服务 ----------

TOOLS_SPEC = [
    {
        "name": "batch_begin",
        "description": "翻译批次续跑入口（幂等）。按确定性分区计算批次书单；块级回收 doing 残留（全部块已译且过校验→回填done；部分块已译→保持doing标注断点待续；无可复用→重置todo）；返回重试队列+候选书单+建议首选。每个额度窗口/会话开始时调用一次。batch_id=0 仅只读总览。",
        "inputSchema": {
            "type": "object",
            "properties": {
                "batch_id": {"type": "integer", "enum": [0, 1, 2, 3]},
                "dry_run": {"type": "boolean", "default": False},
            },
            "required": ["batch_id"],
        },
    },
    {
        "name": "claim_task",
        "description": "认领项目首个 todo 章节（置 doing + 刷新认领锁）。返回章节文件名与剩余 todo 数。并发子代理各自调用即天然互斥。",
        "inputSchema": {
            "type": "object",
            "properties": {"project": {"type": "string"}},
            "required": ["project"],
        },
    },
    {
        "name": "context_pack",
        "description": "单章翻译上下文包：领域配置摘要 + 术语表本章命中词条 + 黄金样本节选 + 前章末尾衔接 + 本章标题清单。替代逐个读 6 个配置文件。",
        "inputSchema": {
            "type": "object",
            "properties": {"project": {"type": "string"}, "file": {"type": "string"}},
            "required": ["project", "file"],
        },
    },
    {
        "name": "get_blocks",
        "description": "读取原文并分块返回（标题与正文分离，块约≤2.4KB，几百字数段一块）。带块级断点标记：translated/remaining_blocks 指明已译块，只需翻译剩余块。",
        "inputSchema": {
            "type": "object",
            "properties": {"project": {"type": "string"}, "file": {"type": "string"}},
            "required": ["project", "file"],
        },
    },
    {
        "name": "submit_translation",
        "description": "提交各块中文译文：服务端自动合并既有已译块、拼装双语文件（标题合并「En / Zh」+ 交替 ===Original===/===Chinese===）、落盘、跑 check_bilingual.py。全部块齐→校验通过回填 CSV done（返回PASS）；只交部分块→部分落盘保持 doing（返回PARTIAL及剩余块），天然支持块级断点续译。幂等可重复提交覆盖。blocks 格式: {\"1\": {\"chinese\": \"...\", \"title_zh\": \"...\"}}",
        "inputSchema": {
            "type": "object",
            "properties": {
                "project": {"type": "string"},
                "file": {"type": "string"},
                "blocks": {"type": "object"},
            },
            "required": ["project", "file", "blocks"],
        },
    },
]

_DISPATCH = {
    "batch_begin": lambda a: tool_batch_begin(a.get("batch_id", 0), bool(a.get("dry_run", False))),
    "claim_task": lambda a: tool_claim_task(a.get("project", "")),
    "context_pack": lambda a: tool_context_pack(a.get("project", ""), a.get("file", "")),
    "get_blocks": lambda a: tool_get_blocks(a.get("project", ""), a.get("file", "")),
    "submit_translation": lambda a: tool_submit_translation(a.get("project", ""), a.get("file", ""), a.get("blocks")),
}


def _send(obj):
    sys.stdout.write(json.dumps(obj, ensure_ascii=False) + "\n")
    sys.stdout.flush()


def main():
    try:
        sys.stdin.reconfigure(encoding="utf-8", errors="replace")
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            msg = json.loads(line)
        except json.JSONDecodeError:
            continue
        method = msg.get("method", "")
        mid = msg.get("id")
        if mid is None:  # notification
            continue
        try:
            if method == "initialize":
                pv = (msg.get("params") or {}).get("protocolVersion") or "2024-11-05"
                result = {
                    "protocolVersion": pv,
                    "capabilities": {"tools": {"listChanged": False}},
                    "serverInfo": {"name": "translate-mcp", "version": "1.0.0"},
                }
            elif method == "ping":
                result = {}
            elif method == "tools/list":
                result = {"tools": TOOLS_SPEC}
            elif method == "tools/call":
                params = msg.get("params") or {}
                name = params.get("name", "")
                args = params.get("arguments") or {}
                if name not in _DISPATCH:
                    raise ToolError(f"未知工具: {name}")
                try:
                    text = _DISPATCH[name](args)
                    result = {"content": [{"type": "text", "text": text}]}
                except ToolError as e:
                    result = {"content": [{"type": "text", "text": f"错误: {e}"}], "isError": True}
            elif method in ("resources/list", "resources/templates/list"):
                result = {"resources": []}
            elif method == "prompts/list":
                result = {"prompts": []}
            else:
                _send({"jsonrpc": "2.0", "id": mid, "error": {"code": -32601, "message": f"method not found: {method}"}})
                continue
            _send({"jsonrpc": "2.0", "id": mid, "result": result})
        except Exception as e:  # 兜底：不让单次异常杀死服务器
            _send({"jsonrpc": "2.0", "id": mid, "error": {"code": -32603, "message": f"internal error: {e}"}})


if __name__ == "__main__":
    if not os.path.isdir(PROJ_DIR):
        print(f"错误: 找不到项目目录 {PROJ_DIR}", file=sys.stderr)
        sys.exit(1)
    main()
