# 翻译计划（Plan.md）

> An Outback Marriage 翻译计划。按 `prompts/翻译计划模板.md` 建立，执行步骤与运行日志见下方。

---

## 本计划信息

- **项目名称**：banjo-paterson_an-outback-marriage（An Outback Marriage，Banjo Paterson，1906）
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
01-in-the-club.md,13.0,todo
02-a-dinner-for-five.md,8.0,todo
...
```

| 字段 | 含义 | 取值 |
|------|------|------|
| `file` | 源文文件名（在 `原文/` 目录下） | 如 `01-in-the-club.md` |
| `size_kb` | 源文大小（KB）。>50KB 为长文，按通用翻译引擎第七节分段 | 数字 |
| `status` | 翻译状态 | `todo` 待译 / `doing` 翻译中 / `done` 已完成 |

---

## 执行步骤（agent 按此推进，两种模式共用）

> **谁执行**由 `项目说明.md` 的「内容形态」字段决定（见 `WORKFLOW.md`「判断内容形态」）：本项目为长篇，走**委派模式**，由子代理逐篇执行本流程。

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

| # | 篇名 | 源文 | 大小 | 状态 |
|---|------|------|------|------|
| 1 | I In the Club | 01-in-the-club.md | 13KB | todo |
| 2 | II A Dinner for Five | 02-a-dinner-for-five.md | 8KB | todo |
| 3 | III In Push Society | 03-in-push-society.md | 16.5KB | todo |
| 4 | IV The Old Station | 04-the-old-station.md | 14.1KB | todo |
| 5 | V The Coming of the Heiress | 05-the-coming-of-the-heiress.md | 17.5KB | todo |
| 6 | VI A Coach Accident | 06-a-coach-accident.md | 19.2KB | todo |
| 7 | VII Mr. Blake's Relations | 07-mr-blake-s-relations.md | 5.6KB | todo |
| 8 | VIII At the Homestead | 08-at-the-homestead.md | 10.4KB | todo |
| 9 | IX Some Visitors | 09-some-visitors.md | 10.3KB | todo |
| 10 | X A Lawyer in the Bush | 10-a-lawyer-in-the-bush.md | 9.5KB | todo |
| 11 | XI A Walk in the Moonlight | 11-a-walk-in-the-moonlight.md | 13.1KB | todo |
| 12 | XII Mr. Blake Breaks His Engagement | 12-mr-blake-breaks-his-engagement.md | 5.6KB | todo |
| 13 | XIII The Rivals | 13-the-rivals.md | 8.2KB | todo |
| 14 | XIV Red Mick and His Sheep Dogs | 14-red-mick-and-his-sheep-dogs.md | 21.4KB | todo |
| 15 | XV A Proposal and Its Results | 15-a-proposal-and-its-results.md | 10.3KB | todo |
| 16 | XVI The Road to No Man's Land | 16-the-road-to-no-man-s-land.md | 21.4KB | todo |
| 17 | XVII Considine | 17-considine.md | 11.5KB | todo |
| 18 | XVIII The Wild Cattle | 18-the-wild-cattle.md | 17KB | todo |
| 19 | XIX A Chance Encounter | 19-a-chance-encounter.md | 18.8KB | todo |
| 20 | XX A Consultation at Kiley's | 20-a-consultation-at-kiley-s.md | 11.1KB | todo |
| 21 | XXI No Compromise | 21-no-compromise.md | 12.8KB | todo |
| 22 | XXII A Nurse and Her Assistant | 22-a-nurse-and-her-assistant.md | 8.7KB | todo |
| 23 | XXIII Hugh Goes in Search | 23-hugh-goes-in-search.md | 8.2KB | todo |
| 24 | XXIV The Second Search for Considine | 24-the-second-search-for-considine.md | 15.7KB | todo |
| 25 | XXV In the Buffalo Camp | 25-in-the-buffalo-camp.md | 9.2KB | todo |
| 26 | XXVI The Saving of Considine | 26-the-saving-of-considine.md | 22.1KB | todo |
| 27 | XXVII The Real Certificate | 27-the-real-certificate.md | 6.4KB | todo |
| 28 | XXVIII A Legal Battle | 28-a-legal-battle.md | 10.1KB | todo |
| 29 | XXIX Races and a Win | 29-races-and-a-win.md | 11.6KB | todo |
| 30 | Endnotes | 30-endnotes.md | 0.1KB | todo |

（以 `translation_queue.csv` 为准）

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |

## 2026-09-10 批次4 运行日志
- 全书 30 篇（含尾注）全部完成，11 组子代理并发产出。
- 结构校验全本通过；遗留告警均为数字/货币/年份锚点误报（100度/1861/10-/£50/2.30），逐条人工确认。
- 定名统一：加万·布莱克→加文·布莱克(9处)、塔隆→塔龙(8处)；其余各术语组自始遵守建库预置表，零冲突。
- 术语表已回填补充定名表；认领锁已删除，本书流转出批次4。
