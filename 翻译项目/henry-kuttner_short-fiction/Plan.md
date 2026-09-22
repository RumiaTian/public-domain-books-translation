# 亨利·库特纳短篇小说集 翻译计划（Plan.md）

本文件是本项目的翻译执行入口。任务清单（篇目 + 状态）在同目录的 `translation_queue.csv`，翻译须知在 `术语表.md` + `prompts/` 体系。要推进翻译，读本文件即可，无需手动指定篇名。

---

## 本计划信息

- **项目名称**：henry-kuttner_short-fiction（《亨利·库特纳短篇小说集》）
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
| `术语表.md` | 翻译硬约束层（天体名/神话典故/外星种族/科幻概念/军衔/度量）。每篇译完补充新词 | agent / 人工 |
| `translation_queue.csv` | 任务队列。每行一篇，`file, size_kb, status` 三列 | 翻译前改 doing，完成后改 done |
| `Plan.md`（本文件） | 执行步骤 + 运行日志 | agent 追加日志 |
| `原文/*.md` | 源文（已从 epub 转换） | 不改 |
| `译文/*.zh-CN.md` | 译文产出（块对照双语） | 翻译 agent 产出 |

---

## translation_queue.csv 字段说明

| 字段 | 含义 | 取值 |
|------|------|------|
| `file` | 源文文件名（在 `原文/` 目录下） | 如 `the-eyes-of-thar.md` |
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
产出到 `译文/对应文件名去.md加.zh-CN.md`。双语对照格式、标记规则、完整性禁令见 `prompts/通用翻译引擎.md` 第五、六节。

**本流程专有提醒**：
- 逐块对照原文，绝不漏译、不合并段落、不缩写、不总结，尤其结尾别截断。
- 严守术语表：遇表内源词必译为指定译法。新词自行确定统一译法，首次附原文「中文（English）」，译后回填术语表。
- 各篇题材差异大，译文基调随篇调整（哥特恐怖偏书面压抑、太空冒险明快、黑色幽默诙谐），照黄金样本风格译。
- 人造/外星语言片段保留原文转写，首现括注中文大意。
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
- ② 根 `translation_queue.csv` 中 `henry-kuttner_short-fiction,<本篇名>` 那一行（见 `WORKFLOW.md`「双写状态」）。

### 8. 追加日志
在本文件「运行日志」追加一行。

### 9. 循环
回到步骤 2，取下一篇 `todo`，直到全部 `done`。委派模式下由主 agent 决定是否继续派单。

---

## 篇目清单

| # | 篇名 | 源文 | 大小 | 状态 |
|---|------|------|------|------|
| 1 | The Secret of Kralitz（克拉利茨之谜） | the-secret-of-kralitz.md | 15.7KB | todo |
| 2 | The Crystal Circe（水晶喀耳刻） | the-crystal-circe.md | 5.1KB | todo |
| 3 | War-Gods of the Void（虚空战神） | war-gods-of-the-void.md | 15.8KB | todo |
| 4 | Thunder in the Void（虚空之雷） | thunder-in-the-void.md | 2.6KB | todo |
| 5 | Crypt-City of the Deathless One（不死者之城） | crypt-city-of-the-deathless-one.md | 17.3KB | todo |
| 6 | The Eyes of Thar（塔尔之眼） | the-eyes-of-thar.md | 38.1KB | todo |
| 7 | What Hath Me（何降临于我） | what-hath-me.md | 13.2KB | todo |
| 8 | Dream's End（梦的尽头） | dream-s-end.md | 28.1KB | todo |
| 9 | Don't Look Now（此刻别看） | don-t-look-now.md | 28.2KB | todo |
| 10 | The Ego Machine（自我机器） | the-ego-machine.md | 23.8KB | todo |
| 11 | Where the World Is Quiet（静谧之地） | where-the-world-is-quiet.md | 38.5KB | todo |

（详细状态以 `translation_queue.csv` 为准）

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-08-14 | — | 建项目 | 从 待翻译/henry-kuttner_short-fiction.epub 提取 11 篇正文（共 252KB）、通读定调（科幻/奇幻/恐怖短篇集→小说文学→委派）、建术语表初版（含克苏鲁/希腊/北欧/印加神话专名与跨篇天体/技术词）、生成队列 |
| 2026-08-14 | Crypt-City of the Deathless One（不死者之城） | done | 译文 36.1KB（原文 17.3KB）；块对照 28 对，check_bilingual 通过（标记成对/标题合并/0 错配）；守术语表，新词（黑森林/古族/扎尔诺/诺克托利花/银瘟/『猎人号』/威拉德博士/卡弗等）首现附原文，古语 *Ylgana! Vo m’trana al-khron* 与 *Sfant!* 保留转写并注大意 |
| 2026-08-14 | Don't Look Now（此刻别看） | done | 译文 57.6KB（原文 28.2KB）；块对照 28 对，check_bilingual 通过（标记成对/标题合并/0 错配）；守术语表（火星人/火星/莱曼/褐衣男人），新词（柯林斯酒/催眠后暗示/超声波洗涤剂/红外胶片/卡岑贾默顽童/《反常之魔》/弗兰克·劳埃德·赖特/福特/斯皮策/《纽约时报》等）首现附原文 |
| 2026-08-14 | dream-s-end (28.1KB回填) | done | exit 0; 前次中断遗留、校验通过后回填 |
| 2026-08-14 | the-crystal-circe (5.1KB) | done | exit 0 |
| 2026-08-14 | the-ego-machine/the-secret-of-kralitz/thunder-in-the-void (23.8+15.7+2.6KB) | done ×3 | exit 0 |
| 2026-08-14 | the-eyes-of-thar/war-gods-of-the-void/what-hath-me (38.1+15.8+13.2KB) | done ×3 | exit 0 |
| 2026-08-14 | where-the-world-is-quiet (38.5KB) | done | exit 0 | **全书 11/11 译完** |
