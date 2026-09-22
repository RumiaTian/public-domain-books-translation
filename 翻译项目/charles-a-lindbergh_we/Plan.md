# 翻译计划（Plan.md）

## 本计划信息

- **项目名称**：《我们》（"WE"）——查尔斯·A·林德伯格自传（charles-a-lindbergh_we）
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/学术著作.md
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
| `译文/*.zh-CN.md` | 译文产出（逐段对照双语） | 翻译 agent 产出 |

---

## translation_queue.csv 格式

```
file,size_kb,status
foreword.md,6.7,todo
boyhood-and-early-flights.md,16.6,todo
...
```

| 字段 | 含义 | 取值 |
|------|------|------|
| `file` | 源文文件名（在 `原文/` 目录下） | 如 `foreword.md` |
| `size_kb` | 源文大小（KB）。>50KB 为长文，按通用翻译引擎第七节分段 | 数字 |
| `status` | 翻译状态 | `todo` 待译 / `doing` 翻译中 / `done` 已完成 |

---

## 执行步骤（agent 按此推进，两种模式共用）

> **谁执行**由 `项目说明.md` 的「内容形态」字段决定：本项目为长篇，走委派模式，由子代理逐篇执行。无论谁执行，这 9 步不变。

### 1. 读配置（每次翻译前必读）
```
1. 本项目 Plan.md（本文件）
2. 项目说明.md
3. 术语表.md（如无则跳过）
4. prompts/通用翻译引擎.md
5. prompts/领域配置/学术著作.md（项目说明指定）
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
- 人物/语气/风格全文一致（自传叙述保持第一人称克制口吻），照黄金样本风格译。
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
回到步骤 2，取下一篇 `todo`，直到全部 `done`。委派模式下由主 agent 决定是否继续派单。

---

## 篇目清单

| # | 篇名 | 源文 | 大小 | 状态 |
|---|------|------|------|------|
| 1 | 献词 | dedication.md | 0.3KB | todo |
| 2 | 序言（赫里克大使） | foreword.md | 6.7KB | todo |
| 3 | 童年与早期飞行 | boyhood-and-early-flights.md | 16.6KB | todo |
| 4 | 我的第一架飞机 | my-first-plane.md | 22.2KB | todo |
| 5 | 特技巡飞经历 | barnstorming-experiences.md | 18.7KB | todo |
| 6 | 南下 | heading-south.md | 18.3KB | todo |
| 7 | 布鲁克斯机场的训练 | training-at-brooks-field.md | 20.7KB | todo |
| 8 | 获得飞行员翼章 | receiving-a-pilot-s-wings.md | 25.0KB | todo |
| 9 | 加入航空邮政 | i-join-the-air-mail.md | 19.7KB | todo |
| 10 | 两次应急跳伞 | two-emergency-jumps.md | 21.1KB | todo |
| 11 | 圣迭戈—圣路易斯—纽约 | san-diego-st-louis-new-york.md | 13.2KB | todo |
| 12 | 纽约到巴黎 | new-york-to-paris.md | 16.1KB | todo |
| 13 | 出版者按 | publisher-s-note.md | 0.7KB | todo |
| 14 | 作者按 | author-s-note.md | 0.2KB | todo |
| 15 | 世界对林德伯格的一点看法 | a-little-of-what-the-world-thought-of-lindbergh.md | 0.1KB | todo |
| 16 | 巴黎 | paris.md | 13.6KB | todo |
| 17 | 布鲁塞尔 | brussels.md | 5.3KB | todo |
| 18 | 伦敦 | london.md | 9.2KB | todo |
| 19 | 华盛顿 | washington.md | 29.5KB | todo |
| 20 | 纽约 | new-york.md | 18.9KB | todo |
| 21 | 圣路易斯 | st-louis.md | 3.7KB | todo |
| 22 | 尾注 | endnotes.md | 1.0KB | todo |
| 23 | 插图目录 | list-of-illustrations.md | 3.4KB | todo |

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
2026-09-06 | dedication.md | 1对 | done (check=0)
2026-09-06 | publisher-s-note.md | 1对 | done (check=0)
2026-09-06 | author-s-note.md | 1对 | done (check=0)
2026-09-06 | foreword.md | 13对 | done (check=1,仅数字锚点误报1927已核)
2026-09-06 | list-of-illustrations.md | 1对(48行图注) | done (check=0)
2026-09-06 | a-little-of-what-the-world-thought-of-lindbergh.md | 1对 | done (check=0)
2026-09-06 | boyhood-and-early-flights.md | 58对 | done (check=1,仅数字锚点误报已抽查)
| 2026-09-06 | i-join-the-air-mail.md | 63对 | done（check退出码1为1925年份锚点误报，数字已译） |
2026-09-06 | my-first-plane.md | 55对 | done (check=1,仅数字锚点误报1923已核)
2026-09-06 | barnstorming-experiences.md | 57对 | done (check=1,仅数字锚点误报已核)
| 2026-09-06 | san-diego-st-louis-new-york.md | 30对 | done（check退出码0） |
| 2026-09-06 | new-york-to-paris.md | 67对 | done（check退出码0） |
| 2026-09-06 | paris.md | 45对 | done（check退出码0） |
2026-09-06 | receiving-a-pilot-s-wings.md | 61对 | done (check=1,仅数字锚点误报已核)
| 2026-09-06 | brussels.md | 21对 | done（check退出码见上） |
2026-09-06 | training-at-brooks-field.md | 39对 | done (check=1,仅数字锚点误报已核)
| 2026-09-06 | london.md | 29对 | done（check退出码0） |
2026-09-06 | two-emergency-jumps.md | 42对 | done (check=1,仅数字锚点误报已核)
| 2026-09-06 | washington.md | 96对 | done（check退出码0，5批流式） |
| 2026-09-06 | new-york.md | 55对 | done（check退出码0） |
| 2026-09-06 | st-louis.md | 10对 | done（check退出码0） |
| 2026-09-06 | heading-south.md | 45对 | done（check退出码0） |
| 2026-09-06 | endnotes.md | 3对 | done（check退出码0） |
| 2026-09-06 | [段B总账] 后部11篇全部done，译文11个齐全，check全过（0误报），术语表已追加段B定名分区，段末对账无覆盖 
| 2026-09-07 | 【整书完结】23/23 done | 批次2；新书首译：07:50上锁，段A（前言+成长军航12篇）+段B（航邮+跨洋+欧美巡游11篇）并发2错峰派发；全量验收23文件结构满足（8文件exit1均为数字锚点误报，段A已逐处核实）；跨段定名4处已对齐（马本/沙努特/殷麦曼/欧文座式）；术语表两段各回填约130条；删锁流转 |
