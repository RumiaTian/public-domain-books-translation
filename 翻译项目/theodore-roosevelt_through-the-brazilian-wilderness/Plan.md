# 翻译计划（穿越巴西莽荒）

## 本计划信息

- **项目名称**：穿越巴西莽荒（Through the Brazilian Wilderness，西奥多·罗斯福）
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/学术著作.md
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

> 原文已按章序加数字前缀（01—17）。共 17 篇，详见 `translation_queue.csv`。

| # | 篇名（章序） | 源文 | 状态 |
|---|------|------|------|
| 1 | 献词 | 01-dedication.md | todo |
| 2 | 前言 | 02-preface.md | todo |
| 3 | 插图目录 | 03-list-of-illustrations.md | todo |
| 4 | 第一章 启程 | 04-the-start.md | todo |
| 5 | 第二章 溯巴拉圭河 | 05-up-the-paraguay.md | todo |
| 6 | 第三章 塔夸里河猎美洲豹 | 06-a-jaguar-hunt-on-the-taquary.md | todo |
| 7 | 第四章 巴拉圭河源头 | 07-the-headwaters-of-the-paraguay.md | todo |
| 8 | 第五章 溯貘之河 | 08-up-the-river-of-tapirs.md | todo |
| 9 | 第六章 穿越巴西西部高原莽荒 | 09-through-the-highland-wilderness-of-western-brazil.md | todo |
| 10 | 第七章 骡队穿越南比夸拉人之乡 | 10-with-a-mule-train-across-nhambiquara-land.md | todo |
| 11 | 第八章 疑惑之河 | 11-the-river-of-doubt.md | todo |
| 12 | 第九章 沿未知之河入赤道森林 | 12-down-an-unknown-river-into-the-equatorial-forest.md | todo |
| 13 | 第十章 抵亚马逊与归程；考察的动物学与地理学成果 | 13-to-the-amazon-and-home-zoological-and-geographical-results-of-the-expedition.md | todo |
| 14 | 附录A 南美野外动物学家与野外地理学家的工作 | 14-the-work-of-the-field-zoologist-and-field-geographer-in-south-america.md | todo |
| 15 | 附录B 南美莽荒旅行装备 | 15-the-outfit-for-travelling-in-the-south-american-wilderness.md | todo |
| 16 | 附录C 致劳罗·米勒将军的五月一日信 | 16-my-letter-of-may-1-to-general-lauro-m-ller.md | todo |
| 17 | 尾注 | 17-endnotes.md | todo |

## 执行步骤

按 `prompts/翻译计划模板.md`「执行步骤」9 步推进（读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志）。

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
