# Plan.md

---

## 本计划信息

- **项目名称**：arthur-quiller-couch_on-the-art-of-reading（《论阅读的艺术》，Arthur Quiller-Couch 剑桥讲演集，1916–1918）
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
| `译文/*.zh-CN.md` | 译文产出（块对照双语） | 翻译 agent 产出 |

---

## 篇目清单

| # | 篇名 | 大小 | 状态 |
|---|------|------|------|
| 1 | 01-dedication.md | 0.0KB | todo |
| 2 | 02-preface.md | 3.6KB | todo |
| 3 | 03-introductory.md | 27.7KB | todo |
| 4 | 04-apprehension-versus-comprehension.md | 25.5KB | todo |
| 5 | 05-children-s-reading-i.md | 25.8KB | todo |
| 6 | 06-children-s-reading-ii.md | 29.9KB | todo |
| 7 | 07-on-reading-for-examinations.md | 31.7KB | todo |
| 8 | 08-on-a-school-of-english.md | 30.4KB | todo |
| 9 | 09-the-value-of-greek-and-latin-in-english-literature.md | 29.9KB | todo |
| 10 | 10-on-reading-the-bible-i.md | 29.1KB | todo |
| 11 | 11-on-reading-the-bible-ii.md | 25.0KB | todo |
| 12 | 12-on-reading-the-bible-iii.md | 35.5KB | todo |
| 13 | 13-of-selection.md | 25.1KB | todo |
| 14 | 14-on-the-use-of-masterpieces.md | 28.9KB | todo |
| 15 | 15-endnotes.md | 4.3KB | todo |

（权威状态以 `translation_queue.csv` 为准）

---

## 执行步骤（agent 按此推进，两种模式共用）

> **谁执行**由 `项目说明.md` 的「内容形态」字段决定：本项目为**短篇集 → 委派模式**，由子代理逐篇执行本流程。

### 1. 读配置（每次翻译前必读）
```
1. 本项目 Plan.md（本文件）
2. 项目说明.md
3. 术语表.md
4. prompts/通用翻译引擎.md
5. prompts/领域配置/学术著作.md
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
- 英文诗文引文保留原文，紧随中文译文；希腊文/拉丁文引文保留原文，随文给中文大意。
- 讲演体语气（Gentlemen 呼语、反讽、雄辩节奏）全文一致，照黄金样本风格译。
- 长文（源文 >50KB）分段处理见通用翻译引擎第七节（本项目各篇均 <50KB）。

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

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
| 2026-09-10 | 01-dedication.md | 完成；双语块 1 对；check_bilingual 退出码 0 | 新书首篇。献词（致 H. F. S. 与 H. M. C.），缩写照搬不译 |
| 2026-09-10 | 02-preface.md | 完成；双语块 4 对；check_bilingual 退出码 0 | 序言。English Tripos 首现括注原文；《论写作的艺术》斜体保留；Whitehall、博雅教育、人文主义、赫斯珀洛斯号首现附原文 |
| 2026-09-10 | 05-children-s-reading-i.md | 完成；双语块 21 对；check_bilingual 退出码 0 | 第三讲 儿童的阅读（上）。标题「Lecture III」转「第三讲」；Bagehot、Canton、Traherne、Earle、Scott、安徒生等首现附原文；诗文引文原样保留后附译文；拉丁语 tot circa unum caput tumultuantes deos 保留并括注 |
| 2026-09-11 03:17 | 03-introductory / 04-apprehension | 41对/25对 | [1308]额度中断前已落盘，主Agent过检代验收回填done |
| 2026-09-10 | 08-on-a-school-of-english.md | 完成；双语块 22 对；check_bilingual 退出码 0 | 第六讲 论英文学院。Lecture VI 转「第六讲」；English Tripos 按术语表译「剑桥英文荣誉学位考试」；School of English 译「英文学院」；品达散文转写、欧几里得几何证明、公文体信函均原样保留后附译文 |
| 2026-09-10 | 09-the-value-of-greek-and-latin-in-english-literature.md | 完成；双语块 27 对；check_bilingual 退出码 0 | 第七讲 希腊拉丁文在英国文学中的价值。源文件标题断行已合并为「Lecture VII … / 第七讲 …」；拉丁文 Abeunt studia in mores、希腊文 ὀ συνοπτικὸς διαλεκτικός、法语儒贝尔引文均原样保留并括注大意；查塔姆演说、兰多《塔纳格拉》全译；人名首现附原文 |
| 2026-09-10 | 06-children-s-reading-ii.md | 完成；双语块 26 对；check_bilingual 退出码 0 | 第四讲 儿童的阅读（下）。[1308]断点重派：前次子代理额度中断未落盘，本次从头完整翻译。源文标题断行合并为「Lecture IV … / 第四讲 …」；法语 Comte 格言、希腊文 Ἀριστον μὲν ὐδωρ、民谣 Sally Waters、弥尔顿 L Allegro 长段引诗均原样保留后附译文；脚注标记 4 保留为上标⁴；人名首现附原文 |
| 2026-09-10 | 07-on-reading-for-examinations.md | 完成；双语块 21 对；check_bilingual 退出码 0 | 第五讲 论应试阅读。[1308]断点重派：前次子代理额度中断未落盘，本次从头完整翻译。源文标题断行合并为「Lecture V … / 第五讲 论应试阅读」；博洛尼亚私试公试、巴黎 Responsions 与答辩日两段长文献引文全译；雪莱 Adonais、皮尔 Oenone 二重唱、济慈 Greek Urn 诗行均原样保留后附译文；脚注标记 5 保留为上标⁵；Bologna/Responsions/Determination/Rigorosi 等拉丁学术词首现括注；人名首现附原文 |
| 2026-09-10 | 10-on-reading-the-bible-i.md | 完成；双语块 20 对；check_bilingual 退出码 0 | 第八讲 论圣经的阅读（上）。源文标题断行合并为「Lecture VIII On Reading the Bible (I) / 第八讲 论圣经的阅读（上）」；圣经引文（诗篇 137、以赛亚、撒母耳记、列王纪）参照和合本语体；班扬《圣战》《天路历程》引文、彭斯佃农诗、纽曼与兰多引文全译；拉丁文 sui generis / vera causa 原样保留并括注；人名首现附原文 |
| 2026-09-10 | 13-of-selection.md | 完成；双语块 19 对；check_bilingual 退出码 1，仅 1 处数字锚点误报（英文脚注 …14 译为上标 ¹⁴，结构契约全部满足，按派发指令判通过） | 第十一讲 论择书。源文标题断行合并为「Lecture XI Of Selection / 第十一讲 论择书」；布朗《医生的宗教信仰》辩解长引文、《斐德罗篇》苏格拉底祷告、哈蒙德《乡村劳工》、金莱克 Eöthen 荷马热恋四段引文全译；信经两条斜体保留；脚注标记 13/14 保留为上标 ¹³/¹⁴（与 07 讲上标 ⁵ 体例一致）；拉丁文 in impari materia、法语 enfin Malherbe 原样保留并括注；人名首现附原文 |
| 2026-09-10 | 15-endnotes.md | 完成；双语块 12 对；check_bilingual 退出码 0 | 尾注页 16 条全译。尾注编号与 ↩︎ 回链符号照搬；引文出处编号（Book VI, lines 81–86、chapter LXI、XIX 30 ff.）按术语表照搬；期刊名 Zeitschr. f. Ethnologie 与出版社名（Clarendon Press、John Lane）保留原文；注 2 罗杰斯咏简·格雷夫人五行诗与注 15 女性口吻长独白全译；人名首现附原文 |
| 2026-09-10 | 11-on-reading-the-bible-ii.md | 完成；双语块 19 对；check_bilingual 退出码 0 | 第九讲 论圣经的阅读（中）。源文标题断行合并为「Lecture IX On Reading the Bible (II) / 第九讲 论圣经的阅读（中）」；圣经引文（以赛亚、哥林多前书、创世记、雅歌）参照和合本语体；吉本论朗吉努斯第九章、阿诺德论希伯来诗歌平行体、《斐多篇》§ 96 苏格拉底论灵魂两段长引文全译；拉丁文 Nos te, nos facimus, Scriptura, deam 与希腊文书名原样保留并括注大意；40 余种英国文学名著清单全译并附原名；人名首现附原文。注意：本语料源文在「为下一诗节定下基调：」处截止，许诺引录的《诗篇》第 107 篇四段正旋歌不在源文件内（第十二讲另起新题），译文如实到源文末行为止 |
| 2026-09-10 | 12-on-reading-the-bible-iii.md | 完成；双语块 67 对；check_bilingual 退出码 0 | 第十讲 论圣经的阅读（下）。源文标题断行合并为「Lecture X On Reading the Bible (III) / 第十讲 论圣经的阅读（下）」；约伯记 1–3、12–13、28、31 章与诗篇 114/136 引文参照和合本语体逐行对照；弥尔顿《失乐园》开篇、阿诺德《巴尔德之死》、迈尔斯《圣保罗》、雪莱《解放了的普罗米修斯》、梅特林克论静态戏剧各长引文全译；拉丁通俗译本 Ecce, Deus magnus 一句与希腊文 πράττοντας 原样保留并括注大意；1869 年福尔柯克苏格兰无名氏打油译本全译；尾注标记 12 照搬；源文 OCR 诗行间孤立空行与行首空格已规范化为 > 引文体例；人名首现附原文 |
| 2026-09-10 | 14-on-the-use-of-masterpieces.md | 完成；双语块 23 对；check_bilingual 退出码 0 | 第十二讲 论经典的使用（全书末章，至此十二讲全部完成）。源文标题断行合并为「Lecture XII On the Use of Masterpieces / 第十二讲 论经典的使用」；莎士比亚《暴风雨》伊里斯假面剧 13 行、丹尼尔无题诗三节 24 行、奥德修斯冥府遇埃阿斯两行、朗吉努斯《论崇高》结尾两段长引文全译；第一讲老教师「英文班」引文按第三讲既定译法原样复用，「崇高是伟大灵魂的回声」按第九讲既定译法复用；朗吉努斯/芝诺比娅/特伦提安努斯等专名与前文统一；拉丁文 Abeunt studia in mores、Dum domus Æneae、Nec Cereri 与希腊文 ΠΕΡΙΨΠΣΟΥΣ、ΨΥΧΗΣ ἸΑΤΡΕΙΟΝ 原样保留并括注；footnote 标记 15/16 照搬；源文 OCR 诗行断行与行首空格已规范化为 > 引文体例；人名首现附原文 |
