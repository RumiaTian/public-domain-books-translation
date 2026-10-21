# 阶段二：翻译执行工作流（2_翻译WORKFLOW.md）

本文件是**翻译执行阶段的标准操作手册**。
面向 `翻译项目/` 目录下的 647 本精选公版书目，按照任务队列推进高质量双语对照翻译。

> **2026-10-21 重构**：执行方式统一为 **translate-mcp 工具流 + 主模型直译**（每日 3~4 个额度窗口定时推进，提示词正本见 `prompts/批量提示词/2_定时轮次翻译提示词.md`）。旧版"子代理委派/连续双模式、手工 9 步闭环、跨书 Compact、定时轮次并发池"等章节已废止，历史版本见 git。

---

## 一、translate-mcp 工具流（唯一执行路径）

工具来自用户级 MCP 服务器（新会话自动可用，工具名前缀 `mcp__translate-mcp__`）。状态只存在于文件（项目 CSV / 译文 / 认领锁），工具调用即状态推进。

会话标准流程：

1. `batch_begin(batch_id=批次号)` —— 摸底 + doing/断点回收 + 候选书单一步完成；重试队列（含「断点:已译 n/N 块」「整章重投」条目）最优先，建议首选已给出。
2. `claim_task(project)` —— 认领首个 todo 章节（置 doing + 刷新认领锁，跨进程互斥）；返回被外部锁持有则换候选单下一本。
3. `context_pack(project, file)` —— 本章命中术语 + 领域摘要 + 黄金样本节选 + 前章末尾衔接，一次到位。
4. `get_blocks(project, file)` —— 原文分块（约 2.4KB/块，块级断点标记，只译待译块）。
5. 主模型直译 —— 遵守下方格式契约。
6. `submit_translation(project, file, blocks)` —— 服务端拼装双语文件并运行 `check_bilingual.py`：
   - **PASS**：校验通过，CSV 自动回填 done，进下一章；
   - **PARTIAL**：已译块落盘、CSV 保持 doing，按"剩余块"提示补齐后重交；
   - **FAIL**：只返回违规行，修复对应块后重交（幂等覆盖）；同一章 3 次未过即跳过，换下一篇。
7. 循环 2–6 至本书 todo 清零，回 `batch_begin` 候选单换下一本。
8. 收尾：`python scripts/refresh_progress.py` 重建总控状态（根 CSV / Plan.md）→ `git add -A && git commit` → `git -c http.proxy=http://127.0.0.1:7890 push`（git 失败一次即止）。

**中断与额度**：[1301] / 额度耗尽 / 连续报错 → 立即停止开新章。已译块随 PARTIAL 自动落盘，下一窗口 `batch_begin` 自动置顶续译，跨额度窗口天然衔接。

**格式契约**（服务端拼装与 `check_bilingual.py` 强制，模型侧只需遵守三条）：

- 术语硬约束：命中术语表源词必须采用指定译法；
- 保持原文数字锚点（数字、日期、计量不增不减不改写）；
- 标题只需给中文（title_zh），服务端合并为 `## En / Zh` 单行；正文成对标记 `===Original===` / `===Chinese===` 由服务端拼装。

**红线**：

- 批次划分参数（3 批 / index 法）冻结，与 `scan_candidates.py` 保持一致；
- 根 `translation_queue.csv` 由 `refresh_progress.py` 独占重建，逐章只写项目 CSV；
- 译文落盘唯一途径是 `submit_translation`。

---

## 二、项目架构与规范

每个翻译项目位于 `翻译项目/<项目名>/` 下，标准结构如下：

```text
翻译项目/<项目名>/
  ├── 项目说明.md           # 领域、形态、输出粒度、篇目清单
  ├── 术语表.md             # 翻译硬约束层（人物/地名/专名/术语的统一译法）
  ├── Plan.md              # 运行日志（由 refresh_progress.py 维护）
  ├── translation_queue.csv # file, size_kb, status (todo / doing / done)
  ├── 原文/*.md            # 转换自 EPUB spine 的分章源文（UTF-8 无 BOM）
  └── 译文/                # 双语对照产出目录 (*.zh-CN.md)
```

---

## 三、多批次并发互斥

多个批次任务并行推进时的防争抢机制（均由工具流自动执行）：

1. **空间分片**：批次划分由 `scan_candidates.py` 确定性分区（3 批，目录序 index 法，参数冻结），批次间候选池无交集。
2. **动态排他锁**：`认领.md` 书级锁（锁龄 < 48h 视为活跃；`claim_task` 写入/刷新，MCP 持有的锁可被 MCP 接管）。
3. **会话绑定**：一条定时任务绑定其创建会话，轮次在会话内串行注入；因此各批次任务应创建在**各自独立的新会话**中，避免共享上下文。

---

## 四、产物与总控状态刷新

1. 译文结果文件：`翻译项目/<项目名>/译文/<章节>.zh-CN.md`（服务端拼装）。
2. 总控刷新（批次收尾运行，可带 `--snapshot/--log-*` 参数记录运行日志）：
   ```bash
   python scripts/refresh_progress.py
   ```
