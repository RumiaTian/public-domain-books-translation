# Harry Harrison《Short Fiction》翻译计划

本文件是本项目的翻译执行入口。任务清单（篇目 + 状态）在同目录的 `translation_queue.csv`，翻译须知在 `术语表.md` + `prompts/` 体系。要推进翻译，读本文件即可，无需手动指定篇名。

---

## 本计划信息

- **项目名称**：harry-harrison_short-fiction
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
| `术语表.md` | 翻译硬约束层（天体名/科幻概念/军衔/度量）。每篇译完补充新词 | agent / 人工 |
| `translation_queue.csv` | 任务队列。每行一篇，`file, size_kb, status` 三列 | 翻译前改 doing，完成后改 done |
| `Plan.md`（本文件） | 执行步骤 + 运行日志 | agent 追加日志 |
| `原文/*.md` | 源文（已从 epub 转换） | 不改 |
| `译文/*.zh-CN.md` | 译文产出（块对照双语） | 翻译 agent 产出 |

---

## translation_queue.csv 字段说明

| 字段 | 含义 | 取值 |
|------|------|------|
| `file` | 源文文件名（在 `原文/` 目录下） | 如 `Navy-Day.md` |
| `size_kb` | 源文大小（KB），>50KB 为长文，按通用翻译引擎第七节分段 | 数字 |
| `status` | 翻译状态 | `todo` 待译 / `doing` 翻译中 / `done` 已完成 |

---

## 执行步骤（agent 按此推进，委派模式由子代理逐篇执行）

> 本项目内容形态为「短篇集」，执行模式为**委派**：主 agent 只当调度员，把每篇的 9 步下沉到一次性子代理执行（见 `WORKFLOW.md`「委派模式调度循环」）。无论谁执行，这 9 步不变。

### 1. 读配置（每次翻译前必读）
```
1. 本项目 Plan.md（本文件）
2. 项目说明.md
3. 术语表.md（硬约束层）
4. prompts/通用翻译引擎.md
5. prompts/领域配置/小说文学.md
6. 译文/ 下任意一篇已完成的 .zh-CN.md（风格黄金样本，无则跳过）
```

### 2. 取任务
读 `translation_queue.csv`，取第一个 `status=todo` 的行。先 `ls 译文/` 检查该篇译文是否已存在：
- 已存在 → 直接改 `done`，跳到步骤 8。
- 不存在 → 把该行 `status` 改为 `doing` 并保存 CSV（委派模式下双写：项目 CSV + 根 `translation_queue.csv`），继续。

### 3. 读源文
读 `原文/对应文件名`。

### 4. 翻译
产出到 `译文/对应文件名去.md加.zh-CN.md`。

**格式**：块对照双语。
```
## 英文标题 / 中文标题

===Original===
英文原文段落（可连续数段）

===Chinese===
中文译文段落

===Original===
...
```

**关键约束**：
- 标记 `===Original===` / `===Chinese===` 独占一行，成对出现。
- 标题写成「英文 / 中文」合并一行，**不加块标记**。
- 块对照粒度：按场景或每 3-6 段一组。
- 逐块对照原文，绝不漏译、不合并段落、不缩写、不总结，尤其结尾别截断。
- 严守术语表：遇表内源词必译为指定译法。新词自行确定统一译法，首次附原文「中文（English）」。
- 人物语气全文一致。1950-60s 黄金时代科幻腔调，对话口语化。
- 文学性优先，避免翻译腔，像中文创作。
- 罗马数字编号、技术缩写、单位符号照搬不译。
- 不使用 emoji，不加元信息头。
- 长文（源文 >50KB，如 The-K-Factor.md）按通用翻译引擎第七节分段处理。

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
| 1 | An Artist's Life | An-Artists-Life.md | 34.8KB | todo |
| 2 | Navy Day | Navy-Day.md | 11.0KB | todo |
| 3 | The Velvet Glove | The-Velvet-Glove.md | 42.6KB | todo |
| 4 | The Repairman | The-Repairman.md | 29.5KB | todo |
| 5 | Arm of the Law | Arm-of-the-Law.md | 35.2KB | todo |
| 6 | The K-Factor | The-K-Factor.md | 55.3KB | todo |
| 7 | Toy Shop | Toy-Shop.md | 10.7KB | todo |
| 8 | Down to Earth | Down-to-Earth.md | 42.6KB | todo |

（共约 261.7KB；详见 `translation_queue.csv`）

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
| 2026-08-13 | Navy-Day (22578B,27对块) | done | exit 0; 委派子代理。首篇黄金样本,定黄金时代纸浆科幻明快腔调。政治讽刺(陆军裁海军)。新词:Dornifier 多恩化器/Mark-1 Debinder 解缚器 等 |
| 2026-08-13 | Toy-Shop (21846B,12对块) | done | exit 0; 委派子代理。神秘玩具火箭。Atomic Wonder Space Wave Tapper=原子奇迹太空波捕捉器。$17.95 保留数字锚点 |
| 2026-08-13 | The-Repairman (58610B,31对块) | done | exit 0; 委派子代理。星际修理工。molecular disruptor=分子分解器/Solar=索拉枪/credit=信用点。新词:hyperspace 超空间/beacon 信标/Spican 斯皮卡星人 |
| 2026-08-13 | An-Artists-Life (69129B,31对块) | done | exit 1=数字锚点误报(31/10000),结构满足; 委派子代理。月球画家辐射绝症。Mare Imbrium 雨海 |
| 2026-08-13 | Arm-of-the-Law (72010B,49对块) | done | exit 1=数字锚点误报(120000/.50/.75),结构满足; 委派子代理。火星警局机器人。Nineport 意译「九港」(描述性地名,非音译)。Chief Craig=克雷格局长 |
| 2026-08-13 | The-Velvet-Glove (85166B,43对块) | done | exit 1=数字锚点误报,结构满足; 委派子代理。失业机器人觉醒。mech=机械人/atomic generator=原子能发电机。Robot Equality Act=机器人平等法案 |
| 2026-08-13 | Down-to-Earth (84487B,36对块) | done | exit 1=数字锚点误报(480000 miles),结构满足; 委派子代理。首次登月/平行宇宙。the Bug=甲虫号。注:原文 tve 系OCR损坏,按语境译 |
| 2026-08-13 | The-K-Factor (111624B,80对块) | done | exit 0; 委派子代理。**55.3KB长文按§7分12场景段连续译出合并**。Societics=社会工程学/k-factor=K因子/Himmel=希梅尔。新词:Kitezh 基捷日(希梅尔首都)/Debir's Postulate 德比尔公设/Beta-13/Linear Logic Language 三L |
| 2026-08-13 | ★全书完 8/8 | — | harry-harrison_short-fiction 全 8 篇译完(100%)。本会话委派译全 8 篇(~261.7KB源文) |
