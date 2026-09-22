# Plan.md — etsu-inagaki-sugimoto_a-daughter-of-the-samurai

## 本计划信息

- **项目名称**：etsu-inagaki-sugimoto_a-daughter-of-the-samurai（《武士之女》A Daughter of the Samurai）
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
| `原文/*.md` | 源文（3 前置篇＋32 章，共 35 篇） | 不改 |
| `译文/*.zh-CN.md` | 译文产出（块对照双语） | 翻译 agent 产出 |

---

## translation_queue.csv 格式

```
file,size_kb,status
01-dedication.md,0.2,todo
02-acknowledgment-to-nancy-virginia-austen.md,0.3,todo
...
```

| 字段 | 含义 | 取值 |
|------|------|------|
| `file` | 源文文件名（在 `原文/` 目录下） | 如 `04-winters-in-echigo.md` |
| `size_kb` | 源文大小（KB）。>50KB 为长文，按通用翻译引擎第七节分段 | 数字 |
| `status` | 翻译状态 | `todo` 待译 / `doing` 翻译中 / `done` 已完成 |

---

## 执行步骤（agent 按此推进，两种模式共用）

> **谁执行**由 `项目说明.md` 的「内容形态」字段决定（见 `WORKFLOW.md`「判断内容形态」）：本项目为长篇，走**委派模式**，由子代理逐篇执行本流程。

### 1. 读配置（每次翻译前必读）
```
1. 本项目 Plan.md（本文件）
2. 项目说明.md
3. 术语表.md
4. prompts/通用翻译引擎.md
5. prompts/领域配置/小说文学.md
6. 译文/ 下任意一篇已完成的 .zh-CN.md（作为风格黄金样本，照此风格译；无则跳过）
```

### 2. 取任务
读 `translation_queue.csv`，取第一个 `status=todo` 的行。先 `ls 译文/` 检查该篇译文是否已存在：
- 已存在 → 直接改 `done`，跳到步骤 8。
- 不存在 → 把该行 `status` 改为 `doing` 并保存 CSV，继续。

### 3. 读源文
读 `原文/对应文件名`。

### 4. 翻译
产出到 `译文/对应文件名去.md加.zh-CN.md`。

**双语对照格式、标记规则、完整性禁令**：见 `prompts/通用翻译引擎.md` 第五、六节（标记成对、标题合并「英文 / 中文」、不跳过不缩写、UTF-8 无 BOM）。此处不重复。

**本流程专有提醒**：
- 逐块对照原文，绝不漏译、不合并段落、不缩写、不总结，尤其结尾别截断。
- 严守术语表：遇表内源词必译为指定译法。日语罗马字新词自行确定统一译法，首次附原文「中文（English/罗马字）」。
- 人物/语气/风格全文一致（文学类尤其重要），照黄金样本风格译。
- 长文（源文 >50KB）分段处理见通用翻译引擎第七节。

### 5. 自检
- 完整性：源文每一段都在译文 Original 块中出现，末尾无截断。
- 块对称：Original/Chinese 数量相等，每块内段数对应。
- 标题格式：全部「英文 / 中文」合并。
- 术语一致：抽查 5 个术语词，全文译法统一。
- 不满足则改到满足。

### 6. 自动检查
```
python scripts/check_bilingual.py 译文/对应篇名.zh-CN.md
```
结构契约满足（标记成对、标题合并格式、可疑错配少）则继续；有违规回步骤 4 修订。

### 7. 回填状态（双写）
检查通过后，`status` 从 `doing` 改 `done`，改两处：
- ① 项目 `translation_queue.csv` 该行；
- ② 根 `translation_queue.csv` 中 `<本项目名>,<本篇名>` 那一行（`WORKFLOW.md`「双写状态」）。

### 8. 追加日志
在本文件「运行日志」追加一行。

### 9. 循环
回到步骤 2，取下一篇 `todo`，直到全部 `done`。委派模式下由主 agent 决定是否继续派单（见 `WORKFLOW.md`「委派模式调度循环」）。

---

## 篇目清单

| # | 篇名 | 源文 | 大小 | 状态 |
|---|------|------|------|------|
| 1 | 题献 | 01-dedication.md | 0.2KB | todo |
| 2 | 致谢 | 02-acknowledgment-to-nancy-virginia-austen.md | 0.3KB | todo |
| 3 | 序言（Christopher Morley） | 03-introduction.md | 4.4KB | todo |
| 4 | 第一章 越后的冬天（I Winters in Echigo） | 04-winters-in-echigo.md | 16.6KB | todo |
| 5 | 第二章 卷发（II Curly Hair） | 05-curly-hair.md | 10.5KB | todo |
| 6 | 第三章 寒中时节（III Days of Kan） | 06-days-of-kan.md | 13.7KB | todo |
| 7 | 第四章 新与旧（IV The Old and the New） | 07-the-old-and-the-new.md | 14.3KB | todo |
| 8 | 第五章 落叶（V Falling Leaves） | 08-falling-leaves.md | 16.0KB | todo |
| 9 | 第六章 晴朗的新年（VI A Sunny New Year） | 09-a-sunny-new-year.md | 15.6KB | todo |
| 10 | 第七章 未成的婚礼（VII The Wedding That Never Was） | 10-the-wedding-that-never-was.md | 13.8KB | todo |
| 11 | 第八章 两次冒险（VIII Two Ventures） | 11-two-ventures.md | 19.7KB | todo |
| 12 | 第九章 提线木偶的故事（IX The Story of a Marionette） | 12-the-story-of-a-marionette.md | 24.3KB | todo |
| 13 | 第十章 鸟之日（X The Day of the Bird） | 13-the-day-of-the-bird.md | 18.8KB | todo |
| 14 | 第十一章 我的第一次旅行（XI My First Journey） | 14-my-first-journey.md | 14.7KB | todo |
| 15 | 第十二章 旅行与教育（XII Travel Education） | 15-travel-education.md | 18.7KB | todo |
| 16 | 第十三章 外国人（XIII Foreigners） | 16-foreigners.md | 15.8KB | todo |
| 17 | 第十四章 课业（XIV Lessons） | 17-lessons.md | 17.5KB | todo |
| 18 | 第十五章 我如何成为基督徒（XV How I Became a Christian） | 18-how-i-became-a-christian.md | 18.3KB | todo |
| 19 | 第十六章 航向未知之海（XVI Sailing Unknown Seas） | 19-sailing-unknown-seas.md | 22.0KB | todo |
| 20 | 第十七章 第一印象（XVII First Impressions） | 20-first-impressions.md | 25.7KB | todo |
| 21 | 第十八章 奇异的风俗（XVIII Strange Customs） | 21-strange-customs.md | 22.0KB | todo |
| 22 | 第十九章 思考（XIX Thinking） | 22-thinking.md | 15.4KB | todo |
| 23 | 第二十章 邻居（XX Neighbours） | 23-neighbours.md | 16.9KB | todo |
| 24 | 第二十一章 新的经历（XXI New Experiences） | 24-new-experiences.md | 25.5KB | todo |
| 25 | 第二十二章 异乡之花（XXII Flower in a Strange Land） | 25-flower-in-a-strange-land.md | 15.2KB | todo |
| 26 | 第二十三章 千代（XXIII Chiyo） | 26-chiyo.md | 20.2KB | todo |
| 27 | 第二十四章 重回日本（XXIV In Japan Again） | 27-in-japan-again.md | 6.4KB | todo |
| 28 | 第二十五章 我们在东京的家（XXV Our Tokyo Home） | 28-our-tokyo-home.md | 14.4KB | todo |
| 29 | 第二十六章 悲剧琐记（XXVI Tragic Trifles） | 29-tragic-trifles.md | 13.3KB | todo |
| 30 | 第二十七章 祖母大人（XXVII Honourable Grandmother） | 30-honourable-grandmother.md | 18.0KB | todo |
| 31 | 第二十八章 姐姐来访（XXVIII Sister's Visit） | 31-sister-s-visit.md | 12.2KB | todo |
| 32 | 第二十九章 旧日本的一位贵妇（XXIX A Lady of Old Japan） | 32-a-lady-of-old-japan.md | 15.5KB | todo |
| 33 | 第三十章 白牛（XXX The White Cow） | 33-the-white-cow.md | 20.2KB | todo |
| 34 | 第三十一章 无用的珍宝（XXXI Worthless Treasures） | 34-worthless-treasures.md | 17.7KB | todo |
| 35 | 第三十二章 黑船（XXXII The Black Ships） | 35-the-black-ships.md | 5.3KB | todo |

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
