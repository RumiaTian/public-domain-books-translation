# Plan.md — william-morris_the-sundering-flood

## 本计划信息

- **项目名称**：william-morris_the-sundering-flood（分离洪流（William Morris: The Sundering Flood, 1897））
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
| `原文/*.md` | 源文（68 文件） | 不改 |
| `译文/*.zh-CN.md` | 译文产出（块对照双语） | 翻译 agent 产出 |

执行步骤按 `prompts/翻译计划模板.md`「执行步骤」9 步推进。

---

## 篇目清单

| # | 篇名 | 源文 | 大小 | 状态 |
|---|------|------|------|------|
| 1 | chapter-1 | chapter-1.md | 9.7KB | todo |
| 2 | chapter-2 | chapter-2.md | 10.0KB | todo |
| 3 | chapter-3 | chapter-3.md | 6.9KB | todo |
| 4 | chapter-4 | chapter-4.md | 5.3KB | todo |
| 5 | chapter-5 | chapter-5.md | 4.9KB | todo |
| 6 | chapter-6 | chapter-6.md | 7.5KB | todo |
| 7 | chapter-7 | chapter-7.md | 7.8KB | todo |
| 8 | chapter-8 | chapter-8.md | 3.8KB | todo |
| 9 | chapter-9 | chapter-9.md | 11.9KB | todo |
| 10 | chapter-10 | chapter-10.md | 9.6KB | todo |
| 11 | chapter-11 | chapter-11.md | 10.6KB | todo |
| 12 | chapter-12 | chapter-12.md | 5.8KB | todo |
| 13 | chapter-13 | chapter-13.md | 6.2KB | todo |
| 14 | chapter-14 | chapter-14.md | 7.1KB | todo |
| 15 | chapter-15 | chapter-15.md | 6.5KB | todo |
| 16 | chapter-16 | chapter-16.md | 11.2KB | todo |
| 17 | chapter-17 | chapter-17.md | 4.9KB | todo |
| 18 | chapter-18 | chapter-18.md | 3.3KB | todo |
| 19 | chapter-19 | chapter-19.md | 7.2KB | todo |
| 20 | chapter-20 | chapter-20.md | 5.5KB | todo |
| 21 | chapter-21 | chapter-21.md | 5.8KB | todo |
| 22 | chapter-22 | chapter-22.md | 5.9KB | todo |
| 23 | chapter-23 | chapter-23.md | 8.4KB | todo |
| 24 | chapter-24 | chapter-24.md | 10.5KB | todo |
| 25 | chapter-25 | chapter-25.md | 11.2KB | todo |
| 26 | chapter-26 | chapter-26.md | 7.5KB | todo |
| 27 | chapter-27 | chapter-27.md | 9.1KB | todo |
| 28 | chapter-28 | chapter-28.md | 3.5KB | todo |
| 29 | chapter-29 | chapter-29.md | 5.7KB | todo |
| 30 | chapter-30 | chapter-30.md | 18.1KB | todo |
| 31 | chapter-31 | chapter-31.md | 1.7KB | todo |
| 32 | chapter-32 | chapter-32.md | 9.7KB | todo |
| 33 | chapter-33 | chapter-33.md | 3.3KB | todo |
| 34 | chapter-34 | chapter-34.md | 9.2KB | todo |
| 35 | chapter-35 | chapter-35.md | 7.9KB | todo |
| 36 | chapter-36 | chapter-36.md | 4.3KB | todo |
| 37 | chapter-37 | chapter-37.md | 6.0KB | todo |
| 38 | chapter-38 | chapter-38.md | 1.8KB | todo |
| 39 | chapter-39 | chapter-39.md | 12.0KB | todo |
| 40 | chapter-40 | chapter-40.md | 9.7KB | todo |
| 41 | chapter-41 | chapter-41.md | 5.1KB | todo |
| 42 | chapter-42 | chapter-42.md | 5.1KB | todo |
| 43 | chapter-43 | chapter-43.md | 6.6KB | todo |
| 44 | chapter-44 | chapter-44.md | 7.4KB | todo |
| 45 | chapter-45 | chapter-45.md | 9.7KB | todo |
| 46 | chapter-46 | chapter-46.md | 4.5KB | todo |
| 47 | chapter-47 | chapter-47.md | 7.5KB | todo |
| 48 | chapter-48 | chapter-48.md | 7.7KB | todo |
| 49 | chapter-49 | chapter-49.md | 4.1KB | todo |
| 50 | chapter-50 | chapter-50.md | 4.9KB | todo |
| 51 | chapter-51 | chapter-51.md | 9.0KB | todo |
| 52 | chapter-52 | chapter-52.md | 9.6KB | todo |
| 53 | chapter-53 | chapter-53.md | 4.0KB | todo |
| 54 | chapter-54 | chapter-54.md | 10.9KB | todo |
| 55 | chapter-55 | chapter-55.md | 14.9KB | todo |
| 56 | chapter-56 | chapter-56.md | 9.7KB | todo |
| 57 | chapter-57 | chapter-57.md | 11.9KB | todo |
| 58 | chapter-58 | chapter-58.md | 5.3KB | todo |
| 59 | chapter-59 | chapter-59.md | 6.3KB | todo |
| 60 | chapter-60 | chapter-60.md | 4.0KB | todo |
| 61 | chapter-61 | chapter-61.md | 6.2KB | todo |
| 62 | chapter-62 | chapter-62.md | 8.1KB | todo |
| 63 | chapter-63 | chapter-63.md | 7.4KB | todo |
| 64 | chapter-64 | chapter-64.md | 11.1KB | todo |
| 65 | chapter-65 | chapter-65.md | 2.0KB | todo |
| 66 | chapter-66 | chapter-66.md | 3.2KB | todo |
| 67 | chapter-67 | chapter-67.md | 3.0KB | todo |
| 68 | chapter-68 | chapter-68.md | 2.8KB | todo |

---

## 运行日志

| 日期 | 事件 | 备注 |
|------|------|------|
| 2026-08-17 | 建项目 | epub 提取 68 篇，术语表初版建成 |
