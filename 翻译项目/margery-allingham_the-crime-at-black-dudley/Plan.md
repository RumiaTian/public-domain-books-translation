# 翻译计划（Plan.md）— 《布莱克·达德利罪案》

## 本计划信息

- **项目名称**：《布莱克·达德利罪案》（玛格丽·阿林厄姆《The Crime at Black Dudley》）
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
01-candlelight.md,16.6,todo
02-the-ritual-of-the-dagger.md,14.5,todo
...
```

| 字段 | 含义 | 取值 |
|------|------|------|
| `file` | 源文文件名（在 `原文/` 目录下） | 如 `01-candlelight.md` |
| `size_kb` | 源文大小（KB）。>50KB 为长文，按通用翻译引擎第七节分段 | 数字 |
| `status` | 翻译状态 | `todo` 待译 / `doing` 翻译中 / `done` 已完成 |

> **排序说明**：原书章节用罗马数字编号（I–XXIX），文件名按章名生成、不含阿拉伯数字，直接字母序会乱排。故已为每个文件加 `NN-` 前缀（00 献词，01–29 各章），保证 `gen_project_files.py` 的自然排序即为阅读顺序。

---

## 执行步骤（委派模式：子代理逐篇执行）

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
- 人物/语气/风格全文一致（文学类尤其重要）：保持坎皮恩装傻充愣的假高音腔与 1920 年代英国上流社会口吻；米德太太的萨福克乡下口音用带乡土味、略不规范的口语体现。
- 章题合并为「英文 / 中文」并保留罗马数字序号（如「I Candlelight / 第一章 烛光」）。
- **重大悬念**：怀亚特·皮特里为真正行凶者（末章揭示），译到第 29 章前不可在叙述中泄露。
- 各章均 <50KB，无须分段。

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

> 共 30 个文件：1 篇献词 + 29 章（罗马数字 I–XXIX），依原书 spine 顺序。文件名前缀即阅读顺序。附中文篇名供参考，实际文件名以原文目录为准。

| # | 罗马数字 | 中文篇名 | 源文 | 大小 | 状态 |
|---|----------|----------|------|------|------|
| 0 | — | 献词 | 00-dedication.md | 0.0KB | todo |
| 1 | I | 烛光 | 01-candlelight.md | 16.6KB | todo |
| 2 | II | 匕首仪式 | 02-the-ritual-of-the-dagger.md | 14.5KB | todo |
| 3 | III | 车库里 | 03-in-the-garage.md | 11.2KB | todo |
| 4 | IV | 谋杀 | 04-murder.md | 16.1KB | todo |
| 5 | V | 面具 | 05-the-mask.md | 5.1KB | todo |
| 6 | VI | 坎皮恩先生大闹一场 | 06-mr-campion-brings-the-house-down.md | 7.5KB | todo |
| 7 | VII | 清晨五点 | 07-five-o-clock-in-the-morning.md | 9.9KB | todo |
| 8 | VIII | 公开开战 | 08-open-warfare.md | 11.6KB | todo |
| 9 | IX | 克里斯·肯尼迪只得分 | 09-chris-kennedy-scores-a-try-only.md | 13.3KB | todo |
| 10 | X | 急性子的阿伯肖先生 | 10-the-impetuous-mr-abbershaw.md | 8.2KB | todo |
| 11 | XI | 一种解释 | 11-one-explanation.md | 16.8KB | todo |
| 12 | XII | 「再说……」坎皮恩先生道 | 12-furthermore-said-mr-campion.md | 10.8KB | todo |
| 13 | XIII | 阿伯肖发飙 | 13-abbershaw-sees-red.md | 9.0KB | todo |
| 14 | XIV | 阿伯肖得到面谈机会 | 14-abbershaw-gets-his-interview.md | 9.9KB | todo |
| 15 | XV | 阿伯肖医生的推论 | 15-doctor-abbershaw-s-deductions.md | 17.0KB | todo |
| 16 | XVI | 好斗的米德太太 | 16-the-militant-mrs-meade.md | 17.4KB | todo |
| 17 | XVII | 入夜 | 17-in-the-evening.md | 16.5KB | todo |
| 18 | XVIII | 肯尼迪先生的会议 | 18-mr-kennedy-s-council.md | 14.1KB | todo |
| 19 | XIX | 坎皮恩先生的戏法 | 19-mr-campion-s-conjuring-trick.md | 13.9KB | todo |
| 20 | XX | 一网打尽 | 20-the-roundup.md | 21.1KB | todo |
| 21 | XXI | 本杰明·道利什的视角 | 21-the-point-of-view-of-benjamin-dawlish.md | 10.3KB | todo |
| 22 | XXII | 至暗时刻 | 22-the-darkest-hour.md | 12.7KB | todo |
| 23 | XXIII | 一处失策 | 23-an-error-in-taste.md | 12.1KB | todo |
| 24 | XXIV | 布莱克·达德利的尾声 | 24-the-last-of-black-dudley.md | 15.0KB | todo |
| 25 | XXV | 沃特先生解说 | 25-mr-watt-explains.md | 13.1KB | todo |
| 26 | XXVI | 「找出那个女人」 | 26-cherchez-la-femme.md | 14.2KB | todo |
| 27 | XXVII | 夜行 | 27-a-journey-by-night.md | 12.3KB | todo |
| 28 | XXVIII | 医生该不该说？ | 28-should-a-doctor-tell.md | 15.4KB | todo |
| 29 | XXIX | 最后一章 | 29-the-last-chapter.md | 20.2KB | todo |

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-09-21 | 00-dedication.md | done | 批次1直启，check_bilingual PASS（1 对块） |
| 2026-09-21 | 01-candlelight.md | done | 批次1直启，check_bilingual PASS（26 对块） |
| 2026-09-21 | 02-the-ritual-of-the-dagger.md | done | 批次1直启，check_bilingual PASS（16 对块） |
| 2026-09-21 | 03-in-the-garage.md | done | 批次1直启，check_bilingual PASS（20 对块） |
| 2026-09-21 | 04-murder.md | done | 批次1直启，check_bilingual PASS（31 对块） |
| 2026-09-21 | 05-the-mask.md | done | 批次1直启，check_bilingual PASS（11 对块） |
| 2026-09-21 | 06-mr-campion-brings-the-house-down.md | done | 批次1直启，check_bilingual PASS（16 对块） |
| 2026-09-21 | 07-five-o-clock-in-the-morning.md | done | 批次1直启，check_bilingual PASS（10 对块） |
| 2026-09-21 | 08-open-warfare.md | done | 批次1直启，check_bilingual PASS（18 对块） |
| 2026-09-21 | 09-chris-kennedy-scores-a-try-only.md | done | 批次1直启，check_bilingual PASS（24 对块） |
| 2026-09-21 | 10-the-impetuous-mr-abbershaw.md | done | 批次1直启，check_bilingual PASS（11 对块） |
| 2026-09-21 | 11-one-explanation.md | done | 批次1直启，check_bilingual PASS（23 对块） |
| 2026-09-21 | 12-furthermore-said-mr-campion.md | done | 批次1直启，check_bilingual PASS（15 对块） |
| 2026-09-21 | 13-abbershaw-sees-red.md | done | 批次1直启，check_bilingual PASS（22 对块） |
| 2026-09-21 | 14-abbershaw-gets-his-interview.md | done | 批次1直启，check_bilingual PASS（16 对块） |
| 2026-09-21 | 15-doctor-abbershaw-s-deductions.md | done | 批次1直启，check_bilingual PASS（28 对块） |
| 2026-09-21 | 16-the-militant-mrs-meade.md | done | 批次1直启，check_bilingual PASS（19 对块） |
| 2026-09-21 | 17-in-the-evening.md | done | 批次1直启，check_bilingual PASS（50 对块） |
| 2026-09-21 | 18-mr-kennedy-s-council.md | done | 批次1直启，check_bilingual PASS（16 对块） |
| 2026-09-21 | 19-mr-campion-s-conjuring-trick.md | done | 批次1直启，check_bilingual PASS（22 对块） |
| 2026-09-21 | 20-the-roundup.md | done | 批次1直启，check_bilingual PASS（27 对块） |
| 2026-09-21 | 21-the-point-of-view-of-benjamin-dawlish.md | done | 批次1直启，check_bilingual PASS（11 对块） |
| 2026-09-21 | 22-the-darkest-hour.md | done | 批次1直启，check_bilingual PASS（24 对块） |
| 2026-09-21 | 23-an-error-in-taste.md | done | 批次1直启，check_bilingual PASS（21 对块） |
| 2026-09-21 | 24-the-last-of-black-dudley.md | done | 批次1直启，check_bilingual PASS（20 对块） |
| 2026-09-21 | 25-mr-watt-explains.md | done | 批次1直启，check_bilingual PASS（22 对块） |
| 2026-09-21 | 26-cherchez-la-femme.md | done | 批次1直启，check_bilingual PASS（23 对块） |
| 2026-09-21 | 27-a-journey-by-night.md | done | 批次1直启，check_bilingual PASS（18 对块） |
| 2026-09-21 | 28-should-a-doctor-tell.md | done | 批次1直启，check_bilingual PASS（22 对块） |
| 2026-09-21 | 29-the-last-chapter.md | done | 批次1直启，check_bilingual PASS（23 对块） |
