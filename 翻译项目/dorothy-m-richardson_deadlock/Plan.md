# 翻译计划（僵局 / Deadlock）

## 本计划信息

- **项目名称**：《僵局》（多萝西·米勒·理查森）/ Deadlock (Dorothy M. Richardson)
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

按 `prompts/翻译计划模板.md`「执行步骤」9 步推进（读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志）。本作品判定为中篇 → 连续模式，由主 agent 在自身上下文内逐章执行 9 步；单批受上下文限制时可分批续译。

## 篇目清单

| # | 篇名 | 源文 | 大小 | 状态 |
|---|------|------|------|------|
| 1 | 第一章 | chapter-1.md | 82.4KB | todo |
| 2 | 第二章 | chapter-2.md | 77.0KB | todo |
| 3 | 第三章 | chapter-3.md | 99.4KB | todo |
| 4 | 第四章 | chapter-4.md | 6.9KB | todo |
| 5 | 第五章 | chapter-5.md | 20.1KB | todo |
| 6 | 第六章 | chapter-6.md | 15.0KB | todo |
| 7 | 第七章 | chapter-7.md | 49.0KB | todo |
| 8 | 第八章 | chapter-8.md | 21.7KB | todo |
| 9 | 第九章 | chapter-9.md | 6.4KB | todo |
| 10 | 第十章 | chapter-10.md | 9.8KB | todo |
| 11 | 第十一章 | chapter-11.md | 36.8KB | todo |
| 12 | 第十二章 | chapter-12.md | 16.5KB | todo |
| 13 | 第十三章 | chapter-13.md | 14.4KB | todo |

合计 13 章，约 455.4KB / 7.8 万英文词。

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
