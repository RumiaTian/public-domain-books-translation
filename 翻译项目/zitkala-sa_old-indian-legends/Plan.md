# 翻译计划（Plan.md）

> 翻译一整本书或多文件内容时的标准模式。复制本文件到项目文件夹，重命名为 `Plan.md`，填入书名、源文/译文目录、篇目清单（或生成 `translation_queue.csv`），即可用通用提示词推进翻译，无需手动指定每个文件。
>
> 适配任意内容：小说、文集、手册、论文集……只需在「项目说明.md」选好领域配置（技术/历史/学术/小说），Plan.md 的执行流程不变。

---

## 本计划信息

- **项目名称**：zitkala-sa_old-indian-legends（《老印第安传说》Old Indian Legends）
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
第一章.md,12.3,todo
第二章.md,18.1,todo
...
```

| 字段 | 含义 | 取值 |
|------|------|------|
| `file` | 源文文件名（在 `原文/` 目录下） | 如 `The-Bryd.md` |
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
5. prompts/领域配置/对应领域.md（项目说明指定）
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
| 0 | 序言（Preface） | 00-preface.md | 2.0KB | todo |
| 1 | 伊克托米与鸭子 | 01-iktomi-and-the-ducks.md | 9.7KB | todo |
| 2 | 伊克托米的毯子 | 02-iktomi-s-blanket.md | 4.8KB | todo |
| 3 | 伊克托米与麝鼠 | 03-iktomi-and-the-muskrat.md | 5.3KB | todo |
| 4 | 伊克托米与郊狼 | 04-iktomi-and-the-coyote.md | 5.1KB | todo |
| 5 | 伊克托米与小鹿 | 05-iktomi-and-the-fawn.md | 8.6KB | todo |
| 6 | 獾与熊 | 06-the-badger-and-the-bear.md | 11.6KB | todo |
| 7 | 被缚于树上 | 07-the-tree-bound.md | 10.6KB | todo |
| 8 | 射落红鹰 | 08-shooting-of-the-red-eagle.md | 5.4KB | todo |
| 9 | 伊克托米与乌龟 | 09-iktomi-and-the-turtle.md | 5.0KB | todo |
| 10 | 野牛头骨中的舞会 | 10-dance-in-a-buffalo-skull.md | 2.9KB | todo |
| 11 | 蟾蜍与男孩 | 11-the-toad-and-the-boy.md | 6.8KB | todo |
| 12 | 伊亚，食营兽 | 12-iya-the-camp-eater.md | 8.4KB | todo |
| 13 | 曼斯汀，兔子 | 13-man-tin-the-rabbit.md | 8.2KB | todo |
| 14 | 好战的七个 | 14-the-warlike-seven.md | 4.8KB | todo |

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
| 2026-08-15 | 00-preface | done | 4.2KB |
| 2026-08-15 | 01-iktomi-and-the-ducks.md | done | 9.7KB |
| 2026-08-15 | 08-shooting-of-the-red-eagle.md | done | check 退出码 0，6 对块 |
| 2026-08-15 | 09-iktomi-and-the-turtle.md | done | check 退出码 0，7 对块 |
| 2026-08-15 | 10-dance-in-a-buffalo-skull.md | done | check 退出码 0，3 对块 |
| 2026-08-15 | 11-the-toad-and-the-boy.md | done | check 退出码 0，7 对块 |
| 2026-08-15 | 12-iya-the-camp-eater.md | done | check 退出码 0，7 对块 |
| 2026-08-15 | 13-man-tin-the-rabbit.md | done | check 退出码 0，6 对块 |
| 2026-08-15 | 14-the-warlike-seven.md | done | check 退出码 0，6 对块 |
| 2026-08-15 | 02-07 (6篇,10-23KB) | done ×6 | exit 0×6; 委派子代理(单代理连译)。讲故事口吻对齐黄金样本,感叹/拟声/重复节奏保留。新词:Inyan 因扬/大神灵/慷慨的赐予者/魔箭/蒸汽汗屋 等+一批达科他拟声词。术语表并发写已重读干净追加 |
| 2026-08-15 | 08-14 (7篇,6-17KB) | done ×7 | exit 0×7; 委派子代理(单代理连译)。角色名严守术语表(伊克托米/帕特卡沙/曼斯汀/双面老怪/伊亚食营兽);斜体达科他语双保留;新词:Chaske 查斯克/《好战的七位》拟人角色 等 |
| 2026-08-15 | ★全书完 15/15 | — | zitkala-sa《老印第安传说》全部15篇译完(100%)。本会话 2 子代理并行译 13 篇(~88KB源文) |
