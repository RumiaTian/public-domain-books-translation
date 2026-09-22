# Plan.md — w-n-p-barbellion_the-journal-of-a-disappointed-man

## 本计划信息

- **项目名称**：w-n-p-barbellion_the-journal-of-a-disappointed-man（一个失意者的日记（W. N. P. Barbellion: The Journal of a Disappointed Man, 1919））
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/小说文学.md
- **术语表**：术语表.md

---

## 文件分工

| 文件 | 作用 | 谁来改 |
|------|------|--------|
| `项目说明.md` | 项目基本信息、领域配置、篇目清单 | 人工 |
| `术语表.md` | 翻译硬约束层。每篇译完补充新词 | agent / 人工 |
| `translation_queue.csv` | 任务队列。每行一文件，`file, size_kb, status` 三列 | 翻译前改 doing，完成后改 done |
| `Plan.md`（本文件） | 执行步骤 + 运行日志 | agent 追加日志 |
| `原文/*.md` | 源文（5 文件） | 不改 |
| `译文/*.zh-CN.md` | 译文产出（块对照双语） | 翻译 agent 产出 |

执行步骤按 `prompts/翻译计划模板.md`「执行步骤」9 步推进。

---

## 篇目清单

| # | 篇名 | 源文 | 大小 | 状态 |
|---|------|------|------|------|
| 1 | part-1 | part-1.md | 97.6KB | todo |
| 2 | part-2 | part-2.md | 292.1KB | todo |
| 3 | part-3 | part-3.md | 158.2KB | todo |
| 4 | epigraph | epigraph.md | 0.5KB | todo |
| 5 | introduction | introduction.md | 7.0KB | todo |

---

## 运行日志

| 日期 | 事件 | 备注 |
|------|------|------|
| 2026-08-17 | 建项目 | epub 提取 5 篇，术语表初版建成 |
