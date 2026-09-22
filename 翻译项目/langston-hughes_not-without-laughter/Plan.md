# 翻译计划（Plan.md）

> 翻译一整本书或多文件内容时的标准模式。复制本文件到项目文件夹，重命名为 `Plan.md`，填入书名、源文/译文目录、篇目清单（或生成 `translation_queue.csv`），即可用通用提示词推进翻译，无需手动指定每个文件。
>
> 适配任意内容：小说、文集、手册、论文集……只需在「项目说明.md」选好领域配置（技术/历史/学术/小说），Plan.md 的执行流程不变。

---

## 本计划信息

- **项目名称**：不是没有笑（Not Without Laughter）—— langston-hughes_not-without-laughter
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
01-storm.md,12.3,todo
02-conversation.md,18.1,todo
...
```

| 字段 | 含义 | 取值 |
|------|------|------|
| `file` | 源文文件名（在 `原文/` 目录下） | 如 `01-storm.md` |
| `size_kb` | 源文大小（KB）。>50KB 为长文，按通用翻译引擎第七节分段 | 数字 |
| `status` | 翻译状态 | `todo` 待译 / `doing` 翻译中 / `done` 已完成 |

---

## 执行步骤（agent 按此推进，两种模式共用）

> **谁执行**由 `项目说明.md` 的「内容形态」字段决定（见 `WORKFLOW.md`「判断内容形态」）：委派模式由子代理逐篇执行本流程；连续模式（中篇）由主 agent 自己执行。无论谁执行，这 9 步不变。

### 1. 读配置（每次翻译前必读）
```
1. 本项目 Plan.md（本文件）
2. 项目说明.md
3. 术语表.md（如无则跳过）
4. prompts/通用翻译引擎.md
5. prompts/领域配置/小说文学.md（项目说明指定）
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
- 标题格式：全部「英文 / 中文」合并（章节标题保留罗马数字，如 "I Storm / 一 风暴"）。
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

全书 30 章（罗马数字 I–XXX），源文文件已按阅读顺序加数字前缀，清单由 `translation_queue.csv` 管理（运行 `python scripts/gen_project_files.py` 生成）。

| # | 章名 | 源文 |
|---|------|------|
| 1 | I Storm | 01-storm.md |
| 2 | II Conversation | 02-conversation.md |
| 3 | III Jimboy's Letter | 03-jimboy-s-letter.md |
| 4 | IV Thursday Afternoon | 04-thursday-afternoon.md |
| 5 | V Guitar | 05-guitar.md |
| 6 | VI Work | 06-work.md |
| 7 | VII White Folks | 07-white-folks.md |
| 8 | VIII Dance | 08-dance.md |
| 9 | IX Carnival | 09-carnival.md |
| 10 | X Punishment | 10-punishment.md |
| 11 | XI School | 11-school.md |
| 12 | XII Hard Winter | 12-hard-winter.md |
| 13 | XIII Christmas | 13-christmas.md |
| 14 | XIV Return | 14-return.md |
| 15 | XV One by One | 15-one-by-one.md |
| 16 | XVI Nothing but Love | 16-nothing-but-love.md |
| 17 | XVII Barbershop | 17-barbershop.md |
| 18 | XVIII Children's Day | 18-children-s-day.md |
| 19 | XIX Ten Dollars and Costs | 19-ten-dollars-and-costs.md |
| 20 | XX Hey, Boy! | 20-hey-boy.md |
| 21 | XXI Note to Harriett | 21-note-to-harriett.md |
| 22 | XXII Beyond the Jordan | 22-beyond-the-jordan.md |
| 23 | XXIII Tempy's House | 23-tempy-s-house.md |
| 24 | XXIV A Shelf of Books | 24-a-shelf-of-books.md |
| 25 | XXV Pool Hall | 25-pool-hall.md |
| 26 | XXVI The Doors of Life | 26-the-doors-of-life.md |
| 27 | XXVII Beware of Women | 27-beware-of-women.md |
| 28 | XXVIII Chicago | 28-chicago.md |
| 29 | XXIX Elevator | 29-elevator.md |
| 30 | XXX Princess of the Blues | 30-princess-of-the-blues.md |

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
