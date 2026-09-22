# 翻译计划（Plan.md）— compton-mackenzie_sinister-street

---

## 本计划信息

- **项目名称**：compton-mackenzie_sinister-street（邪恶街 / Sinister Street）
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

## translation_queue.csv 格式

```
file,size_kb,status
01-to-the-reverend-e-d-stone.md,2.3,todo
02-epigraph.md,0.3,todo
...
```

| 字段 | 含义 | 取值 |
|------|------|------|
| `file` | 源文文件名（在 `原文/` 目录下） | 如 `04-the-new-world.md` |
| `size_kb` | 源文大小（KB）。>50KB 为长文，按通用翻译引擎第七节分段 | 数字 |
| `status` | 翻译状态 | `todo` 待译 / `doing` 翻译中 / `done` 已完成 |

---

## 执行步骤（agent 按此推进，两种模式共用）

> **谁执行**由 `项目说明.md` 的「内容形态」决定：本项目为**长篇 → 委派模式**，由子代理逐篇执行本流程。9 步不变：

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
产出到 `译文/对应文件名去.md加.zh-CN.md`。双语对照格式、标记规则、完整性禁令见 `prompts/通用翻译引擎.md` 第五、六节。本流程专有提醒：
- 逐块对照原文，绝不漏译、不合并段落、不缩写、不总结，尤其结尾别截断。
- 严守术语表：遇表内源词必译为指定译法。新词自行确定统一译法，首次附原文「中文（English）」。
- 人物/语气/风格全文一致（本书为成长小说，人物跨卷延续，尤其 Michael/Stella/母亲/Lily/Alan），照黄金样本风格译。
- 长文（源文 >50KB，如 56/58/61 章）分段处理见通用翻译引擎第七节。

### 5. 自检
- 完整性：源文每一段都在译文 Original 块中出现，末尾无截断。
- 块对称：Original/Chinese 数量相等，每块内段数对应。
- 标题格式：全部「英文 / 中文」合并（含罗马数字章号）。
- 术语一致：抽查 5 个术语词，全文译法统一。
- 不满足则改到满足。

### 6. 自动检查
```
python scripts/check_bilingual.py 译文/对应篇名.zh-CN.md
```

### 7. 回填状态（双写）
`doing` → `done`，改两处：① 项目 `translation_queue.csv`；② 根 `translation_queue.csv` 中 `<本项目名>,<本篇名>` 行。

### 8. 追加日志
在本文件「运行日志」追加一行。

### 9. 循环
回到步骤 2，直到全部 `done`。委派模式下由主 agent 决定是否继续派单。

---

## 篇目清单（共 63 篇，约 1966KB；顺序=阅读顺序）

| # | 篇名 | 源文 | 大小 | 状态 |
|---|------|------|------|------|
| 1 | To the Reverend E. D. Stone（献词信） | 01-to-the-reverend-e-d-stone.md | 2.3KB | todo |
| 2 | Epigraph（卷首题词） | 02-epigraph.md | 0.3KB | todo |
| 3 | The Prison House（Book I 题页） | 03-the-prison-house.md | 0.3KB | todo |
| 4 | The New World | 04-the-new-world.md | 32.7KB | todo |
| 5 | Bittersweet | 05-bittersweet.md | 33.0KB | todo |
| 6 | Fears And Fantasies | 06-fears-and-fantasies.md | 12.4KB | todo |
| 7 | Unending Childhood | 07-unending-childhood.md | 42.6KB | todo |
| 8 | The First Fairy Princess | 08-the-first-fairy-princess.md | 25.1KB | todo |
| 9 | The Enchanted Palace | 09-the-enchanted-palace.md | 19.5KB | todo |
| 10 | Randell House | 10-randell-house.md | 27.9KB | todo |
| 11 | Siamese Stamps | 11-siamese-stamps.md | 26.9KB | todo |
| 12 | Holidays in France | 12-holidays-in-france.md | 21.5KB | todo |
| 13 | Classic Education（Book II 题页） | 13-classic-education.md | 0.4KB | todo |
| 14 | The Jacobean | 14-the-jacobean.md | 32.1KB | todo |
| 15 | The Quadruple Intrigue | 15-the-quadruple-intrigue.md | 30.3KB | todo |
| 16 | Pastoral | 16-pastoral.md | 21.9KB | todo |
| 17 | Boyhood's Glory | 17-boyhood-s-glory.md | 37.1KB | todo |
| 18 | Incense | 18-incense.md | 42.8KB | todo |
| 19 | Pax | 19-pax.md | 27.4KB | todo |
| 20 | Cloven Hoofmarks | 20-cloven-hoofmarks.md | 24.0KB | todo |
| 21 | Mirrors | 21-mirrors.md | 30.6KB | todo |
| 22 | The Yellow Age | 22-the-yellow-age.md | 47.5KB | todo |
| 23 | Stella | 23-stella.md | 21.6KB | todo |
| 24 | Action And Reaction | 24-action-and-reaction.md | 42.3KB | todo |
| 25 | Alan | 25-alan.md | 14.4KB | todo |
| 26 | Sentiment | 26-sentiment.md | 39.5KB | todo |
| 27 | Arabesque | 27-arabesque.md | 32.0KB | todo |
| 28 | Grey Eyes | 28-grey-eyes.md | 33.2KB | todo |
| 29 | Blue Eyes | 29-blue-eyes.md | 18.1KB | todo |
| 30 | Lily | 30-lily.md | 32.9KB | todo |
| 31 | Eighteen Years Old | 31-eighteen-years-old.md | 38.5KB | todo |
| 32 | Parents | 32-parents.md | 16.1KB | todo |
| 33 | Music | 33-music.md | 31.2KB | todo |
| 34 | Dreaming Spires（Book III 题页） | 34-dreaming-spires.md | 0.4KB | todo |
| 35 | The First Day | 35-the-first-day.md | 49.4KB | todo |
| 36 | The First Week | 36-the-first-week.md | 24.9KB | todo |
| 37 | The First Term | 37-the-first-term.md | 26.1KB | todo |
| 38 | Cheyne Walk | 38-cheyne-walk.md | 35.4KB | todo |
| 39 | Youth'S Domination | 39-youth-s-domination.md | 45.1KB | todo |
| 40 | Gray And Blue | 40-gray-and-blue.md | 56.6KB | todo |
| 41 | Venner's | 41-venner-s.md | 37.1KB | todo |
| 42 | The Oxford Looking Glass | 42-the-oxford-looking-glass.md | 30.2KB | todo |
| 43 | The Lesson Of Spain | 43-the-lesson-of-spain.md | 45.1KB | todo |
| 44 | Stella In Oxford | 44-stella-in-oxford.md | 26.7KB | todo |
| 45 | Sympathy | 45-sympathy.md | 34.7KB | todo |
| 46 | 202 High（牛津寓所） | 46-202-high.md | 42.0KB | todo |
| 47 | Plashers Mead | 47-plashers-mead.md | 31.6KB | todo |
| 48 | 99 St. Giles（牛津寓所） | 48-99-st-giles.md | 34.0KB | todo |
| 49 | The Last Term | 49-the-last-term.md | 18.1KB | todo |
| 50 | The Last Week | 50-the-last-week.md | 23.0KB | todo |
| 51 | The Last Day | 51-the-last-day.md | 21.9KB | todo |
| 52 | Romantic Education（Book IV 题页） | 52-romantic-education.md | 0.3KB | todo |
| 53 | Ostia Ditis | 53-ostia-ditis.md | 37.8KB | todo |
| 54 | Neptune Crescent | 54-neptune-crescent.md | 53.5KB | todo |
| 55 | The Café d'Orange | 55-the-caf-d-orange.md | 43.3KB | todo |
| 56 | Leppard Street | 56-leppard-street.md | 93.9KB | todo |
| 57 | The Innermost Circle | 57-the-innermost-circle.md | 26.0KB | todo |
| 58 | Tinderbox Lane | 58-tinderbox-lane.md | 95.6KB | todo |
| 59 | The Gate Of Ivory | 59-the-gate-of-ivory.md | 51.4KB | todo |
| 60 | Seeds Of Pomegranate | 60-seeds-of-pomegranate.md | 29.7KB | todo |
| 61 | The Gate Of Horn | 61-the-gate-of-horn.md | 84.0KB | todo |
| 62 | The Old World | 62-the-old-world.md | 3.9KB | todo |
| 63 | Epilogical Letter to John Nicolas Mavrogordato（跋信） | 63-epilogical-letter-to-john-nicolas-mavrogordato.md | 6.4KB | todo |

> Book I The Prison House（03 题页起）→ Book II Classic Education（13 题页起）→ Book III Dreaming Spires（34 题页起）→ Book IV Romantic Education（52 题页起）。四个题页（03/13/34/52）仅含卷题+题词，快速翻过。

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
