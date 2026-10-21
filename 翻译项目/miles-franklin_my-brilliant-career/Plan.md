# 翻译计划（我的光辉生涯）

## 本计划信息

- **项目名称**：我的光辉生涯（My Brilliant Career，迈尔斯·富兰克林）
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/小说文学.md
- **术语表**：术语表.md

## 文件分工

| 文件 | 作用 | 谁来改 |
|------|------|--------|
| `项目说明.md` | 项目基本信息、领域配置、篇目清单 | 人工 |
| `术语表.md` | 翻译硬约束层。每篇译完补充新词 | agent / 人工 |
| `translation_queue.csv` | 任务队列。每行一文件，`file, size_kb, status` 三列 | 翻译前改 doing，完成后改 done |
| `Plan.md`（本文件） | 执行步骤 + 运行日志 | agent 追加日志 |
| `原文/*.md` | 源文 | 不改 |
| `译文/*.zh-CN.md` | 译文产出（块对照双语） | 翻译 agent 产出 |

## 执行步骤

按 `prompts/翻译计划模板.md`「执行步骤」9 步推进（读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志）。本项目为「长篇／委派模式」，由子代理逐篇译，主 agent 统管术语与风格连贯。

## 篇目清单

> 全书 38 章（罗马数字 I–XXXVIII），另含亨利·劳森《前言》、作者《引言》及书末《注释》，共 41 个文件。各篇文件名原为纯文字无编号（部分含嵌入式日期会干扰自然排序），已加 `01-`–`41-` 阿拉伯数字前缀，严格对应阅读顺序。合计约 474.7KB。

| # | 篇名 | 源文 | 大小 | 状态 |
|---|------|------|------|------|
| 1 | 前言（亨利·劳森） | 01-preface.md | 1.5KB | todo |
| 2 | 引言 | 02-introduction.md | 2.4KB | todo |
| 3 | 一　我记得，我记得 | 03-i-remember-i-remember.md | 7.1KB | todo |
| 4 | 二　袋熊谷初识 | 04-an-introduction-to-possum-gully.md | 5.3KB | todo |
| 5 | 三　死气沉沉的生活 | 05-a-lifeless-life.md | 8.6KB | todo |
| 6 | 四　一场很快栽了的事业 | 06-a-career-which-soon-careered-to-an-end.md | 8.2KB | todo |
| 7 | 五　零散速写与牢骚 | 07-disjointed-sketches-and-grumbles.md | 15.3KB | todo |
| 8 | 六　反叛 | 08-revolt.md | 13.6KB | todo |
| 9 | 七　哪有玫瑰不长刺 | 09-was-e-er-a-rose-without-its-thorn.md | 18.8KB | todo |
| 10 | 八　告别袋熊谷，好哇！好哇！ | 10-possum-gully-left-behind-hurrah-hurrah.md | 19.0KB | todo |
| 11 | 九　海伦姨妈的妙方 | 11-aunt-helen-s-recipe.md | 14.2KB | todo |
| 12 | 十　埃弗拉德·格雷 | 12-everard-grey.md | 17.2KB | todo |
| 13 | 十一　呸 | 13-yah.md | 15.3KB | todo |
| 14 | 十二　一段刻骨铭心的情 | 14-one-grand-passion.md | 11.4KB | todo |
| 15 | 十三　他 | 15-he.md | 16.3KB | todo |
| 16 | 十四　多是书信 | 16-principally-letters.md | 12.2KB | todo |
| 17 | 十五　心怀年少时 | 17-when-the-heart-is-young.md | 9.0KB | todo |
| 18 | 十六　时来运转 | 18-when-fortune-smiles.md | 14.5KB | todo |
| 19 | 十七　青春牧歌 | 19-idylls-of-youth.md | 20.2KB | todo |
| 20 | 十八　但愿我被迫听过的布道大都这般短 | 20-as-short-as-i-wish-had-been-the-majority-of-sermons-to-which-i-have-been-forced-to-give-ear.md | 4.6KB | todo |
| 21 | 十九　1896 年 11 月 9 日 | 21-the-9th-of-november-1896.md | 15.1KB | todo |
| 22 | 二十　故事续篇 | 22-same-yarn-continued.md | 16.2KB | todo |
| 23 | 二十一　我又不淑女了 | 23-my-unladylike-behaviour-again.md | 8.9KB | todo |
| 24 | 二十二　芳龄十七 | 24-sweet-seventeen.md | 16.9KB | todo |
| 25 | 二十三　“啊，哪怕一小时的烈火之爱，也胜过一世纪的冷清敬意！” | 25-ah-for-one-hour-of-burning-love-tis-worth-an-age-of-cold-respect.md | 15.0KB | todo |
| 26 | 二十四　祸福旦夕难料 | 26-thou-knowest-not-what-a-day-may-bring-forth.md | 8.0KB | todo |
| 27 | 二十五　缘何？ | 27-because.md | 8.9KB | todo |
| 28 | 二十六　莫向明日夸海口 | 28-boast-not-thyself-of-tomorrow.md | 16.2KB | todo |
| 29 | 二十七　我的旅程 | 29-my-journey.md | 5.4KB | todo |
| 30 | 二十八　活下去 | 30-to-life.md | 14.4KB | todo |
| 31 | 二十九　活下去（续） | 31-to-life-continued.md | 23.4KB | todo |
| 32 | 三十　无知是福，聪明反被聪明误 | 32-where-ignorance-is-bliss-tis-folly-to-be-wise.md | 9.8KB | todo |
| 33 | 三十一　麦斯沃特先生和我大吵一场 | 33-mr-m-swat-and-i-have-a-bust-up.md | 14.6KB | todo |
| 34 | 三十二　别了，巴尼山口 | 34-ta-ta-to-barney-s-gap.md | 5.8KB | todo |
| 35 | 三十三　重返袋熊谷 | 35-back-at-possum-gully.md | 8.7KB | todo |
| 36 | 三十四　然而故人易忘 | 36-but-absent-friends-are-soon-forgot.md | 12.0KB | todo |
| 37 | 三十五　1898 年 12 月 3 日 | 37-the-3rd-of-december-1898.md | 9.4KB | todo |
| 38 | 三十六　从前，日子漫长而炎热 | 38-once-upon-a-time-when-the-days-were-long-and-hot.md | 19.6KB | todo |
| 39 | 三十七　轻视小事者必渐倾覆 | 39-he-that-despiseth-little-things-shall-fall-little-by-little.md | 7.3KB | todo |
| 40 | 三十八　一个讲完的故事，一个了结的日子 | 40-a-tale-that-is-told-and-a-day-that-is-done.md | 4.4KB | todo |
| 41 | 注释 | 41-endnotes.md | 0.1KB | todo |

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
| 2026-10-15 | 04-an-introduction-to-possum-gully.md（第2章 袋熊谷初识） | done | check_bilingual.py 退出码 0；6 对块，11 段全译；U+FEFF×2 照录 |
| 2026-10-15 | 03-i-remember-i-remember.md（第一章 我记得，我记得） | done | check_bilingual.py 退出码 0；8 对块，23 段全译；U+FEFF×2 照录 |
| 2026-10-15 | 05-a-lifeless-life.md（第3章 死气沉沉的生活，8.6KB/31 段） | done | check_bilingual.py 退出码 0；31 对块逐段对照，0 可疑错配；隐形字符（4×U+FEFF、3×U+00A0）照录保真；术语表新增 Blackshaw、Tiger Swamp、sallie-tree |
| 2026-10-15 | 06-a-career-which-soon-careered-to-an-end.md（第4章 一场很快栽了的事业，8.2KB/27 段） | done | check_bilingual.py 退出码 0；27 对块逐段对照，0 可疑错配；U+FEFF×4 照录（仅 Original 块）；脚注锚点（shouting1、poddied2）保留；术语表新增 Homebush、Bourke、Shoalhaven、Auburn Street、cocky |
| 2026-10-15 | 07-disjointed-sketches-and-grumbles.md（第5章 零散速写与牢骚，15.3KB/47 段） | done | check_bilingual.py 退出码 0；47 对块逐段对照，0 可疑错配；子标题 A Drought Idyll 合并为「旱灾牧歌」；原文块由脚本自源文逐字节注入，U+FEFF×18、U+00A0×2 照录保真；术语表新增 old Harris、dogleg、leg-ropes、separator |
| 2026-10-15 | 08-revolt.md（第6章 反叛，13.6KB/52 段） | done | check_bilingual.py 退出码 0；52 对块逐段对照，0 可疑错配；13×U+FEFF 照录保真；术语表新增 Jansen，old Harris 与既有条目合并 |
| 2026-10-15 | 11-aunt-helen-s-recipe.md（第9章 海伦姨妈的妙方，14.2KB/27 段） | done | check_bilingual.py 退出码 0；27 对块逐段对照，0 可疑错配；原文块自源文逐字节注入并校验一致，12×U+FEFF、2×U+00A0 照录保真；源内 --- 分隔线保留；术语表新增 Caine、codlin moth |
| 2026-10-15 | 10-possum-gully-left-behind-hurrah-hurrah.md（第8章 告别袋熊谷，好哇！好哇！，19.0KB/58 段） | done | check_bilingual.py 退出码 0；58 对块逐段对照，0 可疑错配；原文块由脚本自源文逐字节注入，U+FEFF×15、U+00A0×18 照录保真；术语表新增 Yass、Young、Halfway House、Woolpack Hotel、Borgongs、Pheasant Gap、Billy Haizelip、lyrebird、curlew、Corelli、Trilby |
| 2026-10-15 | 09-was-e-er-a-rose-without-its-thorn.md（第7章 哪有玫瑰不长刺，18.8KB/58 段） | done | check_bilingual.py 退出码 0；58 对块逐段对照，0 可疑错配；外婆信与三首诗各整块对照、诗行版式镜像保留；原文块自源文逐字节注入，31×U+FEFF 照录保真；子标题 Self Analysis 合并为「自我剖析」；术语表新增 Patti、Melba、Irving、Terry、Kipling、Gladstone、wattle，Caine/Corelli 与既有条目合并 |
| 2026-10-15 | 14-one-grand-passion.md（第12章 一段刻骨铭心的情，11.4KB/46 段） | done | check_bilingual.py 退出码 0；46 对块逐段对照，0 可疑错配；原文块自源文逐字节注入，U+FEFF×14、U+00A0×6 照录保真；术语表新增 Mrs. Hickey、messmate、wild clematis、senna、leather-head |
| 2026-10-15 | 12-everard-grey.md（第10章 埃弗拉德·格雷，17.2KB/72 段） | done | check_bilingual.py 退出码 0；72 对块逐段对照，0 可疑错配；原文块自源文逐字节注入并校验一致，13×U+FEFF、9×U+00A0 照录保真；杰杰舅舅、弗兰克·霍登全名首次登场并括注；术语表新增 Wagga Wagga、Albury、Forbes、Dandaloo、Hay、Tumut、Monaro、Peak Hill、ringer |
| 2026-10-15 | 13-yah.md（第11章 呸，15.3KB/80 段） | done | check_bilingual.py 退出码 0；80 对块逐段对照，0 可疑错配；原文块自源文逐字节注入并校验一致，8×U+FEFF、5×U+00A0 照录保真；斜体标记（*bold bad*、*would*、*dare*）镜像保留；术语表新增 blackfellow、Kowalski's galop、Gaite de Coeur、Weber's Last、Three Fishers |
| 2026-10-15 | 17-when-the-heart-is-young.md（第15章 心怀年少时，9.0KB/40 段） | done | check_bilingual.py 退出码 0；40 对块逐段对照，0 可疑错配；原文块自源文逐字节注入并校验一致，8×U+FEFF、7×U+00A0 照录保真；姑奶奶书信 blockquote 镜像保留；娃娃语（Dimme wide、yim duts、luz oo 等）以汉语儿语音译风味体现；术语表新增 Sarah、aunt Gussie、Minnie Benson、O'Doolan、小负鼠、old Spanker、本森家女眷、Yarrangung、sulky |
| 2026-10-15 | 15-he.md（第13章 他，16.3KB/101 段） | done | check_bilingual.py 退出码 0；101 对块逐段对照，0 可疑错配；原文块自源文逐字节注入并校验一致，13×U+FEFF、5×U+00A0 照录保真；源内 --- 分隔线保留；问答体（Question/Q）以**问。**／**答。**镜像；术语表新增 myall、banksia、kurrajong、Marechal Niel、Judge Fossilt、Tyson、Wallerawang West、Quat-Quatta、Queensland |
| 2026-10-15 | 16-principally-letters.md（第14章 多是书信，12.2KB/35 段） | done | check_bilingual.py 退出码 0；28 对块（家书 6 行、致埃弗拉德半信 3 行各整块对照、> 书信版式镜像保留，其余 26 段逐段对照），0 可疑错配；原文块自源文逐字节注入并校验一致，14×U+FEFF 照录保真；数字锚点 365 保留；术语表新增 kookaburra、squatter’s chair、go on the wallaby、Brisbane |
| 2026-10-15 | 20-as-short-as-i-wish-had-been-the-majority-of-sermons-to-which-i-have-been-forced-to-give-ear.md（第18章 但愿我被迫听过的布道大都这般短，4.6KB/22 段） | done | check_bilingual.py 退出码 0；22 对块逐段对照，0 可疑错配；原文块自源文逐字节注入并校验一致，2×U+FEFF 照录保真；术语沿用既有定名（海伦姨妈、哈罗德/哈里·比彻姆、牧场学徒），“hideous barbarian”循 13-yah 既有“丑八怪”风味译作“丑八怪野人” |
| 2026-10-15 | 19-idylls-of-youth.md（第17章 青春牧歌，20.2KB/85 段） | done | check_bilingual.py 退出码 0；85 对块逐段对照，0 可疑错配；原文块自源文逐字节注入并校验一致，15×U+FEFF、12×U+00A0 照录保真；对白“拦得住/你才不”连珠体镜像保留，乔·斯洛科姆、巴特勒太太土腔以汉语乡土口语体现；术语表新增 Warrigal、Barney、Mrs. Butler、Joe Slocombe、Old Nick、bogey、tea-tree |
| 2026-10-15 | 18-when-fortune-smiles.md（第16章 时来运转，14.5KB/61 段） | done | check_bilingual.py 退出码 0；61 对块逐段对照，0 可疑错配；原文块自源文逐字节注入并校验一致，14×U+FEFF、5×U+00A0 照录保真；斜体 *When fortune smiles!* 镜像保留；爱尔兰土腔（O'i can't plaze yez、tazin'）以汉语乡土口语体现，“sun-struck/daughter-struck”“Mights don't fly”双关以中暑／‘暑’、‘万一’不会飞再造；术语表新增 Miss Augusta（奥古斯塔）、goanna、Triangle paddock、quart pot、nobblers、Erard、Waterbury，Warrigal 首见章与 Joe Archer 章注合并 |
| 2026-10-15 | 23-my-unladylike-behaviour-again.md（第21章 我又不淑女了，8.9KB/43 段） | done | check_bilingual.py 退出码 0；43 对块逐段对照，0 可疑错配；原文块自源文逐字节注入并校验一致，4×U+FEFF、1×U+00A0 照录保真；术语沿用既有定名（乔·阿彻、瓦里加尔、杰杰舅舅、哈罗德·比彻姆），无新增术语 |
| 2026-10-15 | 21-the-9th-of-november-1896.md（第19章 1896 年 11 月 9 日，15.1KB/74 段） | done | check_bilingual.py 退出码 0；74 对块逐段对照，0 可疑错配；原文块自源文逐字节注入并校验一致，12×U+FEFF、14×U+00A0 照录保真；术语沿用既有定名（杰杰舅舅、五博丘、牧场学徒），“Treminjous intoirely, sor”以拖腔汉语口语体现；术语表新增 James Grant、Blanche Derrick、old Benson、Clancy、old Boxer、drag、box-tree、guinea，Barney 条目补注 |
| 2026-10-15 | 22-same-yarn-continued.md（第20章 故事续篇，16.2KB/56 段） | done | check_bilingual.py 退出码 0；56 对块逐段对照，0 可疑错配；原文块自源文逐字节注入并校验一致，14×U+FEFF、2×U+00A0、1×U+200A 照录保真；哈罗德求婚与马鞭一节完整译出，德里克小姐译名与第19章衔接；术语表新增 mopoke、Cootamundra，Blanche Derrick 条目补注第20章 |
| 2026-10-15 | 26-thou-knowest-not-what-a-day-may-bring-forth.md（第24章 祸福旦夕难料，8.0KB/29 段） | done | check_bilingual.py 退出码 0；29 对块逐段对照，0 可疑错配；原文块自源文逐字节注入并校验一致，10×U+FEFF 照录保真；术语沿用既有定名（哈罗德·比彻姆、卡达加特、五博丘、比彻姆两位姑奶奶、巡栏员），新增西比拉全名佩内洛普（Sybylla Penelope Melvyn）与巴库（Barcoo）首见 |
| 2026-10-15 | 25-ah-for-one-hour-of-burning-love-tis-worth-an-age-of-cold-respect.md（第23章 “啊，哪怕一小时的烈火之爱，也胜过一世纪的冷清敬意！”，15.0KB/70 段） | done | check_bilingual.py 退出码 0；70 对块逐段对照，0 可疑错配；原文块自源文逐字节注入并校验一致，17×U+FEFF、11×U+00A0 照录保真；斜体 *you*/*my* 镜像保留；术语表新增 Archie Goodchum、Goodjay、Miss Craddock、Hal、tomtit |
| 2026-10-15 | 24-sweet-seventeen.md（第22章 芳龄十七，16.9KB/71 段） | done | check_bilingual.py 退出码 0；71 对块逐段对照，0 可疑错配；原文块自源文逐字节注入并校验一致，22×U+FEFF、18×U+00A0 照录保真；数字锚点（2:30、104、100）循既有体例以空格分隔保留；古德杰伊（Goodjay）定名与第23章并行译文对齐；术语表新增 George Ledwood、muster、billy、damper、saltbush、mulga、boss-of-the-board、spring-cart、bulldog ant、jackass、cockatoo、La France、Hordern's，Goodchum/Goodjay/Craddock 条目补注第22章首现 |
| 2026-10-15 | 29-my-journey.md（第27章 我的旅程，5.4KB/15 段） | done | check_bilingual.py 退出码 0；15 对块逐段对照，0 可疑错配；原文块自源文逐字节注入并校验一致，3×U+FEFF、1×U+00A0 照录保真；术语沿用既有定名（弗兰克·霍登、迪克·梅尔文、外婆、土著黑人、弹簧轻马车、赶牛车人），“Ta-ta”循第23章“回头见”；麦斯沃特先生于译文首现并括注；术语表新增 Yarnung |
| 2026-10-15 | 27-because.md（第25章 缘何？，8.9KB/33 段） | done | check_bilingual.py 退出码 0；33 对块逐段对照，0 可疑错配；原文块自源文逐字节注入并校验一致，19×U+FEFF 照录保真；日期数字锚点 1896 循既有体例保留；术语沿用既有定名（杰杰舅舅、比彻姆两位姑奶奶、五博丘、牲口大清点、斜叶桉），术语表新增 hickory |
| 2026-10-15 | 28-boast-not-thyself-of-tomorrow.md（第26章 莫向明日夸海口，16.2KB/44 段） | done | check_bilingual.py 退出码 0；44 对块逐段对照，0 可疑错配；原文块自源文逐字节注入并校验一致，27×U+FEFF、6×U+00A0 照录保真；母亲书信 blockquote 版式镜像保留；数字锚点（500、20、1897、10、50、110）循既有体例以阿拉伯数字保留；狗陷报信人土腔（tremenjous、goin'、moke）以汉语乡土口语体现；术语表新增 Flea Creek、Bimbalong、Birribalong、Manly、Parramatta、Cyclorama、Paddy's Market、old Tadpole、Boxing Day、blackthorn、musk、cedar、sidesaddle、moke，Yarnung 条目与第27章并行译文合并 |
| 2026-10-15 | 30-to-life.md（第28章 活下去，14.4KB/59 段） | done | check_bilingual.py 退出码 0；59 对块逐段对照，0 可疑错配；原文块自源文逐字节注入并校验一致，6×U+FEFF、13×U+00A0 照录保真；麦斯沃特一家乡土土腔（wen／groin’／munce／wu-r-r-r-ld、rale／wite／picter／toon／peeany 等）以汉语乡土口语体现；术语表新增 Mary Ann、Lizer、Rose Jane、Jimmy、Red Hill、poley cup、wagonette、Marche Hongroise |
| 2026-10-15 | 32-where-ignorance-is-bliss-tis-folly-to-be-wise.md（第30章 无知是福，聪明反被聪明误，9.8KB/27 段） | done | check_bilingual.py 退出码 0；27 对块逐段对照，0 可疑错配；原文块自源文逐字节注入并校验一致，1×U+FEFF、5×U+00A0 照录保真；霍勒斯家书整块对照、blockquote 版式镜像保留；数字锚点（50、1,600、40,000）循既有体例保留；莱泽/吉米定名与第28章并行译文对齐；术语表新增 Gulf of Carpentaria、Victoria、Mack Pot、Black's Camp、Sullivan's Ginger、Young Ladies' Journal、Australasian，Lizer/Jimmy 条目补注第30章 |
| 2026-10-15 | 31-to-life-continued.md（第29章 活下去（续），23.4KB/79 段） | done | check_bilingual.py 退出码 0；79 对块逐段对照，0 可疑错配；原文块自源文逐字节注入并校验一致，21×U+FEFF、17×U+00A0 照录保真；三段麦斯沃特日记与外婆、母亲三封书信 blockquote 版式镜像保留；麦斯沃特家土腔及日记错拼（Toosday、prawfit、darter、sharn't 及 wint、sheap、sqre padick、boagy 等）以错字乡土风味体现；数字锚点（60、52、20、1896 等）循既有体例空格分隔保留；莱泽、吉米、罗丝·简、红山沿用第28章定名，汤米、萨拉本章首现括注；术语表新增 Tommy、Sarah、Joe Harris、Dave Duffy、Boggie Creek、skillion、paper collars、larrikinism、stone、quince、Tattersall，Jimmy 条目补注第31章 |
| 2026-10-15 | 34-ta-ta-to-barney-s-gap.md（第32章 别了，巴尼山口，5.8KB/19 段） | done | check_bilingual.py 退出码 0；19 对块逐段对照，0 可疑错配；原文块自源文逐字节注入并校验一致，9×U+00A0 照录保真（无 U+FEFF）；麦斯沃特父子土腔（winder／matther／gu-r-r-r-l／prawperty／divil 等）以汉语乡土口语与拖腔错字风味体现，gu-r-r-r-l 循第28章「世——界——」体例作「姑——娘——」；术语沿用既有定名（巴尼山口、莱泽、罗丝·简、古尔本、外婆），无新增术语 |
| 2026-10-15 | 35-back-at-possum-gully.md（第33章 重返袋熊谷，8.7KB/15 段） | done | check_bilingual.py 退出码 0；15 对块逐段对照（含引诗 1 块版式镜像保留），0 可疑错配；原文块自源文逐字节注入并校验一致，7×U+FEFF、1×U+00A0 照录保真；源内 --- 分隔线×2 保留；斜体 *his* 镜像保留；术语沿用既有定名（袋熊谷、巴尼山口、卡达加特、迪克·梅尔文、背起行囊去流浪、霍勒斯口中的“老头子”循第30章），无新增术语 |
| 2026-10-15 | 33-mr-m-swat-and-i-have-a-bust-up.md（第31章 麦斯沃特先生和我大吵一场，14.6KB/40 段） | done | check_bilingual.py 退出码 0；40 对块逐段对照，0 可疑错配；原文块自源文逐字节注入并校验一致，18×U+FEFF、12×U+00A0 照录保真；外婆复活节书信 blockquote 版式镜像保留；斜体 *dare* 镜像保留；麦斯沃特父子土腔（gu-r-r-r-l→姑——娘——、prawperty→家当、coortin'、ev、yuz 及 yeos／hoggets 等）以拖腔／错字乡土风味体现，gu-r-r-r-l 译法与第32章并行译文对齐；数字锚点 1,600 循既有体例保留；术语表新增 Butler、Mick、young Charters、Western Australia、gu-r-r-r-l |
| 2026-10-15 | 37-the-3rd-of-december-1898.md（第35章 1898 年 12 月 3 日，9.4KB/55 段） | done | check_bilingual.py 退出码 0；55 对块逐段对照，0 可疑错配；原文块自源文逐字节注入并校验一致，9×U+FEFF、3×U+00A0 照录保真；哈罗德·比彻姆重逢一节完整译出，Syb 循既有定名作「西比」、Hal 作「哈尔」，奥罗拉娃娃语（Sybyller/somesing/比彻先生等）以汉语儿语错字风味体现，罗瑞（Rory）首现括注，half a crown 首现括注半克朗；术语沿用既有定名（手喂牛犊、五博丘、遮阳帽、围场、桉树），无新增术语 |
| 2026-10-15 | 38-once-upon-a-time-when-the-days-were-long-and-hot.md（第36章 从前，日子漫长而炎热，19.6KB/80 对块） | done | check_bilingual.py 退出码 0；78 段逐段对照＋欧文·梅雷迪思引诗、西比拉拒婚长信各整块对照（blockquote 版式镜像保留），0 可疑错配；原文块自源文逐字节注入并校验一致，28×U+FEFF、1×U+00A0 照录保真；斜体 *will* 镜像保留；老曾祖母土腔（Sybyller→西比拉尔、"How long it do be waiting for the Lord"等）以汉语乡土口语体现，罗瑞（Rory）、西比拉尔译名与第35章并行译文对齐，信末署名循第22章全名西比拉·佩内洛普·梅尔文；本章无 2 位数字锚点；术语表新增 Tocumwal、Bombala、tiger-snake、blarney-stone、Owen Meredith、Rory |
| 2026-10-15 | 36-but-absent-friends-are-soon-forgot.md（第34章 然而故人易忘，12.0KB/39 段） | done | check_bilingual.py 退出码 0；39 对块逐段对照（哈尔求婚信、西比拉回绝信、哈罗德认拒信、格蒂三信、外婆与海伦姨妈信 blockquote 版式镜像保留），0 可疑错配；原文块自源文逐字节注入并校验一致，6×U+FEFF、2×U+00A0 照录保真；数字锚点（1897、1898）循既有体例保留；术语沿用既有定名（杰杰舅舅、五博丘、老尼克、牧场学徒），署名 S.佩内洛普·梅尔文循第22章全名；术语表新增 George Melvyn、she-oak、stock-route |
| 2026-10-15 | 39-he-that-despiseth-little-things-shall-fall-little-by-little.md（第37章 轻视小事者必渐倾覆，7.3KB/22 对块） | done | check_bilingual.py 退出码 0；22 对块逐段对照（格蒂信、外婆信 blockquote 版式镜像保留，引诗整块对照版式镜像保留），0 可疑错配；原文块自源文逐字节注入并校验一致，8×U+FEFF、1×U+00A0 照录保真；子标题 I／II 合并为「### I / 一」「### II / 二」；术语沿用既有定名（哈罗德·比彻姆、哈里、格蒂、杰杰舅舅、五博丘、袋熊谷），衔接第36章拒婚信情节；术语表新增 Mr. Creyton |
| 2026-10-15 | 40-a-tale-that-is-told-and-a-day-that-is-done.md（第38章 一个讲完的故事，一个了结的日子，4.4KB/18 对块）＋ 41-endnotes.md（尾注，0.1KB/1 对块） | done | 两篇均 check_bilingual.py 退出码 0、0 可疑错配；全书末章三首引诗整块对照、诗行版式镜像保留（> 引号与空行交错照录），源内 --- 分隔线×3 游离保留，**Amen.** 加粗镜像；原文块自源文逐字节注入并校验一致，40 章 11×U+FEFF、41 章 2×U+FEFF 照录保真；尾注编号与 ↩︎ 锚点照录，Shouting/Poddied 循术语表「请客（买酒）」「手喂」定名；术语沿用既有定名（袋熊谷、金合欢、黄杨桉、笑翠鸟、袋鸮、庄稼人），muzhiks 首现括注俄国农奴；数字锚点 1899 循既有体例保留 |
