# 《九解之案》前半卷（Part A：第 01–10 篇）审校报告

- **审校日期**：2026-10-06
- **质量等级**：B 良好（合格可出版）
- **一句话结论**：全卷文字典雅洗练且术语零违规，惟第06与10章源文抽取脱落3处核心本格图表需补齐。

---

## 一、审校范围与概况

本次审校严格遵照只读红线，对英国推理黄金时代本格巨匠 J. J. 康宁顿（J. J. Connington）代表作《九解之案》（*The Case with Nine Solutions*，又译《九种解答》）前半卷（Part A：第 01~10 篇）进行了 100% 全覆盖的逐章、逐段、逐句双语对照只读精读审校。

全卷共计审校 **10 篇**，覆盖 **475 个双语对照块**，英文原文 **41,473 词**，中文译文 **61,467 汉字**。详细章节数据与核查状态如下表所示：

| 序号 | 文件名 | 中文篇名 | 双语块数 | 原文词数 | 译文字数 | 核查状态 |
|:---:|:---|:---|:---:|:---:|:---:|:---:|
| 01 | `01-the-dying-man.zh-CN.md` | 一 垂死的人 | 37 | 4,843 | 7,059 | 通过（优秀） |
| 02 | `02-the-house-next-door.zh-CN.md` | 二 隔壁的宅子 | 22 | 2,257 | 3,261 | 通过（优秀） |
| 03 | `03-sir-clinton-at-ivy-lodge.zh-CN.md` | 三 常春藤小屋的克林顿爵士 | 44 | 5,088 | 7,571 | 通过（优秀） |
| 04 | `04-the-crime-at-heatherfield.zh-CN.md` | 四 希瑟菲尔德的罪案 | 34 | 3,924 | 5,787 | 通过（优秀） |
| 05 | `05-the-bungalow-tragedy.zh-CN.md` | 五 平房惨案 | 58 | 5,998 | 8,605 | 通过（优秀） |
| 06 | `06-the-nine-possible-solutions.zh-CN.md` | 六 九种可能的解答 | 48 | 4,004 | 6,031 | 需修正（良好） |
| 07 | `07-the-fly-in-the-amber.zh-CN.md` | 七 琥珀中的苍蝇 | 102 | 5,619 | 8,617 | 通过（优秀） |
| 08 | `08-the-hassendean-journal.zh-CN.md` | 八 哈森丁的日记 | 34 | 3,253 | 4,745 | 通过（优秀） |
| 09 | `09-the-creditor.zh-CN.md` | 九 债主 | 38 | 1,878 | 2,849 | 通过（优秀） |
| 10 | `10-information-received.zh-CN.md` | 十 情报到手 | 58 | 4,609 | 6,942 | 需修正（良好） |
| 合计 | **共 10 篇** | —— | **475** | **41,473** | **61,467** | **整体 B 良好** |

---

## 二、缺陷与问题修改建议

根据独立审校标准，缺陷划分为 A 级重大问题（语义错配、整段漏译、章末截断、重大数字错译）、B 级重要问题（关键本格物证/图表遗漏、术语违规、英文残留、重要逻辑误译）与 C 级轻微问题（微小润色、体例不一）。

### （一）A级重大问题

本卷 A 级重大缺陷为 **0** 项。
各章节段落结构完整，双语块完全对齐，无悬空断句，无整段漏译，亦无黑白颠倒之语义错配。

---

### （二）B级重要问题

共发现 **2** 项重要问题（涉及 3 处图表脱落），皆因项目初始阶段将原书 EPUB 转换为源文 Markdown 时，转换脚本丢失了 HTML `<table>` 标签，导致翻译 Agent 在忠实于源文时带入译文。经查阅底本 `原书/j-j-connington_the-case-with-nine-solutions.epub`，此 3 处图表均为小说本格解谜之核心物证，必须予以补回：

#### 1. 【第 06 篇 第 19 块】全书题眼“九种排列组合表格”脱落

- **文件定位**：`译文/06-the-nine-possible-solutions.zh-CN.md` 第 19 块（行 210–217）
- **现有文本引文**：
  ```markdown
  ===Original===
  He drew a sheet of paper towards him, scribbled on it for a moment or two, and then slid it across the table towards the Inspector. Flamborough bent over and read as follows:

  “Now, since in that table we’ve got every possible arrangement which theoretically could occur,” Sir Clinton continued, “the truth must lie somewhere within the four corners of it.”
  ===Chinese===
  他把一张纸拉到面前，涂写了一两分钟，然后推过桌面，递给探长。弗拉姆伯勒俯身读道：

  “如今，这张表里既然把理论上可能出现的排列一网打尽，”克林顿爵士接着说道，“真相必定就落在这张纸的四框之内。”
  ```
- **缺陷分析**：
  弗拉姆伯勒探长“俯身读道：”（read as follows:）冒号后没有任何内容，直接跳到了克林顿爵士的台词，造成严重阅读断层。在原书 EPUB `chapter-6.xhtml` 中，此处有一张完整的 9 种可能解法排列组合表。该表不仅是第六章的标题来源，更是贯穿全书的核心推理模型与数学穷举道具。若无此表，中文读者无法直观理解克林顿爵士为何称“赔率至多八比一”以及下文逐一推演的情形一至情形九。
- **修改建议代码**：
  在原书与译文第 19 块中补充该核心表格：
  ```markdown
  ===Original===
  He drew a sheet of paper towards him, scribbled on it for a moment or two, and then slid it across the table towards the Inspector. Flamborough bent over and read as follows:

  | Hassendean | Mrs. Silverdale |
  | :--- | :--- |
  | 1.—Accident | Accident |
  | 2.—Suicide | Suicide |
  | 3.—Murder | Murder |
  | 4.—Accident | Suicide |
  | 5.—Suicide | Accident |
  | 6.—Accident | Murder |
  | 7.—Murder | Accident |
  | 8.—Suicide | Murder |
  | 9.—Murder | Suicide |

  “Now, since in that table we’ve got every possible arrangement which theoretically could occur,” Sir Clinton continued, “the truth must lie somewhere within the four corners of it.”
  ===Chinese===
  他把一张纸拉到面前，涂写了一两分钟，然后推过桌面，递给探长。弗拉姆伯勒俯身读道：

  | 哈森丁 | 西尔弗代尔太太 |
  | :--- | :--- |
  | 1.——意外 | 意外 |
  | 2.——自杀 | 自杀 |
  | 3.——谋杀 | 谋杀 |
  | 4.——意外 | 自杀 |
  | 5.——自杀 | 意外 |
  | 6.——意外 | 谋杀 |
  | 7.——谋杀 | 意外 |
  | 8.——自杀 | 谋杀 |
  | 9.——谋杀 | 自杀 |

  “如今，这张表里既然把理论上可能出现的排列一网打尽，”克林顿爵士接着说道，“真相必定就落在这张纸的四框之内。”
  ```

---

#### 2. 【第 10 篇 第 22、23 块】破案关键“化学称量实验记录表”两处脱落

- **文件定位**：`译文/10-information-received.zh-CN.md` 第 22 块（行 149–154）与 第 23 块（行 156–163）
- **现有文本引文**：
  ```markdown
  【第 22 块现有译文】
  克林顿爵士懒懒地翻动纸页，这里那里察看一两笔。最后一条似乎让他满意了，他便不再检视。弗拉姆伯勒俯身桌上，见摊开的那页上仅有如下一条记录，不由大惑不解：
  “对了，”克林顿爵士漫不经心地说，“你手边可有你自己的一本笔记簿——上头记着同类名堂的那种？”

  【第 23 块现有译文】
  马克菲尔德显然一头雾水，走到一只抽屉跟前，抽出一本笔记簿递给郡警察局长……细看马克菲尔德那本摊开的一页，得到的犒赏如下：——
  “见鬼，我真看不出他这是打的什么主意，”探长狠狠地自语道。“对我简直如读天书。”
  “毛手毛脚的年轻人，”郡警察局长刻薄地下了断语。“我扫过这些记录，一眼就撞见三处初等算术的低级错误。这一页上就有一处，”他指了指摊开的那本簿子。“瞧这架势，他是个做事极其马虎草率的人。”
  ```
- **缺陷分析**：
  在两处“如下一条记录：”与“得到的犒赏如下：——”后均空无一物，紧接着克林顿爵士突然指称“我一眼就撞见三处初等算术的低级错误。这一页上就有一处”。
  经比对原书 EPUB `chapter-10.xhtml`，此处缺失了两份至关重要的化学称量数据表：
  1. **哈森丁的草簿**：记录了钾碱球（potash bulb）吸收二氧化碳的称重，单位全部写作 **`grs.`（格令）**，且计算存在算术低级错误——`50.9825 - 50.7789 = 0.2036`，但哈森丁误记为 **`0.2046`**！克林顿爵士正是指着这一行说他马虎！
  2. **马克菲尔德的草簿**：记录了U型管（U-tube）吸收水分的称重，单位全部写作 **`gms.`（克）**，且计算严丝合缝（`24.9047 - 24.7792 = 0.1255`）。
  此二表是全书破案的“阿喀琉斯之踵”——青年化学家哈森丁习惯使用英国药衡制缩写 `grs.`，而留德归来的马克菲尔德习惯使用公制缩写 `gms.`。凶手在后文伪造标签与投毒剂量时正是露出了这一马脚（详见第18、19章）。缺失这组表格，不仅使克林顿爵士现场嘲讽哈森丁算术错误的台词失去依据，更斩断了全书最精彩的法医化学推理线索。
- **修改建议代码**：
  **第 22 块建议修复为**：
  ```markdown
  ===Original===
  Sir Clinton turned over the leaves idly, examining an entry here and there. The last one seemed to satisfy him, and he put an end to his inspection. Flamborough bent over the table and was mystified to find only the following entry on the exposed leaf:

  | Weight of potash bulb | = | 50.7789 | grs. |
  | Weight of potash bulb + CO₂ | = | 50.9825 | grs. |
  | Weight of CO₂ | = | 0.2046 | grs. |

  “By the way,” said Sir Clinton casually, “do you happen to have one of your own notebooks at hand—something with the same sort of thing in them?”
  ===Chinese===
  克林顿爵士懒懒地翻动纸页，这里那里察看一两笔。最后一条似乎让他满意了，他便不再检视。弗拉姆伯勒俯身桌上，见摊开的那页上仅有如下一条记录，不由大惑不解：

  | 钾碱球重量 | = | 50.7789 | grs.（格令） |
  | 钾碱球 + CO₂ 重量 | = | 50.9825 | grs.（格令） |
  | CO₂ 重量 | = | 0.2046 | grs.（格令） |

  “对了，”克林顿爵士漫不经心地说，“你手边可有你自己的一本笔记簿——上头记着同类名堂的那种？”
  ```
  **第 23 块建议修复为**：
  ```markdown
  ===Original===
  Markfield, obviously puzzled, went over to a drawer and pulled out a notebook which he passed to the Chief Constable. Again Sir Clinton skimmed over the pages, apparently at random, and then left the second book open beside the first one. Flamborough, determined to miss nothing, examined the exposed page in Markfield’s notebook, and was rewarded by this:—

  | Weight of U-tube | = | 24.7792 | gms. |
  | Weight of U-tube + H₂O | = | 24.9047 | gms. |
  | Weight of H₂O | = | 0.1255 | gms. |

  “Damned if I see what he’s driving at,” the Inspector said savagely to himself. “It’s Greek to me.”
  “A careless young fellow,” the Chief Constable pronounced acidly. “My eye caught three blunders in plain arithmetic as I glanced through these notes. There’s one on this page here,” he indicated the open book. “He seems to have been a very slapdash sort of person.”
  ===Chinese===
  马克菲尔德显然一头雾水，走到一只抽屉跟前，抽出一本笔记簿递给郡警察局长。克林顿爵士又把纸页溜了一遍，看样子是随手乱翻，随后把第二本摊开在第一本旁边。弗拉姆伯勒决意不放过丝毫，细看马克菲尔德那本摊开的一页，得到的犒赏如下：——

  | U型管重量 | = | 24.7792 | gms.（克） |
  | U型管 + H₂O 重量 | = | 24.9047 | gms.（克） |
  | H₂O 重量 | = | 0.1255 | gms.（克） |

  “见鬼，我真看不出他这是打的什么主意，”探长狠狠地自语道。“对我简直如读天书。”
  “毛手毛脚的年轻人，”郡警察局长刻薄地下了断语。“我扫过这些记录，一眼就撞见三处初等算术的低级错误。这一页上就有一处，”他指了指摊开的那本簿子。“瞧这架势，他是个做事极其马虎草率的人。”
  ```

---

### （三）C级轻微问题

共发现 **2** 项润色与体例微瑕：

1. **【第 05 篇 第 23 块】主语动作承载者轻微泛化省略**
   - **定位**：`05-the-bungalow-tragedy.zh-CN.md` 行 212
   - **原文**：`Inspector Flamborough stepped down from the back seat of the car as Sir Clinton drew up.`
   - **现译**：`车一停稳，弗拉姆伯勒探长便从后座跨了下来。`
   - **分析**：英文中 `as Sir Clinton drew up` 表明是克林顿爵士亲自驾车并刹停（后文亦有两人关于克林顿车技的呼应）。中文译文使用了无主句“车一停稳”，将克林顿爵士的操作隐含化。
   - **修改建议**：建议微调为：`克林顿爵士一把车停稳，弗拉姆伯勒探长便从后座跨了下来。`

2. **【全卷排版体例】报刊名称书名号体例偶有不一致**
   - **定位**：第 01、08 篇 vs 第 05、06 篇
   - **现象**：
     - 第 01 篇第 1 块使用书名号：`《英国医学杂志》（*B.M.J.*，British Medical Journal）`；
     - 第 08 篇第 14 块使用书名号：`《信使报》（*Courier*）和《公报》（*Gazette*）`；
     - 但第 05 篇第 9 块使用星号斜体：`塞进*先驱报*（*Herald*）最后版面的简讯`；
     - 第 06 篇第 7 块使用星号斜体：`今晚见*晚间观察报*（*Evening Observer*）`。
   - **修改建议**：建议出版定稿前统一报刊书名体例，均采用中文标准书名号《先驱报》与《晚间观察报》。

---

## 三、数据层与格式严格核查

### 1. 结构与格式对齐核查
- **双语块配对**：475 个 `===Original===` 与 `===Chinese===` 完全一一对应，块数匹配率 100%。
- **段落对应**：每个双语块内，中英文段落数 100% 保持 1:1，全卷 0 段落错位、0 空行溢出。
- **章末完整性**：10 个章节末段均严格对应原文收尾句子，末尾标点完整，无任何提前截断或内容丢失。

### 2. 人物、地名与专有名词核查（术语表遵从率 100%）
- **主要人物**：
  - Sir Clinton Driffield / Sir Clinton -> 克林顿·德里菲尔德爵士 / 克林顿爵士（职位统一作“郡警察局长”，未出现“总警监”等杂译）；
  - Inspector Flamborough -> 弗拉姆伯勒探长（贯穿全书，未受外部干扰）；
  - Dr. Ringwood -> 林伍德医生（全书统一，严格执行术语表音义兼顾译法）；
  - Ronald Hassendean / Edward Hassendean / Miss Hassendean -> 罗纳德·哈森丁 / 爱德华·哈森丁 / 哈森丁小姐；
  - Dr. Trevor Markfield -> 特雷弗·马克菲尔德博士/医生；
  - Silverdale / Yvonne Silverdale -> 西尔弗代尔 / 伊冯娜·西尔弗代尔（西尔弗代尔太太）；
  - Avice Deepcar -> 艾维斯·迪普卡；
  - Miss Hailsham -> 海尔沙姆小姐（诺玛·海尔沙姆）；
  - Whalley -> 沃利；
  - Spratton / Dudley Amyas Guisborough -> 斯普拉顿 / 达德利·埃米亚斯·吉斯伯勒；
  - Octave Renard -> 奥克塔夫·勒纳尔；
  - Dr. Carew / Shenstone -> 卡鲁医生 / 申斯通；
  - Detective-Sergeant Yarrow -> 亚罗侦缉警士；
  - Old Thornton / Gilling -> 老索顿 / 吉灵。
- **地名与机构**：
  - Westerhaven -> 韦斯特黑文；
  - Lauderdale Avenue -> 劳德代尔大街；
  - Ivy Lodge -> 常春藤小屋；
  - Heatherfield -> 希瑟菲尔德；
  - the bungalow -> 平房（全书高频核心物证地点，100% 统一作“平房”）；
  - Lizardbridge Road -> 蜥蜴桥路；
  - Croft-Thornton Institute -> 克罗夫特-索顿研究所；
  - the Alhambra / the Grosvenor / the Blue Boar -> 阿兰布拉 / 格罗夫纳 / 蓝野猪酒吧；
  - Fountain Street Police Station -> 喷泉街警察局。
- **专有名词与本格术语**：
  - “Justice” -> “正义”（严格恒带引号，无“正义先生”或“贾斯蒂斯”）；
  - hyoscine -> 东莨菪碱；
  - Twilight Sleep -> “朦胧睡眠”；
  - mydriatic -> 扩瞳剂 / 扩瞳生物碱；
  - tourniquet -> 止血带；
  - signet ring -> 图章戒指；
  - dance programme -> 舞序卡；
  - cigarette-holder -> 烟嘴。

### 3. 数字、度量与时间逻辑核查
- **时间线**：林伍德接诊出诊时间（晚 10:20、预估 10:45、雾夜车程）、匿名电报交发与收件时间（晨 8:05 a.m.、邮筒收件 7:00 a.m.、前晚 8:00 p.m.）精确无误。
- **戒指与信封物证日期**：
  - 婚戒：7–11–23（刻 Y. S. 与 F. S.）；
  - 订婚戒：4–10–23（同上）；
  - 小指素金图章戒：15–11–25 / 5–11–25（刻 Y 与 B）；
  - 碎信封邮戳：1925 年，残留邮戳字母 VEN（Westerhaven 之末尾字母），数字与字母照搬精准。
- **毒理与药物剂量数据**：
  - 氢溴酸东莨菪碱极量：0.6 毫克（按药衡制约合 1/100 格令，Verbatim 准确）；
  - 检出估算剂量：7~8 毫克（折合约极量的 10~12 倍，无计算与数量级偏差）；
  - 汽车牌号：GX.9074 精准无误。

---

## 四、翻译文学性与本格九解逻辑深度评价

《九解之案》是黄金时代本格推理中极具学术厚度与智性趣味的杰作，其叙事特色在于“高度客观克制的英式绅士风度”与“严密如数理推导的法医学实证”。本译本在文学性与本格韵味上表现出极高造诣：

1. **古典本格文气质朴典雅**：
   译文遣词造句极具英伦民国风骨，叙事从容不迫。例如首章对大雾中疲惫医生的描写“厚实的绒毯踩在脚底绵软非常；几把马鞍形大扶手椅仿佛在对他说，一天劳顿之后，这里尽是纯粹的身体安逸与松弛”，既有生活实感，又带着古典散文的温润节奏。在处理各涉案角色的对话时，克林顿爵士的从容犀利、弗拉姆伯勒探长的好胜与豁达、海尔沙姆小姐的怨毒与尖刻，均各具声口，入木三分。

2. **法医学与化学推演准确精当**：
   作者 J. J. 康宁顿本名阿尔弗雷德·斯图尔特（Alfred Walter Stewart），系著名有机化学教授，书中涉及大量严苛的实验细节。译者对“混合熔点（mixed melting-point）”、“扩瞳生物碱（mydriatic alkaloids）”、“药衡制（apothecaries' weights）与公制”、“肋间动脉破裂导致的胸膜内出血与外出血对比”等法医及化学术语的翻译展现了极强的专业素养，因果推导分毫不爽。

3. **伏线克制与无剧透原则**：
   译文严格恪守项目设定的悬念原则：对于哈森丁临终遗言“Caught me… pistol… shot… thought it was… all right… never guessed…”，译作“……抓住我了……手枪……开了枪……我还以为……没事……万没想到……”，严格保留了英文“Caught”兼具“击中/暗算/撞破”的多重未定性，绝无提前增添剧透暗示；对匿名投书者“正义”亦全篇保持客观直译，完美保留了本格读者与侦探同步解谜的智力平等权。

综上所述，前半卷译文质量非常扎实，文气流畅，逻辑严谨。只要将第 06 篇与第 10 篇因底本转换疏漏的 3 处核心物证图表补齐，整部译作即达出版级水准。
