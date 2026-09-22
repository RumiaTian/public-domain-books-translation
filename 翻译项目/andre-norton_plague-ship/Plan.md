# 翻译计划（疫船）

## 本计划信息

- **项目名称**：andre-norton_plague-ship
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
01-perfumed-planet.md,18.1,todo
02-rivals.md,19.1,todo
...
```

| 字段 | 含义 | 取值 |
|------|------|------|
| `file` | 源文文件名（在 `原文/` 目录下） | 如 `01-perfumed-planet.md` |
| `size_kb` | 源文大小（KB）。>50KB 为长文，按通用翻译引擎第七节分段 | 数字 |
| `status` | 翻译状态 | `todo` 待译 / `doing` 翻译中 / `done` 已完成 |

---

## 执行步骤（agent 按此推进，两种模式共用）

> **谁执行**由 `项目说明.md` 的「内容形态」字段决定（见 `WORKFLOW.md`「判断内容形态」）：本书为长篇，走委派模式，由子代理逐篇执行本流程。无论谁执行，这 9 步不变。

### 1. 读配置（每次翻译前必读）
```
1. 本项目 Plan.md（本文件）
2. 项目说明.md
3. 术语表.md（如无则跳过）
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
| 1 | I Perfumed Planet | 01-perfumed-planet.md | ~19KB | todo |
| 2 | II Rivals | 02-rivals.md | ~19KB | todo |
| 3 | III Contact at Last | 03-contact-at-last.md | ~19KB | todo |
| 4 | IV Gorp Hunt | 04-gorp-hunt.md | ~18KB | todo |
| 5 | V The Perilous Seas | 05-the-perilous-seas.md | ~18KB | todo |
| 6 | VI Duelist's Challenge | 06-duelist-s-challenge.md | ~19KB | todo |
| 7 | VII Barring Accident | 07-barring-accident.md | ~19KB | todo |
| 8 | VIII Headaches | 08-headaches.md | ~19KB | todo |
| 9 | IX Plague! | 09-plague.md | ~18KB | todo |
| 10 | X E-Stat Landing | 10-e-stat-landing.md | ~19KB | todo |
| 11 | XI Desperate Measures | 11-desperate-measures.md | ~19KB | todo |
| 12 | XII Strange Behavior of a Hoobat | 12-strange-behavior-of-a-hoobat.md | ~19KB | todo |
| 13 | XIII Off the Map | 13-off-the-map.md | ~18KB | todo |
| 14 | XIV Special Mission | 14-special-mission.md | ~19KB | todo |
| 15 | XV Medic Hovan Reports | 15-medic-hovan-reports.md | ~19KB | todo |
| 16 | XVI The Battle of the Video | 16-the-battle-of-the-video.md | ~17KB | todo |
| 17 | XVII In Custody | 17-in-custody.md | ~18KB | todo |
| 18 | XVIII Bargain Concluded | 18-bargain-concluded.md | ~18KB | todo |

（以 `translation_queue.csv` 为准）

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
| 2026-09-09 | 01 Perfumed Planet | done | 段A/批次2 |
| 2026-09-09 | 02 Rivals | done | 段A/批次2 |
| 2026-09-09 | 10 E-Stat Landing | done | 段B/批次2 |
| 2026-09-09 | 03 Contact at Last | done | 段A/批次2 |
| 2026-09-09 | 04 Gorp Hunt | done | 段A/批次2 |
| 2026-09-09 | 05 The Perilous Seas | done | 段A/批次2 |
| 2026-09-09 | 11 Desperate Measures | done | 段B/批次2 |
| 2026-09-09 | 12 Strange Behavior of a Hoobat | done | 段B/批次2 |
| 2026-09-09 | 06 Duelist’s Challenge | done | 段A/批次2 |
| 2026-09-09 | 13 Off the Map | done | 段B/批次2 |
| 2026-09-09 | 07 Barring Accident | done | 段A/批次2 |
| 2026-09-09 | 14 Special Mission | done | 段B/批次2 |
| 2026-09-09 | 08 Headaches | done | 段A/批次2 |
| 2026-09-09 | 15 Medic Hovan Reports | done | 段B/批次2 |
| 2026-09-09 | 09 Plague! | done | 段A/批次2 |
| 2026-09-09 | 16 The Battle of the Video | done | 段B/批次2 |
| 2026-09-09 | 17 In Custody | done | 段B/批次2 |
| 2026-09-09 | 18 Bargain Concluded | done | 段B/批次2 |
| 2026-09-09 | 【整书完结】18/18 done | 批次2；段A（01-09）+段B（10-18）双并发首译，第01章黄金样本开路；全书 check 退出码 0、可疑错配 0；新增定名回填术语表约 120 条（段A 49 + 段B 71），「太阳女王号」系列首定译名；并发写冲突 2 次均经写后核验恢复；删锁流转 | 
