# Plan.md

---

## 本计划信息

- **项目名称**：rafael-sabatini_captain-blood（《船长血》Captain Blood）
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
01-the-messenger.md,17.1,todo
02-kirke-s-dragoons.md,16.6,todo
...
```

| 字段 | 含义 | 取值 |
|------|------|------|
| `file` | 源文文件名（在 `原文/` 目录下） | 如 `01-the-messenger.md` |
| `size_kb` | 源文大小（KB）。>50KB 为长文，按通用翻译引擎第七节分段 | 数字 |
| `status` | 翻译状态 | `todo` 待译 / `doing` 翻译中 / `done` 已完成 |

---

## 执行步骤（agent 按此推进，两种模式共用）

> 本项目为「长篇」，走**委派模式**：主 agent 当调度员，每章下沉到一次性子代理执行下列 9 步；跨章连贯性靠术语表 + 黄金样本 + 前章末尾补偿。

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

全书 31 章，按罗马数字 I~XXXI 顺序，文件名加两位数字前缀。详表见 `translation_queue.csv`。

| # | 章号 | 章名 | 源文 |
|---|------|------|------|
| 1 | I | The Messenger | 01-the-messenger.md |
| 2 | II | Kirke's Dragoons | 02-kirke-s-dragoons.md |
| 3 | III | The Lord Chief Justice | 03-the-lord-chief-justice.md |
| 4 | IV | Human Merchandise | 04-human-merchandise.md |
| 5 | V | Arabella Bishop | 05-arabella-bishop.md |
| 6 | VI | Plans of Escape | 06-plans-of-escape.md |
| 7 | VII | Pirates | 07-pirates.md |
| 8 | VIII | Spaniards | 08-spaniards.md |
| 9 | IX | The Rebels-Convict | 09-the-rebels-convict.md |
| 10 | X | Don Diego | 10-don-diego.md |
| 11 | XI | Filial Piety | 11-filial-piety.md |
| 12 | XII | Don Pedro Sangre | 12-don-pedro-sangre.md |
| 13 | XIII | Tortuga | 13-tortuga.md |
| 14 | XIV | Levasseur's Heroics | 14-levasseur-s-heroics.md |
| 15 | XV | The Ransom | 15-the-ransom.md |
| 16 | XVI | The Trap | 16-the-trap.md |
| 17 | XVII | The Dupes | 17-the-dupes.md |
| 18 | XVIII | The Milagrosa | 18-the-milagrosa.md |
| 19 | XIX | The Meeting | 19-the-meeting.md |
| 20 | XX | Thief and Pirate | 20-thief-and-pirate.md |
| 21 | XXI | The Service of King James | 21-the-service-of-king-james.md |
| 22 | XXII | Hostilities | 22-hostilities.md |
| 23 | XXIII | Hostages | 23-hostages.md |
| 24 | XXIV | War | 24-war.md |
| 25 | XXV | The Service of King Louis | 25-the-service-of-king-louis.md |
| 26 | XXVI | M. de Rivarol | 26-m-de-rivarol.md |
| 27 | XXVII | Cartagena | 27-cartagena.md |
| 28 | XXVIII | The Honour of M. de Rivarol | 28-the-honour-of-m-de-rivarol.md |
| 29 | XXIX | The Service of King William | 29-the-service-of-king-william.md |
| 30 | XXX | The Last Fight of the Arabella | 30-the-last-fight-of-the-arabella.md |
| 31 | XXXI | His Excellency the Governor | 31-his-excellency-the-governor.md |

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
