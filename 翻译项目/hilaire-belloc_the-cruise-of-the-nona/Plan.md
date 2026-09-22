# 翻译计划（诺娜号巡航记）

## 本计划信息

- **项目名称**：诺娜号巡航记（The Cruise of the Nona，希莱尔·贝洛克）
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

## 篇目清单

> 原书无章节，为连续散文；据原文场景分隔（`<hr>`）析为 16 部，加 2 篇卷首，共 18 篇。详见 `translation_queue.csv`。

| # | 篇名 | 源文 | 大小 | 状态 |
|---|------|------|------|------|
| 1 | 献词（致菲利普·克肖） | 01-dedication.md | 0.1KB | todo |
| 2 | 致莫里斯·巴林（题献） | 02-to-maurice-baring.md | 12.9KB | todo |
| 3 | 正文 第一部 | 03-cruise-part-01.md | 40.3KB | todo |
| 4 | 正文 第二部 | 04-cruise-part-02.md | 41.4KB | todo |
| 5 | 正文 第三部 | 05-cruise-part-03.md | 14.4KB | todo |
| 6 | 正文 第四部 | 06-cruise-part-04.md | 45.8KB | todo |
| 7 | 正文 第五部 | 07-cruise-part-05.md | 46.2KB | todo |
| 8 | 正文 第六部 | 08-cruise-part-06.md | 31.7KB | todo |
| 9 | 正文 第七部 | 09-cruise-part-07.md | 34.6KB | todo |
| 10 | 正文 第八部 | 10-cruise-part-08.md | 33.7KB | todo |
| 11 | 正文 第九部 | 11-cruise-part-09.md | 43.3KB | todo |
| 12 | 正文 第十部 | 12-cruise-part-10.md | 44.0KB | todo |
| 13 | 正文 第十一部 | 13-cruise-part-11.md | 32.1KB | todo |
| 14 | 正文 第十二部 | 14-cruise-part-12.md | 36.9KB | todo |
| 15 | 正文 第十三部 | 15-cruise-part-13.md | 50.3KB | todo |
| 16 | 正文 第十四部 | 16-cruise-part-14.md | 29.3KB | todo |
| 17 | 正文 第十五部 | 17-cruise-part-15.md | 43.6KB | todo |
| 18 | 正文 第十六部 | 18-cruise-part-16.md | 21.5KB | todo |

## 执行步骤

按 `prompts/翻译计划模板.md`「执行步骤」9 步推进（读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志）。

委派模式下，各子代理以较早完成的译文（尤以 03-cruise-part-01 为散文基调范本）为风格黄金样本，保持全书絮语体声口一致。

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
