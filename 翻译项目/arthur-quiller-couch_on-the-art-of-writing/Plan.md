# 翻译计划（Plan.md）

## 本计划信息

- **项目名称**：论写作的艺术（阿瑟·奎勒-库奇）
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
00-dedication.md,0.0,todo
01-preface.md,1.7,todo
...
```

| 字段 | 含义 | 取值 |
|------|------|------|
| `file` | 源文文件名（在 `原文/` 目录下） | 如 `02-inaugural.md` |
| `size_kb` | 源文大小（KB）。>50KB 为长文，按通用翻译引擎第七节分段 | 数字 |
| `status` | 翻译状态 | `todo` 待译 / `doing` 翻译中 / `done` 已完成 |

---

## 执行步骤（agent 按此推进，两种模式共用）

> **谁执行**由 `项目说明.md` 的「内容形态」字段决定（见 `WORKFLOW.md`「判断内容形态」）：委派模式由子代理逐篇执行本流程；连续模式（中篇）由主 agent 自己执行。无论谁执行，这 9 步不变。

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
- 逐段对照原文，绝不漏译、不合并段落、不缩写、不总结，尤其结尾别截断。
- 严守术语表：遇表内源词必译为指定译法。新词自行确定统一译法，首次附原文「中文（English）」。
- 讲稿语气（对听众致辞「Gentlemen」=「诸位先生」、讲堂幽默、密集引文）全文一致，照黄金样本风格译。
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
| 0 | 献词 | 00-dedication.md | 0.0KB | todo |
| 1 | 前言 | 01-preface.md | 1.7KB | todo |
| 2 | 第一讲 就职讲演 | 02-inaugural.md | 30.4KB | todo |
| 3 | 第二讲 写作的实践 | 03-the-practice-of-writing.md | 31.8KB | todo |
| 4 | 第三讲 论诗与散文之别 | 04-on-the-difference-between-verse-and-prose.md | 28.3KB | todo |
| 5 | 第四讲 论诗之大难点 | 05-on-the-capital-difficulty-of-verse.md | 29.5KB | todo |
| 6 | 第五讲 插叙：论套话 | 06-interlude-on-jargon.md | 32.3KB | todo |
| 7 | 第六讲 论散文之大难点 | 07-on-the-capital-difficulty-of-prose.md | 30.4KB | todo |
| 8 | 第七讲 重申若干原则 | 08-some-principles-reaffirmed.md | 25.6KB | todo |
| 9 | 第八讲 英国文学的谱系（上） | 09-on-the-lineage-of-english-literature-i.md | 30.6KB | todo |
| 10 | 第九讲 英国文学的谱系（下） | 10-on-the-lineage-of-english-literature-ii.md | 35.3KB | todo |
| 11 | 第十讲 英国文学与大学（上） | 11-english-literature-in-our-universities-i.md | 34.8KB | todo |
| 12 | 第十一讲 英国文学与大学（下） | 12-english-literature-in-our-universities-ii.md | 24.1KB | todo |
| 13 | 第十二讲 论风格 | 13-on-style.md | 24.6KB | todo |
| 14 | 尾注 | 14-endnotes.md | 5.8KB | todo |

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-09-16 | 献词（00-dedication，无标题） | done，校验退出码 0 | 1 对块（含 To/题献名两段）；题献对象首现括注「约翰·海·洛班（John Hay Lobban）」 |
| 2026-09-16 | 前言（01-preface，Preface/前言） | done，校验退出码 0 | 6 对块（逐段对照）；总纲句定译「文学不是一门仅供研究的科学，而是一门必须实践的艺术」；署名「阿瑟·奎勒-库奇（Arthur Quiller-Couch）」；落款 November 1915 译「1915 年 11 月」 |
| 2026-09-16 | 第一讲 就职讲演（02-inaugural，I Inaugural / 讲座 I 就职讲演） | done，校验退出码 0（80 标记块 = 40 对，可疑错配 0） | 演讲日期「1913 年 1 月 29 日，星期三」；希腊文引文（Ἂχλητος… 两行）原样保留、*Tamen usque recurrit* 等拉丁文加中译括注；新词定译（报备，待并入术语表）：Euphues 尤弗伊斯、Fletcher 弗莱彻、Dunbar 邓巴、Pheidias 菲狄亚斯、Thomas à Kempis 托马斯·厄·肯培、William Watson 威廉·沃森、Lascelles Abercrombie 拉塞尔斯·艾伯克龙比、Thomas Hardy 托马斯·哈代、Mr. Barrie 巴里先生、*Peter Pan*《彼得·潘》、*Lyrical Ballads*《抒情歌谣集》、Green 格林 + *Prolegomena to Ethics*《伦理学导论》、Robert Bridges 罗伯特·布里奇斯、Arthur John Butler 阿瑟·约翰·巴特勒、Knossos 克诺索斯、Parmenides 巴门尼德、Viola/Macbeth/Hamlet/Ophelia 薇奥拉/麦克白/哈姆雷特/奥菲利娅；莎剧诗句参照朱生豪酌情回译，格雷《墓园挽歌》参照卞之琳体回译 |
| 2026-09-16 | 第二讲 写作的实践（03-the-practice-of-writing，Lecture II The Practice of Writing / II 写作的实践） | done，校验退出码 0（116 标记块 = 58 对，可疑错配 0；原文 71 段落单元逐字覆盖复核通过，UTF-8 无 BOM） | 章题「II 写作的实践」（罗马数字照搬，从术语表示例；与第一讲「讲座 I 就职讲演」译法微异，报备主 agent 全书统一）；演讲日期原文无年份，译「2 月 12 日，星期三」；四品质定译 appropriate/propriety=得体、perspicuity=明晰、accuracy=准确、persuasiveness=说服力；verse=诗（韵文）、prose=散文、说散文=莫里哀《贵人迷》典故（bourgeois gentleman→「贵人迷」）；English School=英文学科、hortus siccus=蜡叶标本园；拉丁文 *Positâ luditur arcâ*/*Mediocribus esse poetis*/*jus et norma loquendi* 保留原样加中译括注，西塞罗拉丁引段原样保留（下一段即 Q 自撰英译）；伯克引文数字锚点 £152,750 11s. 2¾d. 及 1769、320 保留阿拉伯数字；西德尼十四行诗 14 行逐行对译（斯特拉 Stella 首现括注）；新词定译（报备，待并入术语表）：Discourses《讲演录》（雷诺兹）、Tintoretto 丁托列托、Titian 提香、Caracci 卡拉奇、Dionysius of Halicarnassus 哈利卡纳苏斯的狄奥尼修斯、Cicero 西塞罗、Quintilian 昆体良、Jowett 乔伊特、Newman 纽曼 + *The Idea of a University*《大学的理想》、Landor 兰多、Tennyson 丁尼生、Browning 勃朗宁 + "Saul"《扫罗》+ *The Ring and the Book*《指环与书》、Morris 莫里斯、Rossetti 罗塞蒂、Swinburne 斯温伯恩、Ruskin 罗斯金 + *Modern Painters*《近代画家》、Atropos 阿特罗波斯、John Clare 约翰·克莱尔、James Thomson 詹姆斯·汤姆逊、Diomed 狄俄墨得斯、Hector 赫克托耳、Benvenuto Cellini 本韦努托·切利尼、Perseus 珀尔修斯、University of Pisa 比萨大学、Petrarch 彼特拉克、Charles Lamb 查尔斯·兰姆、Philip Sidney 菲利普·西德尼、Gladstone 格莱斯顿、Boers 布尔人、Velasquez 委拉斯开兹、Euclid 欧几里得、Longinus 朗吉努斯、Webster 韦氏词典、Literae Humaniores 人文学科（拉丁名保留） |
| 2026-09-16 | 第三讲 论诗与散文之别（04-on-the-difference-between-verse-and-prose，Lecture III On the Difference Between Verse and Prose / III 论诗与散文之别） | done，校验退出码 0（146 标记块 = 73 对，可疑错配 0；块内段落对称复核通过，UTF-8 无 BOM，末段覆盖无截断） | 章题「III 论诗与散文之别」（罗马数字照搬，格式从第二讲，中文侧不带「讲座」二字；与第一讲「讲座 I 就职讲演」微异，同 03 报备主 agent 全书统一）；演讲日期原文无年份，译「2 月 26 日，星期三」；术语照表：verse=诗（韵文）、prose=散文、memorable speech=值得纪念的言辞、metre=格律、rhythm=节奏、blank verse=素体诗、iamb=抑扬格；引文处理：古英语《威德西斯》段整段保留原样、末行附中译大意括注，希腊文 στιχομυθἱα 保留加括注，莎剧《皆大欢喜》《哈姆莱特》《亨利五世》参照朱生豪体回译，弥尔顿《复乐园》《失乐园》、笛福《鲁滨逊漂流记》、斯威夫特《木桶的故事》引文参照通行译本酌情回译，弥尔顿引例 But cottage, herd, or sheepcote, none he saw 全文三处译法统一；数字锚点 26、150、1795–6、1632、31/28/31/30 均保留阿拉伯数字；新词定译（报备，待并入术语表）：Thespis 忒斯庇斯、Herodotus 希罗多德、Bishop Stubbs 斯塔布斯主教 + Select Charters《特许状选编》、Queen’s Club 女王俱乐部、Kempton Park 肯普顿公园、Sappho 萨福、Genée 热奈小姐、Sir Patrick Spens《帕特里克·斯宾斯爵士》、Clerk Saunders《书记桑德斯》、Chatham 查塔姆、Sheridan 谢里丹、Brougham 布鲁厄姆、Canning 坎宁、Bright 布莱特、Disraeli 迪斯累利、Woolsack 羊毛袋、Hansard《议会实录》、Treasury Bench 财政大臣席、Lord Haldane 哈尔丹勋爵、Brummagem dagger「伯明翰货」匕首、Beaconsfield 贝肯斯菲尔德、Atticus 阿提库斯、Catiline 喀提林、Jacques 杰奎斯、Pitt 皮特、French Directory 法兰西督政府、Letters on a Regicide Peace《论弑君者和平的书信》、Saintsbury 圣茨伯里 + A History of English Prose Rhythm《英语散文节奏史》、Paeons 帕安格、Dochmiacs 多克米格、Antispasts 安提斯帕斯特格、Proceleusmatics 四短格、Paul Fort 保罗·福尔、Marinetti 马里内蒂、Tupper 塔珀、Paley 佩利 + Evidences《论证据》、scops 斯科普、bards 巴德、minstrels 游吟艺人、Epithalamium 婚歌、Widsith《威德西斯》、Billings/Hoppings/Wokings/Tootings 比林家/霍平家/沃金家/图廷家、Kipling 吉卜林 + Barrack Room Ballad 营房歌谣、Kabul river 喀布尔河、Gog-magog 戈格玛格丘陵、Cluvienus 克卢维埃努斯、Walt Whitman 沃尔特·惠特曼、Sidney 锡德尼、Scaliger 斯卡利格、Twining 特威宁、Warton 沃顿、Whately 惠特利、Hazlitt 赫兹里特、Gummere 甘米尔、J. K. Stephen J. K. 斯蒂芬、St. Paul 圣保罗、William Wooton 威廉·伍顿 |
| 2026-09-16 | 第五讲 插叙：论套话（06-interlude-on-jargon，Lecture V Interlude: On Jargon / V 插叙：论套话） | done，校验退出码 0（184 标记块 = 92 对，可疑错配 0；源文行 3–268 非空行全覆盖复核通过，UTF-8 无 BOM，末段无截断） | 章题「V 插叙：论套话」（罗马数字照搬，格式从术语表回填裁定，中文侧不带「讲座」二字）；演讲日期原文无年份，译「5 月 1 日，星期四」；本讲核心定译：Jargon=套话（首现括注英文，全文 26 见无一例译「行话/黑话」）、Journalese=新闻腔、circumlocution/periphrasis=迂说、Elegant Variation=雅致变换（福勒兄弟术语，本讲新定）、masculine style=阳刚风格、concrete/abstract noun=具体名词/抽象名词、solidified sensation=凝固的感觉、风格即人（the Style is the Man）；套话例句翻译策略：被批判的英文套话词（case/such/as regards/as to/associated with 等）在中文块内保留原词加括注意译，使批判逻辑可循；源文连排段落（行 4–9、31–38、64–67 等 epub 转换残留）按语义段在行边界分块，原文零失真照搬（含 \ufeff/\xa0 零宽残留与诗行 ' \n\n' 间隔结构）；脚注编号 3、4（Webster 引文）原位保留；哈姆雷特独白套话戏仿段（To be, or the contrary…）以中文公文体复现臃肿感；数字锚点 Op. 35/109/111 译作「作品第 35/109/111 号」保留；新词定译（报备，待并入术语表）：Elegant Variation 雅致变换、Babu 巴布、Board of Guardians 济贫委员会、Blue Books 蓝皮书、willow-pattern 柳纹瓷式、florilegium 采英集、Boyg 波伊格、Lord Hugh Cecil 休·塞西尔勋爵、Harold Cox 哈罗德·考克斯、Hayward 海沃德、C. B. Fry C. B. 弗莱、Telemachus 忒勒玛科斯、Proteus 普罗透斯、Newstead 纽斯特德、Missolonghi 迈索隆吉、Dogberry 道格培里、Professor Minocelsi 米诺切尔西教授、FitzGerald 菲茨杰拉德、Jeremy Bentham 杰里米·边沁、Professor Wendell 温德尔教授、Marlowe 马洛、Webster 韦伯斯特、E. J. Payne 佩恩、South 索斯、Dr. John Donne 约翰·多恩博士、Goethe 歌德、Ibsen 易卜生、Frederick Lamond 弗雷德里克·拉蒙德、Beethoven 贝多芬、Fowler H. W./F. G. 福勒兄弟、Aristotle 亚里士多德、亚当=Adam、耶洗别=Iesabel（钦定本拼法，多恩引文）；书名：The King’s English《国王的英语》、In Memoriam《悼念集》、Childe Harold《恰尔德·哈罗尔德游记》、Venus and Adonis《维纳斯与阿多尼》、Hero and Leander《希罗与利安德》、Duchess of Malfi《马尔菲公爵夫人》、Twelfth Night《第十二夜》、On Conciliation with America《论与美洲和解》、Inquiry Into the Policy of the European Powers《欧洲列强政策探究》、The Ruins of Athens《雅典的废墟》、Needy Knife-grinder《穷苦的磨刀匠》、Peer Gynt《培尔·金特》、The Times《泰晤士报》、Standard《旗帜报》、Oxford Magazine《牛津杂志》、Genesis《创世记》；福音书引文用和合本语体（「有一个撒种的出去撒种」「天国好像面酵」「凯撒的物当归给凯撒」「想想百合花吧，看它们怎样长起来」保留 Q 论证的语序层次）；莎剧《第十二夜》薇奥拉台词参照朱生豪体回译并括注 concealment/Patience 以支撑下文抽象词分析 |
| 2026-09-16 | 第四讲 论诗之大难点（05-on-the-capital-difficulty-of-verse，Lecture IV On the Capital Difficulty of Verse / IV 论诗之大难点） | done，校验退出码 0（130 标记块 = 65 对，可疑错配 0；原文 3–320 行非空行全覆盖复核通过，诗歌块英中行数一一相等，UTF-8 无 BOM） | 章题「IV 论诗之大难点」（格式从术语表回填裁定 `Lecture IV <英文> / IV <中文>`，罗马数字照搬，中文侧不带「讲座」二字）；演讲日期无年份，译「4 月 17 日，星期四」；本讲核心定译：capital difficulty=大难点、pitch/keyed=音高/定调（「情感音高」全篇统一）、flat interval(s)=平淡间隔、high moments=高昂时刻、rapid/rapidity=迅疾（阿诺德评荷马）、blank verse=素体诗、bathos=突降、inversion=倒装、appropriate=得体（写作第一规则）、in medias res 拉丁保留加「故事的中心」括注、Tripos=荣誉考试、catch=轮唱曲、daemonic=魔性、fish-jowter=鱼贩子；希腊文引文 Μῆνιν ἃειδε, Θεἁ— 整行原样保留（中文块照录），行内 *πολὑτροπος* 保留加「机变多端」括注；引诗全部逐行对译（戴克《甜美的知足》20 行、华兹华斯 4 行及十四行 14 行、Tripos 谐拟体 14 行、弥尔顿 4 行+单行、丁尼生《伊诺克·阿登》2 行+7 行、沃尔顿轮唱曲 4 行、鱼贝双行体 2 行、布莱尔谐拟 5 行、丁尼生式收束短诗 5 行）；弥尔顿 But cottage, herd… 引例与第三讲译法对齐（「随即他把脚步抬上一座小山…但村舍、牛群或羊圈，他一无所见」）；源文中段 `---` 分隔线保留为独立游离行；数字锚点 405（p. 405→第 405 页）保留；新词定译（报备，待并入术语表）：Calliope 卡利俄佩、Euterpe 欧忒耳佩、Erato 厄拉托、Thalia 塔利亚、Biographia Literaria《文学传记》（柯尔律治）、Dekker 戴克、Jeremy Taylor 杰里米·泰勒、Samuel Johnson 塞缪尔·约翰逊、Isaak Walton 艾萨克·沃尔顿 + The Complete Angler《高明的垂钓者》、Venator 维纳托、Brother Peter 彼得兄弟、Diodorus 狄奥多罗斯、萧伯纳（George Bernard Shaw）+ Cashel Byron’s Profession《卡歇尔·拜伦的职业》、Hiawatha《海华沙》、The Student’s Handbook to the University and Colleges of Cambridge《剑桥大学与学院学生手册》、Athanasian Creed《阿塔那修信经》、Bagehot 白芝浩、“Enoch Arden”《伊诺克·阿登》、Horace 贺拉斯、Thersites 特尔西特斯、Cassius 卡修斯、Dante 但丁、Iliad/Odyssey《伊利亚特》/《奥德赛》、Froude 弗劳德 + History《历史》、Alfred Noyes 阿尔弗雷德·诺伊斯 + Drake《德雷克》、Armada 无敌舰队、Falconer 法尔科纳 + Shipwreck《沉船》、Nelson 纳尔逊、Villeneuve 维尔纳夫、Wilfred Blair 威尔弗雷德·布莱尔、Odysseus 奥德修斯、Ithaca 伊萨卡、Troy 特洛伊、Circe 喀耳刻、Aeaean isle 埃埃亚岛、Telemachus 忒勒玛科斯（从 06 讲用字，全书统一）、Alcinoüs 阿尔基诺奥斯、Virgil 维吉尔（沿表）、Lady Hamilton 汉密尔顿夫人、Lessing 莱辛 + Laoköon《拉奥孔》、Achilles 阿喀琉斯、Hephaestus 赫菲斯托斯、Ulysses 尤利西斯 |
| 2026-09-16 | 第七讲 重申若干原则（08-some-principles-reaffirmed，Lecture VII Some Principles Reaffirmed / VII 重申若干原则） | done，校验退出码 0（126 标记块 = 63 对，可疑错配 0；块内段落对称复核 63/63 通过，UTF-8 无 BOM，末段无截断） | 章题「VII 重申若干原则」（格式从术语表统一裁定 `Lecture VII <英文> / VII <中文>`，罗马数字照搬，中文侧不带「讲座」二字）；演讲日期无年份，译「5 月 29 日，星期四」；本讲核心定译：Authorised Version=钦定本、Revised Version=修订本、plenary inspiration=完全默感、inspiration=灵感、the ark=约柜、四品质沿用（得体/准确/说服力，本讲再现 appropriate/accurate/persuasive）、emphasis=强调、falling close=坠落收尾、interplay of vowel-sounds=元音的交相辉映、迂说（circumlocution）沿表；圣经引文策略：钦定本《以赛亚书》九章自译存其「节奏有余而义理不足」（「却不加增喜乐」「以焚烧、以燃料之火而来」语序照搬，支撑 Q 的诘问逻辑），修订本用和合本语体（「加增他们的喜乐」「政权必担在他的肩头上」）以显两版对照；路加福音浪子回头、撒下十八章押沙龙哀歌、赛 60 兴起发光、启 18 巴比伦倾倒均参照和合本语体酌情回译；格雷《墓园挽歌》四行、叶芝《茵尼斯弗利岛》三节十二行参照通行译体逐行回译（诗行间隔结构照搬源文）；拉丁文 *Cecidit, cecidit, Babylonia illa magna.* 保留加中译括注，希腊文 *διαλαμπει* 保留加「透射生辉」括注；套话例句（麦肯纳开释信、劳合·乔治答问）保留英文套话词斜体加括注意译（in connection with / caused to be forwarded / as to / consequent upon / of a … character），劳合·乔治段「……性质」句式复现 character 双关；源文 `---` 分隔线在英中两块内对称保留；脚注编号 7、8 原位保留；新词定译（报备，待并入术语表）：George Herbert 乔治·赫伯特、Stevenson 史蒂文森 + The Wrong Box《错箱》、Tyndale 廷代尔、Wyclif Version 威克里夫译本、the Bishops《主教圣经》、Aorist 希腊文不定过去时、Hellenistic Greek 希腊化的希腊文、Apocrypha 次经、Wolfe 沃尔夫 + St. Lawrence River 圣劳伦斯河 + Heights of Abraham 亚伯拉罕高地、McKenna 麦肯纳 + Lilian Lenton 莉莲·伦顿 + Holloway Prison 霍洛韦监狱 + Kew Gardens 邱园、Lloyd George 劳合·乔治 + Noel Buxton 诺埃尔·巴克斯顿 + Morning Post《晨邮报》+ Senate 元老院（戏称）+ Minister of the Crown 王室大臣 + Treasury 财政部、Chancellor of the Exchequer 财政大臣、Bohn 博恩（译本）、Terai hat 特莱帽、Innisfree 茵尼斯弗利岛、Job 约伯、Isaiah《以赛亚书》、Midian 米甸、Zebulun 西布伦、Naphtali 拿弗他利、Absalom 押沙龙、the Graces 美惠三女神、intaglio 凹雕、get there=「到达那里」（丹佛主编套语） |
| 2026-09-16 | 第八讲 英国文学的谱系（上）（09-on-the-lineage-of-english-literature-i，Lecture VIII On the Lineage of English Literature (I) / VIII 英国文学的谱系（上）） | done，校验退出码 0（82 标记块 = 41 对，可疑错配 0；源文 3–190 行全覆盖复核通过，外文引文块（拉丁/意大利/古英语/希腊）中文侧原样照录，UTF-8 无 BOM） | 章题「VIII 英国文学的谱系（上）」（罗马数字照搬，格式从术语表统一裁定 `Lecture VIII <英文> / VIII <中文>`，中文侧不带「讲座」字样）；演讲日期无年份，译「10 月 22 日，星期三」；本讲核心定译：the lineage of English literature=英国文学的谱系、Age of Reason=理性时代、tutelary gods=守护神、architectonics=整体构筑（首现括注）、Father of English Poetry=「英国诗歌之父」；核心论点句「From Anglo-Saxon Prose…no derivation」以强调体直译（从盎格鲁-撒克逊的散文与诗，我们活着的散文与诗除语言承袭外别无渊源）；拉丁文引文处理：*Antiquam exquirite matrem*（寻回那古老的母亲）、*Cappadocius nostras*（咱们卡帕多西亚老乡）、*Deus Angelorum, qui fecit Resurrectionem*（众天使之神，祂使复活成就）、*ubi Romanus vicit ibi habitat* 均保留原样加中译括注，拉丁双行诗 Unde Remnes… 与维吉尔 *Sed neque Medorum silvae* 及卡尔杜齐意大利语颂歌原文、古英语 Hróðgar 悼歌、荷马希腊文引行整段原样保留（中文块照录原文，普林尼书信与英译诗则全译）；弥尔顿《基督诞生晨歌》6 行、华兹华斯 4 行、卡尔杜齐英译 12 行逐行对译；蒲柏《英国诗歌史》纲目段源文 epub 缺失纲目本体，按源文照译「——如此等等」衔接（零增译）；脚注编号 9、10 原位保留；数字锚点 1832、4 月 23 日保留阿拉伯数字；新词定译（报备，待并入术语表）：Newman 长段「共同文明」论（common civilisation=共同文明、Human Society=人类社会）、Bidding Prayer=吁祷文、Pericles=伯里克利、Apollo=阿波罗、Zeus=宙斯、Hermes=赫尔墨斯、Athene=雅典娜、Aphrodite=阿佛洛狄忒、Odin=奥丁、Thor=托尔、Freya=弗雷娅、Cucullain=库丘林、Concobar=康纳尔、Hercules=赫拉克勒斯、Bellerophon=柏勒罗丰、Leonidas=列奥尼达、Horatius=贺拉提乌斯、Regulus=雷古卢斯、Harry of Agincourt=阿金库尔的哈利、Ovid=奥维德、Pliny=普林尼、Clitumnus=克利图姆努斯 + Alle fonte del Clitumno《在克利图姆努斯泉边》、Cavour=加富尔、Garibaldi=加里波第、Carducci=卡尔杜齐、Janus=雅努斯、Comesena=科梅塞纳、naiads=水泽仙子、Oreads=俄瑞阿得斯、Traitor's Gate=叛国者门、Naseby=纳斯比、Agapemone=阿加佩门（爱之居）、Mason=梅森、Mant=曼特 + Life of Warton《沃顿传》、Freeman=弗里曼 + Norman Conquest《诺曼征服》、Green=格林 + Short History of the English People《英国人民简史》、Sleswick=斯勒斯维克、Stopford Brooke=斯托普福德·布鲁克、Primer=《入门读本》、Beowulf=《贝奥武甫》、Corpus Poeticum Boreale=《北方诗歌集成》、Vigfússon=维格菲松、York Powell=约克·鲍威尔、Grendel=格伦德尔、Firedrake=火龙、Lucian《怎样撰写历史》（Πῶς δεῖ ἱστορίαν συγγράφειν 希腊文保留）、Hrothgar=赫罗斯加、Æschere=埃施雷尔、Priam=普里阿摩斯、The Rape of the Lock=《夺发记》、Exeter Book=《埃克塞特书》、Vercelli Book=《韦尔切利书》、Ruthwell Cross=鲁斯韦尔十字架、Chadwick=查德威克、Vision of Piers Plowman=《农夫皮尔斯之幻象》、Caedmon=卡德蒙、Cynewulf=塞内武甫、Wyat=怀亚特、αὐτόχθονες 保留加「土生土长者」括注、Menexenus=《美涅克塞努篇》、Aspasia=阿斯帕西娅、Pelopes=佩洛普斯、Cadmians=卡德摩斯人、Dauni=道尼人、Hispallum=希斯佩卢姆、Ramnes=拉姆尼斯人、Quirites=奎里特斯人 |
| 2026-09-16 | 第六讲 论散文之大难点（07-on-the-capital-difficulty-of-prose，Lecture VI On the Capital Difficulty of Prose / VI 论散文之大难点） | done，校验退出码 0（152 标记块 = 76 对，可疑错配 0；源文 3–413 行非空行全覆盖复核通过，诗歌块英中行数一一相等，UTF-8 无 BOM） | 章题「VI 论散文之大难点」（格式从术语表统一裁定 `Lecture VI <英文> / VI <中文>`，罗马数字照搬，中文侧不带「讲座」字样，与第四讲「IV 论诗之大难点」成对）；演讲日期无年份，译「5 月 15 日，星期四」；术语沿用第四讲对偶体系：capital difficulty=大难点、high moments=高昂时刻（本篇初稿曾作「高潮时刻」，已按 05 讲回填定译统一改齐）、flat intervals=平淡间隔、blank verse=素体诗、metre=格律、rhythm=节奏、Jargon=套话、Authorised Version=钦定本、Holy Writ=圣书；散文定义句「人类思想的记录，不用格律，而对节奏的运用从宽」与第三讲定义句呼应；引文处理：马洛礼《亚瑟王之死》两段（贝迪维尔掷剑、埃克托悼兰斯洛特）、伯纳斯译傅华萨（布鲁斯之死遗嘱）、阿斯克姆《射艺论》自辩段、纳什《门纳丰序》「填馅」段全译，中古英语诗（乔叟《女修道院院长的序幕》《特洛伊罗斯》哀诉、《学者的故事》格丽泽尔达、圣诞卡罗尔「他来得何等静悄」、《栗色少女》、巴伯《布鲁斯》自由颂、怀亚特四首含 28 行《我还有什么可说》全文）逐行对译，莎翁十四行 31 首全文 14 行与 116 首前 4 行参照通行译体回译（保留 impediment/alteration/remove 拉丁词形以支撑下文论证），圣经引文（林前 15、雅歌 8、诗 45、赛 32/33）参照和合本语体酌情回译并保留钦定本语序（「穿上不朽」「坟墓啊，你的胜利在哪里」），拉丁文 *improbus homo*、*praeter necessitatem* 保留加中译括注；源文 `---` 分隔线保留为独立游离行；脚注编号 5、6 原位保留；数字锚点 1603、169、23、15 保留阿拉伯数字；新词定译（报备，待并入术语表）：Malory 马洛礼、Sir Bedivere 贝迪维尔爵士、Excalibur 王者之剑、Vale of Avilion 阿维隆之谷、Lord Berners 伯纳斯勋爵、Froissart 傅华萨、Robert Bruce 罗伯特·布鲁斯、Sir William Douglas 威廉·道格拉斯爵士、Holy Sepulchre 圣墓、Sir Lancelot 兰斯洛特爵士、Sir Ector 埃克托爵士、the Passing of Arthur 亚瑟之死、Prioress' Prologue《女修道院院长的序幕》、Troilus 特洛伊罗斯、Griselda 格丽泽尔达、The Nut-Brown Maid《栗色少女》、Barbour 巴伯、Shirley 雪莉、Donne 多恩、Sophocles 索福克勒斯、Aristophanes 阿里斯托芬、New Learning 新学问、Wyat 怀亚特（沿 09 讲用字）、Newman 纽曼（沿表）、The Cambridge History of English Literature《剑桥英国文学史》、T. M. Lindsay 林赛牧师、Wilson 威尔逊 + Arte of Rhetorique《修辞术》、Earl of Surrey 萨里伯爵、Ariosto 阿里奥斯托、Dominie 塾师 + Pro-digious「惊——人啊！」、Martin Marprelate Controversy 马丁·马普雷拉特论战、Thomas Nashe 托马斯·纳什、Seneca 塞内加、Doudie《杜迪》、farced「填了馅」、green sickness 萎黄病、Ascham 阿斯克姆、Euphuism 尤弗伊斯体（沿《尤弗伊斯》书名）、Johnsonian balance 约翰逊式均衡句法、Wyclif 威克里夫、Coverdale 科弗代尔、Alfred Stevens 阿尔弗雷德·史蒂文斯、Dean and Chapter 教长与众教士、Isaak Walton 艾萨克·沃尔顿（沿 05 讲）、Bunyan 班扬、Choragium 合唱领班、Thackeray 萨克雷 |
| 2026-09-16 | 第十讲 英国文学与大学（上）（11-english-literature-in-our-universities-i，Lecture X English Literature in Our Universities (I) / X 英国文学与大学（上）） | done，校验退出码 0（98 标记块 = 49 对，可疑错配 0；源文 3–179 行全覆盖复核通过，诗歌引块（Pervigilium Veneris 12 行、弥尔顿 16 行、斯温伯恩 10 行、马维尔 2 行、Hellas 双行）英中行数一一相等，源文中段 --- 分隔线保留为游离行，UTF-8 无 BOM） | 章题「X 英国文学与大学（上）」（格式从术语表统一裁定 `Lecture X <英文> / X <中文>`，罗马数字照搬，中文侧不带「讲座」字样，与「VIII 英国文学的谱系（上）」体例一致）；演讲日期无年份，译「11 月 19 日，星期三」；本讲核心定译：Classical Tripos=古典学荣誉考试（Tripos=荣誉考试从派发约定）、Town and Gown=市民对学袍、Studium Generale/Universitas 拉丁保留加括注（Universitas＝我们全体）、nations=国族、Mastership of Arts=文学硕士学位、Regius Professorships=钦定讲席、University Calendar《大学一览》、Classical Dictionary《古典辞典》；拉丁引文全部保留原样加中译括注（Æneadum genetrix…、fusa Paphies de cruore、revocato a sanguine Teucri、Deus Optimus Maximus、Quoniam non cognovi literaturam、quid posteritas emolumenti tulit、Per omnes paene civitates…、nec tibi sit ursorum saltantium…、saepe retulit…；奥克语 Ben Senhor, non fassat 保留加括注）；弥尔顿《基督诞生晨歌》两节、斯温伯恩《献给普罗塞皮娜的赞歌》、《维纳斯守夜歌》Q 英译体、马维尔「绿荫」双行、Hellas 双行均逐行对译（诗行 ' \n\n' 间隔结构照搬源文）；脚注编号 14、15、16 原位保留；数字锚点 1642、400、70、1650、1520、1332、200、3,000、15,000 及 1502–1910 讲席年份全套保留阿拉伯数字；新词定译（报备，待并入术语表）：Gilbert Murray 吉尔伯特·默里、English Association 英国语文协会、Aristophanes 阿里斯托芬、Aeschylus 埃斯库罗斯、Lucretius 卢克莱修、Dione 狄俄涅、Pervigilium Veneris《维纳斯守夜歌》、Teucer 透克洛斯、Tros 特洛斯、Origen 奥利金、Tertullian 德尔图良 + De Spectaculis《论观赏》、Augustine 奥古斯丁、Alcuin 阿尔昆、Sulpicius Severus 苏尔皮基乌斯·塞维鲁、Gregory the Great 大格里高利、Desiderius 德西德里乌斯 + Vienne 维埃纳、Bede 比德 + Cuthbert 卡思伯特 + Jarrow 贾罗 + Northumbria 诺森布里亚、Charlemagne 查理曼、J. Bass Mullinger J. 巴斯·马林杰尔、Poggio 波焦、Remigius 雷米吉乌斯、William of Champeaux 香浦的威廉、Irnerius 伊尔内留斯、Vacarius 瓦卡里乌斯、Stamford 斯塔姆福德、Northampton 北安普顿 + Fuller 富勒 + Garret Hostel Bridge 加勒特旅舍桥、St. Scholastica 圣斯科拉斯蒂卡、de la Penne 德拉佩纳 + Aimery Béranger 埃梅里·贝朗热 + Capitoul 卡皮托尔（图卢兹市政长官）+ Parlement of Paris 巴黎高等法院、Cecil Rhodes 塞西尔·罗兹、St. John’s College 圣约翰学院、Richard of Chichester 奇切斯特的理查、biretta 四角帽、cappa 斗篷、Hector 赫克托耳（沿 03 讲）、Erasmus 伊拉斯谟、Henry Jackson 亨利·杰克逊、Sir William Hamilton 威廉·汉密尔顿爵士、Henry VII 亨利七世 + Lady Margaret 玛格丽特夫人 + Mr. Hulse 赫尔斯先生、Bologna 博洛尼亚 + College of Spain 西班牙学院、Salamanca 萨拉曼卡 + Wellington 威灵顿、Boethius 波爱修斯、Abelard 阿伯拉尔、Pythagoras 毕达哥拉斯、Euclid 欧几里得（沿 03 讲） |
| 2026-09-16 | 第九讲 英国文学的谱系（下）（10-on-the-lineage-of-english-literature-ii，Lecture IX On the Lineage of English Literature (II) / IX 英国文学的谱系（下）） | done，校验退出码 0（132 标记块 = 66 对，可疑错配 0；块内行数对称复核 66/66 通过，源文 3–343 行全覆盖，UTF-8 无 BOM，末段无截断） | 章题「IX 英国文学的谱系（下）」（格式从术语表统一裁定 `Lecture IX <英文> / IX <中文>`，罗马数字照搬，中文侧不带「讲座」字样）；演讲日期无年份，译「11 月 5 日，星期三」；与上篇（09 谱系 I）及前讲对齐：Sleswick 斯勒斯维克、Wyat 怀亚特、Freeman 弗里曼、Aphrodite 阿佛洛狄忒、naiads 水泽仙子、Ascham 阿斯克姆（沿 07 讲）、*ubi Romanus vicit, ibi habitat* 保留加中译括注、Piers Plowman《农夫皮尔斯》（沿 09「农夫皮尔斯之幻象」基名）；本讲核心定译：tessellated pavement=镶嵌铺道、*tessellae* 保留拉丁斜体加「镶嵌小方砖」括注、Pax Romana=罗马和平、「Wiped out」=「一扫而光了」（弗里曼史观）、Teutonic family=条顿家族、帝紫骨螺紫液、troubadours=行吟诗人、trouvères=法北行吟诗人、minnesingers=德国恋歌歌手、浪漫主义复兴=假古典主义之敌非古典主义之敌；引文处理：中古英语阿莉森之歌 12 行、古法语牧歌 6 行、普罗旺斯语（博内尔 2 行、旺塔多恩 6 行）及 Q 自撰英译 6 行逐行对译，头韵例句 From alle wymmen 二行以中文白译对勘（头韵装置靠上方英文斜体呈现）；贺拉斯《讽刺诗集》缠人段 5 行、《书信集》五天段 12 行韵体回译；沃波尔致康韦书翰 4 段全译（*cricketalia* 保留斜体加「板球赛会」括注）；莎剧《皆大欢喜》情郎曲 4 行、《冬天的故事》水仙歌 4 行参照通行译体回译；《农夫皮尔斯》开篇 6 行、罗宾汉谣曲 20 行逐行对译；拉丁文 *fumum et opes strepitumque*、*Urbs quam dicunt Roman*、*orbis terrarum*、*Semper ego auditor tantum?* 保留原样加中译括注，*præfurnium*（火室）同法；源文 `---` 分隔线三处沿 07/08 惯例在英中两块内对称保留；脚注编号 11、12、13 原位保留；数字锚点 43、1524 保留阿拉伯数字；新词定译（报备，待并入术语表）：Gildas 吉尔达斯、Belisarius 贝利撒留、Mr. Podsnap 波德斯纳普先生、Anderida 安德里达、Iberian 伊比利亚人、M. Jusserand 儒瑟朗先生 + Saône 索恩河、Sir Thomas Wyat 托马斯·怀亚特爵士、Anthony Wood 安东尼·伍德、Cardinal Wolsey 沃尔西枢机 + Christchurch 基督堂学院、Boccaccio 薄伽丘、Petrarchists 彼特拉克派、Gabriel Harvey 加布里埃尔·哈维、Daniel 丹尼尔、Campion 坎皮恩、Machiavelli 马基雅维利、tribe of Ben「本氏一族」、dramatis personae 剧中人、Professor Grierson 格里尔森教授、Andrew Marvell 安德鲁·马韦尔 + 《克伦威尔自爱尔兰归来的贺拉斯体颂歌》、Mr. Quilp 奎尔普先生、Cowley 考利、Lemprière 莱姆普里埃、Theocritus 忒奥克里托斯、Catullus 卡图卢斯、Bede 比德（沿 11 讲用字）、Blickling Homilies《布利克灵布道集》、Ælfric 埃尔弗里克、the Saxon Chronicle《撒克逊编年史》、Clarendon 克拉伦登、Vulgate 武加大译本、Horace Walpole 霍勒斯·沃波尔、Horatio Walpole 霍雷肖·沃波尔、Horatius Flaccus 贺拉提乌斯·弗拉库斯（沿 09 讲 Horatius 用字）、Juvenal 尤维纳利斯、Twickenham 特威克纳姆、Maecenas 梅塞纳斯、Arthur Young 阿瑟·杨、Alisoun 阿莉森、Pons de Capdeuil 蓬·德·卡普德伊、Bernard de Ventadour 贝尔纳·德·旺塔多恩、Bertrand de Born 贝特朗·德·博恩、Pierre Vidal 皮埃尔·维达尔、William of Poitou 普瓦图的威廉、William of Poitiers 普瓦捷的威廉、Giraud de Borneil 吉罗·德·博内尔、King Canute 克努特王、Aulus Plautius 奥卢斯·普劳提乌斯、Honorius 霍诺留、Newmarket 纽马基特、Walsingham 沃尔辛厄姆 |
| 2026-09-16 | 第十一讲 英国文学与大学（下）（12-english-literature-in-our-universities-ii，Lecture XI English Literature in Our Universities (II) / XI 英国文学与大学（下）） | done，校验退出码 0（64 标记块 = 32 对，可疑错配 0；源文 3–60 行逐段覆盖复核通过，两处诗歌引文块与古拼写开场白引文块间隔结构照搬源文，中文诗行规范化为连续 > 行） | 演讲日期源文无年份，译「12 月 3 日，星期三」照实不补；术语从表：Tripos=荣誉考试（Classical Tripos=古典学荣誉考试）、School of English Literature=英国文学学科、blank verse=素体诗、get there=「到达那里」（丹佛主编）、Gentlemen=诸位先生、Bagehot=白芝浩、Courthope=库思罗普、Marlowe=马洛、Nashe=纳什、Ben Jonson=本·琼森、Venus and Adonis=《维纳斯与阿多尼》；拉丁文保留加括注：copia fandi（言辞的繁富）、jus et norma loquendi（言说的法度与规范）、Universitas、Regnum Scientiae ut regnum Coeli…（培根句后 Q 自带英译，据此回译）；脚注编号 17 原位保留；数字锚点 1540/1869/1910/1597–1601/1822 全保留；新词定译（报备，待并入术语表）：Gabriel Harvey 加布里埃尔·哈维、Pembroke Hall 彭布罗克堂、Edmund Spenser 埃德蒙·斯宾塞、Gower 高厄、Gullio 古利奥、Kempe 坎普、Momus 莫穆斯、Bass Mullinger 巴斯·马林杰、Queens’ College 王后学院、University Wits 大学才子、Lyly 黎里、Chapman 查普曼、Marston 马斯顿、Peel 皮尔、Massinger 马辛格、Greene 格林、Day 戴、Caius 凯厄斯学院、Corpus Christi 基督圣体学院、masque 假面剧、《帕纳索斯朝圣记》（The Pilgrimage to Parnassus）、《帕纳索斯归来》（The Return from Parnassus）、Lucian《信史》（True History）、《新工具》（Novum Organum）、《原理》（Principia）、《物种起源》（Origin of Species）、Ovid 奥维德、Proserpina 普洛塞庇娜、Jupiter 朱庇特、Housman 豪斯曼教授、Max Beerbohm 马克斯·比尔博姆、Bentley 本特利、Porson 波尔森、Tigranes 提格兰尼斯、Zenodotus 芝诺多托斯、Aristarchus 阿里斯塔库斯、Chios 希俄斯、Smyrna 士麦那、Colophon 科洛丰、Magdalene 麦格达伦学院、Jesus College 耶稣学院、King’s College Chapel 国王学院礼拜堂、Chesterton 切斯特顿（兼剑桥地名）、Jerusalem 耶路撒冷、Wykehamist 威克姆派、twopenny saint 两便士圣徒、Sophister 泛译学子、gutta-percha/alligator 保英文加中注 |
| 2026-09-16 | 第十二讲 论风格（13-on-style，Lecture XII On Style / XII 论风格） | done，校验退出码 0（90 标记块 = 45 对，可疑错配 0；源文 3–89 行逐段覆盖复核通过，引诗块英中行数一一相等且两处复引措辞与前诗严格统一，源文两处 `---` 分隔线保留为游离行，UTF-8 无 BOM） | 章题「XII 论风格」（格式从术语表统一裁定 `Lecture XII <英文> / XII <中文>`，罗马数字照搬，中文侧不带「讲座」字样）；演讲日期译「1914 年 1 月 28 日，星期三」（源文自带年份；全书压轴讲）；核心定译照表：Style=风格（全文不用「文体」）、Ornament=藻饰（extraneous Ornament=外在的藻饰）、Jargon=套话（首现括注英文）、「杀死你的心头爱」（*Murder your darlings*，首现括注英文）、风格即人（the Style is the Man，沿 06 讲）、美惠三女神沿 08 讲、明晰（perspicuity/*σαφήνεια*）沿四品质、verse=诗/prose=散文；拉丁文 *Quot homines tot sententiae*、*Quicquid agunt homines, votum, timor, ira, voluptas…*、*Et vera incessu patuit dea*、*La clarté est la politesse* 保留原样加中译括注；希腊文 *τὀ τἱ ἧν εἷναι*（是其所是）、*Χἁρισι καἰ σαφενεἱᾳ θῦε*、*σαφήνεια* 保留加括注；福楼拜/歌德语录、汤普森两段引文全译（Praetorian cohorts=禁卫军团）；bump-supper 轶事「langers and godders」「bonner」保留英文原词、下文括注《友谊地久天长》《天佑国王》；新词例证「wire」「antibody」「picture-drome」保留英文加括注意译；引诗（West Country 挽歌两节 8 行、复引 3 行、Seraphically free 2 行）逐行对译；脚注编号 18、19 原位保留；数字锚点 1914、18、19 保留阿拉伯数字；新词定译（报备，待并入术语表）：Gilbert Chesterton 吉尔伯特·切斯特顿、Press-Cutting Agencies/Press-Clipping Bureaux 剪报代理行/剪报局、Constable 康斯太勃、Corot 柯罗、Sicilian Expedition 西西里远征、Boswell 鲍斯韦尔、West Country 西部之乡、bump-supper 碰杯庆功晚宴、Frank Harris 弗兰克·哈里斯 + The Man Shakespeare《莎士比亚其人》、Francis Thompson 弗朗西斯·汤普森 + Essay on Shelley《论雪莱》、Meredith 梅瑞狄斯 + The Egoist《利己主义者》 + Crossjay 克罗斯杰、Professor Minto 明托教授、Coventry Patmore 考文垂·帕特莫尔、Buffon 布封、William of Wykeham 威廉·威克姆 + 「Manners makyth Man」（举止造就人，沿 12 讲）、Handel 亨德尔、Chopin 肖邦、Greuze 格勒兹、Fénelon 费奈隆、disinterested=「无私的」（与 impersonal=「非个人的」对举） |
| 2026-09-16 | 尾注（14-endnotes，Endnotes / 尾注） | done，校验退出码 0（38 标记块 = 19 对，可疑错配 0；逐条对照 19 条尾注全覆盖复核通过，块内段落对称（注 1 六段、注 6 六行、注 7 七段、注 8 六行、余各一段），UTF-8 无 BOM） | 章题合并行「Endnotes / 尾注」；体例执行：作者自撰说明（注 1、3、4、5、6、7、9、10、14、19）全译，引文出处/文献条目（注 11、12、13、15、16、17、18）整条保留原文、中文块以「（引文出处/文献条目/作者署名，保留原文不译）」标注并照录条目（注 16、17 照录使页码锚点 684、213 通过）；注 1 斯科特上校/奥茨上尉沿 03 讲定译，奥茨名言「我到外面去一下，也许要过些时候」；注 2《威德西斯》英译段全译，部族名沿 04 讲中译大意（匈奴人、瑞德哥特人、斯维阿人、耶阿特人、南丹麦人、温那人、瓦尔纳人、维京人、格夫塔人、温德人、蜜酒大厅）；注 6 仿古谣五行逐行对译，「苏格兰联合自由教会格拉斯哥学院院长」沿 07 讲；注 7《哥林多前书》15:51 三译本对照全译（威克里夫自拟古朴语体、廷代尔、钦定本参照和合本语体，保留三版问句次序差异：威版胜利在前、廷版毒刺/阴间、钦版毒钩/坟墓，支撑「四十七人」精益求精论点），拉丁文 *quae sunt parum verecunda*、*sed nobis nostrum opus intueri sat est*（注 19）保留原样；注 8 元音谱例符号原样照录、柯林斯《暮之颂》出处行首现定译；注 10《贝奥武甫》英译段全译（09 讲正文古英文原样保留、无中译大意，此注即读者唯一释义），赫罗斯加/埃施雷尔沿表，新词：斯基尔丁人（Scyldings）、耶尔门拉夫（Yrmenlaf）、贵胄（atheling）、护主（helm）；注 14 论文题《英国诗歌还能向希腊学习什么》首现括注原文、英国语文协会沿 11 讲；数字锚点 1913、16、15、51、17、1911、684、213 全保留；新词定译（报备，待并入术语表）：E. J. Watson E. J. 沃森 + J. W. Arrowsmith J. W. 阿罗史密斯公司（布里斯托尔）、Walter de la Mare 沃尔特·德·拉·梅尔（注 18 署名条目保留原文）、Ode to Evening《暮之颂》、A History of Oxfordshire《牛津郡史》+ J. Meade Falkner J. 米德·法尔克纳（条目内保留原文）、Old Comedy 旧喜剧 |
