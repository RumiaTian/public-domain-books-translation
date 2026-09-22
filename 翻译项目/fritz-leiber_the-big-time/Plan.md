# 翻译计划（大时光）

## 本计划信息

- **项目名称**：fritz-leiber_the-big-time
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

## translation_queue.csv 格式

```
file,size_kb,status
01-enter-three-hussars.md,22.2,todo
02-a-right-hand-glove.md,19.5,todo
...
```

| 字段 | 含义 | 取值 |
|------|------|------|
| `file` | 源文文件名（在 `原文/` 目录下） | 如 `01-enter-three-hussars.md` |
| `size_kb` | 源文大小（KB）。>50KB 为长文，按通用翻译引擎第七节分段 | 数字 |
| `status` | 翻译状态 | `todo` 待译 / `doing` 翻译中 / `done` 已完成 |

## 执行步骤

按 `prompts/翻译计划模板.md`「执行步骤」9 步推进（读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志）。本项目为长篇/委派模式，由子代理逐章执行。

## 篇目清单

| # | 章名 | 源文 | 状态 |
|---|------|------|------|
| 1 | I Enter Three Hussars | 01-enter-three-hussars.md | todo |
| 2 | II A Right-Hand Glove | 02-a-right-hand-glove.md | todo |
| 3 | III Nine for a Party | 03-nine-for-a-party.md | todo |
| 4 | IV SOS from Nowhere | 04-sos-from-nowhere.md | todo |
| 5 | V Sid Insists on Ghostgirls | 05-sid-insists-on-ghostgirls.md | todo |
| 6 | VI Crete Circa 1300 BC | 06-crete-circa-1300-bc.md | todo |
| 7 | VII Time to Think | 07-time-to-think.md | todo |
| 8 | VIII A Place to Stand | 08-a-place-to-stand.md | todo |
| 9 | IX A Locked Room | 09-a-locked-room.md | todo |
| 10 | X Motives and Opportunities | 10-motives-and-opportunities.md | todo |
| 11 | XI The Western Front, 1917 | 11-the-western-front-1917.md | todo |
| 12 | XII A Big Opportunity | 12-a-big-opportunity.md | todo |
| 13 | XIII The Tiger Is Loose | 13-the-tiger-is-loose.md | todo |
| 14 | XIV "Now Will You Talk?" | 14-now-will-you-talk.md | todo |
| 15 | XV Lord Spider | 15-lord-spider.md | todo |
| 16 | XVI The Possibility-Binders | 16-the-possibility-binders.md | todo |

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
| 2026-08-17 | 全 16 章（215.8KB） | 完成 16/16，check 全 0；术语表 +40 条；章首引诗均注明出处 | ✅ |
