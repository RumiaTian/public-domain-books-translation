# Plan.md — w-e-b-du-bois_darkwater

## 本计划信息

- **项目名称**：w-e-b-du-bois_darkwater（暗水（W. E. B. Du Bois: Darkwater, 1920））
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
| `原文/*.md` | 源文（13 文件） | 不改 |
| `译文/*.zh-CN.md` | 译文产出（块对照双语） | 翻译 agent 产出 |

执行步骤按 `prompts/翻译计划模板.md`「执行步骤」9 步推进。

---

## 篇目清单

| # | 篇名 | 源文 | 大小 | 状态 |
|---|------|------|------|------|
| 1 | chapter-1 | chapter-1.md | 33.1KB | todo |
| 2 | chapter-2 | chapter-2.md | 38.3KB | todo |
| 3 | chapter-3 | chapter-3.md | 37.5KB | todo |
| 4 | chapter-4 | chapter-4.md | 41.6KB | todo |
| 5 | chapter-5 | chapter-5.md | 36.8KB | todo |
| 6 | chapter-6 | chapter-6.md | 41.1KB | todo |
| 7 | chapter-7 | chapter-7.md | 43.1KB | todo |
| 8 | chapter-8 | chapter-8.md | 38.0KB | todo |
| 9 | chapter-9 | chapter-9.md | 44.5KB | todo |
| 10 | chapter-10 | chapter-10.md | 31.9KB | todo |
| 11 | dedication | dedication.md | 0.0KB | todo |
| 12 | preface | preface.md | 1.5KB | todo |
| 13 | prologue | prologue.md | 2.8KB | todo |

---

## 运行日志

| 日期 | 事件 | 备注 |
|------|------|------|
| 2026-08-17 | 建项目 | epub 提取 13 篇，术语表初版建成 |
