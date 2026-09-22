# 翻译计划（Plan.md）

---

## 本计划信息

- **项目名称**：e-e-cummings_the-enormous-room（《巨大的房间》The Enormous Room，E. E. Cummings, 1922）
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
01-for-this-my-son-was-dead-and-is-alive-again-he-was-lost-and-is-found.md,11.0,todo
02-i-begin-a-pilgrimage.md,31.4,todo
...
```

| 字段 | 含义 | 取值 |
|------|------|------|
| `file` | 源文文件名（在 `原文/` 目录下） | 如 `05-le-nouveau.md` |
| `size_kb` | 源文大小（KB）。>50KB 为长文，按通用翻译引擎第七节分段 | 数字 |
| `status` | 翻译状态 | `todo` 待译 / `doing` 翻译中 / `done` 已完成 |

---

## 执行步骤（agent 按此推进，两种模式共用）

> **谁执行**：本项目内容形态为**中篇**（引言 + 13 章单一叙事弧），执行模式**连续**——主 agent 在自身上下文内逐篇执行以下 9 步。注意全书约 538KB，超出单批约 150KB 产能，需分多批续接（每批从队列第一个 todo 续起）。

### 1. 读配置（每次翻译前必读）
```
1. 本项目 Plan.md（本文件）
2. 项目说明.md
3. 术语表.md（硬约束）
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

**双语对照格式、标记规则、完整性禁令**：见 `prompts/通用翻译引擎.md` 第五、六节。此处不重复。

**本流程专有提醒**：
- 逐块对照原文，绝不漏译、不合并段落、不缩写、不总结，尤其结尾别截断。
- 严守术语表：遇表内源词必译为指定译法。法语斜体词按术语表策略保留原文。新词自行确定统一译法，首次附原文。
- 人物绰号、反讽语气、意识流节奏全文一致，照黄金样本风格译。
- 长文（>50KB：05/07/08 三章）分段处理见通用翻译引擎第七节。

### 5. 自检
- 完整性：源文每一段都在译文 Original 块中出现，末尾无截断。
- 块对称：Original/Chinese 数量相等，每块内段数对应。
- 标题格式：全部「英文 / 中文」合并。
- 术语一致：抽查 5 个术语词（如 planton、La Ferté、The Zulu），全文译法统一。
- 不满足则改到满足。

### 6. 自动检查
```
python scripts/check_bilingual.py 译文/对应篇名.zh-CN.md
```
结构契约满足则继续；有违规回步骤 4 修订。

### 7. 回填状态（双写）
检查通过后，`status` 从 `doing` 改 `done`，改两处：
- ① 项目 `translation_queue.csv` 该行；
- ② 根 `translation_queue.csv` 中 `<本项目名>,<本篇名>` 那一行。

### 8. 追加日志
在本文件「运行日志」追加一行。

### 9. 循环
回到步骤 2，取下一篇 `todo`，直到全部 `done`；单批上下文将满时收尾汇报退出，下批续接。

---

## 篇目清单

| # | 篇名 | 源文 | 大小 | 状态 |
|---|------|------|------|------|
| 1 | Introduction "For This My Son Was Dead…"（引言） | 01-for-this-my-son-was-dead-and-is-alive-again-he-was-lost-and-is-found.md | 11KB | todo |
| 2 | Ch. I I Begin a Pilgrimage | 02-i-begin-a-pilgrimage.md | 31KB | todo |
| 3 | Ch. II En Route | 03-en-route.md | 22KB | todo |
| 4 | Ch. III A Pilgrim's Progress | 04-a-pilgrim-s-progress.md | 41KB | todo |
| 5 | Ch. IV Le Nouveau | 05-le-nouveau.md | 82KB | todo |
| 6 | Ch. V A Group of Portraits | 06-a-group-of-portraits.md | 46KB | todo |
| 7 | Ch. VI Apollyon | 07-apollyon.md | 50KB | todo |
| 8 | Ch. VII An Approach to the Delectable Mountains | 08-an-approach-to-the-delectable-mountains.md | 62KB | todo |
| 9 | Ch. VIII The Wanderer | 09-the-wanderer.md | 24KB | todo |
| 10 | Ch. IX Zoo-Loo | 10-zoo-loo.md | 37KB | todo |
| 11 | Ch. X Surplice | 11-surplice.md | 25KB | todo |
| 12 | Ch. XI Jean le Nègre | 12-jean-le-n-gre.md | 44KB | todo |
| 13 | Ch. XII Three Wise Men | 13-three-wise-men.md | 32KB | todo |
| 14 | Ch. XIII I Say Goodbye to La Misère | 14-i-say-goodbye-to-la-mis-re.md | 32KB | todo |

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
