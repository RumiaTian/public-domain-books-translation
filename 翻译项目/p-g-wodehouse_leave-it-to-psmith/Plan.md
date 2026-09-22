# Plan（《交给皮史密斯吧》翻译计划）

> 从 `prompts/翻译计划模板.md` 复制建立。执行步骤、CSV 格式等通用规范见模板，此处为本书实例。

---

## 本计划信息

- **项目名称**：p-g-wodehouse_leave-it-to-psmith（《交给皮史密斯吧》，P. G. 伍德豪斯）
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
| `原文/*.md` | 源文 | 不改 |
| `译文/*.zh-CN.md` | 译文产出（块对照双语） | 翻译 agent 产出 |

---

## 篇目清单

| # | 篇名 | 源文 | 大小 | 状态 |
|---|------|------|------|------|
| 1 | 布兰丁斯城堡密谋 | 01-dark-plottings-at-blandings-castle.md | 47.2KB | todo |
| 2 | 皮史密斯登场 | 02-enter-psmith.md | 32.0KB | todo |
| 3 | 伊芙借伞 | 03-eve-borrows-an-umbrella.md | 10.3KB | todo |
| 4 | 蜂子俱乐部的难堪一幕 | 04-painful-scene-at-the-drones-club.md | 6.1KB | todo |
| 5 | 皮史密斯求职 | 05-psmith-applies-for-employment.md | 14.0KB | todo |
| 6 | 埃姆斯沃思勋爵会见诗人 | 06-lord-emsworth-meets-a-poet.md | 51.3KB | todo |
| 7 | 巴克斯特起疑 | 07-baxter-suspects.md | 35.9KB | todo |
| 8 | 湖上谈心 | 08-confidences-on-the-lake.md | 50.5KB | todo |
| 9 | 皮史密斯雇男仆 | 09-psmith-engages-a-valet.md | 61.1KB | todo |
| 10 | 诗歌朗诵会上的轰动事件 | 10-sensational-occurrence-at-a-poetry-reading.md | 53.6KB | todo |
| 11 | 几乎全与花盆有关 | 11-almost-entirely-about-flowerpots.md | 48.7KB | todo |
| 12 | 花盆话题再谈 | 12-more-on-the-flowerpot-theme.md | 19.0KB | todo |
| 13 | 皮史密斯会客 | 13-psmith-receives-guests.md | 48.3KB | todo |
| 14 | 皮史密斯就任新职 | 14-psmith-accepts-employment.md | 22.4KB | todo |

> 共 14 章，约 500KB。各章 >50KB 者（06/08/09/10）按通用翻译引擎第七节分段处理。

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
