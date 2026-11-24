#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
reorder_queues.py — 把未完结书目的 translation_queue.csv 重排为真实阅读序（EPUB spine 为准）。

策略：
- 取 原书/*.epub（多卷按文件名自然序拼接）的 OPF spine 条目（复用 epub_to_md.spine_entries）；
- md↔spine 对齐：先按文件名多重集完全一致直接对齐（epub_to_md kebab 命名产物），
  否则按「正文特征串」相似度（精确相等/前缀包含/difflib 比率）做 1:1 贪心匹配；
- 仅当全部 md 与全部 spine 条目一一对应时才重排；任何对不齐的情况打印清单并跳过该书；
- 硬约束：只改行序。每行原文逐字节保留（file/size_kb/status 原样），行数不变；
  不重命名、不删除 原文/ 与 译文/ 下任何文件。

用法：
    python scripts/reorder_queues.py                # dry-run：只输出计划，不写盘
    python scripts/reorder_queues.py --apply        # 落地写入
    python scripts/reorder_queues.py --only lardner # 只处理项目名含该子串的书
"""
import csv
import difflib
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from epub_to_md import spine_entries

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJ_DIR = os.path.join(ROOT, "翻译项目")
SIM_THRESHOLD = 0.60

_ROMAN_RE = re.compile(r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$", re.IGNORECASE)
_ROMAN_VAL = {"i": 1, "v": 5, "x": 10, "l": 50, "c": 100, "d": 500, "m": 1000}


def _roman_value(s):
    total, prev = 0, 0
    for ch in reversed(s.lower()):
        v = _ROMAN_VAL[ch]
        total = total - v if v < prev else total + v
        prev = max(prev, v)
    return total


def natural_key(name):
    keys = []
    for tok in re.findall(r"\d+|[A-Za-z]+", name):
        if tok.isdigit():
            keys.append((0, int(tok), ""))
        elif _ROMAN_RE.match(tok):
            keys.append((0, _roman_value(tok), ""))
        else:
            keys.append((1, 0, tok.lower()))
    return keys or [(2, 0, "")]


def norm_sig(text):
    s = re.sub(r"[^A-Za-z0-9]+", " ", text).strip().lower()
    return s[:400]


def similarity(a, b):
    if not a or not b:
        return 0.0
    if a == b:
        return 1.0
    probe = min(120, len(a), len(b))
    # 包含匹配要求较短一方有足够内容，防止「Part I」类卷分隔页短串虚高撞上长章节
    if min(len(a), len(b)) >= 60 and (a[:probe] in b or b[:probe] in a):
        return 0.95
    sm = difflib.SequenceMatcher(None, a, b)
    # 上界剪枝：real/quick 比率低于阈值就不做全量比对（诗集等大体量书目必需）
    if sm.real_quick_ratio() < SIM_THRESHOLD or sm.quick_ratio() < SIM_THRESHOLD:
        return 0.0
    return sm.ratio()


def is_unfinished(proj_path):
    q = os.path.join(proj_path, "translation_queue.csv")
    if not os.path.isfile(q):
        return False
    try:
        with open(q, "r", encoding="utf-8", errors="ignore", newline="") as f:
            rows = list(csv.reader(f))
    except OSError:
        return False
    return any(r and len(r) >= 3 and r[2].strip().lower() in ("todo", "doing") for r in rows[1:])


def load_raw_queue(qpath):
    """返回 (header_line, data_lines, had_trailing_newline)。行内容逐字节保留。"""
    with open(qpath, "r", encoding="utf-8", errors="strict", newline="") as f:
        raw = f.read()
    had_trailing = raw.endswith("\n")
    lines = raw.split("\n")
    if had_trailing:
        lines.pop()  # 末尾空串
    if not lines:
        raise ValueError("空队列文件")
    return lines[0], lines[1:], had_trailing


def spine_order_for(proj_path):
    """拼接各卷 spine 条目；返回 (entries, None) 或 (None, 错误原因)。"""
    epub_dir = os.path.join(proj_path, "原书")
    epubs = [f for f in sorted(os.listdir(epub_dir), key=natural_key) if f.endswith(".epub")] \
        if os.path.isdir(epub_dir) else []
    if not epubs:
        return None, "原书/ 无 EPUB，无法确定阅读序"
    entries = []
    for ep in epubs:
        try:
            entries += spine_entries(os.path.join(epub_dir, ep))
        except Exception as e:
            return None, f"EPUB 解析失败 {ep}: {e}"
    if not entries:
        return None, "spine 为空（全部条目被过滤）"
    return entries, None


def align_md_to_spine(md_sigs, entries):
    """返回 (order_md_files, method, min_score) 或 (None, 原因, None)。
    要求全部 md 一一配到不同 spine 条目；spine 侧多出的条目（插图页/注释等未入原文）
    仅当其对任何 md 的最佳分都低于阈值时才允许存在。"""
    md_names = [m for m, _ in md_sigs]
    entry_names = [e["file"] for e in entries]
    # 路径1：文件名多重集完全一致（epub_to_md kebab 产物）
    if len(md_names) == len(entry_names) and sorted(md_names) == sorted(entry_names):
        return entry_names, "文件名精确对齐", 1.0
    # 路径2：正文特征串对齐。先做特征串精确相等的 O(n) 预分配（渲染产物占绝大多数），
    # 剩余未配对再走带剪枝的相似度贪心
    md_used, ent_used, assign = set(), set(), {}
    min_score = 1.0
    sig_index = {}
    for ei, ent in enumerate(entries):
        sig_index.setdefault(ent["sig"], []).append(ei)
    for mi, (_, msig) in enumerate(md_sigs):
        cands = [ei for ei in sig_index.get(msig, ()) if ei not in ent_used]
        if cands:
            ei = cands[0]
            md_used.add(mi)
            ent_used.add(ei)
            assign[mi] = ei
    pairs = []
    rem_md = [(mi, msig) for mi, (_, msig) in enumerate(md_sigs) if mi not in md_used]
    rem_ent = [ei for ei in range(len(entries)) if ei not in ent_used]
    for mi, msig in rem_md:
        for ei in rem_ent:
            s = similarity(msig, entries[ei]["sig"])
            if s >= SIM_THRESHOLD:
                pairs.append((s, mi, ei))
    pairs.sort(reverse=True)
    for s, mi, ei in pairs:
        if mi in md_used or ei in ent_used:
            continue
        md_used.add(mi)
        ent_used.add(ei)
        assign[mi] = ei
        min_score = min(min_score, s)
    if len(assign) != len(md_names):
        unmatched_md = [md_names[i] for i in range(len(md_names)) if i not in md_used]
        return None, (f"签名对齐不全：{len(unmatched_md)} 个 md 无 spine 对应 "
                      f"{unmatched_md[:4]} (阈值 {SIM_THRESHOLD})"), None
    # spine 侧剩余条目必须确实没有 md 对应（防止漏配被当残留放过）
    leftovers = []
    for ei, ent in enumerate(entries):
        if ei in ent_used:
            continue
        best = max(similarity(ent["sig"], msig) for _, msig in md_sigs)
        if best >= SIM_THRESHOLD:
            return None, (f"spine 条目 {ent['file']} 疑似有对应 md 但未配上 (best={best:.2f})"), None
        leftovers.append(ent["file"])
    method = f"正文签名对齐(min={min_score:.2f}"
    if leftovers:
        method += f"；spine 多出 {len(leftovers)} 条无对应: {leftovers[:3]}{'…' if len(leftovers) > 3 else ''}"
    method += "）"
    # md 按 其对应 spine 条目位置 排列（assign: md下标 → spine下标）
    return [md_names[mi] for mi in sorted(assign, key=lambda mi: assign[mi])], method, min_score


def plan_book(name):
    """返回 dict：status(ok/skip/noop), method, min_score, changed, new_order, reason, qpath, raw_lines"""
    proj_path = os.path.join(PROJ_DIR, name)
    qpath = os.path.join(proj_path, "translation_queue.csv")
    src_dir = os.path.join(proj_path, "原文")
    result = {"name": name, "qpath": qpath, "status": "skip", "reason": "", "method": "",
              "min_score": None, "changed": False, "new_order": None}

    entries, err = spine_order_for(proj_path)
    if entries is None:
        result["reason"] = err
        return result

    md_files = sorted(f for f in os.listdir(src_dir) if f.endswith(".md")) if os.path.isdir(src_dir) else []
    md_sigs = [(m, norm_sig(open(os.path.join(src_dir, m), encoding="utf-8", errors="ignore").read()))
               for m in md_files]

    # 队列行集合必须与 原文 文件集合一致，否则重排无法安全落地
    header, data_lines, trailing = load_raw_queue(qpath)
    q_files = []
    for ln in data_lines:
        cols = next(csv.reader([ln]), None)
        if not cols or len(cols) < 3 or not cols[0].strip():
            result["reason"] = f"队列行格式异常: {ln[:60]!r}"
            return result
        q_files.append(cols[0].strip())
    if len(set(q_files)) != len(q_files):
        result["reason"] = "队列存在重复文件名"
        return result
    if set(q_files) != set(md_files):
        only_q = sorted(set(q_files) - set(md_files))[:4]
        only_m = sorted(set(md_files) - set(q_files))[:4]
        result["reason"] = f"队列与 原文/ 不一致（仅队列有 {only_q}；仅目录有 {only_m}）"
        return result

    order, method, min_score = align_md_to_spine(md_sigs, entries)
    if order is None:
        result["reason"] = method
        return result
    result["method"] = method
    result["min_score"] = min_score
    result["new_order"] = order
    result["changed"] = order != q_files
    result["status"] = "ok" if result["changed"] else "noop"
    result["raw"] = (header, data_lines, trailing)
    result["q_files"] = q_files
    return result


def apply_book(res):
    header, data_lines, trailing = res["raw"]
    rowmap = {}
    for ln in data_lines:
        fname = next(csv.reader([ln]))[0].strip()
        rowmap[fname] = ln
    new_lines = [header] + [rowmap[f] for f in res["new_order"]]
    out = "\n".join(new_lines) + ("\n" if trailing else "")
    with open(res["qpath"], "w", encoding="utf-8", newline="") as f:
        f.write(out)
    # 写后自检：行多重集必须与写前完全一致
    h2, d2, t2 = load_raw_queue(res["qpath"])
    assert sorted(d2) == sorted(data_lines) and h2 == header and t2 == trailing, \
        f"{res['name']}: 写后行集合与写前不一致，已中止"
    return len(data_lines)


def main():
    apply = "--apply" in sys.argv
    only = None
    if "--only" in sys.argv:
        only = sys.argv[sys.argv.index("--only") + 1]
    names = sorted(d for d in os.listdir(PROJ_DIR)
                   if os.path.isdir(os.path.join(PROJ_DIR, d)) and not d.startswith("_"))
    todo_books = [n for n in names if is_unfinished(os.path.join(PROJ_DIR, n))]
    if only:
        todo_books = [n for n in todo_books if only in n]
    print(f"未完结书目 {len(todo_books)} 本；模式={'APPLY 落地' if apply else 'DRY-RUN 预览'}\n")

    n_ok = n_noop = n_skip = 0
    skips = []
    for name in todo_books:
        try:
            res = plan_book(name)
        except Exception as e:
            res = {"name": name, "status": "skip", "reason": f"异常: {e}"}
        if res["status"] == "skip":
            n_skip += 1
            skips.append((name, res["reason"]))
            print(f"[SKIP] {name}: {res['reason']}")
            continue
        moved = sum(1 for a, b in zip(res["q_files"], res["new_order"]) if a != b)
        total = len(res["new_order"])
        tag = f"[{'APPLY' if apply else 'PLAN'}] {name}: {total} 章 ({res['method']})"
        if res["status"] == "noop":
            n_noop += 1
            print(f"[NOOP] {name}: 已是 spine 阅读序，无需改动")
            continue
        n_ok += 1
        print(f"{tag} 位置变动 {moved}/{total}；示例: "
              f"{res['q_files'][:3]} → {res['new_order'][:3]}")
        if apply:
            n = apply_book(res)
            print(f"        已写入 {n} 行（行集合自检通过）")
    print(f"\n汇总: 需重排 {n_ok} | 已正确 {n_noop} | 跳过 {n_skip}")
    if skips:
        print("\n== 跳过清单（需人工处理） ==")
        for n, r in skips:
            print(f"  {n}: {r}")
    if not apply:
        print("\n（dry-run 未写盘；确认后加 --apply 落地）")


if __name__ == "__main__":
    main()
