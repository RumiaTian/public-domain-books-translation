# 翻译计划（Plan.md）

---

## 本计划信息

- **项目名称**：edgar-wallace_the-man-who-knew（《无所不知的人》）
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
01-the-man-in-the-laboratory.md,15.2,todo
02-the-girl-who-cried.md,11.4,todo
...
```

| 字段 | 含义 | 取值 |
|------|------|------|
| `file` | 源文文件名（在 `原文/` 目录下） | 如 `01-the-man-in-the-laboratory.md` |
| `size_kb` | 源文大小（KB）。>50KB 为长文，按通用翻译引擎第七节分段 | 数字 |
| `status` | 翻译状态 | `todo` 待译 / `doing` 翻译中 / `done` 已完成 |

---

## 执行步骤（agent 按此推进，两种模式共用）

> **谁执行**由 `项目说明.md` 的「内容形态」字段决定：本项目为**中篇 → 连续模式**，主 agent 自身逐篇执行下列 9 步。

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
- 标题格式：全部「英文 / 中文」合并（罗马数字照搬）。
- 术语一致：抽查 5 个术语词，全文译法统一。
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
回到步骤 2，取下一篇 `todo`，直到全部 `done`。连续模式下主 agent 一气呵成；上下文将满时按通用翻译引擎七点五节收尾退出。

---

## 篇目清单

| # | 篇名 | 源文 | 大小 | 状态 |
|---|------|------|------|------|
| 1 | I The Man in the Laboratory | 01-the-man-in-the-laboratory.md | 15.2KB | todo |
| 2 | II The Girl Who Cried | 02-the-girl-who-cried.md | 11.4KB | todo |
| 3 | III Four Important Characters | 03-four-important-characters.md | 16.6KB | todo |
| 4 | IV The Accountant at the Bank | 04-the-accountant-at-the-bank.md | 12.1KB | todo |
| 5 | V John Minute's Legacy | 05-john-minute-s-legacy.md | 22.6KB | todo |
| 6 | VI The Man Who Knew | 06-the-man-who-knew.md | 8.9KB | todo |
| 7 | VII Introducing Mr. Rex Holland | 07-introducing-mr-rex-holland.md | 23.1KB | todo |
| 8 | VIII Sergeant Smith Calls | 08-sergeant-smith-calls.md | 17.7KB | todo |
| 9 | IX Frank Merrill at the Altar | 09-frank-merrill-at-the-altar.md | 17.3KB | todo |
| 10 | X A Murder | 10-a-murder.md | 23.8KB | todo |
| 11 | XI The Case Against Frank Merrill | 11-the-case-against-frank-merrill.md | 16.9KB | todo |
| 12 | XII The Trial of Frank Merrill | 12-the-trial-of-frank-merrill.md | 19.6KB | todo |
| 13 | XIII The Man Who Came to Montreux | 13-the-man-who-came-to-montreux.md | 15.2KB | todo |
| 14 | XIV The Man Who Looked Like Frank | 14-the-man-who-looked-like-frank.md | 15.8KB | todo |
| 15 | XV A Letter in the Grate | 15-a-letter-in-the-grate.md | 7.8KB | todo |
| 16 | XVI The Coming of Sergeant Smith | 16-the-coming-of-sergeant-smith.md | 24.2KB | todo |
| 17 | XVII The Man Called "Merrill" | 17-the-man-called-merrill.md | 23.7KB | todo |

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-09-02 | 全书 17 章 | 完成 17/17 | 批次1三段并行于 09-01 20:24-26 全灭[1308]额度墙，死前抢救 12/17 干净存稿；次日两续作代理并行补齐 5 件遗章（定名逐名衔接既有章节）；17 件全量过检零告警，全部定名零变体漂移；引文块/粗体信件/场景分隔线成对保留 |
