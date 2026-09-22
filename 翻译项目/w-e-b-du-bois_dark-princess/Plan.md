# Plan.md — w-e-b-du-bois_dark-princess

## 本计划信息

- **项目名称**：w-e-b-du-bois_dark-princess（黑暗公主（W. E. B. Du Bois: Dark Princess, 1928））
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
| `原文/*.md` | 源文（6 文件） | 不改 |
| `译文/*.zh-CN.md` | 译文产出（块对照双语） | 翻译 agent 产出 |

执行步骤按 `prompts/翻译计划模板.md`「执行步骤」9 步推进。

---

## 篇目清单

| # | 篇名 | 源文 | 大小 | 状态 |
|---|------|------|------|------|
| 1 | dedication | dedication.md | 0.3KB | todo |
| 2 | epilogue | epilogue.md | 0.6KB | todo |
| 3 | the-chicago-politician | the-chicago-politician.md | 229.6KB | todo |
| 4 | the-exile | the-exile.md | 67.9KB | todo |
| 5 | the-maharajah-of-bwodpur | the-maharajah-of-bwodpur.md | 206.3KB | todo |
| 6 | the-pullman-porter | the-pullman-porter.md | 143.3KB | todo |

---

## 运行日志

| 日期 | 事件 | 备注 |
|------|------|------|
| 2026-08-17 | 建项目 | epub 提取 6 篇，术语表初版建成 |
