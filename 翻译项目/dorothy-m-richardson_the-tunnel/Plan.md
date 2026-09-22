# 翻译计划（隧道 / The Tunnel）

## 本计划信息

- **项目名称**：《隧道》（多萝西·米勒·理查森）/ The Tunnel (Dorothy M. Richardson)
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

按 `prompts/翻译计划模板.md`「执行步骤」9 步推进（读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志）。本作品判定为长篇 → 委派模式，主 agent 只当调度员，每章的 9 步下沉到一次性子代理执行（简报：项目说明 + 术语表 + 通用翻译引擎 + 小说文学领域配置 + 黄金样本 + 前章末尾 2-3 段，并发 ≤3）。长章（chapter-3、chapter-6 等 >50KB）由子代理按通用翻译引擎第七节分段处理，单章不可中途截断。

## 篇目清单

| # | 篇名 | 源文 | 大小 | 状态 |
|---|------|------|------|------|
| 1 | 第一章 | chapter-1.md | 25.5KB | todo |
| 2 | 第二章 | chapter-2.md | 15.8KB | todo |
| 3 | 第三章 | chapter-3.md | 88.5KB | todo |
| 4 | 第四章 | chapter-4.md | 47.4KB | todo |
| 5 | 第五章 | chapter-5.md | 18.3KB | todo |
| 6 | 第六章 | chapter-6.md | 55.7KB | todo |
| 7 | 第七章 | chapter-7.md | 0.9KB | todo |
| 8 | 第八章 | chapter-8.md | 12.8KB | todo |
| 9 | 第九章 | chapter-9.md | 16.8KB | todo |
| 10 | 第十章 | chapter-10.md | 28.0KB | todo |
| 11 | 第十一章 | chapter-11.md | 9.9KB | todo |
| 12 | 第十二章 | chapter-12.md | 3.4KB | todo |
| 13 | 第十三章 | chapter-13.md | 6.2KB | todo |
| 14 | 第十四章 | chapter-14.md | 7.8KB | todo |
| 15 | 第十五章 | chapter-15.md | 20.1KB | todo |
| 16 | 第十六章 | chapter-16.md | 4.6KB | todo |
| 17 | 第十七章 | chapter-17.md | 9.7KB | todo |
| 18 | 第十八章 | chapter-18.md | 5.2KB | todo |
| 19 | 第十九章 | chapter-19.md | 2.8KB | todo |
| 20 | 第二十章 | chapter-20.md | 7.1KB | todo |
| 21 | 第二十一章 | chapter-21.md | 3.9KB | todo |
| 22 | 第二十二章 | chapter-22.md | 13.2KB | todo |
| 23 | 第二十三章 | chapter-23.md | 4.3KB | todo |
| 24 | 第二十四章 | chapter-24.md | 8.3KB | todo |
| 25 | 第二十五章 | chapter-25.md | 8.2KB | todo |
| 26 | 第二十六章 | chapter-26.md | 17.7KB | todo |
| 27 | 第二十七章 | chapter-27.md | 6.5KB | todo |
| 28 | 第二十八章 | chapter-28.md | 5.3KB | todo |
| 29 | 第二十九章 | chapter-29.md | 7.1KB | todo |
| 30 | 第三十章 | chapter-30.md | 28.2KB | todo |
| 31 | 第三十一章 | chapter-31.md | 26.0KB | todo |
| 32 | 第三十二章 | chapter-32.md | 14.7KB | todo |
| 33 | 第三十三章 | chapter-33.md | 5.8KB | todo |

合计 33 章，约 535.6KB / 9.4 万英文词。

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
