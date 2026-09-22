# 翻译计划（18号病房的病人）

## 本计划信息

- **项目名称**：18号病房的病人（mignon-g-eberhart_the-patient-in-room-18）
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

按 `prompts/翻译计划模板.md`「执行步骤」9 步推进（读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志）。

## 篇目清单

| # | 篇名 | 源文 | 大小 | 状态 |
|---|------|------|------|------|
| 1 | 献词 | 01-dedication.md | 0.0KB | todo |
| 2 | 一场不愉快的晚宴 | 02-an-unpleasant-dinner-party.md | 32.4KB | todo |
| 3 | 18号病房 | 03-in-room-18.md | 31.2KB | todo |
| 4 | 莱瑟尼医生没有回来 | 04-dr-letheny-does-not-return.md | 32.0KB | todo |
| 5 | 黄色油布雨衣及其他难题 | 05-a-yellow-slicker-and-other-problems.md | 30.4KB | todo |
| 6 | 青金石袖扣 | 06-a-lapis-cuff-link.md | 27.3KB | todo |
| 7 | 我有个发现，却后悔了 | 07-i-make-a-discovery-and-regret-it.md | 23.8KB | todo |
| 8 | 消失的钥匙与一场验尸审讯 | 08-the-disappearing-key-and-part-of-an-inquest.md | 26.8KB | todo |
| 9 | 金色亮片 | 09-a-gold-sequin.md | 20.3KB | todo |
| 10 | 小檗丛下 | 10-under-the-barberry-bush.md | 15.9KB | todo |
| 11 | 午夜访客 | 11-a-midnight-visitor.md | 20.6KB | todo |
| 12 | 借着火柴的光 | 12-by-the-light-of-a-match.md | 21.5KB | todo |
| 13 | 又是18号病房 | 13-room-18-again.md | 26.7KB | todo |
| 14 | 镭出现了 | 14-the-radium-appears.md | 23.7KB | todo |
| 15 | 证据问题 | 15-a-matter-of-evidence.md | 31.1KB | todo |
| 16 | 科罗尔吐露真情 | 16-corole-is-moved-to-candour.md | 25.1KB | todo |
| 17 | 门上方的红灯 | 17-the-red-light-above-the-door.md | 16.1KB | todo |
| 18 | 奥利里讲了一个故事 | 18-o-leary-tells-a-story.md | 27.0KB | todo |
| 19 | 奥利里修改了他的故事 | 19-o-leary-revises-his-story.md | 15.1KB | todo |

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-08-17 | - | 建项目 | 从 待翻译/mignon-g-eberhart_the-patient-in-room-18.epub 提取正文（18 章＋献词，共 19 文件，已加数字前缀保阅读顺序）、建术语表初版、生成队列 |
