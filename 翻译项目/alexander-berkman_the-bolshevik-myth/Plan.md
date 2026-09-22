# 翻译计划（Plan.md）— alexander-berkman_the-bolshevik-myth

---

## 本计划信息

- **项目名称**：alexander-berkman_the-bolshevik-myth（《布尔什维克神话》，Alexander Berkman 旅苏日记 1920–1922）
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/历史古籍.md
- **术语表**：术语表.md
- **内容形态**：长篇（42 篇，单一叙事弧日记体）→ 执行模式：委派

---

## 文件分工

| 文件 | 作用 | 谁来改 |
|------|------|--------|
| `项目说明.md` | 项目基本信息、领域配置、篇目清单 | 人工 |
| `术语表.md` | 翻译硬约束层。每篇译完补充新词 | agent / 人工 |
| `translation_queue.csv` | 任务队列。每行一文件，`file, size_kb, status` 三列 | 翻译前改 doing，完成后改 done |
| `Plan.md`（本文件） | 执行步骤 + 运行日志 | agent 追加日志 |
| `原文/*.md` | 源文（01-42 数字前缀=阅读顺序） | 不改 |
| `译文/*.zh-CN.md` | 译文产出（块对照双语） | 翻译 agent 产出 |

---

## translation_queue.csv 格式

```
file,size_kb,status
01-preface.md,3.6,todo
02-the-log-of-the-transport-buford.md,25.4,todo
...
```

| 字段 | 含义 | 取值 |
|------|------|------|
| `file` | 源文文件名（在 `原文/` 目录下） | 如 `14-lenin.md` |
| `size_kb` | 源文大小（KB）。>50KB 为长文，按通用翻译引擎第七节分段 | 数字 |
| `status` | 翻译状态 | `todo` 待译 / `doing` 翻译中 / `done` 已完成 |

---

## 执行步骤（agent 按此推进，两种模式共用）

> 本项目为**委派模式**：主 agent 只当调度员，逐篇把 9 步下沉到一次性子代理执行（简报与并发上限见 `WORKFLOW.md`「委派模式调度循环」）。

### 1. 读配置（每次翻译前必读）
```
1. 本项目 Plan.md（本文件）
2. 项目说明.md
3. 术语表.md
4. prompts/通用翻译引擎.md
5. prompts/领域配置/历史古籍.md
6. 译文/ 下任意一篇已完成的 .zh-CN.md（作为风格黄金样本；无则跳过）
```

### 2. 取任务
读 `translation_queue.csv`，取第一个 `status=todo` 的行。先 `ls 译文/` 检查该篇译文是否已存在：
- 已存在 → 直接改 `done`，跳到步骤 8。
- 不存在 → 把该行 `status` 改为 `doing` 并保存 CSV，继续。

### 3. 读源文
读 `原文/对应文件名`。

### 4. 翻译
产出到 `译文/对应文件名去.md加.zh-CN.md`。

**本流程专有提醒**：
- 逐块对照原文，绝不漏译、不合并段落、不缩写、不总结，尤其结尾别截断（本章日期条目常到末尾）。
- 严守术语表：遇表内源词必译为指定译法。新词自行确定统一译法，首次附原文「中文（English）」。
- 罗马数字章号照搬；日记日期条目格式全书统一（见术语表策略总则第 3 条）。
- 长文（源文 >50KB）分段处理见通用翻译引擎第七节。本项目最大单篇约 36KB，无需分段。

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
结构契约满足则继续；有违规回步骤 4 修订。

### 7. 回填状态（双写）
`status` 从 `doing` 改 `done`，改两处：
- ① 项目 `translation_queue.csv` 该行；
- ② 根 `translation_queue.csv` 中 `alexander-berkman_the-bolshevik-myth,<本篇名>` 那一行。

### 8. 追加日志
在本文件「运行日志」追加一行。

### 9. 循环
回到步骤 2，取下一篇 `todo`，直到全部 `done`。委派模式下由主 agent 决定是否继续派单。

---

## 篇目清单

| # | 篇名 | 源文 | 大小 | 状态 |
|---|------|------|------|------|
| 1 | 序言 Preface | 01-preface.md | 3.6KB | todo |
| 2 | 运输船布福德号日志 | 02-the-log-of-the-transport-buford.md | 25.4KB | todo |
| 3 | 踏上苏维埃土地 | 03-on-soviet-soil.md | 5.8KB | todo |
| 4 | 在彼得格勒 | 04-in-petrograd.md | 16.5KB | todo |
| 5 | 莫斯科 | 05-moscow.md | 6.3KB | todo |
| 6 | 宾馆 | 06-the-guest-house.md | 7.1KB | todo |
| 7 | 契切林与卡拉汉 | 07-chicherin-and-karakhan.md | 8.8KB | todo |
| 8 | 市场 | 08-the-market.md | 9.4KB | todo |
| 9 | 在莫斯科公社旅馆 | 09-in-the-moskkommune.md | 6.9KB | todo |
| 10 | 特维尔大街的俱乐部 | 10-the-club-on-the-tverskaya.md | 11.1KB | todo |
| 11 | 访彼得·克鲁泡特金 | 11-a-visit-to-peter-kropotkin.md | 7.2KB | todo |
| 12 | 布尔什维克的活动 | 12-bolshevik-activities.md | 9.5KB | todo |
| 13 | 景象与观感 | 13-sights-and-views.md | 10.7KB | todo |
| 14 | 列宁 | 14-lenin.md | 7.2KB | todo |
| 15 | 在拉脱维亚边境 | 15-on-the-latvian-border.md | 36.4KB | todo |
| 16 | 重返彼得格勒 | 16-back-in-petrograd.md | 17.9KB | todo |
| 17 | 工人疗养院 | 17-rest-homes-for-workers.md | 6.1KB | todo |
| 18 | 五一节 | 18-the-first-of-may.md | 5.9KB | todo |
| 19 | 英国工党代表团 | 19-the-british-labor-mission.md | 15.0KB | todo |
| 20 | 狂热的精神 | 20-the-spirit-of-fanaticism.md | 15.7KB | todo |
| 21 | 其他人 | 21-other-people.md | 9.7KB | todo |
| 22 | 赴乌克兰途中 | 22-en-route-to-the-ukraine.md | 8.2KB | todo |
| 23 | 初到哈尔科夫 | 23-first-days-in-kharkov.md | 18.4KB | todo |
| 24 | 在苏维埃机构里 | 24-in-soviet-institutions.md | 13.0KB | todo |
| 25 | 流亡者约西夫 | 25-yossif-the-emigrant.md | 13.7KB | todo |
| 26 | 涅斯托尔·马赫诺 | 26-nestor-makhno.md | 11.6KB | todo |
| 27 | 监狱与集中营 | 27-prison-and-concentration-camp.md | 11.5KB | todo |
| 28 | 继续南下 | 28-further-south.md | 4.5KB | todo |
| 29 | 遭蹂躏的法斯托夫 | 29-fastov-the-pogromed.md | 19.0KB | todo |
| 30 | 基辅 | 30-kiev.md | 11.2KB | todo |
| 31 | 各处走访 | 31-in-various-walks.md | 26.3KB | todo |
| 32 | 契卡 | 32-the-cheka.md | 7.4KB | todo |
| 33 | 敖德萨的生活与幻象 | 33-odessa-life-and-vision.md | 26.5KB | todo |
| 34 | 阴郁的人们 | 34-dark-people.md | 14.1KB | todo |
| 35 | 一次布尔什维克审判 | 35-a-bolshevik-trial.md | 6.9KB | todo |
| 36 | 归返彼得格勒 | 36-returning-to-petrograd.md | 14.5KB | todo |
| 37 | 在遥远北方 | 37-in-the-far-north.md | 7.0KB | todo |
| 38 | 1921 年初的日子 | 38-early-days-of-1921.md | 8.4KB | todo |
| 39 | 喀琅施塔得 | 39-kronstadt.md | 20.1KB | todo |
| 40 | 锁链的最后几环 | 40-last-links-in-the-chain.md | 24.1KB | todo |
| 41 | 布尔什维克神话的教训 | 41-the-lessons-of-the-bolshevik-myth.md | 29.8KB | todo |
| 42 | 尾注 | 42-endnotes.md | 3.6KB | todo |

（权威进度以 `translation_queue.csv` 为准）

---

## 运行日志

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
