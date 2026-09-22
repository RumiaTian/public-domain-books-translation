# 翻译计划（Plan.md）

---

## 本计划信息

- **项目名称**：baroness-orczy_lord-tonys-wife（《托尼勋爵的妻子》，红花侠系列）
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
00-dedication.md,0.1,todo
01-nantes-1789.md,49.2,todo
...
```

| 字段 | 含义 | 取值 |
|------|------|------|
| `file` | 源文文件名（在 `原文/` 目录下） | 如 `03-the-moor.md` |
| `size_kb` | 源文大小（KB）。>50KB 为长文，按通用翻译引擎第七节分段 | 数字 |
| `status` | 翻译状态 | `todo` 待译 / `doing` 翻译中 / `done` 已完成 |

---

## 执行步骤（agent 按此推进，两种模式共用）

> **谁执行**由 `项目说明.md` 的「内容形态」字段决定（见 `WORKFLOW.md`「判断内容形态」）：本项目为长篇 → **委派模式**，由子代理逐篇执行本流程。

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

> 共 24 件：题献 1 + 序章 1 + 卷一题名页 1 + 卷一 9 章 + 卷二题名页 1 + 卷二 10 章 + 尾注 1。正文 20 章（>50KB 者：13-the-tiger-s-lair.md 51.9KB）。顺序即阅读顺序，权威清单见 `translation_queue.csv`。

| # | 篇名 | 源文 | 大小 | 状态 |
|---|------|------|------|------|
| 0 | 题献 | 00-dedication.md | 0.1KB | todo |
| 1 | 序章：南特，1789 | 01-nantes-1789.md | 49.2KB | todo |
| 2 | 卷一题名页：巴斯，1793 | 02-book-1-bath-1793.md | 0.0KB | todo |
| 3 | 荒野（I） | 03-the-moor.md | 11.1KB | todo |
| 4 | 「底」客栈（II） | 04-the-bottom-inn.md | 46.1KB | todo |
| 5 | 舞会厅（III） | 05-the-assembly-rooms.md | 34.6KB | todo |
| 6 | 父亲（IV） | 06-the-father.md | 13.7KB | todo |
| 7 | 巢（V） | 07-the-nest.md | 21.2KB | todo |
| 8 | 红花侠（VI） | 08-the-scarlet-pimpernel.md | 11.4KB | todo |
| 9 | 玛格丽特（VII） | 09-marguerite.md | 6.3KB | todo |
| 10 | 通往波蒂斯黑德之路（VIII） | 10-the-road-to-portishead.md | 21.0KB | todo |
| 11 | 法国海岸（IX） | 11-the-coast-of-france.md | 20.5KB | todo |
| 12 | 卷二题名页：南特，1793 年 12 月 | 12-book-2-nantes-december-1793.md | 0.0KB | todo |
| 13 | 虎穴（I） | 13-the-tiger-s-lair.md | 51.9KB | todo |
| 14 | 布法伊（II） | 14-le-bouffay.md | 26.5KB | todo |
| 15 | 猎鸟人（III） | 15-the-fowlers.md | 35.9KB | todo |
| 16 | 罗 网（IV） | 16-the-net.md | 36.2KB | todo |
| 17 | 希望的讯息（V） | 17-the-message-of-hope.md | 16.6KB | todo |
| 18 | 「死鼠」酒馆（VI） | 18-the-rat-mort.md | 18.3KB | todo |
| 19 | 酒馆混战（VII） | 19-the-fracas-in-the-tavern.md | 31.3KB | todo |
| 20 | 英格兰冒险家们（VIII） | 20-the-english-adventurers.md | 22.1KB | todo |
| 21 | 总督（IX） | 21-the-proconsul.md | 22.4KB | todo |
| 22 | 托尼勋爵（X） | 22-lord-tony.md | 9.2KB | todo |
| 23 | 尾注 | 23-endnotes.md | 0.1KB | todo |

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
