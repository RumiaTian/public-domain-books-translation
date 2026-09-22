# 翻译计划：anna-julia-cooper_a-voice-from-the-south

## 本计划信息

- **项目名称**：anna-julia-cooper_a-voice-from-the-south（《来自南方的声音》 A Voice from the South, Anna Julia Cooper, 1892）
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/学术著作.md
- **术语表**：术语表.md
- **内容形态 / 执行模式**：短篇集 / 委派（8 篇独立论文 + 卷首题词/献词/部题/尾注，共 14 个文件，约 346KB 源文）

---

## 文件分工

| 文件 | 作用 | 谁来改 |
|------|------|--------|
| `项目说明.md` | 项目基本信息、领域配置、篇目清单 | 人工 |
| `术语表.md` | 翻译硬约束层。每篇译完补充新词 | agent / 人工 |
| `translation_queue.csv` | 任务队列。每行一文件，`file, size_kb, status` 三列 | 翻译前改 doing，完成后改 done |
| `Plan.md`（本文件） | 执行步骤 + 运行日志 | agent 追加日志 |
| `原文/*.md` | 源文 | 不改 |
| `译文/*.zh-CN.md` | 译文产出（逐段对照双语） | 翻译 agent 产出 |

---

## translation_queue.csv 格式

```
file,size_kb,status
01-epigraph.md,0.1,todo
02-dedication.md,0.4,todo
...
```

| 字段 | 含义 | 取值 |
|------|------|------|
| `file` | 源文文件名（在 `原文/` 目录下） | 如 `05-womanhood-a-vital-element-in-the-regeneration-and-progress-of-a-race.md` |
| `size_kb` | 源文大小（KB）。>50KB 为长文，按通用翻译引擎第七节分段 | 数字 |
| `status` | 翻译状态 | `todo` 待译 / `doing` 翻译中 / `done` 已完成 |

---

## 执行步骤（agent 按此推进，两种模式共用）

> **谁执行**由 `项目说明.md` 的「内容形态」字段决定（见 `WORKFLOW.md`「判断内容形态」）：本项目为短篇集 → **委派模式**，子代理逐篇执行本流程。

### 1. 读配置（每次翻译前必读）
```
1. 本项目 Plan.md（本文件）
2. 项目说明.md
3. 术语表.md
4. prompts/通用翻译引擎.md
5. prompts/领域配置/学术著作.md
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
- 逐段对照原文，绝不漏译、不合并段落、不缩写、不总结，尤其结尾别截断。
- 严守术语表：遇表内源词必译为指定译法。新词自行确定统一译法，首次附原文「中文（English）」。
- 术语表「人物」多用通行译名；法语/拉丁语短语保留原文随文括注意译。
- 长文（源文 >50KB，本项目中为 11、12 两篇）分段处理见通用翻译引擎第七节。

### 5. 自检
- 完整性：源文每一段都在译文 Original 块中出现，末尾无截断。
- 块对称：Original/Chinese 数量相等，每块内段数对应。
- 标题格式：全部「英文 / 中文」合并。
- 术语一致：抽查 5 个术语词（如 Negro／colored／Black Woman／Wimodaughsis），全文译法统一。
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
| 1 | 卷首题词 | 01-epigraph.md | 0.1KB | todo |
| 2 | 献词 | 02-dedication.md | 0.4KB | todo |
| 3 | 我们的存在理由（卷首自陈） | 03-our-raison-detre.md | 2.8KB | todo |
| 4 | 第一部「女高音助奏」部题 | 04-soprano-obligato.md | 0.5KB | todo |
| 5 | 女性品格：种族新生与进步的关键要素 | 05-womanhood-a-vital-element-in-the-regeneration-and-progress-of-a-race.md | 44.7KB | todo |
| 6 | 女子高等教育 | 06-the-higher-education-of-women.md | 37.9KB | todo |
| 7 | 女性对阵印第安人 | 07-woman-versus-the-indian.md | 54.7KB | todo |
| 8 | 美国女性地位 | 08-the-status-of-woman-in-america.md | 21.6KB | todo |
| 9 | 第二部「随意合奏」部题 | 09-tutti-ad-libitum.md | 0.7KB | todo |
| 10 | 美国有种族问题吗？若有，如何解决为佳？ | 10-has-america-a-race-problem-if-so-how-can-it-best-be-solved.md | 29.4KB | todo |
| 11 | 美国文学之一面 | 11-one-phase-of-american-literature.md | 62.8KB | todo |
| 12 | 我们的价值何在 | 12-what-are-we-worth.md | 68.6KB | todo |
| 13 | 信念的收益 | 13-the-gain-from-a-belief.md | 21.6KB | todo |
| 14 | 尾注 | 14-endnotes.md | 0.6KB | todo |

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
