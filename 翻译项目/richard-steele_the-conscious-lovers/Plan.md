# 翻译计划：有情的恋人

## 本计划信息

- **项目名称**：richard-steele_the-conscious-lovers
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/小说文学.md
- **术语表**：术语表.md
- **执行模式**：连续（中篇；见 WORKFLOW.md「单篇翻译流程」）

## 执行步骤

单篇 9 步（读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志）以 `prompts/翻译计划模板.md`「执行步骤」为准，本文件不重复。连续模式下由主 agent 直接执行。

## 篇目清单

由 `translation_queue.csv` 管理（11 篇，约 149KB）。

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-08-27 | 全书 11 章 | 完成 11/11 | 首派[1301]拦截后免责重派；昨 19:28 三代理撞[1308]限额中断，剩余章节由并行批次补完；抽验 preface/act-v/prologue 全过 |
| 2026-08-26 | act-ii | done | 委派子代理，check 退出码 0（21 对块）；术语表回填 18 条定名 |
| 2026-08-26 | act-iv | done | 委派子代理，check 退出码 0（24 对块） |
| 2026-08-26 | act-v | done | 委派子代理，check 退出码 0（19 对块） |
| 2026-08-26 | dedication / epigraph / prologue / epilogue / endnotes | done | 委派子代理，5 件 check 全过 |
| 2026-08-26 | 全书 11/11 done | 完结 | 主代理抽验 8 文件全过、CSV 无 doing；refresh_progress 已刷新 |
