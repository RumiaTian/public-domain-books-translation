# 翻译计划（《克雷格·肯尼迪科学探案集》）

## 本计划信息

- **项目名称**：《克雷格·肯尼迪科学探案集》（阿瑟·B·里夫）
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/小说文学.md
- **术语表**：术语表.md

## 文件分工

| 文件 | 作用 | 谁来改 |
|------|------|--------|
| `项目说明.md` | 项目基本信息、领域配置、篇目清单 | 人工 |
| `术语表.md` | 翻译硬约束层。每篇译完补充新词 | agent / 人工 |
| `translation_queue.csv` | 任务队列。每行一文件，`file, size_kb, status` 三列 | 翻译前改 doing，完成后改 done |
| `Plan.md`（本文件） | 执行步骤 + 运行日志 | agent 追加日志 |
| `原文/*.md` | 源文 | 不改 |
| `译文/*.zh-CN.md` | 译文产出（块对照双语） | 翻译 agent 产出 |

## 执行步骤

按 `prompts/翻译计划模板.md`「执行步骤」9 步推进（读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志）。委派模式下由主 agent 把每篇下沉到一次性子代理执行。

## 篇目清单

| # | 篇名 | 源文 | 状态 |
|---|------|------|------|
| 1 | Craig Kennedy’s Theories（序章） | prologue.md | todo |
| 2 | The Silent Bullet | the-silent-bullet.md | todo |
| 3 | The Scientific Cracksman | the-scientific-cracksman.md | todo |
| 4 | The Bacteriological Detective | the-bacteriological-detective.md | todo |
| 5 | The Deadly Tube | the-deadly-tube.md | todo |
| 6 | The Seismograph Adventure | the-seismograph-adventure.md | todo |
| 7 | The Diamond Maker | the-diamond-maker.md | todo |
| 8 | The Azure Ring | the-azure-ring.md | todo |
| 9 | “Spontaneous Combustion” | spontaneous-combustion.md | todo |
| 10 | The Terror in the Air | the-terror-in-the-air.md | todo |
| 11 | The Black Hand | the-black-hand.md | todo |
| 12 | The Artificial Paradise | the-artificial-paradise.md | todo |
| 13 | The Steel Door | the-steel-door.md | todo |

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-08-13 | - | 建项目 | 从 Standard Ebooks epub 提取序章 + 12 篇探案，建术语表初版，生成队列（13 篇，约 500KB）。领域小说文学，形态短篇集，委派模式。 |
