# 翻译计划（Plan.md）— 蓝色礁湖（The Blue Lagoon）

> 翻译一整本书或多文件内容时的标准模式。填入书名、源文/译文目录、篇目清单（`translation_queue.csv`），即可用通用提示词推进翻译，无需手动指定每个文件。

---

## 本计划信息

- **项目名称**：蓝色礁湖（The Blue Lagoon）
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
| `原文/*.md` | 源文（01–58 数字前缀，顺序=阅读顺序） | 不改 |
| `译文/*.zh-CN.md` | 译文产出（块对照双语） | 翻译 agent 产出 |

---

## translation_queue.csv 格式

```
file,size_kb,status
01-book-i.md,0.0,todo
03-where-the-slush-lamp-burns.md,6.5,todo
...
```

| 字段 | 含义 | 取值 |
|------|------|------|
| `file` | 源文文件名（在 `原文/` 目录下） | 如 `03-where-the-slush-lamp-burns.md` |
| `size_kb` | 源文大小（KB）。>50KB 为长文，按通用翻译引擎第七节分段 | 数字 |
| `status` | 翻译状态 | `todo` 待译 / `doing` 翻译中 / `done` 已完成 |

---

## 执行步骤（agent 按此推进，两种模式共用）

> **谁执行**由 `项目说明.md` 的「内容形态」字段决定（见 `WORKFLOW.md`「判断内容形态」）：本项目为长篇，走**委派模式**，由子代理逐篇执行本流程。

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
- 人物/语气/风格全文一致（文学类尤其重要），照黄金样本风格译；帕迪的爱尔兰方言口吻按术语表策略处理。
- 长文（源文 >50KB）分段处理见通用翻译引擎第七节。

### 5. 自检
- 完整性：源文每一段都在译文 Original 块中出现，末尾无截断。
- 块对称：Original/Chinese 数量相等，每块内段数对应。
- 标题格式：全部「英文 / 中文」合并（章号罗马数字照搬）。
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

共 58 个文件：卷/部隔页 9 个 + 正文章节 48 个 + 插图目录 1 个，合计约 450KB。详见 `translation_queue.csv`。

- **Book I**（01–27）：「诺森伯兰号」航行与失火、帕迪携两童漂流、初上礁岛、帕迪之死。
- **Book II**（28–52）：八年后，迪克与埃米琳长大成人、爱情、婴儿汉纳、气旋、鲨鱼、漂流出海。
- **Book III**（53–57）：莱斯特兰奇寻找孩子，方登船长线索，「拉拉通加号」南下，结尾「永不苏醒浆果」。
- 58：原书插图目录。

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
| 2026-09-06 | 01-book-i.md | done | 题页，仅合并标题，check=0，0 块 |
| 2026-09-06 | 02-part-i.md | done | 题页，仅合并标题，check=0，0 块 |
| 2026-09-06 | 13-part-ii.md | done | 题页，仅合并标题，check=0，0 块 |
| 2026-09-06 | 19-part-iii.md | done | 题页，仅合并标题，check=0，0 块 |
| 2026-09-06 | 28-book-ii.md | done | 题页，仅合并标题，check=0，0 块 |
| 2026-09-06 | 29-part-i-2.md | done | 题页，仅合并标题，check=0，0 块 |
| 2026-09-06 | 39-part-ii-2.md | done | 题页，仅合并标题，check=0，0 块 |
| 2026-09-06 | 53-book-iii.md | done | 题页，仅合并标题，check=0，0 块 |
| 2026-09-06 | 30-under-the-artu-tree.md | done | 3 块，check=0 |
| 2026-09-06 | 31-half-child-half-savage.md | done | 8 块，check=0 |
| 2026-09-06 | 32-the-demon-of-the-reef.md | done | 5 块，check=0 |
| 2026-09-06 | 33-what-beauty-concealed.md | done | 6 块，check=0 |
| 2026-09-06 | 34-the-sound-of-a-drum.md | done | 5 块，check=0 |
| 2026-09-06 | 35-sails-upon-the-sea.md | done | 9 块，check=0 |
| 2026-09-06 | 36-the-schooner.md | done | 7 块，check=0 |
| 2026-09-06 | 37-love-steps-in.md | done | 5 块，check=0 |
| 2026-09-06 | 38-the-sleep-of-paradise.md | done | 2 块，check=0 |
| 2026-09-06 | 40-an-island-honeymoon.md | done | 4 块，check=0 |
| 2026-09-06 | 41-the-vanishing-of-emmeline.md | done | 6 块，check=0 |
| 2026-09-06 | 42-the-vanishing-of-emmeline-continued.md | done | 4 块，check=0 |
| 2026-09-06 | 43-the-newcomer.md | done | 4 块，check=0 |
| 2026-09-06 | 44-hannah.md | done | 6 块，check=0 |
| 2026-09-06 | 45-the-lagoon-of-fire.md | done | 5 块，check=0 |
| 2026-09-06 | 46-the-cyclone.md | done | 6 块，check=0 |
| 2026-09-06 | 47-the-stricken-woods.md | done | 5 块，check=0 |
| 2026-09-06 | 48-a-fallen-idol.md | done | 4 块，check=0 |
| 2026-09-06 | 49-the-expedition.md | done | 11 块，check=0 |
| 2026-09-06 | 50-the-keeper-of-the-lagoon.md | done | 4 块，check=0 |
| 2026-09-06 | 51-the-hand-of-the-sea.md | done | 2 块，check=0 |
| 2026-09-06 | 52-together.md | done | 2 块，check=0 |
| 2026-09-06 | 54-mad-lestrange.md | done | 5 块，check=0 |
| 2026-09-06 | 55-the-secret-of-the-azure.md | done | 6 块，check=0 |
| 2026-09-06 | 01-book-i.md | done | 块数 0，check 退出码 0，译文存在=True |
| 2026-09-06 | 02-part-i.md | done | 块数 0，check 退出码 0，译文存在=True |
| 2026-09-06 | 03-where-the-slush-lamp-burns.md | done | 块数 8，check 退出码 0，译文存在=True |
| 2026-09-06 | 04-under-the-stars.md | done | 块数 12，check 退出码 0，译文存在=True |
| 2026-09-06 | 05-the-shadow-and-the-fire.md | done | 块数 8，check 退出码 0，译文存在=True |
| 2026-09-06 | 06-and-like-a-dream-dissolved.md | done | 块数 10，check 退出码 0，译文存在=True |
| 2026-09-06 | 07-voices-heard-in-the-mist.md | done | 块数 10，check 退出码 0，译文存在=True |
| 2026-09-06 | 08-dawn-on-a-wide-wide-sea.md | done | 块数 14，check 退出码 0，译文存在=True |
| 2026-09-06 | 09-story-of-the-pig-and-the-billy-goat.md | done | 块数 7，check 退出码 0，译文存在=True |
| 2026-09-06 | 10-s-h-e-n-a-n-d-o-a-h.md | done | 块数 14，check 退出码 0，译文存在=True |
| 2026-09-06 | 11-shadows-in-the-moonlight.md | done | 块数 11，check 退出码 0，译文存在=True |
| 2026-09-06 | 12-the-tragedy-of-the-boats.md | done | 块数 7，check 退出码 0，译文存在=True |
| 2026-09-06 | 13-part-ii.md | done | 块数 0，check 退出码 0，译文存在=True |
| 2026-09-06 | 14-the-island.md | done | 块数 6，check 退出码 0，译文存在=True |
| 2026-09-06 | 15-the-lake-of-azure.md | done | 块数 12，check 退出码 0，译文存在=True |
| 2026-09-06 | 16-death-veiled-with-lichen.md | done | 块数 6，check 退出码 0，译文存在=True |
| 2026-09-06 | 17-echoes-of-fairyland.md | done | 块数 7，check 退出码 0，译文存在=True |
| 2026-09-06 | 18-fair-pictures-in-the-blue.md | done | 块数 3，check 退出码 0，译文存在=True |
| 2026-09-06 | 19-part-iii.md | done | 块数 0，check 退出码 0，译文存在=True |
| 2026-09-06 | 20-the-poetry-of-learning.md | done | 块数 18，check 退出码 0，译文存在=True |
| 2026-09-06 | 21-the-devil-s-cask.md | done | 块数 6，check 退出码 0，译文存在=True |
| 2026-09-06 | 22-the-rat-hunt.md | done | 块数 5，check 退出码 0，译文存在=True |
| 2026-09-06 | 23-starlight-on-the-foam.md | done | 块数 6，check 退出码 0，译文存在=True |
| 2026-09-06 | 24-the-dreamer-on-the-reef.md | done | 块数 6，check 退出码 0，译文存在=True |
| 2026-09-06 | 25-the-garland-of-flowers.md | done | 块数 5，check 退出码 0，译文存在=True |
| 2026-09-06 | 26-alone.md | done | 块数 3，check 退出码 0，译文存在=True |
| 2026-09-06 | 27-they-move-away.md | done | 块数 3，check 退出码 0，译文存在=True |
| 2026-09-06 | 56-captain-fountain.md | done | 15 块，check=0 |
| 2026-09-06 | 57-due-south.md | done | 14 块，check=0 |
| 2026-09-06 | 58-list-of-illustrations.md | done | 1 块，check=0 |
| 2026-09-06 | 段B 28–58（31 篇） | done | 全部完成：题页 4 篇 0 块 + 正文 26 篇共 166 块 + 插图目录 1 块；check 全 0；术语表已回填卷二/卷三新定名 |
| 2026-09-08 | 【整书完结】58/58 done | 批次2；首译：08:05上锁；段A（卷一27篇）+段B（卷二三31篇）并发2；全量验收58文件exit 0全过、零可疑；段B对齐段A定名5文件回改重检；两段合计回填百余条术语（永不苏醒浆果/蓝色礁湖等核心意象统一）；56章原书章号排印讹误照搬；删锁流转 |
