# 翻译计划（Plan.md）

---

## 本计划信息

- **项目名称**：anthony-trollope_short-fiction（安东尼·特罗洛普短篇小说集）
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/小说文学.md
- **术语表**：术语表.md
- **内容形态/执行模式**：短篇集 / 委派（子代理逐篇执行下方 9 步）

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
01-a-tale-of-antwerp.md,44.0,todo
...
```

| 字段 | 含义 | 取值 |
|------|------|------|
| `file` | 源文文件名（在 `原文/` 目录下） | 如 `01-a-tale-of-antwerp.md` |
| `size_kb` | 源文大小（KB）。>50KB 为长文，按通用翻译引擎第七节分段 | 数字 |
| `status` | 翻译状态 | `todo` 待译 / `doing` 翻译中 / `done` 已完成 |

> 文件名两位数字前缀 = 原书 spine 阅读顺序，勿重排。

---

## 执行步骤（agent 按此推进，两种模式共用）

> **谁执行**由 `项目说明.md` 的「内容形态」字段决定（见 `WORKFLOW.md`「判断内容形态」）：本项目为短篇集，走**委派模式**，由子代理逐篇执行本流程。

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

| # | 文件 | 大小 | 状态 |
|---|------|------|------|
| 1 | 01-a-tale-of-antwerp.md | 44.0KB | todo |
| 2 | 02-the-o-conors-of-castle-conor-county-mayo.md | 40.9KB | todo |
| 3 | 03-the-courtship-of-susan-bell.md | 65.2KB | todo |
| 4 | 04-an-unprotected-female-at-the-pyramids.md | 61.7KB | todo |
| 5 | 05-the-ch-teau-of-prince-polignac.md | 48.0KB | todo |
| 6 | 06-miss-sarah-jack-of-spanish-town-jamaica.md | 53.1KB | todo |
| 7 | 07-john-bull-on-the-guadalquivir.md | 52.9KB | todo |
| 8 | 08-la-m-re-bauche.md | 68.7KB | todo |
| 9 | 09-a-ride-across-palestine.md | 82.2KB | todo |
| 10 | 10-mrs-general-talboys.md | 51.0KB | todo |
| 11 | 11-the-parson-s-daughter-of-oxney-colne.md | 61.1KB | todo |
| 12 | 12-the-man-who-kept-his-money-in-a-box.md | 63.1KB | todo |
| 13 | 13-the-house-of-heine-brothers-in-munich.md | 53.1KB | todo |
| 14 | 14-returning-home.md | 46.8KB | todo |
| 15 | 15-aaron-trow.md | 62.4KB | todo |
| 16 | 16-the-mistletoe-bough.md | 49.2KB | todo |
| 17 | 17-george-walker-at-suez.md | 41.7KB | todo |
| 18 | 18-the-journey-to-panama.md | 44.6KB | todo |
| 19 | 19-the-widow-s-mite.md | 55.0KB | todo |
| 20 | 20-the-two-generals.md | 48.3KB | todo |
| 21 | 21-miss-ophelia-gledd.md | 45.7KB | todo |
| 22 | 22-malachi-s-cove.md | 43.4KB | todo |
| 23 | 23-or-love-shall-still-be-lord-of-all.md | 18.0KB | todo |
| 24 | 24-father-giles-of-ballymoy.md | 40.8KB | todo |
| 25 | 25-lotta-schmidt.md | 46.0KB | todo |
| 26 | 26-the-adventures-of-fred-pickering.md | 45.6KB | todo |
| 27 | 27-the-last-austrian-who-left-venice.md | 46.2KB | todo |
| 28 | 28-the-turkish-bath.md | 53.5KB | todo |
| 29 | 29-mary-gresley.md | 56.5KB | todo |
| 30 | 30-josephine-de-montmorenci.md | 49.8KB | todo |
| 31 | 31-the-panjandrum.md | 102.7KB | todo |
| 32 | 32-the-spotted-dog.md | 111.4KB | todo |
| 33 | 33-mrs-brumby.md | 53.7KB | todo |
| 34 | 34-christmas-day-at-kirkby-cottage.md | 69.8KB | todo |
| 35 | 35-never-never-never-never.md | 11.5KB | todo |
| 36 | 36-christmas-at-thompson-hall.md | 86.5KB | todo |
| 37 | 37-why-frau-frohmann-raised-her-prices.md | 146.2KB | todo |
| 38 | 38-the-telegraph-girl.md | 80.1KB | todo |
| 39 | 39-the-lady-of-launay.md | 131.0KB | todo |
| 40 | 40-alice-dugdale.md | 132.5KB | todo |
| 41 | 41-the-two-heroines-of-plumplington.md | 137.2KB | todo |
| 42 | 42-endnotes.md | 0.3KB | todo |

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
