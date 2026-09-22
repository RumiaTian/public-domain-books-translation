# 翻译计划（我的光辉生涯）

## 本计划信息

- **项目名称**：我的光辉生涯（My Brilliant Career，迈尔斯·富兰克林）
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

按 `prompts/翻译计划模板.md`「执行步骤」9 步推进（读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志）。本项目为「长篇／委派模式」，由子代理逐篇译，主 agent 统管术语与风格连贯。

## 篇目清单

> 全书 38 章（罗马数字 I–XXXVIII），另含亨利·劳森《前言》、作者《引言》及书末《注释》，共 41 个文件。各篇文件名原为纯文字无编号（部分含嵌入式日期会干扰自然排序），已加 `01-`–`41-` 阿拉伯数字前缀，严格对应阅读顺序。合计约 474.7KB。

| # | 篇名 | 源文 | 大小 | 状态 |
|---|------|------|------|------|
| 1 | 前言（亨利·劳森） | 01-preface.md | 1.5KB | todo |
| 2 | 引言 | 02-introduction.md | 2.4KB | todo |
| 3 | 一　我记得，我记得 | 03-i-remember-i-remember.md | 7.1KB | todo |
| 4 | 二　袋熊谷初识 | 04-an-introduction-to-possum-gully.md | 5.3KB | todo |
| 5 | 三　死气沉沉的生活 | 05-a-lifeless-life.md | 8.6KB | todo |
| 6 | 四　一场很快栽了的事业 | 06-a-career-which-soon-careered-to-an-end.md | 8.2KB | todo |
| 7 | 五　零散速写与牢骚 | 07-disjointed-sketches-and-grumbles.md | 15.3KB | todo |
| 8 | 六　反叛 | 08-revolt.md | 13.6KB | todo |
| 9 | 七　哪有玫瑰不长刺 | 09-was-e-er-a-rose-without-its-thorn.md | 18.8KB | todo |
| 10 | 八　告别袋熊谷，好哇！好哇！ | 10-possum-gully-left-behind-hurrah-hurrah.md | 19.0KB | todo |
| 11 | 九　海伦姨妈的妙方 | 11-aunt-helen-s-recipe.md | 14.2KB | todo |
| 12 | 十　埃弗拉德·格雷 | 12-everard-grey.md | 17.2KB | todo |
| 13 | 十一　呸 | 13-yah.md | 15.3KB | todo |
| 14 | 十二　一段刻骨铭心的情 | 14-one-grand-passion.md | 11.4KB | todo |
| 15 | 十三　他 | 15-he.md | 16.3KB | todo |
| 16 | 十四　多是书信 | 16-principally-letters.md | 12.2KB | todo |
| 17 | 十五　心怀年少时 | 17-when-the-heart-is-young.md | 9.0KB | todo |
| 18 | 十六　时来运转 | 18-when-fortune-smiles.md | 14.5KB | todo |
| 19 | 十七　青春牧歌 | 19-idylls-of-youth.md | 20.2KB | todo |
| 20 | 十八　但愿我被迫听过的布道大都这般短 | 20-as-short-as-i-wish-had-been-the-majority-of-sermons-to-which-i-have-been-forced-to-give-ear.md | 4.6KB | todo |
| 21 | 十九　1896 年 11 月 9 日 | 21-the-9th-of-november-1896.md | 15.1KB | todo |
| 22 | 二十　故事续篇 | 22-same-yarn-continued.md | 16.2KB | todo |
| 23 | 二十一　我又不淑女了 | 23-my-unladylike-behaviour-again.md | 8.9KB | todo |
| 24 | 二十二　芳龄十七 | 24-sweet-seventeen.md | 16.9KB | todo |
| 25 | 二十三　“啊，哪怕一小时的烈火之爱，也胜过一世纪的冷清敬意！” | 25-ah-for-one-hour-of-burning-love-tis-worth-an-age-of-cold-respect.md | 15.0KB | todo |
| 26 | 二十四　祸福旦夕难料 | 26-thou-knowest-not-what-a-day-may-bring-forth.md | 8.0KB | todo |
| 27 | 二十五　缘何？ | 27-because.md | 8.9KB | todo |
| 28 | 二十六　莫向明日夸海口 | 28-boast-not-thyself-of-tomorrow.md | 16.2KB | todo |
| 29 | 二十七　我的旅程 | 29-my-journey.md | 5.4KB | todo |
| 30 | 二十八　活下去 | 30-to-life.md | 14.4KB | todo |
| 31 | 二十九　活下去（续） | 31-to-life-continued.md | 23.4KB | todo |
| 32 | 三十　无知是福，聪明反被聪明误 | 32-where-ignorance-is-bliss-tis-folly-to-be-wise.md | 9.8KB | todo |
| 33 | 三十一　麦斯沃特先生和我大吵一场 | 33-mr-m-swat-and-i-have-a-bust-up.md | 14.6KB | todo |
| 34 | 三十二　别了，巴尼山口 | 34-ta-ta-to-barney-s-gap.md | 5.8KB | todo |
| 35 | 三十三　重返袋熊谷 | 35-back-at-possum-gully.md | 8.7KB | todo |
| 36 | 三十四　然而故人易忘 | 36-but-absent-friends-are-soon-forgot.md | 12.0KB | todo |
| 37 | 三十五　1898 年 12 月 3 日 | 37-the-3rd-of-december-1898.md | 9.4KB | todo |
| 38 | 三十六　从前，日子漫长而炎热 | 38-once-upon-a-time-when-the-days-were-long-and-hot.md | 19.6KB | todo |
| 39 | 三十七　轻视小事者必渐倾覆 | 39-he-that-despiseth-little-things-shall-fall-little-by-little.md | 7.3KB | todo |
| 40 | 三十八　一个讲完的故事，一个了结的日子 | 40-a-tale-that-is-told-and-a-day-that-is-done.md | 4.4KB | todo |
| 41 | 注释 | 41-endnotes.md | 0.1KB | todo |

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
