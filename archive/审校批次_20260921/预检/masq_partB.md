# 《化装舞会者》独立审校报告（2026-09-21 批次）· 分区报告 B（第 18–33 章 + 专项④⑤及体例/数字/一致性扫描）

审校日期: 2026-09-21
质量等级：B 良好
一句话结论：数据层近乎无瑕（英文块零损坏、源文覆盖 100%、数字零错、引号 99.98% 统一），但人物称谓与敬称跨章多形成片，落 B。

> 本文件是**分区报告 B**，覆盖**阅读序末段 16 篇（ch17–ch32，含末章）**的逐块精读 + 以下**全书性程序化专项**：④夹带与幽灵内容、⑤IME 形近字扫描、中文侧引号体例/半角全角标点/不可见字符、中文侧英文残留逐章计数、数字双向比对（EN⇄CN）、术语与**称谓跨章异写**（含摄政时期爵位称谓 `my lord/lady` 体系、法语词）。与之不重叠的「术语表硬约束落位／幽灵条目」由 A 分区裁决，本报告仅在需要时交叉引用并在「元数据备注」提示。

---

## 一、项目与核对范围

- 项目：`georgette-heyer_the-masqueraders`（《化装舞会者》，Georgette Heyer 1924 摄政罗曼史）
- 体量：`原文/` 33 个 `.md`（32 章正文 + `dedication.md` 献词页）；`译文/` 对应 33 个 `<同名>.zh-CN.md`。原文正文 **2743 行**；译文 **621 个块对**，EN 块 **2676 段** / CN 块 **2676 段**。无 `*.all.zh-CN.md` 合并产物干扰，`原文/` `译文/` 下无附录类额外文件。
- **阅读序核定**：`epub_spine.py` 报 `spine content 33, total spine 38`，顺序为 `dedication → chapter-1 … chapter-32`。文件名为 kebab 篇题，**字母序 ≠ 阅读序**（`a-lady-in-distress` 是 ch1、`journey-s-end` 是 ch32；`the-honourable-robin-tremaine` 是 ch31 而非 ch1）。本报告全篇「章号」均指 spine 章号。篇题 ↔ 章号映射：

| 章 | 文件 | 章 | 文件 |
|---|---|---|---|
| ch1 | a-lady-in-distress | ch17 | sad-falling-out-of-friends |
| ch2 | arrival-of-a-large-gentleman | **ch18** | **the-large-gentleman-is-awake** |
| ch3 | my-lady-lowestoft | **ch19** | **meeting-in-arlington-street** |
| ch4 | mistress-prudence-to-herself | **ch20** | **ingenuity-of-my-lord-barham** |
| ch5 | sir-humphrey-grayson-waits-upon-mr-merriot | **ch21** | **proceedings-of-mr-markham** |
| ch6 | the-polite-world-receives-mr-and-miss-merriot | **ch22** | **tortuous-methods-of-my-lord-barham** |
| ch7 | a-taste-of-a-large-gentleman-s-temper | **ch23** | **the-fight-by-moonlight** |
| ch8 | the-black-domino | **ch24** | **return-of-miss-grayson** |
| ch9 | mohocks-abroad | **ch25** | **mystery-of-the-masked-man** |
| ch10 | sudden-and-startling-appearance-of-the-old-gentleman | **ch26** | **arrest-of-mr-merriot** |
| ch11 | my-lord-barham-in-arlington-street | **ch27** | **violence-on-the-king-s-high-road** |
| ch12 | passage-of-arms-between-prudence-and-sir-anthony | **ch28** | **exit-miss-merriot** |
| ch13 | encounter-at-white-s | **ch29** | **the-ride-through-the-night** |
| ch14 | my-lord-barham-becomes-mysterious | **ch30** | **triumph-of-lord-barham** |
| ch15 | challenge-to-mr-merriot | **ch31** | **the-honourable-robin-tremaine** |
| ch16 | unaccountable-behaviour-of-sir-anthony-fanshawe | **ch32** | **journey-s-end** |

- **B 分区覆盖**：**逐块精读 ch17–ch32 共 16 篇**（阅读序末 16 篇，末章在内）。简报称本书「33 章」而实际为 **32 章正文 + 献词页**，为消除 off-by-one 歧义，把 **ch17** 一并纳入精读（与 A 分区在 ch17 可能有 1 章重叠，属有意安全冗余）。程序化专项按**全书 33 文件**执行。
- 已跑工具与命令（全部只读；自建脚本置于系统临时目录，未在项目内写任何文件）：
  - `python C:\...\scripts\epub_spine.py georgette-heyer_the-masqueraders`（权威阅读序）
  - `python C:\...\scripts\check_chapter_ratio.py georgette-heyer_the-masqueraders --min-ratio 0.20`（逐章译率）
  - 自建：块/段解析器、**源文行级覆盖**、EN 块 ↔ 源文 `difflib` 逐字 diff、**EN 单元 ↔ CN 单元 1:1 对齐**（621 块零差异）、称谓/敬称归类器、引号/标点/不可见字符统计、数字双向比对、英文残留（剔合法保留）、夹带与幽灵内容（含 265 条括注英文回查源文）、跨书重复子串、单元级译率异常值。

## 二、数据层核对（程序化结论）

| 项 | 结果 |
|---|---|
| 块数 O=C | **621 = 621，零不对称**（33 文件逐篇核，无一篇失衡） |
| 段数 原文/EN/CN 三方 | 源文正文行 **2743**；EN 块段 **2676**；CN 块段 **2676**，逐块零差异。差 67 全部来自 `mohocks-abroad`（ch9）：该篇单文件以**单换行**分隔段落（其余 32 篇用空行），故其块内「段」是多行合并单元。改按**行单元**重算后：**EN 单元数 = CN 单元数，621 块全部逐块相等**；且源文 2743 行逐行回查 EN 块**命中 2743 / 缺失 0**。三方口径闭合，**无漏段、无双侧同缺** |
| 英文对照块逐字 diff | **全库零词级损坏**。33 文件对源文逐字 `difflib` 比对（先做弯引号/撇号→直引号、U+FEFF/U+00A0→空格 归一），**33/33 文件 opcodes = 0、相似度 1.0000**。`ste轮` 型破词、中文串入英文块、整句被中译覆盖**一处未现**——本库历史第一高发专项在本书完全落空 |
| 英文残留（剔合法保留） | 中文块内拉丁串共 **33 处位于括号之外**，逐条核语境后**全部合法**：保留法语/拉丁原句（`mademoiselle`、`m'sieur`、`Au revoir`、`réunion`、`pièce de résistance`、`chefs d'oeuvres`、`Tiens`、`je ne sais quoi`、`point-de-vice`、`beau geste` 等）、字母形状描写（`她那两瓣涂得极红的嘴唇撮成一个 O 形` ← `formed an O`）、献词页受赠人缩写 `G. R. R.`。另有 **710 处** `（English）` 括注（属合法保留，体例问题见 B-6）。**违规残留 0 处** |
| 术语表硬约束落位 | A 分区主责，本报告不裁决。**交叉观察（供合并提防误判）**：术语表把 `Lord Barham / my Lord Barham` 定为「巴勒姆勋爵」，译文中「巴勒姆勋爵」实际出现 **57 次**；`Lord Barham` 词条预检所报「译 0 次／残留『勋爵大人』×355」系**口径误判**——「勋爵大人」正是 `my lord` 呼语的合法主译法（详见 B-1 与六·专项）。 |
| 幽灵条目/归一残留 | EN 块**幽灵文本 0**（每个 EN 段落都能在源文按序定位）；CN 块**夹带源文所无内容 0**（265 条不同括注英文逐条回查源文，仅 6 处属译者补全姓名的规范化，见 C-2）。CN 侧 U+FEFF/U+00A0/U+200B **各 0**；EN 侧 U+FEFF 计数**逐文件与源文完全相等**（28/18/16/…，共 33 篇吻合），属写盘管线归一残留，非缺陷 |
| 原文素材覆盖（含 --min-chars 25） | **源文行级覆盖 100%**：2743 行正文逐行回查 EN 块，缺失 **0**（33 篇全部 0 缺失）。末章 `journey-s-end` 末段与源文末行逐字对应（`「不必怀疑。」…我是个非常伟大的人。` ← `“Do not doubt it,”…I am a very great man.`）。**无截断、无整节缺失、无素材残缺** |
| 逐章译率（check_chapter_ratio） | 33 章译率**中位 0.39**；最低为 `dedication.md` 0.20（5 字母/1 汉字，献词页天然），正文最低 `the-fight-by-moonlight` 0.36、`violence-on-the-king-s-high-road` 0.37。**无任何章跌破 0.20 阈值**，无整章未译。另做单元级译率核查（EN≥60 字母的 2044 个单元）：中位 0.396，**低异常 0、高异常 0**（最低 0.264、最高 0.620），**无句内截断迹象** |
| 异常字符 / 引号字形 | **引号体例高度统一**：全书 `“”`(U+201C/201D) **0 次**、直引号 `"` **0 次**，中文对白一律 `「」`（合 6231 个括号）。`『』` 共 38 处，逐处核验**全为「」内嵌套引语**（引述口号、绰号、船名、内心引用）体例正确。例外 **1 处**：`exit-miss-merriot`(ch28) `「`×107 / `」`×106 **缺一个右引号**（见 B-7）。中文块内**半角标点后接汉字 0 处**（半角 `,` `.` `?` `!` `:` `;` 命中全为 0）；无谚文、无西里尔字母、无全角拉丁字母 |
| 数字双向比对 | **块内 EN 数字集合 ↔ CN 数字集合逐块比对：621 块全部一致**（EN 独有 0、CN 独有 0）。年份/金额（几尼、先令）/度量/牌局点数/钟点等关键数字**零错译** |

## 三、A 级问题（必须修）—— 共 0 处

**本分区（ch17–ch32）未发现 A 级问题**，且经全书程序化核验为「零 A」提供了可复算证据：

1. **无整段漏译／截断**：源文 2743 行逐行回查 EN 块，缺失 0；621 块 EN 段数 = CN 段数 = 源文对应行数（`mohocks-abroad` 单换行口径已校正），双向零不对称。末章末段完整（见二·原文素材覆盖行）。
2. **无语义错配**：EN 单元与 CN 单元按行单元 1:1 对齐（621 块零差异），逐单元核对 ch17–ch32 全部叙事段与对白段，未发现「英文讲 A 中文讲 B」。
3. **无重大数字错译**：621 块数字集合双向比对，零不匹配。
4. **无章末截断**：`journey-s-end`(ch32) 末块末句与源文末行逐字对应；`journey-s-end` 前的 `---` 分隔块在 EN/CN 两侧同形保留。

> 说明：ch22「孟妄」（生造词）、ch24「你那座的耳朵」（掉字）、ch28 缺右引号——三处均为**字符级硬伤**，不涉及内容缺失或错配，按 B 级「应修」计入（若派发方倾向从严，前三者可升 A；本报告按「A 级只留给影响读者读到内容的缺陷」口径落 B）。

## 四、B 级问题（应修）—— 共 9 处（其中 5 类为跨章成片，按「合并类」计）

### B-1 核心人物巴勒姆勋爵的称谓在 **ch15 整章**漂移为「老爷」（21 处；全书主译法「勋爵大人」355 次），ch27 亦漂移（3 处）

逐章计数（数字均为**出现次数**，与源文 `my lord` 次数对照；「老爷孤用」已剔除「老爷子」「天老爷」）：

| 章 | 源文 `my lord` | 勋爵大人 | 巴勒姆勋爵 | 老先生 | 老爷子 | **老爷孤用** |
|---|---|---|---|---|---|---|
| ch11 | 19 | 21 | 1 | 4 | 0 | 0 |
| ch13 | 33 | 32 | 8 | 13 | 0 | 0 |
| ch14 | 13 | 14 | 1 | 8 | 0 | 0 |
| **ch15** | **16** | **0** | **0** | 6 | 0 | **21** |
| ch19 | 26 | 27 | 3 | 1 | 1 | 0 |
| ch20 | 66 | 64 | 4 | 1 | 0 | 0 |
| **ch27** | 7 | 3 | 2 | 0 | 0 | **3** |
| ch28 | 29 | 32 | 1 | 1 | 0 | 0 |
| ch30 | 61 | 56 | 3 | 1 | 0 | 0 |
| 全书 | 405 | **355** | **57** | **92** | **6** | **26**（其中 ch15 21 + ch27 3 指巴勒姆） |

全书另两处「老爷孤用」指代不同、**不计入**：ch1 `有人把他家老爷的马车赶跑了`（店主人称主人）、ch10 `那位被挤下宝座的老爷`。

- 文件：`译文/challenge-to-mr-merriot.zh-CN.md`（ch15）
- 英文块：`“You’re playing a game I don’t understand, my lord,” John said severely.` → 中文块：`「老爷，您这是在玩一场我看不懂的把戏，」约翰正色道，「…可您为什么要这么干，老爷，我实在看不明白。」`
- 英文块：`“I plan a great coup,” my lord assured him.`（叙述句）→ 中文块：`「我筹划的是一桩惊天妙举，」老爷向他担保`
- 文件：`译文/violence-on-the-king-s-high-road.zh-CN.md`（ch27）——同一章内叙述用「勋爵大人」×3、约翰口中用「老爷」×3：`「…我得去报老爷。」`（← `I must get to my lord.`）；同章安东尼爵士又称其「他老人家」×1（← `We won’t trouble his lordship.`）
- 定性：同名异译（九项·6）。**同一仆人约翰**在 ch27 说「老爷」、在 ch28 说「是，勋爵大人」（← `“Yes, my lord,” said John`），**相邻两章、同一说话人、同一指称对象不一致**，属跨章成片（合并 1 类）。

### B-2 敬称 `the Honourable` 跨章两译：「尊贵的」×11 / 「尊敬的」×6（均为出现次数）

| 译法 | 出处（文件:ch） | 中文摘录 |
|---|---|---|
| 尊贵**的** ×2 | the-polite-world… ch6 | `尊贵的查尔斯·贝尔福特（Charles Belfort）`、`尊贵的查尔斯神色郑重起来` |
| 尊敬**的** ×3 | a-taste-of-a-large-gentleman… ch7 | `尊敬的查尔斯（the Honourable Charles）有种讨…`、`尊敬的查尔斯的暗示`、`尊敬的查尔斯倒还站得住` |
| 尊敬**的** ×2 | mohocks-abroad ch9 | `尊敬的查尔斯（the Honourable Charles）两个…`、`尊敬的查尔斯一路上还是隔三差五地央告普鲁登丝随他回家` |
| 尊敬**的** ×1 | passage-of-arms… ch12 | `尊敬的普鲁登丝便配得上去做一位…` |
| 尊贵**的** ×2 | my-lord-barham-in-arlington-street ch11 | `尊贵的罗宾·特雷梅因和尊贵的普鲁登丝·特雷梅因了` |
| 尊贵**的** ×3 | unaccountable-behaviour… ch16 | `尊贵的查尔斯（Charles）走进来时`、`尊贵的查尔斯兴冲冲地辞别了他`、`尊贵的查尔斯——在她眼里` |
| 尊贵**的** ×1 | ingenuity-of-my-lord-barham ch20 | `尊贵的查尔斯（The Honourable Charles）露面来` |
| 尊贵**的** ×1 | exit-miss-merriot ch28 | `尊贵的普鲁登丝·特雷梅因` |
| 尊贵**的** ×2 | the-honourable-robin-tremaine ch31 | **章题**`## XXXI The Honourable Robin Tremaine / XXXI 尊贵的罗宾·特雷梅因`、`尊贵的普鲁登丝·特雷梅因（the Honourable Prudence Tremaine）碰碰运气` |

源文对应：`the Honourable Charles`（ch6/7/9/16/20）、`the Honourable Prudence Tremaine`（ch11/28/31）、`the Honourable Prudence`（ch12）、`the Honourable Robin … Tremaine`（ch11）、章题 `The Honourable Robin Tremaine`（ch31）。合计 **尊贵的 11 / 尊敬的 6**（另有 1 处 `尊敬的姑母` 在 ch30，意为 "my respected aunt"，**非**该敬称，不计入）。定性：同名异译；「尊贵的」作敬称亦偏离汉语惯例（通行作「尊敬的／可敬的」）。

### B-3 人物固定修饰语「大块头绅士」在 **ch2** 作「大个子绅士」（7 处，且同章两形并存）

- 文件：`译文/arrival-of-a-large-gentleman.zh-CN.md`（ch2）
- `the large gentleman` 全书译「大块头绅士」**36 次**（本分区已核 ch18 `[2.2]`/`[7.2]`/`[9.4]`/`[15.2]`、ch19、ch20 `[2.5]`、ch25 `[8.1]`/`[17.3]`、ch27、ch29 `[1.1]`）；「大个子绅士」全书 **7 次、全部集中在 ch2**，而 ch2 内部又另有 **1 次**用「大块头绅士」→ **同一章内两形并存**：`进来一位大个子绅士，步态极为从容。`（← `a large gentleman entered with every appearance of leisure.`）、`「我开始对这位大个子绅士生出好感来了。」`（← `“I begin to be attracted towards this large gentleman,”`）
- 定性：同名异译；术语表既有定名 `the large gentleman → 大块头绅士`，ch2 属未按定名。

### B-4 「the old gentleman」主译「老先生」（92 次）与「老爷子」（6 次）并存

- 全书「老先生」92 次（另有 1 次于 ch10 章题 `X 老先生的突然现身`）；「老爷子」共 **6 次**：`译文/mistress-prudence-to-herself.zh-CN.md`（ch4）**5 次**、`译文/meeting-in-arlington-street.zh-CN.md`（ch19）**1 次**
- ch4 中文块：`「哦，请相信我，夫人，我们自己也在纳闷呢！老爷子脑子里怕是钻了蛆虫。」` ← `“Oh, indeed, madam, we wonder as much ourselves! There’s a screw loose in the old gentleman, I believe.”`；`「这么着，倒更像老爷子的作为了——顺手借来就用。」` ← `“The more like the old gentleman to appropriate it,”`；`单是同老爷子一起过活`／`倒不是老爷子`／`老爷子当年断定这样最稳妥`
- ch19 中文块：`我相信老爷子能把他的事务料理妥帖。` ← `I believe the old gentleman may settle his affairs.`
- **对应关系核实**：ch4 的 5 处中 4 处对应源文 `the old gentleman`（b2/b5/b7 各 1、b11 内 1），另 1 处（同在 b11 内）对应源文 `her father` —— 即**同一段内**同一人物被译为「老爷子」两次，而源文分别是 `the old gentleman` 与 `her father`；ch19 的 1 处对应 `the old gentleman`。
- 定性：同一固定称法两译（老先生／老爷子），可与 B-1/B-3 合并为「人物称谓跨章漂移」一类。

### B-5 「昆斯伯里公爵夫人」被套用王室尊称「殿下」（3 处）

- 文件：`译文/sudden-and-startling-appearance-of-the-old-gentleman.zh-CN.md`（ch10）
- 英文块：`arriving on the day of her Grace of Queensberry’s rout`／`Her Grace of Queensberry came forward to welcome the newcomer`
- 中文块：`抵达那日恰逢昆斯伯里公爵夫人（Duchess of Queensberry）殿下开盛大晚会`；`殿下的厅堂够宽敞`；`殿下立在楼梯口迎客`
- 定性：`her Grace`（公爵夫人）译作「殿下」，把王室尊称套在贵族夫人头上；术语表定名为「昆斯伯里公爵夫人」且已标出「残留·殿下」。称谓误用／术语表违规。（同书 `his Grace of Cumberland` → 「坎伯兰公爵殿下」为**公爵**用例，可保留，须与本案分开。）

### B-6 「（English）」首现括注在每章重复，共 710 处 / 265 个不同词条（体例偏差，全书性）

- 术语表「翻译策略」明定：`人名用通行音译，首次出现附原文「中文（English）」，后文统一中文译名`。实际执行是**每章首现重新括注**：`Robin`(罗宾) 括注 25 次、`Prudence`(普鲁登丝) 25 次、`John`(约翰) 20 次、`Sir Anthony Fanshawe`(安东尼·范肖爵士) 18 次、`Lord Barham`(巴勒姆勋爵) 15 次、`Prue` 14 次……
- 逐章括注数：ch30 = 40、ch13/ch28 = 33、ch9/ch25/ch31 = 30、ch6 = 29、ch3/ch7/ch20 = 28……
- 定性：**术语表体例未按约定执行**（按「合并类」1 条计）。**须注意**：此偏差不损伤阅读（对按章阅读的读者反而便利），**不得据此单独降级**；如派发方认定属既定「逐章独立可读」方针，可整条降为 C 或不报。

### B-7 `exit-miss-merriot`(ch28) 中文块缺一个右引号 `」`（全书唯一失衡点）

- 文件：`译文/exit-miss-merriot.zh-CN.md`，ch28 第 5 块第 3 单元（约翰的长段叙述）
- 中文块开头 `「哦，这个他压根没放在心上，少爷！…`，全篇结尾作 `…连我自个儿都敢说他要把菊花青马扎死在车辕上呢！` —— **句末缺 `」`**，紧接即 `===Original===`；该文件 `「`=107 / `」`=106，为全书 6231 个角引号中**唯一一处不配对**（其余 32 篇全部左右相等）
- 英文块：`“Oh, he made nothing of that, sir! …I thought myself he would spear the roan on the shaft of the coach!”`
- 定性：字符级硬伤，可 `grep` 复现（搜 `扎死在车辕上呢！` 后紧跟换行）。建议补 `」`。

### B-8 `return-of-miss-grayson`(ch24) 中文块掉字，短语失义：「你那座的耳朵」

- 文件：`译文/return-of-miss-grayson.zh-CN.md`，ch24 第 6 块
- 英文块：`“Pocket that: she’s not to know. Egad, if this comes to your mountain’s ears I’m like to be sped.”`
- 中文块：`「把它收好：不能让她知道。天哪，这事要是传进**你那座的耳朵**，我怕是要吃不了兜着走了。」` —— 应为「你那座**山**的耳朵」
- 佐证：全书同类结构均作 `那座山`（`你要同那座山并辔而行么？`/`我有心要迷倒那座山。`/`那座山来了。`/`那座山！可这是怎么办到的` 等 20+ 处），**唯此一处脱落 `山` 字**。

### B-9 生造词／别字（⑤ 同族）：`孟妄`（ch22）、`月人`（ch9）

- `译文/tortuous-methods-of-my-lord-barham.zh-CN.md`（ch22）：英文块 `He dared—you shudder at such temerity—he dared to use threats to me!`；中文块 `他竟敢——这样的**孟妄**你听了都要打颤——他竟敢对我出言威胁！`。「孟妄」非汉语词（疑为「狂妄／妄为」之误），同书 ch7 已正确使用 `如此**狂妄**的臆测`。
- `译文/mohocks-abroad.zh-CN.md`（ch9，**属 A 分区 ch1–17，此处按专项⑤全书扫描报出，请勿重复计数**）：`她心想，自己已渐渐觉得，与其说像个女人，倒不如说更像个月人了` ← `she was beginning, she thought, to feel more of a man than a woman` —— 应为「**男人**」。本库历史高发「X 个月人」族，全书扫描**仅此 1 处**。

## 五、C 级问题（建议优化）—— 共 4 类

1. **译者善意修正源文讹字（1 处）**：ch18 源文 `Her **ringers** closed round the stem of her wineglass`（`ringers` 为源书讹字，全书仅此 1 处），英文块照录原文，**中文块正确译为「她的手指拢住酒杯的杯脚」**。按本库判例记 C。
2. **括注英文与源文当处用词不完全同形（6 处，非缺陷）**：如 ch6/ch15 中文写 `安东尼·范肖爵士（Sir Anthony Fanshawe）` 而源文当处仅作 `Sir Anthony`（全名是译者补全）；ch10 中文写 `昆斯伯里公爵夫人（Duchess of Queensberry）` 而源文作 `her Grace of Queensberry`；ch7 `汉弗莱·格雷森爵士（Sir Humphrey Grayson）` vs 源文 `Sir Humphrey`；ch31 `洛斯托夫特夫人（My Lady Lowestoft）` vs 源文 `my Lady Lowestoft`。人名指称正确、便于读者，**建议保留**，仅备案。
3. **敬称/称谓的零散单点异形（各 1–2 次，未成片）**：`他老人家`×2（ch27、ch32，对应 `his lordship`）、`爵爷大人`×1（ch29`我的爵爷大人` ← `my lord`，说话人普鲁登丝戏称安东尼爵士）、`爵爷`×2 指巴勒姆（ch7）；`太太`×1 指洛斯托夫特夫人（ch4`「太太，您瞧瞧我这位小导师！」` ← `“Madam, behold my little mentor!”`，其余场合均作「夫人」）。
4. **`份量`（1 处，规范词形应为「分量」）**：ch28 `我若没有圣徒般的耐心，只怕要禁不住把这整桩事，按它应得的份量痛斥一番。`

## 六、逐项清单结论

### 九项标准项（本分区 ch17–ch32 逐块核对）

| # | 检查项 | 结论 | 缺陷数 |
|---|---|---|---|
| 1 | 语义错配 | 无。EN/CN 行单元 1:1 对齐，621 块零差异；ch17–ch32 全部叙事段与对白段逐单元核对未见 A/B 错配 | 0 |
| 2 | 整段漏译 | 无。源文 2743 行 100% 覆盖；块内 EN 段数 = CN 段数 | 0 |
| 3 | 章末截断 | 无。末章 ch32 末块末句与源文末行逐字对应；各章末块均完整 | 0 |
| 4 | 重大数字错译 | 无。621 块数字集合双向比对零不匹配 | 0 |
| 5 | 术语表违规 | 有。定名体例两处未守：`the Honourable` 两译（B-2）、`the large gentleman` ch2 作「大个子绅士」（B-3）；另有 `her Grace` 套「殿下」（B-5） | 3 类 |
| 6 | 同名异译 | 有，且为本书主要缺陷面：巴勒姆勋爵称谓跨章 5 形（勋爵大人/巴勒姆勋爵/老爷/爵爷/他老人家，ch15 整章漂移，B-1）、`the old gentleman` 老先生/老爷子（B-4） | 2 类（成片） |
| 7 | 英文单词残留 | 无违规。33 处括外拉丁串全部合法（法/拉丁原句、字母形状、缩写），剔合法保留后**违规 0** | 0 |
| 8 | 语义误译 | 有 1 处掉字致短语失义（ch24「你那座的耳朵」，B-8）；1 处非词（ch22「孟妄」，B-9） | 2 |
| 9 | 风格与流畅度 | 总体优秀：长句拆分得当、对白口吻区分清楚（约翰的仆人口语、爵爷的自恋夸饰、德弗罗的花花公子腔均有对应中文色彩），罕有翻译腔。仅零星用词可酌（C-3/C-4） | 0 硬伤 |

### 七项本库高发专项

| 专项 | 结论 | 缺陷数 |
|---|---|---|
| ① 英文对照块逐字损坏 | **零处损坏**。33/33 文件 `difflib` opcodes = 0、相似度 1.0000（字形档：弯引号→直引号、U+FEFF/U+00A0 归一本属管线副产品，已单列计数，不参与定级） | 0 |
| ② 段数三方对齐 | 口径已查清并闭合：源文 2743 行 / EN 2676 段 / CN 2676 段；`mohocks-abroad` 单换行致 67 行合并，改按行单元后 EN=CN 逐块相等。**零不对称** | 0 |
| ③ 双侧同缺 | **未命中**。逐块「块内 EN 段数 ↔ 源文行索引跨度」全等（锚点全部命中、跨度与段数一致，无 ANCHOR 失效）；源文逐行回查 EN 块零缺失，故不存在「EN=CN 对称但中间吞段」的情形 | 0 |
| ④ 夹带与幽灵内容 | **未命中**。EN 块幽灵文本 0；CN 块夹带源文所无内容 0；跨书重复子串仅**括注重复**（710 处，见 B-6），**无章末重复对话、无杜撰署名块、无幽灵残句**；ch32 末块 `---` 两侧同形保留 | 0（B-6 体例另计） |
| ⑤ IME 形近字扫描 | 命中 2：「月人」（ch9，应为「男人」）、「孟妄」（ch22，非词）；47 处「量词+的」候选逐条核验后仅 ch24 一处为真掉字（B-8），其余为合法结构（`一副爱司打头的四连张`、`那么几个`）。 | 2 |
| ⑥ 原文素材完整性 | 已跑源文行级覆盖：2743/2743 命中，**零缺失**；无 `### II` 型截断、无题词/署名行缺失、无诗行丢失（本书无诗行） | 0 |
| ⑦ 逐章译率核对 | 33 章中位 0.39，**无章跌破 0.20**；逐章清单见二·逐章译率行。**无「整章未译」** | 0 |

## 七、等级判定理由

- **A 级问题 0 处**（本分区）。故不可能判 C（C 的定义为「A 级若干」）。
- **数据层五项**：块段三方零不对称 ✅／英文块**词级**逐字一致 ✅（33/33 ratio 1.0000）／英文残留 0 ✅／数字全对 ✅ —— 四项全清；**唯有「术语零违规」不成立**：定名体例与称谓出现**成片跨章多形**（≥5 类）。
- 按本库口径「**A 优秀**」须满足「数据层五项全清 + 余下瑕疵仅零星」，而「零星」明确定义为**单一术语分义项/上下文漂移 ≤1 类**；本书实为 ≥5 类（B-1 至 B-5），明显超出。
- 按「**成片即降**」：同类问题多处蔓延（术语跨章多形、敬称两译、固定修饰语整章异写）→ 落 **B 良好**。
- 未达 **C 需关注**：C 要求「A 级若干」或「B 级成片**十几组**系统性错误」；本书 B 级合为 5 类 + 4 处零星字符级硬伤（B-7/B-8/B-9 及 C-4），未达十几组，且**内容层零缺失**（A 级 0），文体质量过硬。
- 未触及 **D 严重**：B-5 四条判据（a 缺失≥10% 段落、b 整幕/整节/整篇缺失、c ≥2 处章末缺失、d 合集内某篇结尾缺失）**均不成立**——本书源文覆盖 100%、章节结构完整、末章完整。**无「挂起·待修」项**。
- **产物级缺陷例外不适用**：无 `_partN` 分片，主交付物 33 文件齐备且与 `原文/` 一一对应，无覆盖率倒挂。
- 结论：**B 良好**。

## 八、元数据备注（不改文件，仅提示人工）

1. **章数口径需修正**：简报与`项目说明.md`称「全书 33 篇 / 33 章」，实际为 **32 章正文 + `dedication.md` 献词页**（`epub_spine.py`：`spine content 33`，即 `dedication` + `chapter-1` … `chapter-32`）。分区派发若按「33 章」切分，请核对 A/B 边界。
2. **阅读序陷阱**：文件名为 kebab 篇题，**字母序与阅读序完全不同**；`the-honourable-robin-tremaine`（ch31）在字母序中排在最前，`a-lady-in-distress`（ch1）与 `journey-s-end`（ch32）分列两端的字母序位置亦相反。务必以 spine 表为准。
3. **术语表幽灵/失效条目（提示 A 分区，本报告不裁决）**：术语表备注中提到的化名「**洛里安少爷**」（Prudence 化名）与「**瑟尔小姐**」（Robin 化名）在**源文与译文中均 0 次出现**（全书 `洛里安`=0、`瑟尔`=0）；实际的化名体系是 `Mr./Peter Merriot`（普鲁登丝扮男装）与 `Miss Merriot/Kate`（罗宾扮女装）。该两条备注属建库期误植，**不得据此判译者违规**。
4. **预检口径提示（供合并时防误报）**：预检摘要中 `Lord Barham / my Lord Barham → 巴勒姆勋爵 源×21 译×0 残留「勋爵大人」×355`、`巴勒姆/巴勒姆勋爵 源×116 译×133`、`the large gentleman … 残留「大个子绅士」×6` 三行，前两行的「译 0」与「残留」是**词表型计数把合法呼语译法算成未落位**；实测「巴勒姆勋爵」57 次、「勋爵大人」355 次为**合法的呼语/称名分工**。真正需要修的是其中**别处成片的两形**（见 B-1/B-3）。
5. **`项目说明.md` 与源文一致，未发现张冠李戴**；`译文/` 下无 `*.all.zh-CN.md` 合并产物，`原文/`、`译文/` 下无附录类额外文件，块数/段数统计无须扣减。

## 九、审校方法与局限

- **读取范围**：`原文/` 与 `译文/` 全部 33 文件（全书程序化处理）；**逐单元精读 ch17–ch32**（16 篇，含末章）。ch1–ch16 仅做程序化核验（源文覆盖、EN 逐字 diff、数字、引号、残留、夹带、IME），**未做逐单元人工精读**——故本报告对 ch1–ch16 的人工判断仅限程序化命中项（如 ch9「月人」、ch2「大个子绅士」、ch15「老爷」）。
- **方法**：先建解析器把 `===Original===`/`===Chinese===` 拆成块，再按**行单元**（`\n`/`\n\n` 统一切分）建 EN↔CN 1:1 映射（621 块零差异，是该报告所有逐单元结论的基础）；随后做源文行级覆盖、`difflib` 逐字 diff、数字集合比对、称谓归类、引号/标点/不可见字符统计、括注英文回查源文、跨书重复子串、单元级译率异常值。
- **误报防线已执行**：`殿下`（`his Grace of Cumberland` 为公爵合法用例，与公爵夫人案分开）；`爵士` 作 `sir` 呼语、`少爷` 作约翰对罗宾的 `sir`、`小姐` 作 `madam`（对扮作未婚女子的 Miss Merriot/莱蒂）——均核对说话人与受话人后判为合法，未计入缺陷；ch16 的 `my lord` 经回读源文（同段有 `my Lord Kestrel`、`The chuckle died on my Lord Kestrel’s lips`）确认为 **Lord Kestrel**，译文作「凯斯特雷尔勋爵」**正确**，不计缺陷。
- **存疑/未决**：
  - B-7（ch28 缺 `」`）与 B-8（ch24 掉「山」）为字符级硬伤，定级 B；若派发方按「文本完整性」从严，可升 A——本报告已在第三节明示该两可读法。
  - B-6（括注逐章重复）是否为预期体例，取决于该项目「逐章独立可读」是否为其既定方针；若属既定，应整条降为 C 或不报。
  - B-9 的「月人」在 ch9（A 分区），本报告按专项⑤全书扫描口径报出，**合并时请勿重复计数**。
- **可复算命令**（证据链）：`python C:\Users\HanTi\OneDrive\translate\scripts\epub_spine.py georgette-heyer_the-masqueraders`；`python C:\Users\HanTi\OneDrive\translate\scripts\check_chapter_ratio.py georgette-heyer_the-masqueraders --min-ratio 0.20`；`grep -n "扎死在车辕上呢" "译文/exit-miss-merriot.zh-CN.md"`（B-7）；`grep -n "你那座的耳朵" "译文/return-of-miss-grayson.zh-CN.md"`（B-8）；`grep -n "孟妄" "译文/tortuous-methods-of-my-lord-barham.zh-CN.md"`（B-9）；`grep -c "勋爵大人" / "老爷" "译文/challenge-to-mr-merriot.zh-CN.md"`（B-1）。
