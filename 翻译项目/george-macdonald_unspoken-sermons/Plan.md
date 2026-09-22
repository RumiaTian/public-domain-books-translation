# 翻译计划（《无声的布道》——乔治·麦克唐纳）

## 本计划信息

- **项目名称**：《无声的布道》（George MacDonald, *Unspoken Sermons*, Series I–III, 1867/1885/1889）
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

按 `prompts/翻译计划模板.md`「执行步骤」9 步推进（读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志）。本内容形态为「短篇集」，走委派模式，每篇下沉到一次性子代理执行。

## 篇目清单

共 44 文件（36 篇布道 + 题词 + 三辑扉页/献词 + 尾注），文件名已加全局序号前缀 01–44。详见 `translation_queue.csv`。

### 第一辑（Series I, 1867）

| # | 篇名 | 源文 | 大小 | 状态 |
|---|------|------|------|------|
| 04 | The Child in the Midst | 04-chapter-1-1.md | 25.9KB | todo |
| 05 | The Consuming Fire | 05-chapter-1-2.md | 22.8KB | todo |
| 06 | The Higher Faith | 06-chapter-1-3.md | 15.7KB | todo |
| 07 | It Shall Not Be Forgiven | 07-chapter-1-4.md | 32.7KB | todo |
| 08 | The New Name | 08-chapter-1-5.md | 17.4KB | todo |
| 09 | The Heart with the Treasure | 09-chapter-1-6.md | 6.7KB | todo |
| 10 | The Temptation in the Wilderness | 10-chapter-1-7.md | 36.5KB | todo |
| 11 | The Eloi | 11-chapter-1-8.md | 16.7KB | todo |
| 12 | The Hands of the Father | 12-chapter-1-9.md | 8.7KB | todo |
| 13 | Love Thy Neighbour | 13-chapter-1-10.md | 27.7KB | todo |
| 14 | Love Thine Enemy | 14-chapter-1-11.md | 14.2KB | todo |
| 15 | The God of the Living | 15-chapter-1-12.md | 12.9KB | todo |

### 第二辑（Series II, 1885）

| # | 篇名 | 源文 | 大小 | 状态 |
|---|------|------|------|------|
| 18 | The Way | 18-chapter-2-1.md | 28.2KB | todo |
| 19 | The Hardness of the Way | 19-chapter-2-2.md | 24.8KB | todo |
| 20 | The Cause of Spiritual Stupidity | 20-chapter-2-3.md | 24.3KB | todo |
| 21 | The Word of Jesus on Prayer | 21-chapter-2-4.md | 26.4KB | todo |
| 22 | Man's Difficulty Concerning Prayer | 22-chapter-2-5.md | 28.1KB | todo |
| 23 | The Last Farthing | 23-chapter-2-6.md | 23.7KB | todo |
| 24 | Abba, Father! | 24-chapter-2-7.md | 31.4KB | todo |
| 25 | Life | 25-chapter-2-8.md | 26.9KB | todo |
| 26 | The Fear of God | 26-chapter-2-9.md | 20.2KB | todo |
| 27 | The Voice of Job | 27-chapter-2-10.md | 53.0KB | todo |
| 28 | Self-Denial | 28-chapter-2-11.md | 32.6KB | todo |
| 29 | The Truth in Jesus | 29-chapter-2-12.md | 44.1KB | todo |

### 第三辑（Series III, 1889）

| # | 篇名 | 源文 | 大小 | 状态 |
|---|------|------|------|------|
| 32 | The Creation in Christ | 32-chapter-3-1.md | 28.4KB | todo |
| 33 | The Knowing of the Son | 33-chapter-3-2.md | 19.8KB | todo |
| 34 | The Mirrors of the Lord | 34-chapter-3-3.md | 16.0KB | todo |
| 35 | The Truth | 35-chapter-3-4.md | 31.9KB | todo |
| 36 | Freedom | 36-chapter-3-5.md | 17.4KB | todo |
| 37 | Kingship | 37-chapter-3-6.md | 12.1KB | todo |
| 38 | Justice | 38-chapter-3-7.md | 62.6KB | todo |
| 39 | Light | 39-chapter-3-8.md | 22.4KB | todo |
| 40 | The Displeasure of Jesus | 40-chapter-3-9.md | 30.9KB | todo |
| 41 | Righteousness | 41-chapter-3-10.md | 23.5KB | todo |
| 42 | The Final Unmasking | 42-chapter-3-11.md | 20.7KB | todo |
| 43 | The Inheritance | 43-chapter-3-12.md | 18.4KB | todo |

### 前后附属文件

| # | 内容 | 源文 | 大小 | 状态 |
|---|------|------|------|------|
| 01 | 卷首题词（Ἔπεα Ἄπτερα 等） | 01-epigraph.md | 0.1KB | todo |
| 02 | 第一辑扉页 | 02-first-series.md | 0.0KB | todo |
| 03 | 第一辑献词（致妻子与友人） | 03-dedication-1.md | 0.1KB | todo |
| 16 | 第二辑扉页 | 16-second-series.md | 0.0KB | todo |
| 17 | 第二辑献词 | 17-dedication-2.md | 0.1KB | todo |
| 30 | 第三辑扉页 | 30-third-series.md | 0.0KB | todo |
| 31 | 第三辑献词（附短诗） | 31-dedication-3.md | 0.2KB | todo |
| 44 | 卷末尾注（Endnotes 6 条） | 44-endnotes.md | 2.2KB | todo |

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
