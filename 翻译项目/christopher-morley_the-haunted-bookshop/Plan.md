# 翻译计划：christopher-morley_the-haunted-bookshop

## 本计划信息

- **项目名称**：christopher-morley_the-haunted-bookshop（《闹鬼书店》 The Haunted Bookshop, Christopher Morley, 1919）
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/小说文学.md
- **术语表**：术语表.md
- **内容形态 / 执行模式**：长篇 / 委派（15 章 + 献词 + 尾注，共 17 篇，约 343KB）

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
00-dedication.md,1.2,todo
01-the-haunted-bookshop.md,30.9,todo
...
```

| 字段 | 含义 | 取值 |
|------|------|------|
| `file` | 源文文件名（在 `原文/` 目录下） | 如 `01-the-haunted-bookshop.md` |
| `size_kb` | 源文大小（KB）。>50KB 为长文，按通用翻译引擎第七节分段 | 数字 |
| `status` | 翻译状态 | `todo` 待译 / `doing` 翻译中 / `done` 已完成 |

---

## 执行步骤（agent 按此推进，两种模式共用）

> **谁执行**由 `项目说明.md` 的「内容形态」字段决定（见 `WORKFLOW.md`「判断内容形态」）：本项目为长篇 → **委派模式**，子代理逐篇执行以下 9 步。

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
- 长文（源文 >50KB）分段处理见通用翻译引擎第七节。本项目单篇最大 31.2KB，无须分段。

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
| 0 | 献词：致书商们 | 00-dedication.md | 1.2KB | todo |
| 1 | I 闹鬼的书店 | 01-the-haunted-bookshop.md | 30.9KB | todo |
| 2 | II 玉米芯烟斗俱乐部 | 02-the-corn-cob-club.md | 31.1KB | todo |
| 3 | III 蒂塔尼亚来了 | 03-titania-arrives.md | 26.5KB | todo |
| 4 | IV 消失的书 | 04-the-disappearing-volume.md | 25.7KB | todo |
| 5 | V 奥布里半路步行半路搭车 | 05-aubrey-walks-part-way-home-and-rides-the-rest-of-the-way.md | 13.4KB | todo |
| 6 | VI 蒂塔尼亚学做书店生意 | 06-titania-learns-the-business.md | 31.2KB | todo |
| 7 | VII 奥布里租房 | 07-aubrey-takes-lodgings.md | 22.2KB | todo |
| 8 | VIII 奥布里看电影，后悔德语没多学 | 08-aubrey-goes-to-the-movies-and-wishes-he-knew-more-german.md | 20.8KB | todo |
| 9 | IX 叙事再次减速 | 09-again-the-narrative-is-retarded.md | 16.6KB | todo |
| 10 | X 罗杰夜袭冰箱 | 10-roger-raids-the-icebox.md | 13.1KB | todo |
| 11 | XI 蒂塔尼亚尝试卧读 | 11-titania-tries-reading-in-bed.md | 22.4KB | todo |
| 12 | XII 奥布里决意提供「与众不同」的服务 | 12-aubrey-determines-to-give-service-that-s-different.md | 18.3KB | todo |
| 13 | XIII 卢德洛街之战 | 13-the-battle-of-ludlow-street.md | 21.1KB | todo |
| 14 | XIV 《克伦威尔》最后一次露面 | 14-the-cromwell-makes-its-last-appearance.md | 25.1KB | todo |
| 15 | XV 查普曼先生挥动魔杖 | 15-mr-chapman-waves-his-wand.md | 23.0KB | todo |
| 16 | 尾注 | 16-endnotes.md | 0.2KB | todo |

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
| 2026-09-10 | 全书 17 文件（献词+正文XV+尾注） | 整书完结 | 批次4委派模式：10 个并发子代理译完（342.8KB）；17/17 done，check_bilingual 结构契约 0 违规（非零退出码均为数字本地化改写型锚点误报）；无 doing 残留、无失败重试。术语表硬约束全程生效（罗杰·米夫林、博克勿译薄伽丘、施勒太太、「好心朋友」带引号、《克伦威尔》简称）。 |
