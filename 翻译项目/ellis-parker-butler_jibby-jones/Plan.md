# 翻译计划（Plan.md）

---

## 本计划信息

- **项目名称**：ellis-parker-butler_jibby-jones（《吉比·琼斯》）
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
第一章.md,12.3,todo
第二章.md,18.1,todo
...
```

| 字段 | 含义 | 取值 |
|------|------|------|
| `file` | 源文文件名（在 `原文/` 目录下） | 如 `The-Bryd.md` |
| `size_kb` | 源文大小（KB）。>50KB 为长文，按通用翻译引擎第七节分段 | 数字 |
| `status` | 翻译状态 | `todo` 待译 / `doing` 翻译中 / `done` 已完成 |

---

## 执行步骤（agent 按此推进，两种模式共用）

> **谁执行**由 `项目说明.md` 的「内容形态」字段决定（见 `WORKFLOW.md`「判断内容形态」）：委派模式由子代理逐篇执行本流程；连续模式（中篇）由主 agent 自己执行。无论谁执行，这 9 步不变。

### 1. 读配置（每次翻译前必读）
```
1. 本项目 Plan.md（本文件）
2. 项目说明.md
3. 术语表.md（如无则跳过）
4. prompts/通用翻译引擎.md
5. prompts/领域配置/对应领域.md（项目说明指定）
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

| # | 章次 | 篇名 | 源文 | 状态 |
|---|------|------|------|------|
| 1 | I | Oliver Parmenter Jones | oliver-parmenter-jones.md | todo |
| 2 | II | The Pearl-Diggers | the-pearl-diggers.md | todo |
| 3 | III | The Climbing Rabbit | the-climbing-rabbit.md | todo |
| 4 | IV | Do Fish Climb Trees? | do-fish-climb-trees.md | todo |
| 5 | V | The Fishing Prize | the-fishing-prize.md | todo |
| 6 | VI | The Prize-Winner | the-prize-winner.md | todo |
| 7 | VII | The Tough Customer | the-tough-customer.md | todo |
| 8 | VIII | The Redheaded Bandit | the-redheaded-bandit.md | todo |
| 9 | IX | The Abduction of Rover | the-abduction-of-rover.md | todo |
| 10 | X | The Treasure Hunt | the-treasure-hunt.md | todo |
| 11 | XI | Where Is Greenland? | where-is-greenland.md | todo |
| 12 | XII | The Worm Mine | the-worm-mine.md | todo |
| 13 | XIII | The Viking Ship | the-viking-ship.md | todo |
| 14 | XIV | Uncle Beeswax | uncle-beeswax.md | todo |
| 15 | XV | The Grape Tree | the-grape-tree.md | todo |
| 16 | XVI | Congo Magic | congo-magic.md | todo |
| 17 | XVII | Grains of Sand | grains-of-sand.md | todo |
| 18 | XVIII | Pirate's Treasure | pirate-s-treasure.md | todo |
| 19 | XIX | The Tough Customer Appears | the-tough-customer-appears.md | todo |
| 20 | XX | Orlando | orlando.md | todo |
| 21 | XXI | Winged Enemies | winged-enemies.md | todo |
| 22 | XXII | A New Swimming-Hole | a-new-swimming-hole.md | todo |
| 23 | XXIII | Treasure Trove | treasure-trove.md | todo |
| 24 | XXIV | The Treasure | the-treasure.md | todo |

（另：list-of-illustrations.md 为插图清单，不列入翻译队列。）

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
| 2026-09-10 | 全书 24 章 | 整书完结 | 批次4委派模式：10 个并发子代理按阅读顺序分组译完（344KB 连续叙事，组间衔接前章译文尾部）；24/24 done，check_bilingual 结构契约 0 违规（非零退出码均为 1804/1835 年份等数字锚点误报，规则内通过）；组4 子代理中途输出损坏留下 doing 残留，主 agent 验收补收 07 章 + 重派补译 08 章；无失败章节。术语表硬约束全程生效（吉比·琼斯、蜂蜡大叔、红发强盗、凶汉、1804银元）。 |
