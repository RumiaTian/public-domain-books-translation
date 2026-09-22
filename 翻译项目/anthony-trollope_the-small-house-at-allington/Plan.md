# 翻译计划（Plan.md）

---

## 本计划信息

- **项目名称**：anthony-trollope_the-small-house-at-allington（《奥灵顿的小宅》，安东尼·特罗洛普，1864，巴塞特郡纪事第五部）
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/小说文学.md
- **术语表**：术语表.md
- **内容形态**：长篇（60 章）→ **执行模式**：委派（子代理逐章执行下方 9 步）

---

## 文件分工

| 文件 | 作用 | 谁来改 |
|------|------|--------|
| `项目说明.md` | 项目基本信息、领域配置、篇目清单 | 人工 |
| `术语表.md` | 翻译硬约束层。每篇译完补充新词 | agent / 人工 |
| `translation_queue.csv` | 任务队列。每行一文件，`file, size_kb, status` 三列 | 翻译前改 doing，完成后改 done |
| `Plan.md`（本文件） | 执行步骤 + 运行日志 | agent 追加日志 |
| `原文/*.md` | 源文（60 章，01-… 至 60-…，数字前缀即阅读顺序） | 不改 |
| `译文/*.zh-CN.md` | 译文产出（块对照双语） | 翻译 agent 产出 |

---

## translation_queue.csv 格式

```
file,size_kb,status
01-the-squire-of-allington.md,18.9,todo
02-the-two-pearls-of-allington.md,25.7,todo
...
```

| 字段 | 含义 | 取值 |
|------|------|------|
| `file` | 源文文件名（在 `原文/` 目录下） | 如 `01-the-squire-of-allington.md` |
| `size_kb` | 源文大小（KB）。>50KB 为长文，按通用翻译引擎第七节分段 | 数字 |
| `status` | 翻译状态 | `todo` 待译 / `doing` 翻译中 / `done` 已完成 |

---

## 执行步骤（agent 按此推进，两种模式共用）

> **谁执行**由 `项目说明.md` 的「内容形态」字段决定：本项目为长篇 → 委派模式，子代理逐章执行本流程。无论谁执行，这 9 步不变。

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
- 严守术语表：遇表内源词必译为指定译法。新词自行确定统一译法，首次附原文「中文（English）」。
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
| 1 | 第1章 | 01-the-squire-of-allington.md | 18.9KB | todo |
| 2 | 第2章 | 02-the-two-pearls-of-allington.md | 25.7KB | todo |
| 3 | 第3章 | 03-the-widow-dale-of-allington.md | 23.7KB | todo |
| 4 | 第4章 | 04-mrs-roper-s-boardinghouse.md | 22.5KB | todo |
| 5 | 第5章 | 05-about-l-d.md | 17.0KB | todo |
| 6 | 第6章 | 06-beautiful-days.md | 28.1KB | todo |
| 7 | 第7章 | 07-the-beginning-of-troubles.md | 27.3KB | todo |
| 8 | 第8章 | 08-it-cannot-be.md | 16.6KB | todo |
| 9 | 第9章 | 09-mrs-dale-s-little-party.md | 28.0KB | todo |
| 10 | 第10章 | 10-mrs-lupex-and-amelia-roper.md | 19.2KB | todo |
| 11 | 第11章 | 11-social-life.md | 15.7KB | todo |
| 12 | 第12章 | 12-lilian-dale-becomes-a-butterfly.md | 34.1KB | todo |
| 13 | 第13章 | 13-a-visit-to-guestwick.md | 22.3KB | todo |
| 14 | 第14章 | 14-john-eames-takes-a-walk.md | 16.0KB | todo |
| 15 | 第15章 | 15-the-last-day.md | 26.7KB | todo |
| 16 | 第16章 | 16-mr-crosbie-meets-an-old-clergyman-on-his-way-to-courcy-castle.md | 14.2KB | todo |
| 17 | 第17章 | 17-courcy-castle.md | 33.5KB | todo |
| 18 | 第18章 | 18-lily-dale-s-first-love-letter.md | 18.9KB | todo |
| 19 | 第19章 | 19-the-squire-makes-a-visit-to-the-small-house.md | 21.4KB | todo |
| 20 | 第20章 | 20-dr-crofts.md | 17.2KB | todo |
| 21 | 第21章 | 21-john-eames-encounters-two-adventures-and-displays-great-courage-in-both.md | 29.3KB | todo |
| 22 | 第22章 | 22-lord-de-guest-at-home.md | 19.5KB | todo |
| 23 | 第23章 | 23-mr-plantagenet-palliser.md | 40.3KB | todo |
| 24 | 第24章 | 24-a-mother-in-law-and-a-father-in-law.md | 11.2KB | todo |
| 25 | 第25章 | 25-adolphus-crosbie-spends-an-evening-at-his-club.md | 22.1KB | todo |
| 26 | 第26章 | 26-lord-de-courcy-in-the-bosom-of-his-family.md | 20.6KB | todo |
| 27 | 第27章 | 27-on-my-honour-i-do-not-understand-it.md | 24.3KB | todo |
| 28 | 第28章 | 28-the-board.md | 25.1KB | todo |
| 29 | 第29章 | 29-john-eames-returns-to-burton-crescent.md | 20.0KB | todo |
| 30 | 第30章 | 30-is-it-from-him.md | 24.0KB | todo |
| 31 | 第31章 | 31-the-wounded-fawn.md | 21.1KB | todo |
| 32 | 第32章 | 32-pawkins-s-in-jermyn-street.md | 20.5KB | todo |
| 33 | 第33章 | 33-the-time-will-come.md | 24.9KB | todo |
| 34 | 第34章 | 34-the-combat.md | 17.6KB | todo |
| 35 | 第35章 | 35-vae-victis.md | 26.1KB | todo |
| 36 | 第36章 | 36-see-the-conquering-hero-comes.md | 26.3KB | todo |
| 37 | 第37章 | 37-an-old-man-s-complaint.md | 16.0KB | todo |
| 38 | 第38章 | 38-doctor-crofts-is-called-in.md | 24.8KB | todo |
| 39 | 第39章 | 39-dr-crofts-is-turned-out.md | 26.0KB | todo |
| 40 | 第40章 | 40-preparations-for-the-wedding.md | 32.5KB | todo |
| 41 | 第41章 | 41-domestic-troubles.md | 18.3KB | todo |
| 42 | 第42章 | 42-lily-s-bedside.md | 18.8KB | todo |
| 43 | 第43章 | 43-fie-fie.md | 25.8KB | todo |
| 44 | 第44章 | 44-valentine-s-day-at-allington.md | 18.2KB | todo |
| 45 | 第45章 | 45-valentine-s-day-in-london.md | 26.4KB | todo |
| 46 | 第46章 | 46-john-eames-at-his-office.md | 27.2KB | todo |
| 47 | 第47章 | 47-the-new-private-secretary.md | 18.7KB | todo |
| 48 | 第48章 | 48-nemesis.md | 24.8KB | todo |
| 49 | 第49章 | 49-preparations-for-going.md | 23.1KB | todo |
| 50 | 第50章 | 50-mrs-dale-is-thankful-for-a-good-thing.md | 17.2KB | todo |
| 51 | 第51章 | 51-john-eames-does-things-which-he-ought-not-to-have-done.md | 29.6KB | todo |
| 52 | 第52章 | 52-the-first-visit-to-the-guestwick-bridge.md | 23.3KB | todo |
| 53 | 第53章 | 53-loquitur-hopkins.md | 20.4KB | todo |
| 54 | 第54章 | 54-the-second-visit-to-the-guestwick-bridge.md | 24.9KB | todo |
| 55 | 第55章 | 55-not-very-fie-fie-after-all.md | 30.6KB | todo |
| 56 | 第56章 | 56-showing-how-mr-crosbie-became-again-a-happy-man.md | 18.4KB | todo |
| 57 | 第57章 | 57-lilian-dale-vanquishes-her-mother.md | 20.6KB | todo |
| 58 | 第58章 | 58-the-fate-of-the-small-house.md | 20.6KB | todo |
| 59 | 第59章 | 59-john-eames-becomes-a-man.md | 23.3KB | todo |
| 60 | 第60章 | 60-conclusion.md | 23.6KB | todo |

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
