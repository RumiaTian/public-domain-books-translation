# 翻译计划（Plan.md）

---

## 本计划信息

- **项目名称**：anonymous_gudrun_mary-pickering-nichols（《古德伦》Gudrun 英译韵文本，Mary Pickering Nichols 译，1889）
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
01-preface.md,5.8,todo
04-how-hagen-was-carried-off-by-the-griffin.md,18.5,todo
...
```

| 字段 | 含义 | 取值 |
|------|------|------|
| `file` | 源文文件名（在 `原文/` 目录下） | 如 `01-preface.md` |
| `size_kb` | 源文大小（KB）。>50KB 为长文，按通用翻译引擎第七节分段 | 数字 |
| `status` | 翻译状态 | `todo` 待译 / `doing` 翻译中 / `done` 已完成 |

---

## 执行步骤（agent 按此推进，两种模式共用）

> **谁执行**由 `项目说明.md` 的「内容形态」字段决定：本项目为**长篇 → 委派模式**，每篇的 9 步由一次性子代理执行。

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
- 本书为**韵诗**：诗节按语义分组对照，保留分行；章首「Tale + 罗马数字照搬 + 标题意译 + 散文提要」结构不变。
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

共 35 件：01 前言 + 02 人名表 + 03 地名表 + 04~35 为 Tale I~XXXII。明细由 `translation_queue.csv` 管理（35 行，全 todo），文件名数字前缀即阅读顺序。

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
| 2026-10-17 | 03-names-of-places.md | done（check_bilingual 退出码 0） | 地名表 34 条定名（新定：巴利安/巴利根、卡拉迪、卡西安等），已同步术语表；U+FEFF 34 处照录保留 |
| 2026-10-15 | 01-preface.md | done（check_bilingual 退出码 0） | 前言 5.8KB，12 段逐段成对（12 对 Original/Chinese，0 可疑错配），12 处 U+FEFF 隐形字符原样照录；术语表全部命中（古德伦/尼伯龙根/哈根/希尔达/卡尔·巴奇/中古高地德语/斯卡尔徳等），CSV 双写 done |
| 2026-10-15 | 02-names-of-persons.md（人名表） | done（check_bilingual 退出码 0） | 23 条目按语义分 4 对块对称无漏译；21 个定名与术语表完全一致（术语表已预登记，无新增）；23 处 U+FEFF 照录保留；两位 Hilda 同译希尔达靠释义区分；CSV 双写 done |
| 2026-10-17 | 06-how-hagen-sailed-to-his-home.md | done（check_bilingual 退出码 0） | 第三诗章（Tale III）韵诗 37 节按节分块 + 散文提要，共 38 对 Original/Chinese 对称无漏译、每节 4 行分行保留；人名地名全按术语表（哈根/西格班德/乌特/加拉迪/伊瑟兰/狮鹫等，首现附原文）；源文 1 处 U+FEFF（诗节 29「yearning—」行）照录保留，提取残留空行按语义合并为诗节；项目 CSV 06 行置 done（根目录 CSV 未动，交 refresh_progress.py 重建） |
| 2026-10-15 | 05-how-hagen-slew-the-griffin.md（Tale II 哈根如何诛杀狮鹫） | done（check_bilingual 退出码 0） | 13.4KB 韵诗 94 节逐节成对 + 散文提要 = 95 对 Original/Chinese，0 可疑错配、末节无截断，诗行四行结构保留；本篇源文无 U+FEFF/U+00A0（已核）；术语全按术语表（哈根/狮鹫/幼狮鹫/西格班德/卡拉迪/加拉迪 Garadé/萨尔梅，岩窟统一），章号体例「Tale II / 第二诗章」合并单行；项目 CSV 05 行置 done（根目录 CSV 未动，交 refresh_progress.py 重建） |
| 2026-10-15 | 04-how-hagen-was-carried-off-by-the-griffin.md（Tale I 哈根如何被狮鹫掳走） | done（check_bilingual 退出码 0，0 可疑错配） | 18.5KB 韵诗 132 节逐节成对 + 散文提要 = 133 对 Original/Chinese，每节译文保留四行分行、末节无截断；4 处 U+FEFF（行内破折号前）照录保留，提取残留空行按语义合并为诗节；术语全按术语表（西格班德/乌特/格尔/哈根/狮鹫/爱尔兰/挪威/苏格兰，首现附原文），章号体例「Tale I / 第一诗章」合并单行；项目 CSV 04 行置 done（根目录 CSV 未动，交 refresh_progress.py 重建） |
| 2026-10-15 | 07-how-hagen-was-met-by-his-father-and-mother.md（Tale IV 哈根如何与父母相会） | done（check_bilingual 退出码 0，0 可疑错配） | 14.7KB 韵诗 106 节逐节成对 + 散文提要 = 107 对 Original/Chinese，每节译文保留四行分行、末节无截断；源文隐形字符照录保留（U+FEFF 1 处：诗节 22「living—」；U+200A 1 处：诗节 104 引号内），提取残留空行按语义合并为诗节；术语全按术语表（哈根/希尔达/乌特/西格班德/加拉迪/巴利安/伊瑟兰/瓦莱斯，首现附原文），pilgrims 从 06 定名「朝圣的旅人」（4 处统一），cave 从 05 定名「岩窟」，绰号「诸王中的魔王」2 处统一；项目 CSV 07 行置 done（根目录 CSV 未动，交 refresh_progress.py 重建） |
| 2026-10-15 | 09-how-sweetly-horant-sang.md（Tale VI 霍兰特唱得何等甜美） | done（check_bilingual 退出码 0，0 可疑错配） | 19.0KB 韵诗 136 节逐节成对 + 散文提要 = 137 对 Original/Chinese，每节译文保留四行分行、末节无截断；3 处 U+FEFF（诗节 65/104/119 行内破折号前）照录保留、无 U+00A0，提取残留空行按语义合并为诗节；术语全按术语表（霍兰特/莫伦克/希尔达/黑特尔/哈根/弗鲁特/瓦特 Wâ-te/丹麦兰/阿米莱 Amilé/黑格林人，首现附原文；wild Hagen 统一「暴烈的哈根」、chamberlain 统一「内侍」、bower 统一「闺阁」、queenly 统一「王后般」），章号体例「Tale VI / 第六诗章」合并单行；项目 CSV 09 行置 done（根目录 CSV 未动，交 refresh_progress.py 重建） |
| 2026-10-15 | 08-how-w-te-was-sent-to-ireland-as-a-suitor.md（Tale V 瓦特如何奉命前往爱尔兰求亲） | done（check_bilingual 退出码 0，0 可疑错配） | 46KB 全书最长诗章之一：Tale V 韵诗 168 节逐节成对 + 散文提要 = 169 对 Original/Chinese，每节译文四行分行保留、末节无截断；5 处 U+FEFF（行内破折号前）照录保留、无 U+00A0，提取残留空行按语义合并为诗节（每节 4 诗行＝8 半行，诗节 141 首行为提取时未拆分的整行，已按 4 诗行正确重组）；术语全按术语表（瓦特/霍兰特/弗鲁特/黑特尔/莫伦克/伊罗尔德/丹麦兰/施图尔姆兰/奥特兰/弗里西亚/尼夫兰/坎帕蒂勒/巴利安/坎帕利亚/阿拉比/阿巴利等，首现附原文；wild Hagen 统一「暴烈的哈根」、bower 统一「闺阁」、queenly 统一「王后般」，与 04-09 章体例一致），章号体例「Tale V / 第五诗章」合并单行；项目 CSV 08 行置 done（根目录 CSV 未动，交 refresh_progress.py 重建） |
| 2026-10-15 | 12-how-gudrun-was-sought-by-siegfried.md（Tale IX 西格弗里德如何求娶古德伦） | done（check_bilingual 退出码 0，0 可疑错配） | 6.6KB 短章：Tale IX 韵诗 48 节逐节成对 + 散文提要 = 49 对 Original/Chinese，每节译文保留四行分行、末节无截断；本篇源文无 U+FEFF/U+00A0（已核），提取残留空行经 Gutenberg 原书（46109-h）对照验证诗节边界后按语义合并（印刷本每节 4 长行 aabb 韵、提取在半行处断开，本项目按 4 短行块对照体例处理）；术语全按术语表（西格弗里德/古德伦/奥特温/伊罗尔德/施图尔姆兰/尼夫兰/吉弗斯/奥特兰/丹麦兰/阿尔扎比 Alzabé/伊卡利亚/黑格林人/赫尔维克，首现附原文；新定名：维加莱斯 Wigaleis；wild Hagen 统一「暴烈的哈根」、queenly 统一「王后般」，与 04-09 章体例一致），章号体例「Tale IX / 第九诗章」合并单行；项目 CSV 12 行置 done（根目录 CSV 未动，交 refresh_progress.py 重建） |
| 2026-10-15 | 10-how-the-maidens-came-to-see-the-ship-and-were-carried-to-hettel-s-kingdom.md（Tale VII 少女们如何来看船并被载往黑特尔的王国） | done（check_bilingual 退出码 0，0 可疑错配） | 13.1KB 韵诗 94 节逐节成对 + 散文提要 = 95 对 Original/Chinese，每节译文保留四行分行、末节无截断；4 处 U+FEFF（诗节 47/83 行内破折号前各 2 处）照录保留、无 U+00A0，提取残留空行按语义合并为诗节，原文行前导空格逐字照录；术语全按术语表（瓦特/莫伦克/弗鲁特/伊罗尔德/希尔德堡/黑特尔/哈根/希尔达/黑格林人/巴利安/奥特兰/弗里西亚/施图尔姆兰 Sturmisch/瓦尔河 Waalisch/狮鹫/马克，首现附原文；wild Hagen 统一「暴烈的哈根」、queenly 统一「王后般」，与 04-09 章体例一致），章号体例「Tale VII / 第七诗章」合并单行；项目 CSV 10 行置 done（根目录 CSV 未动，交 refresh_progress.py 重建） |
| 2026-10-15 | 11-how-hagen-followed-his-daughter.md（Tale VIII 哈根如何追赶他的女儿） | done（check_bilingual 退出码 0，0 可疑错配） | 20.9KB 韵诗 152 节逐节成对 + 散文提要 = 153 对 Original/Chinese，每节译文保留四行分行、末节无截断；14 处 U+FEFF（行内破折号前）照录保留、无 U+00A0，提取残留空行按语义合并为诗节；诗节 124 首行为提取时未拆分的整行（As were the guests of Hagen…），已按半行正确重组（同 08 章诗节 141 先例）；术语全按术语表（哈根/霍兰特/莫伦克/伊罗尔德/黑特尔/瓦特 Wâ-te/弗鲁特/希尔达/希尔德堡/丹麦兰/丹麦/爱尔兰/奥特兰/施图尔姆兰/瓦尔河/巴利安/黑格林人，首现附原文；wild Hagen 统一「暴烈的哈根」、pilgrims 统一「朝圣的旅人」、"of kings the Devil" 从 07 章定名「诸王中的魔王」、queenly 统一「王后般」），章号体例「Tale VIII / 第八诗章」合并单行；项目 CSV 11 行置 done（根目录 CSV 未动，交 refresh_progress.py 重建） |
| 2026-10-15 | 14-how-herwic-sent-to-seek-gudrun-and-how-hartmut-came-himself.md（Tale XI 赫尔维克如何遣使求娶古德伦、哈特穆特如何亲自前来） | done（check_bilingual 退出码 0，0 可疑错配） | 3.8KB 短章：Tale XI 韵诗 26 节逐节成对 + 散文提要 = 27 对 Original/Chinese，每节译文保留四行分行、末节无截断；诗节边界经逐节韵脚核验（year/hear、youthful/truthful、ready/steady 等 26 组，104 半行 = 13 印刷诗节之半）；本篇源文无 U+FEFF/U+00A0（已核），提取残留空行按语义合并为诗节，原文行前导空格逐字照录（含诗节 2「Often his worth was spoken」行首空格）；术语全按术语表（赫尔维克/古德伦/哈特穆特/黑特尔/希尔达/格尔林德/西兰/诺曼底/黑格林人，首现附原文；she-devil 定名「老女魔」），章号体例「Tale XI / 第十一诗章」合并单行；项目 CSV 14 行置 done（根目录 CSV 未动，交 refresh_progress.py 重建） |
| 2026-10-15 | 15-how-herwic-made-war-on-hettel-and-how-gudrun-was-betrothed-to-him.md（Tale XII 赫尔维克如何向黑特尔兴兵，古德伦如何与他订婚） | done（check_bilingual 退出码 0，0 可疑错配） | 10.5KB 韵诗 76 块（每块 4 半行，两块合一印刷诗节，同 12 章体例）逐块成对 + 散文提要 = 77 对 Original/Chinese，每块译文保留四行分行、末块无截断；1 处 U+FEFF（诗节 8「told me—」行内破折号前）照录保留、无 U+00A0，提取残留空行按语义合并、原文行前导空格逐字照录；源文标题两行断开（## Tale / XII …）已合并单行；中文对话用「」角引号（同 04-11 章体例），引号结构与源文逐处镜像（源文 2 处多段对白首段不闭合，译文 16 开 14 闭与之精确对应）；术语全按术语表（赫尔维克/黑特尔/古德伦/哈特穆特/希尔达/黑格林人/施图尔姆兰/伊罗尔德/奥特兰/加莱斯 Galeis/莫伦克/瓦莱斯/阿尔扎比 Alzabie/丹麦，首现附原文；queenly 统一「王后般」），章号体例「Tale XII / 第十二诗章」合并单行；项目 CSV 15 行置 done（根目录 CSV 未动，交 refresh_progress.py 重建） |
| 2026-10-15 | 13-how-hartmut-sent-to-woo-gudrun.md（Tale X 哈特穆特如何遣使向古德伦求亲） | done（check_bilingual 退出码 0，0 可疑错配） | 8.4KB 短章：Tale X 韵诗 60 节逐节成对 + 散文提要 = 61 对 Original/Chinese，每节译文保留四行分行、末节无截断；1 处 U+FEFF（诗节 57「truly say」与破折号之间）照录保留、无 U+00A0，提取残留空行按语义合并为诗节（Original 块 240 诗行经脚本逐字比对与源文一致，含行前导空格）；术语全按术语表（哈特穆特/路德维希/格尔林德/诺曼底/黑特尔/古德伦/希尔达/霍兰特/哈根/丹麦兰/黑格林人，首现附原文；新定名：卡迪根 Cardigan、奥托 Otto，已同步术语表；herald 统一「信使」、errand-bearer/messenger 统一「使者」、queenly 统一「王后般」，与 04-12 章体例一致；中文对话用「」角引号，引号开合与源文逐节镜像），章号体例「Tale X / 第十诗章」合并单行（源文标题两行断开 ## Tale / X … 已合并）；项目 CSV 13 行置 done（根目录 CSV 未动，交 refresh_progress.py 重建） |
| 2026-10-15 | 17-how-hettel-sent-tidings-from-herwic-s-land.md（Tale XIV 黑特尔如何从赫尔维克的国土传来音讯） | done（check_bilingual 退出码 0，0 可疑错配） | 7.9KB 短章：Tale XIV 韵诗 56 块（每块 4 半行，同 12/15 章体例）逐块成对 + 散文提要 = 57 对 Original/Chinese，每块译文保留四行分行、末块无截断；2 处 U+FEFF（诗节 23「selfsame mind」、诗节 27「give you freely」行内破折号前）照录保留且译文镜像同位保留、无 U+00A0，提取残留空行按语义合并、Original 块 224 诗行经脚本逐字比对与源文一致（含行前导空格）；术语全按术语表（黑特尔/希尔达/古德伦/西格弗里德/哈特穆特/赫尔维克/格尔林德/路德维希/瓦特 Wâ-te/弗鲁特/黑格林人/诺曼底/施图尔姆兰/阿尔扎比/摩尔兰/西兰/卡拉迪/奥特兰，首现附原文；新定名：士瓦本 Suabia，已同步术语表；the Moor 从 12 章定名「那摩尔人」、she-devil 从 14 章定名「老女魔」、errand-bearers 统一「使者」，queenly 未现；中文对话用「」角引号，引号开合与源文逐块镜像（各 8 开 8 闭）），章号体例「Tale XIV / 第十四诗章」合并单行（源文标题两行断开 ## Tale / XIV … 已合并）；项目 CSV 17 行置 done（根目录 CSV 未动，交 refresh_progress.py 重建） |
| 2026-10-15 | 16-how-siegfried-made-war-against-herwic.md（Tale XIII 西格弗里德如何向赫尔维克兴兵） | done（check_bilingual 退出码 0，0 可疑错配） | 15.6KB 韵诗 114 块（每块 4 半行，两块合一印刷诗节，同 15 章体例）逐块成对 + 散文提要 = 115 对 Original/Chinese，每块译文保留四行分行、末块无截断；4 处 U+FEFF（诗节 15「weeping—」、诗节 30「brought—」、诗节 56「warriors—/gainsaid—」行内破折号前）照录保留、无 U+00A0，提取残留空行按语义合并、原文行前导空格逐字照录；57 印刷诗节边界经逐节 aabb 韵脚核验（men/seen、bidden/hidden 等 57 组）；中文对话用「」角引号，引号开合与源文逐处镜像（源文 3 处多段对白前段不闭合，译文 13 开 10 闭精确对应）；术语全按术语表（西格弗里德/古德伦/赫尔维克/黑特尔/希尔达/瓦特 Wâ-te/莫伦克/霍兰特/伊罗尔德/奥特温/摩尔兰/西兰/阿尔扎比/阿巴基/施图尔姆兰/丹麦兰/奥特兰/黑格林人/卡拉迪/维加莱斯/弗鲁特，首现附原文；queenly 统一「王后般」、herald 统一「信使」，与 04-15 章体例一致），章号体例「Tale XIII / 第十三诗章」合并单行（源文标题两行断开已合并）；项目 CSV 16 行置 done（根目录 CSV 未动，交 refresh_progress.py 重建） |
| 2026-10-15 | 18-how-hartmut-carried-away-gudrun.md（Tale XV 哈特穆特如何掳走古德伦） | done（check_bilingual 退出码 0，0 可疑错配） | 15.9KB 韵诗 114 块（每块 4 半行，两块合一印刷诗节，同 12/15/16 章体例）逐块成对 + 散文提要 = 115 对 Original/Chinese，每块译文保留四行分行、末块无截断；10 处 U+FEFF（行内破折号前及诗节 57 武尔彭沙洲夹注前后）照录保留、无 U+00A0，提取残留空行按语义合并为诗节；诗节 22 次块首行系提取时未拆分的整行（He then ran forth…treated），经韵脚核验（went/sent、treated/greeted）按半行正确重组为 4 诗行（同 08 章诗节 141、11 章诗节 124 先例）；Original 块 457 诗行经脚本逐字比对与源文一致（含行前导空格与 U+FEFF）；术语全按术语表（哈特穆特/古德伦/赫尔维克/路德维希/希尔达/黑特尔/黑格林人/马特兰/维加莱斯 Wigaleis/瓦特 Wâ-te/瓦尔河 Waalisch/希尔德堡/武尔彭沙洲，首现附原文；诺曼底等通行译名不附注；herald 统一「信使」、errand-bearer 统一「使者」、queenly 统一「王后般」，与 04-17 章体例一致），中文对话用「」角引号，引号开合与源文逐块镜像（源文 20 开 16 闭，译文精确对应），章号体例「Tale XV / 第十五诗章」合并单行（源文标题两行断开已合并）；项目 CSV 18 行置 done（根目录 CSV 未动，交 refresh_progress.py 重建） |
| 2026-10-15 | 20-how-hettel-came-to-the-wulpensand-in-search-of-his-daughter.md（Tale XVII 黑特尔如何来到武尔彭沙洲寻找他的女儿） | done（check_bilingual 退出码 0，0 可疑错配） | 9.2KB 短章：Tale XVII 韵诗 66 块（每块 4 半行，两块合一印刷诗节，同 12/15/16/18 章体例）逐块成对 + 散文提要 = 67 对 Original/Chinese，每块译文保留四行分行、末块无截断；1 处 U+FEFF（诗节 26「they strove upon the sand—」行内破折号前）照录保留、无 U+00A0，提取残留空行按语义合并为诗节；Original 块 264 诗行经脚本逐字比对与源文一致（含行前导空格与 U+FEFF）；术语全按术语表（黑特尔/古德伦/哈特穆特/路德维希/赫尔维克/武尔彭沙洲/黑格林人/瓦特 Wâ-te/马特兰/伊罗尔德/阿巴利 Abalie/莫伦克/奥特温/摩尔兰/西格弗里德/弗鲁特/西兰，首现附原文；诺曼底/丹麦等通行译名不附注；Normans 统一「诺曼人」、pilgrims 从 06 章定名「朝圣的旅人」），中文对话用「」角引号，引号开合与源文逐块镜像（各 3 开 3 闭），章号体例「Tale XVII / 第十七诗章」合并单行（源文标题两行断开已合并）；项目 CSV 20 行置 done（根目录 CSV 未动，交 refresh_progress.py 重建） |
| 2026-10-15 | 21-how-ludwig-slew-hettel-and-stole-away-in-the-night.md（Tale XVIII 路德维希如何诛杀黑特尔，并趁夜潜逃） | done（check_bilingual 退出码 0，0 可疑错配） | 10.9KB 韵诗 78 块（每块 4 半行，两块合一印刷诗节，同 12/15/16/17/18/20 章体例）逐块成对 + 散文提要 = 79 对 Original/Chinese，每块译文保留四行分行、末块无截断；39 印刷诗节 312 半行边界经逐节 aabb 韵脚核验（bore/more、showing/growing 等 39 组）；诗节 32 首行系提取时未拆分的整行（Then asked the warrior Irold, if foes who there lay dead），经韵脚核验（dead/feed、hovered/uncovered）按半行正确重组为 4 诗行（同 08/11/18 章先例）；5 处 U+FEFF（行内破折号前）照录保留、无 U+00A0（源文空白残留行均为普通空格，按语义合并入诗节），Original 块 313 行经脚本逐字比对与源文一致（含行前导空格与 U+FEFF）；术语全按术语表（路德维希/黑特尔/古德伦/瓦特 Wâ-te/霍兰特/赫尔维克/奥特温/哈特穆特/弗鲁特 Fru-te/莫伦克/伊罗尔德/希尔达/马特兰/武尔彭沙洲/奥特兰/瓦尔河 Waal/施图尔姆兰 Sturmisch/摩尔兰/黑格林人，首现附原文；诺曼人等通行译名不附注；grim old Wâ-te 从 18 章定名「狰狞的老瓦特」；sackbut 新定「弯号」附原文、hide 译「海得」），中文对话用「」角引号，引号开合与源文逐处镜像（源文 11 开 9 闭——弗鲁特跨诗节对白逐节重开引号不闭合，译文 11 开 9 闭精确对应），章号体例「Tale XVIII / 第十八诗章」合并单行（源文标题两行断开 ## Tale / XVIII … 已合并）；项目 CSV 21 行置 done（根目录 CSV 未动，交 refresh_progress.py 重建） |
| 2026-10-15 | 19-how-hilda-sent-to-hettel-and-herwic-to-ask-their-help-against-hartmut.md（Tale XVI 希尔达如何遣人向黑特尔与赫尔维克求援抗击哈特穆特） | done（check_bilingual 退出码 0，0 可疑错配） | 10.5KB：Tale XVI 韵诗 74 块（每块 4 半行，同 12/15/16/18 章体例）逐块成对 + 散文提要 = 75 对 Original/Chinese，每块译文保留四行分行、末块无截断；隐形字符照录：2 处 U+FEFF（块 63「pilgrims—/true—」破折号前）+ 1 处 U+200A（块 33 引号后“ ’Tis”行内），按 18 章体例仅在 Original 块照录、中文不镜像，无 U+00A0（已核）；提取残留空行按语义合并为诗节，Original 块 296 诗行经脚本逐字比对与源文一致（含行前导空格）；术语全按术语表（希尔达/黑特尔/赫尔维克/哈特穆特/古德伦/西格弗里德/霍兰特/瓦特 Wâ-te/弗鲁特 Fru-te/伊罗尔德/路德维希/哈根/摩尔兰/阿巴基 Abakia/施图尔姆兰/卡拉迪/阿尔扎比/黑格林人，首现附原文；herald 统一「信使」、errand-bearers 统一「使者」、pilgrims 统一「朝圣的旅人」、queenly 统一「王后般」，与 04-18 章体例一致），中文对话用「」角引号，引号开合与源文逐块镜像（源文 24 开 20 闭，译文精确对应；含块 42「逼近！逼近！」行内引号对），章号体例「Tale XVI / 第十六诗章」合并单行（源文标题两行断开已合并）；项目 CSV 19 行置 done（根目录 CSV 未动，交 refresh_progress.py 重建） |
| 2026-10-15 | 22-how-the-hegelings-went-home-to-their-own-land.md（Tale XIX 黑格林人如何归返故土） | done（check_bilingual 退出码 0，0 可疑错配） | 9.0KB 短章：Tale XIX 韵诗 64 块（每块 4 半行，两块合一印刷诗节，同 12/15/16/18/20/21 章体例）逐块成对 + 散文提要 = 65 对 Original/Chinese，每块译文保留四行分行、末块无截断；32 印刷诗节 256 半行边界经逐节 aabb 韵脚核验（left/bereft、bringing/wringing 等 32 组）；隐形字符照录：1 处 U+FEFF（块 56「heeded—」破折号前）+ 1 处 U+200A（块 27 引号后“ ’Tis”行内），按 18/19 章体例仅在 Original 块照录、中文不镜像，无 U+00A0（已核）；提取残留空行按语义合并为诗节，Original 块 257 行经脚本逐字比对与源文一致（含行前导空格与隐形字符）；术语全按术语表（黑格林人/希尔达/黑特尔/奥特温/奥特兰/古德伦/瓦特 Wâ-te/武尔彭沙洲/施图尔姆兰 Sturmisch 与 Sturmland/哈特穆特/路德维希/哈根/赫尔维克/西兰/马特兰/弗里西亚/莫伦克/瓦莱斯/弗鲁特 Fru-te/西格弗里德/摩尔兰，首现附原文；诺曼人等通行译名不附注；brave old Wâ-te 从 21 章定名「剽悍的老瓦特」、pilgrims 从 06 章定名「朝圣的旅人」、马克 mark 按语境意译），中文对话用「」角引号，引号开合与源文逐块镜像（源文 23 开 22 闭——赫尔维克跨块对白首段不闭合，译文精确对应；内层引号 ‘The church of Wulpensand’ 用『武尔彭沙洲教堂』镜像），章号体例「Tale XIX / 第十九诗章」合并单行（源文标题两行断开 ## Tale / XIX … 已合并）；项目 CSV 22 行置 done（根目录 CSV 未动，交 refresh_progress.py 重建） |
| 2026-10-15 | 23-how-hartmut-went-home-to-normandy.md（Tale XX 哈特穆特如何回到诺曼底家中） | done（check_bilingual 退出码 0，0 可疑错配） | 24.8KB：Tale XX 韵诗 180 块（每块 4 半行，两块合一印刷诗节，同 12/15/16/17/18/20/21 章体例）逐块成对 + 散文提要 = 181 对 Original/Chinese，每块译文保留四行分行、末块无截断；90 印刷诗节 720 半行边界经块首缩进与 aabb 韵脚核验（fared/shared、listen/hasten 等）；隐形字符照录：3 处 U+FEFF（块 23「fair;—」、块 121「true—」、块 165「again—」破折号前）+ 2 处 U+200A（块 57/138 引号后“ ’Twas/’Twere”行内），按 18/19 章体例仅在 Original 块照录、中文不镜像，无 U+00A0（已核）；Original 块 721 行（含提要 1 行）经脚本逐字比对与源文一致（含行前导空格与隐形字符）；术语全按术语表（哈特穆特/古德伦/格尔林德/奥特龙/希尔达/黑特尔/路德维希/哈根/赫加特 Hergart/加利西亚/葡萄牙/爱尔兰/诺曼人/黑格林人/狮鹫 griffin，首现附原文；诺曼底等通行译名不附注；she-devil 从 14 章定名「老女魔」、queenly 统一「王后般」、errand-bearers 统一「使者」，与 04-21 章体例一致），中文对话用「」角引号，引号开合与源文逐块镜像（源文含 4 处多段对白重开引号不闭合——块 35/37、56/57、95/97、138/139 及 162/163/165 三连开，译文精确对应），章号体例「Tale XX / 第二十诗章」合并单行（源文标题两行断开 ## Tale / XX … 已合并）；项目 CSV 23 行置 done（根目录 CSV 未动，交 refresh_progress.py 重建） |
| 2026-10-15 | 24-how-gudrun-must-wash-clothes-on-the-beach.md（Tale XXI 古德伦如何不得不在海滩上洗衣）| done（check_bilingual 退出码 0，0 可疑错配）| 8.3KB：Tale XXI 韵诗 60 块（每块 4 半行，同 12/15/16/17/18/20/21 章体例）逐块成对 + 散文提要 = 61 对 Original/Chinese，每块译文保留四行分行、末块无截断；3 处 U+FEFF（块 39「rue it—/known—」、块 59「lasted—」行内破折号前）照录保留、无 U+00A0（已核），提取残留空行按语义合并为诗节，Original 块 241 行经脚本逐字比对与源文一致（含行前导空格、弯引号与 U+FEFF）；术语全按术语表（古德伦/哈特穆特/奥特龙/格尔林德/希尔德堡/希尔达/路德维希/赫尔维克/诺曼底，首现附原文；she-devil 从 14 章定名「老女魔」、old she-wolf 新译「老母狼」仅 1 处），中文对话用「」角引号，引号开合与源文逐处镜像（源文 19 开 14 闭——古德伦/哈特穆特/希尔堡跨诗节对白逐节重开引号不闭合，译文 19 开 14 闭精确对应），章号体例「Tale XXI / 第二十一诗章」合并单行（源文标题两行断开已合并）；项目 CSV 24 行置 done（根目录 CSV 未动，交 refresh_progress.py 重建） |
| 2026-10-15 | 26-how-hilda-s-warriors-landed-in-sight-of-hartmut-s-kingdom.md（Tale XXIII 希尔达的武士们如何在望见哈特穆特王国之处登陆）| done（check_bilingual 退出码 0，0 可疑错配）| 6.5KB 短章：Tale XXIII 韵诗 46 块（每块 4 半行，同 12/15/16/17/18/20/21/24 章体例）逐块成对 + 散文提要 = 47 对 Original/Chinese，每块译文保留四行分行、末块无截断；隐形字符照录：1 处 U+200A（块 29 引号后“ ’Tis”行内），按 18/19/22 章体例仅在 Original 块照录、中文不镜像，无 U+FEFF/U+00A0（已核），提取残留空行按语义合并为诗节，Original 块 185 行（含提要 1 行）经脚本逐字比对与源文一致（含行前导空格、弯引号与 U+200A）；术语全按术语表（赫尔维克/奥特温/古德伦/伊罗尔德 Irold/瓦特 Wâ-te/弗鲁特 Fru-te/希尔达/哈特穆特/路德维希/奥特兰/黑格林人 Hegeling/古尔斯特雷德 Gulstred，首现附原文；诺曼底等通行译名不附注；wise old Wâ-te 依 21/22 章体例译「睿智的老瓦特」、kinsfolk 从 22/23 章定名「亲友」、kingly 依 queenly「王后般」体例译「王者般的」），中文对话用「」角引号，引号开合与源文逐块镜像（源文 15 开 12 闭——瓦特跨块对白 1 处重开、奥特温嘱托对白 3 连开不闭合，译文 15 开 12 闭精确对应），章号体例「Tale XXIII / 第二十三诗章」合并单行（源文标题两行断开 ## Tale / XXIII … 已合并）；项目 CSV 26 行置 done（根目录 CSV 未动，交 refresh_progress.py 重建）|
| 2026-10-15 | 27-how-their-coming-was-made-known-to-gudrun.md（Tale XXIV 他们的到来如何传报给古德伦）| done（check_bilingual 退出码 0，0 可疑错配）| 11.8KB：Tale XXIV 韵诗 84 块（每块 4 半行，两块合一印刷诗节，同 12/15/16/17/18/20/21/23/24/26 章体例）逐块成对 + 散文提要 = 85 对 Original/Chinese，每块译文保留四行分行、末块无截断；42 印刷诗节 336 半行边界经逐节 aabb 韵脚核验（hear/cheer、swan/man、fell/tell、spake/take、comes/homes、near/here、go/know、twit/slight、brink/think 等 42 组）；隐形字符照录：4 处 U+FEFF（块 36「telling—」、块 40「longing—/lend me—」、块 57「wearing—」行内破折号前）按 18/19 章体例仅在 Original 块照录、中文不镜像，无 U+00A0/U+200A（已核），提取残留空行按语义合并为诗节，Original 块 337 行（含提要 1 行）经脚本逐字比对与源文一致（含行前导空格、弯引号与 U+FEFF）；术语全按术语表（古德伦/希尔德堡/希尔达/奥特温/奥特兰/赫尔维克/莫伦克/伊罗尔德/黑特尔/霍兰特/黑格林人/哈特穆特/瓦特 Wâ-te/施图尔姆兰/弗鲁特 Fru-te/格尔林德/路德维希/加利西亚，首现附原文；丹麦等通行译名不附注；she-wolf 从 24 章定名「母狼」、queenly 统一「王后般」、Norman 作定语统一「诺曼人」，与 04-26 章体例一致），中文对话用「」角引号，引号开合与源文逐块镜像（源文 30 开 29 闭——格尔林德对白块 54/56 跨块重开引号不闭合、天鹅对白多处跨块开而不闭，译文 30 开 29 闭精确对应；块 80「这件事，」行内双引号对镜像），章号体例「Tale XXIV / 第二十四诗章」合并单行（源文标题两行断开 ## Tale / XXIV … 已合并）；项目 CSV 27 行置 done（根目录 CSV 未动，交 refresh_progress.py 重建）|
| 2026-10-15 | 25-how-hilda-made-war-to-bring-back-her-daughter.md（Tale XXII 希尔达如何兴兵夺回她的女儿）| done（check_bilingual 退出码 0，0 可疑错配）| 19.5KB：Tale XXII 韵诗 142 块（每块 4 半行，两块合一印刷诗节，同 12/15/16/17/18/20/21/24 章体例）逐块成对 + 散文提要 = 143 对 Original/Chinese，每块译文保留四行分行、末块无截断；隐形字符照录：4 处 U+FEFF（块 16「dearer—」、块 29「say—」、块 31「queen—」、块 60「fighters—」破折号前）+ 1 处 U+200A（块 119 引号后“ ’Twas”行内），按 18/19 章体例仅在 Original 块照录、中文不镜像，无 U+00A0（已核）；提取残留空行按语义合并为诗节，Original 块 569 行（含提要 1 行）经脚本逐字比对与源文一致（含行前导空格与隐形字符）；术语全按术语表（希尔达/哈特穆特/黑特尔/赫尔维克/古德伦/霍兰特/莫伦克/伊罗尔德/弗鲁特 Fru-te/瓦特 Wâ-te/格尔林德/赫加特 Hergart/奥特温/黑格林人/诺曼底/武尔彭沙洲/吉弗斯 Givers/丹麦兰/瓦尔河 Waalisch 与 Waal/荷尔斯泰因/施图尔姆兰/马特兰/卡拉迪/摩尔兰/丹麦，首现附原文且与提要去重；新定名：边地侯爵 margrave、磁石 loadstone、驯鹰官 falconer，Northland 从 08 章定名「北方」、miles 从前章「英里」、cup-bearer 从前章「司酒官」、marches 从前章「边地」、queenly 统一「王后般」，与 04-24 章体例一致），中文对话用「」角引号，引号开合与源文逐块镜像（源文 24 开 16 闭，译文 24 开 16 闭精确对应，含块 121 瓦特行内引号对「静候时来运转，」），章号体例「Tale XXII / 第二十二诗章」合并单行（源文标题两行断开 ## Tale / XXII … 已合并）；项目 CSV 25 行置 done（根目录 CSV 未动，交 refresh_progress.py 重建）|
| 2026-10-15 | 29-how-the-hegelings-landed-near-ludwig-s-castle.md（Tale XXVI 黑格林人如何在路德维希的城堡附近登陆）| done（check_bilingual 退出码 0，0 可疑错配）| 8.7KB：Tale XXVI 韵诗 62 块（每块 4 半行，两块合一印刷诗节，同 12/15/16/17/18/20/21/22/23/24/25/26/27 章体例）逐块成对 + 散文提要 = 63 对 Original/Chinese，每块译文保留四行分行、末块无截断；31 印刷诗节 248 半行边界经逐块 aabb 韵脚核验（untold/hold、standing/landing、gave/bereave、see/be、spread/speed 等）；本篇源文无 U+FEFF/U+00A0/U+200A（已核），提取残留空行按语义合并为诗节，Original 块 249 行（含提要 1 行）经脚本逐字比对与源文一致（含行前导空格与弯引号）；术语全按术语表（赫尔维克/奥特温/古德伦/希尔德堡/瓦特 Wâ-te/弗鲁特 Fru-te/希尔达/格尔林德/路德维希/哈特穆特/黑格林人，首现附原文且与提要去重；爱尔兰/诺曼底/丹麦等通行译名不附注；Norman 作定语统一「诺曼人」、the aged/old Wâ-te 统一「年迈的瓦特/老瓦特」、queenly 统一「王后般的」、pilgrims 从 06 章定名「朝圣的旅人」、warder 统一「守望者」，与 04-27 章体例一致），中文对话用「」角引号，引号开合与源文逐块镜像（源文 25 开 21 闭——奥特温/瓦特对白多处跨块重开引号不闭合，译文 25 开 21 闭精确对应），章号体例「Tale XXVI / 第二十六诗章」合并单行（源文标题两行断开 ## Tale / XXVI … 已合并）；项目 CSV 29 行置 done（根目录 CSV 未动，交 refresh_progress.py 重建）|
| 2026-10-15 | 28-how-herwic-and-ortwin-found-gudrun.md（Tale XXV 赫尔维克与奥特温如何找到古德伦）| done（check_bilingual 退出码 0，0 可疑错配）| 35.5KB 长章：Tale XXV 韵诗 256 块（每块 4 半行，两块合一印刷诗节，同 12/15/16/17/18/20/21/22/23/24/25/26/27 章体例）逐块成对 + 散文提要 = 257 对 Original/Chinese，每块译文保留四行分行、末块无截断；隐形字符照录：3 处 U+FEFF（块 74「given—」、块 116「treading—/pledge you—」破折号前）+ 1 处 U+200A（块 207 引号后“ ’Tis”行内），按 18/19 章体例仅在 Original 块照录、中文不镜像，无 U+00A0（已核）；提取残留空行按语义合并为诗节，Original 块 1025 行（含提要 1 行）经脚本逐字比对与源文一致（含行前导空格与隐形字符）；术语全按术语表（赫尔维克/奥特温/古德伦/希尔德堡/格尔林德/哈特穆特/奥特龙/路德维希/哈根/希尔达/黑格林人/西兰/奥特兰/阿巴利 Abalie/诺曼底/爱尔兰/阿拉伯，首现附原文且与提要去重；she-devil 从 14 章定名「老女魔」、wolfish 译「恶狼般的」、wild Hagen 统一「暴烈的哈根」、queenly 统一「王后般」、Norman 作定语统一「诺曼人」、hide 从 21 章定名「海得」、chamberlain 从 09 章统一「内侍」、cup-bearer 从 25 章统一「司酒官」、bower 统一「闺阁」，与 04-27 章体例一致），中文对话用「」角引号，引号开合与源文逐块镜像（源文 102 开 90 闭——含古德伦假死试探、格尔林德对白、哈特穆特求亲等多处跨块重开引号不闭合及块 27/28 行内「早安」「晚安」引号对，译文 102 开 90 闭精确对应），章号体例「Tale XXV / 第二十五诗章」合并单行（源文标题两行断开 ## Tale / XXV … 已合并）；项目 CSV 28 行置 done（根目录 CSV 未动，交 refresh_progress.py 重建）|
| 2026-10-15 | 30-how-ludwig-and-hartmut-met-the-hegelings.md（Tale XXVII 路德维希与哈特穆特如何迎战黑格林人）| done（check_bilingual 退出码 0，0 可疑错配）| 20.4KB：Tale XXVII 韵诗 150 块（每块 4 半行，两块合一印刷诗节，同 12/15/16/17/18/20/21/22/23/24/25/26/27/29 章体例）逐块成对 + 散文提要 = 151 对 Original/Chinese，每块译文保留四行分行、末块无截断；75 印刷诗节 600 半行边界经逐节 aabb 韵脚核验（men/seen、below them/show them、dear/near、bringing/flinging、wife/life、willing/dealing 等 75 组）；隐形字符照录：3 处 U+FEFF（块 6「blazoned—」、块 17「coming—/true—」破折号前）+ 2 处 U+200A（块 79/111 引号后“ ’Tis”行内），按 18/19 章体例仅在 Original 块照录、中文不镜像，无 U+00A0（已核）；提取残留空行按语义合并为诗节，Original 块 601 行（含提要 1 行）经脚本逐字比对与源文一致（含行前导空格、弯引号与隐形字符）；术语全按术语表（哈特穆特/路德维希/格尔林德/赫尔维克/黑格林人/瓦特 Wâ-te/施图尔姆兰 Sturmland 与 Sturmisch/奥特兰/奥特温/卡拉迪 Karadé/摩尔兰/霍兰特/弗鲁特 Fru-te/瓦莱斯/莫伦克/弗里西亚/荷尔斯泰因/希尔达/西兰/伊罗尔德/古德伦/奥特龙/黑特尔/武尔彭沙洲，首现附原文且与提要去重；丹麦/诺曼底/诺曼人等通行译名不附注；pilgrims 从 06 章定名「朝圣的旅人」、年迈的瓦特从 27 章体例），中文对话用「」角引号，引号开合与源文逐块镜像（源文 36 开 20 闭——哈特穆特报旗对白跨诗节逐节重开引号不闭合（9 开 1 闭）、格尔林德/老王后/赫尔维克/路德维希对白多处重开、块 43-44 王后告诫诗节源文未闭合，译文 36 开 20 闭精确对应；块 24/45/111/114 行内引号对镜像），章号体例「Tale XXVII / 第二十七诗章」合并单行（源文标题两行断开 ## Tale / XXVII … 已合并）；项目 CSV 30 行置 done（根目录 CSV 未动，交 refresh_progress.py 重建）|
| 2026-10-15 | 31-how-herwic-slew-ludwig.md（Tale XXVIII 赫尔维克如何诛杀路德维希）| done（check_bilingual 退出码 0，0 可疑错配）| 14.7KB：Tale XXVIII 韵诗 106 块（每块 4 半行，两块合一印刷诗节，同 12/15/16/17/18/20/21/22/23/24/25/26/27/29/30 章体例）逐块成对 + 散文提要 = 107 对 Original/Chinese，每块译文保留四行分行、末块无截断；53 印刷诗节 424 半行边界经逐节 aabb 韵脚核验（me/see、maiden/laden、bear it/share it、shield/wield、anew/flew、gate/great、do/hew、maid/shed、gone/own、sprang/rang、blow/low 等 53 组）；隐形字符照录：1 处 U+FEFF（块 73「rascal—」破折号前）+ 1 处 U+200A（块 19 引号后“ ’Tis”行内），按 18/19 章体例仅在 Original 块照录、中文不镜像，无 U+00A0（已核）；提取残留空行按语义合并为诗节，Original 块 425 行（含提要 1 行）经脚本逐字比对与源文一致（含行前导空格、弯引号与隐形字符）；术语全按术语表（赫尔维克/古德伦/路德维希/格尔林德/哈特穆特/瓦特 Wâ-te/弗鲁特 Fru-te/摩尔兰/奥特温/黑格林人 Hegeling/希尔达/奥特龙/西兰 Sealands/哈根，首现附原文且与提要去重；诺曼人等通行译名不附注；grim/狰狞沿 18 章「狰狞的老瓦特」、wild with anger 统一「怒不可遏」、queenly 统一「王后般」、Norman 作定语统一「诺曼人」，与 04-30 章体例一致），中文对话用「」角引号，引号开合与源文逐块镜像（源文 34 开 23 闭——哈特穆特城下长篇军情对白跨诗节逐节重开引号不闭合、奥特龙恳求与古德伦隔窗相认对白多处重开，译文 34 开 23 闭精确对应；块 23/49/81/89 行内「他说，」引号对镜像），章号体例「Tale XXVIII / 第二十八诗章」合并单行（源文标题两行断开 ## Tale / XXVIII … 已合并）；项目 CSV 31 行置 done（根目录 CSV 未动，交 refresh_progress.py 重建）|
| 2026-10-15 | 32-how-hartmut-was-taken-prisoner.md（Tale XXIX 哈特穆特如何被俘）| done（check_bilingual 退出码 0，0 可疑错配）| 18.4KB：Tale XXIX 韵诗 134 块（每块 4 半行，两块合一印刷诗节，同 12/15/16/17/18/20/21/22/23/24/25/26/27/29/30/31 章体例）逐块成对 + 散文提要 = 135 对 Original/Chinese，每块译文保留四行分行、末块无截断；67 印刷诗节 536 半行边界经逐节 aabb 韵脚核验（hall/fall、weeping/reaping、room/come、child/willed、told/hold、gate/hate、spake/take、teaches/riches 等 67 组）；隐形字符照录：3 处 U+FEFF（诗节 23「look—」、诗节 41「castle—」「Kassiane—」破折号前）按 18/19 章体例仅在 Original 块照录、中文不镜像，无 U+00A0/U+200A（已核）；提取残留空行按语义合并为诗节，Original 块 537 行（含提要 1 行）经脚本逐字比对与源文一致（含行前导空格与 U+FEFF）；术语全按术语表（瓦特/哈特穆特/黑格林人/奥特龙/古德伦/格尔林德/霍兰特/希尔达/伊罗尔德/赫尔维克/奥特温/奥特兰/莫伦克/弗鲁特 Fru-te/赫加特 Hergart/黑特尔/路德维希/西格弗里德/摩尔兰/卡拉迪 Karadie/卡西安 Kassiane 与 Kassian/施图尔姆兰 Sturmisch，首现附原文且与提要去重；丹麦/诺曼底/诺曼人等通行译名不附注；新定名：撒克逊 Saxon，已同步术语表；she-devil 从 14 章定名「老女魔」、queenly 统一「王后般的」、warder 从 26 章定名「守望者」、Norman 作定语统一「诺曼人」，与 04-31 章体例一致），中文对话用「」角引号，引号开合与源文逐块镜像（源文 42 开 38 闭——古德伦宽恕赫加特对白、弗鲁特谏焚城堡对白、瓦特答哈特穆特求释对白多处跨块重开引号不闭合，译文 42 开 38 闭精确对应），章号体例「Tale XXIX / 第二十九诗章」合并单行（源文标题两行断开 ## Tale / XXIX … 已合并）；项目 CSV 32 行置 done（根目录 CSV 未动，交 refresh_progress.py 重建）|
| 2026-10-15 | 33-how-gudrun-was-brought-home-to-hilda.md（Tale XXX 古德伦如何被迎回希尔达家中）| done（check_bilingual 退出码 0，0 可疑错配）| 29.2KB：Tale XXX 韵诗 212 块（每块 4 半行，两块合一印刷诗节，同 12/15/16/17/18/20/21/22/23/24/25/26/27/29/30/31/32 章体例）逐块成对 + 散文提要 = 213 对 Original/Chinese，每块译文保留四行分行、末块无截断；106 印刷诗节 848 半行边界经逐节 aabb 韵脚核验（way/sea…leaving/giving、good/mood、say/day…gladdened/saddened、band/land…better/fetter 等组）；诗节 56 第 7 半行系提取时未拆分的整行（Than now they shared so freely: that this should be…），经韵脚核验（found/owned、given/striven）按半行正确重组为 4 诗行（同 08/11/18/21 章先例）；隐形字符照录：10 处 U+FEFF（块 5「hastened—/say—」、块 6「kingdom—」、块 53「feel—」、块 68「sorrowed—/gave him—」、块 70「forget—」、块 78「swear it—」、块 124「love her—」、块 191「fight—」破折号前），按 18/19 章体例仅在 Original 块照录、中文不镜像，无 U+00A0/U+200A（已核）；提取残留空行按语义合并为诗节，Original 块 849 行（含提要 1 行）经脚本逐字比对与源文一致（含行前导空格与 U+FEFF）；术语全按术语表（古德伦/希尔达/哈特穆特/奥特龙/奥特温/希尔德堡/赫尔维克/西格弗里德/伊罗尔德 Irold/瓦特 Wâ-te/弗鲁特 Fru-te/霍兰特/路德维希/马特兰/施图尔姆兰/奥特兰/丹麦兰 Daneland/卡拉迪 Karadie/摩尔兰/阿拉比 Araby/黑格林人 Hegeling，首现附原文且与提要去重；丹麦/诺曼人等通行译名不附注；外甥霍兰特从 08/09 章定名、司酒官从 25 章定名、弯号从 21 章定名、high times 定名「盛会」、Norman 作定语统一「诺曼人」、queenly 统一「王后般」、the aged Wâ-te 统一「年迈的瓦特」，与 04-32 章体例一致），中文对话用「」角引号，引号开合与源文逐块镜像（源文 70 开 66 闭——希尔达闻讯/古德伦求恕/奥特温议婚/古德伦与哈特穆特密谈/卡拉迪王求亲等多处跨块重开引号不闭合，译文 70 开 66 闭程序化核验逐块相等），章号体例「Tale XXX / 第三十诗章」合并单行（源文标题两行断开 ## Tale / XXX … 已合并）；项目 CSV 33 行置 done（根目录 CSV 未动，交 refresh_progress.py 重建）|
| 2026-10-15 | 35-how-they-all-went-to-their-homes.md（Tale XXXII 众人如何各归各家，全书末章）| done（check_bilingual 退出码 0，0 可疑错配）| 3.0KB：Tale XXXII 韵诗 20 块（每块 4 半行，两块合一印刷诗节，同 12/15/16/17/18/20/21/22/23/24/25/26/27/29/30/31/32/33 章体例）逐块成对 + 散文提要 = 21 对 Original/Chinese，每块译文保留四行分行、末块无截断；10 印刷诗节 80 半行边界经逐节 aabb 韵脚核验（more/bore、bringing/singing、them/came、faring/bearing、be/me、feeling/healing、mine/thine、yearly/nearly、done/thrown、maiden/gladden、bred/led、bridle/idle、there/forbear、parted/hearted、give/leave、brother/another、say/day、lady/ready、swore/forevermore、belonging/wronging）；本篇源文无 U+FEFF/U+00A0/U+200A（已核），提取残留空行按语义合并为诗节，源文为 CRLF 行尾、行前导空格呈每诗节 01111111 规律（节首半行无空格、余 7 半行各一前导空格），Original 块 80 诗行经脚本逐字比对与源文一致（含行前导空格与弯引号，译文块以 LF 重建逐字照录）；术语全按术语表（西格弗里德/摩尔兰/赫尔维克/古德伦/希尔达/奥特温/奥特龙/黑格林人 Hegelings/阿尔扎比 Alzabie/马特兰 Matelan/哈特穆特 Hartmut/奥特兰 Ortland，首现附原文且与提要去重；诺曼人等通行译名不附注；queenly 统一「王后般」、Norman 作定语统一「诺曼人」，与 04-33 章体例一致），中文对话用「」角引号，引号开合与源文逐块镜像（各 4 开 4 闭），章号体例「Tale XXXII / 第三十二诗章」合并单行（源文标题两行断开 ## Tale / XXXII … 已合并）；项目 CSV 35 行置 done（根目录 CSV 未动，交 refresh_progress.py 重建）|
| 2026-10-15 | 34-how-the-four-kings-were-wedded-in-hilda-s-land.md（Tale XXXI 四位国王如何在希尔达的国土上成婚）| done（check_bilingual 退出码 0，0 可疑错配）| 8.0KB 短章：Tale XXXI 韵诗 58 块（每块 4 半行，两块合一印刷诗节，同 12/15/16/17/18/20/21/22/23/24/25/26/27/29/30/31/32/33 章体例）逐块成对 + 散文提要 = 59 对 Original/Chinese，每块译文保留四行分行、末块无截断；29 印刷诗节 232 半行边界经逐块 aabb 韵脚核验（yore/more、having/laving、gave/brave、night/slight、flying/vying、found/sound、lasted/wasted、shown/done、morning/turning 等 29 组，印刷诗节边界由提取残空行分布反向印证——诗节间无空行、节内行间有空行）；隐形字符照录：3 处 U+FEFF（块 19「tell you—」、块 21「given also—」、块 36「gainsay—」破折号前），按 18/19 章体例仅在 Original 块照录、中文不镜像，无 U+00A0/U+200A（已核）；提取残留空行按语义合并为诗节，Original 块 233 行（含提要 1 行）经脚本逐字比对与源文一致（含行前导空格与 U+FEFF）；术语全按术语表（希尔达/赫尔维克/奥特温/哈特穆特/西格弗里德/希尔德堡/古德伦/瓦特 Wâ-te/伊罗尔德 Irold/弗鲁特 Fru-te/霍兰特/马特兰/施图尔姆兰 Sturmisch/奥特兰/丹麦兰 Daneland/摩尔兰/西兰 Sealand/阿巴利 Abalie/卡西安 Kassian/卡拉迪 Karadie/爱尔兰，首现附原文且与提要去重；丹麦/诺曼底/诺曼人等通行译名不附注；四处游走的艺人从 04 章定名、管事从 33 章定名、high times 从 33 章定名「盛会」、queenly 统一「王后般」、Norman 作定语统一「诺曼人」、brave old Wâ-te 从 21/22 章定名「剽悍的老瓦特」，与 04-33 章体例一致），中文对话用「」角引号，引号开合与源文逐块镜像（源文 2 开 2 闭——霍兰特答语句中一开一闭重开，译文 2 开 2 闭精确对应），章号体例「Tale XXXI / 第三十一诗章」合并单行（源文标题两行断开 ## Tale / XXXI … 已合并）；项目 CSV 34 行置 done（根目录 CSV 未动，交 refresh_progress.py 重建）|
