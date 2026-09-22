# Plan.md — 《沃特尔博士的学校》

## 本计划信息

- **项目名称**：anthony-trollope_dr-wortles-school（《沃特尔博士的学校》，Dr. Wortle's School）
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/小说文学.md
- **术语表**：术语表.md
- **内容形态**：长篇（24 章，单一叙事弧）→ **执行模式：委派**

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
01-dr-wortle.md,17.2,todo
02-the-new-usher.md,17.0,todo
...
```

| 字段 | 含义 | 取值 |
|------|------|------|
| `file` | 源文文件名（在 `原文/` 目录下） | 如 `01-dr-wortle.md` |
| `size_kb` | 源文大小（KB） | 数字 |
| `status` | 翻译状态 | `todo` 待译 / `doing` 翻译中 / `done` 已完成 |

---

## 执行步骤（agent 按此推进，两种模式共用）

> 本项目为**委派模式**：主 agent 只当调度员，逐章派子代理执行以下 9 步；并发子代理 ≤ 3。简报构成见 `WORKFLOW.md`「子代理简报」。

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
- 不存在 → 把该行 `status` 改为 `doing` 并保存 CSV（双写根表），继续。

### 3. 读源文
读 `原文/对应文件名`。

### 4. 翻译
产出到 `译文/对应文件名去.md加.zh-CN.md`。

**双语对照格式、标记规则、完整性禁令**：见 `prompts/通用翻译引擎.md` 第五、六节。本流程专有提醒：
- 逐块对照原文，绝不漏译、不合并段落、不缩写、不总结，尤其结尾别截断。
- 严守术语表；新词自行确定统一译法，首次附原文「中文（English）」。
- 人物、语气、风格全文一致（维多利亚教会/乡绅社会小说，书信体章节多），照黄金样本风格译。
- 长文（源文 >50KB）分段处理见通用翻译引擎第七节；本书各章 15–19KB，单章单批。

### 5. 自检
完整性 / 块对称 / 标题格式（「英文 / 中文」合并）/ 术语一致（抽查 5 个术语词）。不满足则改到满足。

### 6. 自动检查
```
python scripts/check_bilingual.py 译文/对应篇名.zh-CN.md
```
结构契约满足则继续；有违规回步骤 4 修订。

### 7. 回填状态（双写）
`status` 从 `doing` 改 `done`，改两处：① 项目 `translation_queue.csv` 该行；② 根 `translation_queue.csv` 中 `anthony-trollope_dr-wortles-school,<本篇名>` 那一行。

### 8. 追加日志
在本文件「运行日志」追加一行。

### 9. 循环
回到步骤 2，取下一篇 `todo`，直到全部 `done`；然后触发跨书 compact。

---

## 篇目清单

> 原书分卷：Part I（1–3 章）/ Part II（4–6 章）/ Part III（7–9 章）/ Part IV（10–12 章）/ Part V（13–21 章）/ Conclusion（22–24 章）。卷标题已并入各卷首章文件首行。

| # | 篇名 | 源文 | 大小 | 状态 |
|---|------|------|------|------|
| 1 | Part I · I Dr. Wortle | 01-dr-wortle.md | 17.2KB | todo |
| 2 | II The New Usher | 02-the-new-usher.md | 17.0KB | todo |
| 3 | III The Mystery | 03-the-mystery.md | 17.2KB | todo |
| 4 | Part II · IV The Doctor Asks His Question | 04-the-doctor-asks-his-question.md | 16.3KB | todo |
| 5 | V "Then We Must Go" | 05-then-we-must-go.md | 15.6KB | todo |
| 6 | VI Lord Carstairs | 06-lord-carstairs.md | 16.8KB | todo |
| 7 | Part III · VII Robert Lefroy | 07-robert-lefroy.md | 16.4KB | todo |
| 8 | VIII The Story Is Told | 08-the-story-is-told.md | 15.7KB | todo |
| 9 | IX Mrs. Wortle and Mr. Puddicombe | 09-mrs-wortle-and-mr-puddicombe.md | 16.7KB | todo |
| 10 | Part IV · X Mr. Peacocke Goes | 10-mr-peacocke-goes.md | 16.4KB | todo |
| 11 | XI The Bishop | 11-the-bishop.md | 16.9KB | todo |
| 12 | XII The Stantiloup Correspondence | 12-the-stantiloup-correspondence.md | 18.5KB | todo |
| 13 | Part V · I Mr. Puddicombe's Boot | 13-mr-puddicombe-s-boot.md | 18.7KB | todo |
| 14 | II Everybody's Business | 14-everybody-s-business.md | 18.5KB | todo |
| 15 | III "Amo in the Cool of the Evening" | 15-amo-in-the-cool-of-the-evening.md | 17.6KB | todo |
| 16 | IV "It Is Impossible" | 16-it-is-impossible.md | 17.2KB | todo |
| 17 | V Correspondence with the Palace | 17-correspondence-with-the-palace.md | 15.4KB | todo |
| 18 | VI The Journey | 18-the-journey.md | 18.0KB | todo |
| 19 | VII "Nobody Has Condemned You Here" | 19-nobody-has-condemned-you-here.md | 17.4KB | todo |
| 20 | VIII Lord Bracy's Letter | 20-lord-bracy-s-letter.md | 16.6KB | todo |
| 21 | IX At Chicago | 21-at-chicago.md | 16.8KB | todo |
| 22 | Conclusion · X The Doctor's Answer | 22-the-doctor-s-answer.md | 17.3KB | todo |
| 23 | XI Mr. Peacocke's Return | 23-mr-peacocke-s-return.md | 17.5KB | todo |
| 24 | XII Mary's Success | 24-mary-s-success.md | 16.2KB | todo |

> 注：源书第 20 章标题罗马数字误作 VII（应为 VIII），照原文保留。

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
| 2026-09-12 | III The Mystery | done | 译文 03-the-mystery.zh-CN.md；7 对块、18/18 段对称；check exit 0；术语遵表（皮科克先生、斯坦蒂卢普太太、德·劳尔庄园、助教、密苏里学院）；对话弯引号 |
| 2026-09-12 | IV The Doctor Asks His Question | done | 译文 04-the-doctor-asks-his-question.zh-CN.md；14 对块、42/42 段对称；check exit 0；术语遵表（沃特尔博士、皮科克先生、斯坦蒂卢普太太、主教官邸、助教、副牧师职、鲍威克、圣路易斯）；卷题「# Part II / 第二部」、章题罗马数字照搬；对话弯引号 |
| 2026-09-12 | 01-dr-wortle（Part I · I Dr. Wortle / I 沃特尔博士） | done | check_bilingual 通过（4 对块、段落数 3/3·3/3·2/2·2/2 对称、0 可疑错配）；术语按表：沃特尔博士、鲍威克、副牧师、助教、敬虔之恩、£200/£250/£2 10先令/£5、平河；项目 CSV 已置 done（根 CSV 未动，由主 agent 统一回填） |
| 2026-09-12 | 02-the-new-usher（II The New Usher / II 新助教） | done | check_bilingual 通过（exit 0；4 对块、段落数 4/4·3/3·4/4·3/3 对称、0 可疑错配）；术语按表：皮科克先生/太太、助教、副牧师、鲍威克、三一学院、圣路易斯、德·劳尔夫人、奥尔塔蒙侯爵夫人、"丹麦国里有些东西腐烂了"、牧师俸地、教区牧师宅；usher=助教；对话弯引号、人名首现附原文；项目 CSV 已置 done（根 CSV 未动） |
| 2026-09-12 | V "Then We Must Go" / V 那我们只能走 | done | 译文 05-then-we-must-go.zh-CN.md；17 对块、64/64 段对称、0 可疑错配；check exit 0；术语遵表（皮科克先生/太太、沃特尔博士、德·劳尔夫人、主教、副牧师职、助教、鲍威克、斯坦蒂卢普之流）；新词首现附原文：鲍威克园舍（Bowick Lodge）、皮尔逊先生（Mr. Pearson，乡绅）、帕迪科姆先生（the Rev. Mr. Puddicombe，邻区牧师）；罗马数字照搬、章名取「那我们只能走」；路得经引句按和合本措辞嵌单引号；对话弯引号；项目 CSV 已置 done（根 CSV 未动） |
| 2026-09-12 | 06-lord-carstairs（VI Lord Carstairs / VI 卡斯泰尔斯勋爵） | done | 译文 06-lord-carstairs.zh-CN.md；check_bilingual 通过（exit 0；17 对块、段/行数逐块对称、0 可疑错配、无 BOM）；术语遵表：卡斯泰尔斯勋爵（勋爵与封地宅邸均作卡斯泰尔斯）、布雷西伯爵/勋爵、布雷西夫人、皮科克先生/太太、助教、牧师宅、废奴、圣路易斯/路易斯安那/新奥尔良、布劳顿、罗伯特·勒弗罗伊、基督教堂学院；拉丁引文 Dabit Deus his quoque finem 直译附原文、嵌套弯单引号；布雷西书信保留 blockquote 与粗体；罗马数字照搬、人名首现附原文、对话弯引号、二十五镑按中文数字；项目 CSV 已置 done（根 CSV 未动） |
| 2026-09-12 | 08-the-story-is-told（VIII The Story Is Told / VIII 和盘托出） | done | 译文 08-the-story-is-told.zh-CN.md；check_bilingual 通过（exit 0；23 对块、99/99 段对称、0 可疑错配）；术语按表：皮科克先生/太太（埃拉）、勒弗罗伊上校、罗伯特·勒弗罗伊、费迪南德·勒弗罗伊、卡斯泰尔斯勋爵、沃特尔博士、鲍威克、圣路易斯、助教、牧师宅、新奥尔良、得克萨斯；拉丁引文「问心无所愧，闻罪不改色」直译附原文（Nil conscire sibi—nulla pallescere culpa）；罗马数字照搬；对话弯引号、嵌套弯单引号，无直角引号，UTF-8 无 BOM；人名首现附原文；项目 CSV 已置 done（根 CSV 未动） |
| 2026-09-12 | 07-robert-lefroy（Part III · VII Robert Lefroy / VII 罗伯特·勒弗罗伊） | done | 译文 07-robert-lefroy.zh-CN.md；check_bilingual 通过（exit 0；26 对块、103/103 段对称（首块 3 段+25 块各 4 段）、0 可疑错配、UTF-8 无 BOM）；卷题「# Part III / 第三部」、章题罗马数字照搬；术语按表：罗伯特·勒弗罗伊、费迪南德·勒弗罗伊、勒弗罗伊上校、皮科克先生/太太、沃特尔博士、助教、密苏里学院、圣路易斯、得克萨斯、鲍威克；美国地名/机构首现附原文（St. Louis/Texas/the Missouri College/Mexico）；勒弗罗伊粗鄙美国腔（挣多少？/子儿/私了）与皮科克绅士腔对照，叙述者反讽保留；brother-in-law 弹性称谓按语境分译嫂子/姐夫/小叔子/内弟；对话弯双引号、无直角引号；项目 CSV 已置 done（根 CSV 未动） |
| 2026-09-13 | IX Mrs. Wortle and Mr. Puddicombe / IX 沃特尔太太与帕迪科姆先生 | done | 译文 09-mrs-wortle-and-mr-puddicombe.zh-CN.md；16 对块、93/93 段对称、0 可疑错配；check exit 0；术语遵表（沃特尔博士/太太、皮科克先生/太太、帕迪科姆先生、勒弗罗伊、斯坦蒂卢普太太、鲍威克、布劳顿、主教、副牧师、助教、圣俸）；源文无卷标题（第三部末章），仅章题罗马数字照搬合并；对话弯引号、嵌套无；无直角引号；项目 CSV 已置 done（根 CSV 未动） |
| 2026-09-13 | XI The Bishop / XI 主教 | done | 译文 11-the-bishop.zh-CN.md；check_bilingual 通过（exit 0；18 对块、84/84 段对称、0 可疑错配）；章题罗马数字照搬合并；术语遵表：沃特尔博士、皮科克先生/太太、主教（the Bishop）、帕迪科姆先生、斯坦蒂卢普太太、副牧师职、鲍威克、蒙森乡绅、巴特卡普、布里格斯托克伯爵、玛格丽特·蒙森夫人、奥古斯塔斯·蒙森；新词首现附原文：小格斯（Gus）、抹大拉的马利亚（Mary Magdalene，和合本措辞）；£20,000 照录；声口分立——主教圆滑绵里藏针、博士专断、玛格丽特夫人轻浮伪善、沃特尔太太温怯；对话弯双引号、无直角引号、UTF-8 无 BOM；日期按 date 实测取 2026-09-13；项目 CSV 已置 done（根 CSV 未动） |
| 2026-09-12 | 10-mr-peacocke-goes（Part IV · X Mr. Peacocke Goes / X 皮科克先生启程） | done | 译文 10-mr-peacocke-goes.zh-CN.md；check_bilingual 通过（exit 0；11 对块、53/53 段对称、0 可疑错配）；卷题「# Part IV / 第四部」、章题罗马数字照搬合并；英文块经脚本以源文 53 段逐字回填（保留源文弯引号），中文 53 段逐块对应；术语按表：皮科克先生/太太、帕迪科姆先生、卡斯泰尔斯勋爵、罗伯特·勒弗罗伊、费迪南德·勒弗罗伊、鲍威克、布劳顿、圣路易斯、密苏里、得克萨斯、助教、牧师宅；新词首现附原文：普里奇特（Pritchett）、罗斯先生（Mr. Rose）、凯恩太太（Mrs. Cane）、"羔羊"酒馆（the Lamb）；一千美元照录；勒弗罗伊粗鄙美国腔（不依/铜子儿/凭什么）与博士专断、皮科克哀婉声口分立；对话弯双引号、无直角引号、UTF-8 无 BOM；项目 CSV 已置 done（根 CSV 未动） |
| 2026-09-13 | 12-the-stantiloup-correspondence（XII The Stantiloup Correspondence / XII 斯坦蒂卢普书信） | done | 译文 12-the-stantiloup-correspondence.zh-CN.md；check_bilingual 通过（exit 0；12 对块、57/57 段对称、0 可疑错配、UTF-8 无 BOM、无直角引号）；章题罗马数字照搬合并；术语按表：斯坦蒂卢普太太、蒙森乡绅/蒙森太太、玛格丽特·蒙森夫人、巴特卡普庄园、罗兰太太、格罗格拉姆夫人、安妮·克利福德夫人、塔尔博特、卡斯泰尔斯、布雷西勋爵/夫人、助教、副牧师、三一学院、布劳顿、学园、伊顿；新词首现附原文：希普顿老妈妈（Mother Shipton，斯坦蒂卢普太太诨号）、普里阿摩斯（Priam）、古斯塔夫斯·蒙森（Gustavus Momson）、加斯（Gus）；五通书信保留 blockquote 与粗体、落款逐行对应；嵌套引语（主教'叫她去住客栈'）用弯单引号、对话弯双引号；斯坦蒂卢普太太毒舌腔、博士专断自信腔、罗兰太太怯弱腔分立；数字按文学惯例译中文数字（二百五十镑等）；源文方括号叙述者插注照录；项目 CSV 已置 done（根 CSV 未动） |
| 2026-09-13 | Part V · I Mr. Puddicombe's Boot / I 帕迪科姆先生的靴子 | done | 译文 13-mr-puddicombe-s-boot.zh-CN.md；check_bilingual 通过（exit 0；15 对块、64/64 段对称、0 可疑错配、UTF-8 无 BOM、无直角引号）；卷题「# Part V / 第五部」、章题罗马数字照搬合并（Part V 起编号重排系原书结构）；术语遵表：帕迪科姆先生、沃特尔博士/太太、皮科克先生/太太、斯坦蒂卢普夫妇、勒弗罗伊、圣路易斯、鲍威克、布劳顿公报、副牧师；新词首现附原文：塞缪尔·格里芬爵士（Sir Samuel Griffin）、亨利（Henry）、布列塔尼（Brittany）、penny-a-liner（一文一行卖字的穷文人）；泥靴之喻（诚实泥/蹭污泥）直译存讽；「学生来了又去，我们却永远奔流不息」仿丁尼生《小溪》句式；帕迪科姆干硬公允与博士专断激切口吻分立；日期按 date 实测取 2026-09-13；项目 CSV 已置 done（根 CSV 未动） |
| 2026-09-13 | II Everybody's Business / II 人人的事 | done | 译文 14-everybody-s-business.zh-CN.md；check_bilingual 通过（exit 0；5 对块、段数 1/1·3/3·5/5·4/4·4/4 对称、0 可疑错配、UTF-8 无 BOM、无直角引号）；源文 Part V 起章号重排，章题「## II *Everybody's Business* / II 人人的事」罗马数字照搬；源文连续软换行行按 09/11 章先例逐行计段、块内空行分隔，书信 blockquote 内部保持连续行（沿 12 章先例），21 行英文经脚本逐行校验与源文一致；术语遵表并沿例：希普顿老妈妈（Mother Shipton）、玛格丽特·蒙森夫人→玛格丽特夫人、罗兰太太、奥尔塔蒙侯爵夫人、安妮·克利福德夫人、斯坦蒂卢普太太、主教官邸、《布劳顿公报》；新词首现附原文：《人人的事》（Everybody's Business）、座堂圈（the Close）、罗伯特勋爵（Lord Robert）、克利福德叔叔（Uncle Clifford）；希腊文 τυπτω／拉丁文 amo 斜体照录、直译附原文（我打／我爱），呼应第 15 章章名；博士致主教三段书信保留 blockquote 与粗体抬头、「本月十二日」本地化日期；博士专断反讽（"一帮可怜的懦夫"／以讼相胁）与叙述者维多利亚式反讽（"人人的事"报馆长段议论）声口分立；对话弯双引号、嵌套弯单引号（'教区流言'）；日期按 date 实测取 2026-09-13；项目 CSV 已置 done（根 CSV 未动） |
| 2026-09-13 | Part V · IV "It Is Impossible" / IV 这不可能 | done | 译文 16-it-is-impossible.zh-CN.md；check_bilingual 通过（exit 0；19 对块、94/94 段对称、0 可疑错配、UTF-8 无 BOM、无直角引号）；章题罗马数字 IV 照搬合并（源书第 13 章起重排编号，本章源文 IV 系原书结构）；无卷标题；术语遵表：卡斯泰尔斯勋爵、布雷西勋爵、巴特卡普庄园、鲍威克、牧师宅、塔尔博特、伊顿、牛津、蒙森一家；新词首现附原文：蒙克（Monk）；mamma 沿第 6/11 章惯例译「妈妈」；「烟囱顶上的那块砖」之喻直译存讽；玛丽端谨忸怩、博士专断自得（"大可谢天谢地"/"到底落了个蠢字"）、沃特尔太太温怯患得声口分立；对话弯双引号、人名首现附原文；项目 CSV 已置 done（根 CSV 未动） |
| 2026-09-13 | Part V · III “*Amo* in the Cool of the Evening” / III 晚凉时分*Amo* | done | 译文 15-amo-in-the-cool-of-the-evening.zh-CN.md；check_bilingual 通过（exit 0；11 对块、段落数 5/5·5/5·5/5·3/3·5/5·3/3·4/4·4/4·5/5·3/3·6/6 对称、0 可疑错配、UTF-8 无 BOM、无直角引号）；源文章号 III（第 13 章起重排）罗马数字照搬合并；英文块经脚本从源文 48 段逐字回填（弯引号、零宽字符保留），块内段落沿源文连续行式逐行对应；报纸道歉启事保留 blockquote；术语遵表：沃特尔博士、皮科克先生/太太、主教、斯坦蒂卢普太太、鲍威克、牧师宅、牧师俸地、助教、圣俸、布劳顿主教官邸；£10,000/£20,000 照录、二十名/二十八名等按中文数字；新词首现附原文：涅索斯的毒衫（the shirt of Nessus）、京师报界（metropolitan press）；拉丁文字游戏 *Amo*（拉丁文“我爱”）沿第 14 章先例斜体照录，章内统一“晚凉时分*Amo*”，首现破折号夹注直译；博士专断激愤、律师干练平淡、太太温怯声口分立；提示：“metropolitan press”本章定译“京师报界”，第 17/24 章源文复现，请后续对齐；项目 CSV 已置 done（根 CSV 未动） |
| 2026-09-13 | V Correspondence with the Palace / V 与主教官邸的通信 | done | 译文 17-correspondence-with-the-palace.zh-CN.md；check_bilingual 通过（exit 0；9 对块、逐块段数对称 1/1·1/1·3/3·5/5·5/5·4/4·3/3·3/3·2/2、0 可疑错配、UTF-8 无 BOM、无直角引号）；章题罗马数字 V 照搬合并（源书第 13 章起重排编号，本章源文 V 系原书结构）；无卷标题；两封书信保留 blockquote、粗体抬头（亲爱的主教大人／亲爱的沃特尔博士）、信内连续行不拆、逐行落款（杰弗里·沃特尔／C. 布劳顿），沿 12/14 章先例；术语遵表：主教（布劳顿主教）、帕迪科姆先生、皮科克太太、《人人的事》、metropolitan press 对齐第 15 章定译「京师报界」（10 处）；新词首现附原文：主教官邸（the Palace）、拉丁 in terrorem 斜体照录直译（儆戒之具）；“晚凉时节*Amo*” 嵌套弯单引号、斜体照录呼应第 15 章章名；"two verbs" 报纸笑话、"弄脏自己窝的鸟"、"humble pie" 之喻直译存讽；博士专断怨愤、主教绵里藏针圆滑、帕迪科姆干硬公允声口分立；源文无阿拉伯数字无锚点风险；日期按 date 实测取 2026-09-13；项目 CSV 已置 done（根 CSV 未动） |
| 2026-09-13 | VII “Nobody Has Condemned You Here” / VII “此地无人定你的罪” | done | 译文 19-nobody-has-condemned-you-here.zh-CN.md；check_bilingual 通过（exit 0；15 对块、63/63 段对称（3/5/4/4/4/4/4/4/4/4/5/5/5/5/3）、0 可疑错配、UTF-8 无 BOM、无直角引号）；章题罗马数字 VII 照搬合并（源书第 13 章起重排编号系原书结构）；无卷标题；英文块经脚本从源文 63 段逐字回填（弯引号、零宽字符保留）；术语遵表：沃特尔博士/太太、皮科克先生/太太、费迪南德·勒弗罗伊、罗伯特、斯坦蒂卢普太太、安妮·克利福德夫人、莫布雷、副牧师、主教、助教；新词首现附原文：纽约（New York）、南安普顿（Southampton）、得克萨斯（Texas）；皮科克太太慷慨陈词（「我只有两位审判者——天上的主，与我地上的丈夫」）与沃特尔太太温怯呜咽、博士专断自辩（母龙之喻、「又恶又一事无成才是下作」）声口分立；嵌套弯单引号（'主教把我的行止严加申饬了'）；£2,000 照录（初版数字后接汉字触发锚点误报，改为数字后接破折号沿黄金样本惯例）；项目 CSV 已置 done（根 CSV 未动） |
| 2026-09-13 | VII Lord Bracy's Letter / VII 布雷西勋爵的信 | done | 译文 20-lord-bracy-s-letter.zh-CN.md；check_bilingual 通过（exit 0；14 对块、63/63 段对称（1/5/1/6/1/6/6/6/6/6/6/6/1/6）、0 可疑错配、UTF-8 无 BOM、无直角引号）；源书第 20 章标题误作 VII（按序应为 VIII），照原文保留未改正，章题「## VII Lord Bracy's Letter / VII 布雷西勋爵的信」罗马数字照搬合并；无卷标题；布雷西书信 6 行保留 blockquote、粗体抬头（**我亲爱的沃特尔博士**）、信内连续行不拆、逐行落款（布雷西），沿 12/17 章先例；英文块经脚本从源文 63 段逐字回填（弯引号、零宽字符、不断行空格保留）；术语遵表：布雷西勋爵/夫人、卡斯泰尔斯勋爵、沃特尔博士/太太、皮科克先生/太太、斯坦蒂卢普太太、罗伯特·勒弗罗伊、圣路易斯、旧金山、奥格登枢纽、鲍威克、牛津；新词首现附原文：震颤性谵妄（delirium tremens）；法语 tant mieux 斜体照录直译附原文（那更好）；「烟囱顶上的砖」之喻沿第 16 章定译直译存讽；布雷西勋爵体面持重而暗含怯懦（「多少有些专断的父权」／「我倒不能说我引以为憾」）、博士专断自信（「所谓商量无非是向她下指示」叙述反讽）、玛丽娇羞自尊声口分立；对话弯双引号、信内嵌套『自己已经订了亲』弯单引号；日期按 date 实测取 2026-09-13；项目 CSV 已置 done（根 CSV 未动） |
| 2026-09-13 | VI The Journey / VI 旅程（重派） | done | 译文 18-the-journey.zh-CN.md；check_bilingual 通过（exit 0；20 对块、85/85 段对称、0 可疑错配、UTF-8 无 BOM、无直角引号）；章题罗马数字 VI 照搬合并（源书第 13 章起重排编号）；首行免责前缀（重派要求）；英文块经脚本从源文 85 段逐字回填（保留弯引号与零宽字符）；术语遵表：皮科克先生、罗伯特·勒弗罗伊、费迪南德·勒弗罗伊、费迪、圣路易斯、旧金山、奥格登枢纽、犹他城、莱文沃思、鲍威克、沃特尔博士、主教、密西西比河；新词首现附原文：震颤性谵妄（D.T.）、旅行信用券（circular notes）、鲍伊猎刀（bowie-knife）、基尔布雷克（Kilbrack）、伯克（Burke）、罗伯特大少爷（Master Robert）；勒弗罗伊粗鄙美国腔（掏钱/子儿/老伙计/我估摸着）与皮科克克制绅士腔、叙述者维多利亚式反讽分立；对白 niggers 沿出版译例作「黑鬼」，d——与————脏话删节照录式处理；一千美元/二十四个钟头等按中文数字；对话弯双引号、嵌套弯单引号；项目 CSV 已置 done（根 CSV 未动） |
| 2026-09-13 | IX At Chicago / IX 在芝加哥 | done | 译文 21-at-chicago.zh-CN.md；check_bilingual 通过（exit 0；19 对块、83/83 段对称（4/6/5/5/3/5/4/4/4/5/3/4/4/5/5/5/5/4/3）、0 可疑错配、UTF-8 无 BOM、无直角引号）；章题罗马数字 IX 照搬合并（源书第 13 章起重排编号系原书结构）；无卷标题；英文块经脚本从源文 83 段逐字回填并程序校验逐字一致（弯引号、31 处零宽字符保留）；美国线收束章术语遵表：罗伯特·勒弗罗伊、费迪南德·勒弗罗伊、皮科克先生、沃特尔博士、主教、鲍威克、莱文沃思、旧金山/芝加哥/新奥尔良/奥格登枢纽、六响枪；新词首现附原文：基尔布雷克（Kilbrack，沿第 18 章定译）、琼斯太太的寄宿公寓（Mrs. Jones's boardinghouse）、布法罗（Buffalo）、新英格兰（New England）、加利福尼亚（California）、费迪（Ferdy）、深藏不露（lie perdu）；美元照录（一千美元/九百美元）、四十英里/十五英里按中文数字；勒弗罗伊粗鄙讹诈腔（胡扯/一个子儿不付/老伙计）与皮科克克制绅士腔（"从狗嘴里掏回一块肉"之喻）、叙述者闲汉嚼雪茄段维多利亚式反讽声口分立；对话弯双引号、嵌套无；项目 CSV 已置 done（根 CSV 未动） |
| 2026-09-13 | Conclusion · X The Doctor's Answer / X 博士的答复（断点续校） | done | 译文 22-the-doctor-s-answer.zh-CN.md（35.6KB）；**断点续校：前代理部分产出经全量校验完整**，未续写未改写——程序化比对 90/90 段英文块与源文逐字一致、末段一致、38 处零宽字符保留；check_bilingual 通过（exit 0；20 对块严格交替、逐块段数对称、0 可疑错配、UTF-8 无 BOM、无直角引号）；卷题「# Conclusion / 尾声」、章题「## X The Doctor's Answer / X 博士的答复」按源文实际章号 X 照搬合并；术语遵表：皮科克先生/太太、沃特尔博士/太太、玛丽、布雷西勋爵/夫人、卡斯泰尔斯勋爵、费迪南德·勒弗罗伊、鲍威克、旧金山、主教、牛津；新词首现附原文：利物浦（Liverpool）；博士致布雷西书信两段保留 blockquote 与粗体抬头（**我亲爱的布雷西勋爵**）、落款「杰弗里·沃特尔」逐行对应，沿 12/17/20 章先例；玛丽娇羞忸怩、沃特尔太太温怯患得、博士专断自信（"笔不到手，我从来不知道该说什么"）声口分立；对话弯双引号、嵌套弯单引号（'不'字）；日期按 date 实测取 2026-09-13；项目 CSV 已置 done（根 CSV 未动） |
| 2026-09-13 | XI Mr. Peacocke's Return / XI 皮科克先生归来（断点续校） | done | 译文 23-mr-peacocke-s-return.zh-CN.md（35.0KB）；**断点续校：前代理部分产出经全量校验完整**，中文块未动——程序化比对 14 对块、56/56 段对称（3/6/3/3/6/4/4/4/3/4/5/4/6/1）、末段覆盖源文末段、无截断、无直角引号；仅英文块存空白字符级差异（62×U+00A0、27×U+FEFF、1×U+200A，0 实质差异），沿第 10/15/19/20/21 章先例经脚本从源文 56 段逐字回填对齐并程序复验逐字一致；check_bilingual 通过（exit 0；标记成对 14 对、标题合并满足、0 可疑错配、UTF-8 无 BOM）；章题「## XI Mr. Peacocke's Return / XI 皮科克先生归来」按源文实际章号 XI 照搬合并（源书第 13 章起重排编号系原书结构）；无卷标题；术语遵表：皮科克先生/太太、沃特尔博士/太太、斯坦蒂卢普太太、帕迪科姆先生、布雷西伯爵/夫人、卡斯泰尔斯勋爵、安妮·克利福德夫人、塔尔博特、蒙森先生、鲍威克牧师宅、助教、座堂圈（沿第 14 章定译）；新词首现附原文：利物浦（Liverpool）、查利（Charley）、基督堂学院（Christ-Church）、轻便出租马车（fly）；法国谚语「为自己辩解的人，就是在控告自己」嵌弯单引号直译；十个/二十个等按中文数字；帕迪科姆干硬公允（「在沉默中把这件事熬过去」／「一个人永远不要替自己辩白」）与博士专断自辩、烧信段维多利亚式反讽声口分立；对话弯双引号；日期按 date 实测取 2026-09-13；项目 CSV 已置 done（根 CSV 未动） |
| 2026-09-13 | XII Mary's Success / XII 玛丽的好事有成 | done | 译文 24-mary-s-success.zh-CN.md；check_bilingual 通过（exit 0；13 对块、58/58 段对称（6/4/5/4/6/4/4/6/5/4/4/3/3）、0 可疑错配、UTF-8 无 BOM、无直角引号）；全书末章收束：源文首行即章题、无卷标题，罗马数字 XII 照搬合并；英文块经脚本从源文 58 段逐字回填并程序校验一致（弯引号、零宽字符保留）；术语遵表并沿例：沃特尔博士/太太、玛丽、皮科克先生/太太、帕迪科姆先生、主教、卡斯泰尔斯勋爵、布雷西勋爵/夫人、安妮·克利福德夫人、玛格丽特·蒙森夫人、莫布雷兄弟、乔治·邦科姆爵士、莱文沃思、圣路易斯、费迪南德·勒弗罗伊、助教、副牧师职、京师报界（metropolitan press，沿第 15 章定译）、《布劳顿公报》、鲍威克、布劳顿；末章人物均旧出，未再附原文；声口分立——博士专断自得（「谁稀罕那个」「撤得多么叫人受用」）、玛丽娇羞圆满（「恍如置身乐园」）、卡斯泰尔斯少年意气、皮科克克制坚忍、叙述者维多利亚式反讽（开篇「难道到头来不从来都是这样悬而未决么」、「风向标」之喻直译存讽、收束「怕他们前头还有波折」）；末段主教允授副牧师职许可、皮科克悬而未决处收束全书，无截断；日期按 date 实测取 2026-09-13；项目 CSV 已置 done（根 CSV 未动） |
| 2026-09-13 | **整书完结**：特罗洛普《沃特尔博士的学校》（Dr. Wortle's School，1881）24/24 流转（第 13 册） | 无预算长轮第三册：23:25 上锁至 03:10 完书（中途 [1308] 击杀 ch22-24 在途、限额 02:15 重置后断点续校/重译收口），408KB 零非零 exit；ch18 遭 [1301] 免责前缀重派 1 次成功（本轮首例）；ch22/23 断点续校判例=前代理产出经全量校验已完整、零翻译成本收口（[1308] 死于置 done 前，译文完好） | 风格基线：维多利亚教会小说——博士专断自信却慷慨体面（对主教寸步不让「自己的生意自己最清楚」）／皮科克先生克制绅士／叙述者反讽（「深受旁人敬重——也深受他自己敬重」）；美国线勒弗罗伊粗鄙腔对照（子儿/私了/老伙计）；体例：卷题「# Part I / 第一部」并入卷首章+章题「## 罗马数字照搬 英文 / 中文」+罗马编号两卷重排照实保留+第20章源文误号 VII 照保留；书信 blockquote+粗体抬头+逐行落款沿 12/17/20 章先例；圣经引文按和合本（路得记）；拉丁/希腊文斜体照录直译附原文（Amo/in terrorem/τυπτω）；跨章对齐判例：metropolitan press=京师报界（ch15 立→ch17 改 10 处→ch24 沿用）、基尔布雷克（ch18 立→ch21 改 8 处）；*niggers* 时代语言按出版译例如实译出留审核；终章副牧师职悬置收束 |
