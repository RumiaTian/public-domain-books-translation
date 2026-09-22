# 翻译计划：爱尔兰童话

## 本计划信息

- **项目名称**：james-stephens_irish-fairy-tales
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/小说文学.md
- **术语表**：术语表.md
- **执行模式**：委派（短篇集；见 WORKFLOW.md「单篇翻译流程」）

## 执行步骤

单篇 9 步（读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志）以 `prompts/翻译计划模板.md`「执行步骤」为准，本文件不重复。委派模式下由主 agent 派单，子代理简报含黄金样本与前篇末尾。

## 篇目清单

由 `translation_queue.csv` 管理（12 篇，约 348KB）。

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-09-08 | 全书 12/12（dedication ~ endnotes） | done | 《爱尔兰童话》整本完结。批次1主代理滚动验收：11/12 文件 rc=0；mongan-s-frenzy rc=1 仅两处  边界数字锚点技术性误报（公元538年/624年逐字保留，已复核无错配）。术语表由主代理合并回填 218 行（含蒙根/王土米斯跨篇裁定、Faery 语境二分、克鲁亨元素对齐、### I / I 小节标题格式统一）。全书凯尔特专名体系自洽，脚注锚点双语呼应闭环。 |
| - | - | - | （尚未运行） |
| 2026-09-08 | dedication.md | done | 新定名：Helen Fraser＝海伦·弗雷泽；献词对象 Seumas and Iris 按嘱保留原文 |
| 2026-09-08 | the-story-of-tuan-mac-cairill.md | done | 新定名：Finnian＝芬尼安；Muredac Red-neck＝红颈穆雷达克；Starn＝斯塔恩；Sera＝塞拉；Agnoman＝阿格诺曼；Eirè＝埃雷；Mugain＝穆盖恩；Colm Cillé＝科尔姆·基莱；Leinster＝伦斯特；Semion＝塞米昂；Stariath＝斯塔里亚特；Domnann＝多姆南；Fir Bolg＝菲尔·博尔格；Galiuin＝加利乌因；Beothach＝贝奥塔赫；Iarbonel＝亚博内尔；Andè＝安德神族；Mil（之子）＝米尔（之子）；Faery＝仙灵之族；Doom＝劫数；Time＝时光（拟人）。硬约束词图安·麦克·凯里尔、达南神族按策略区执行；节号罗马数字照搬 |
| 2026-09-08 | the-birth-of-bran.md | done | 新定名：布兰（Bran）、斯科兰（Sceólan）、费格斯·芬利亚斯（Fergus Fionnliath）、戈尔韦、尤尔（Uail）、穆尔娜（Muirne，同 Murna）、阿伦（Allen）、蒂伦（Tuiren）、芬尼亚勇士团（Fianna）、约兰·埃赫塔赫（Iollan Eachtach）、卡尔特·麦克·罗南、戈尔·麦克·莫尔纳（Morna＝莫尔纳）、卢盖德（Lugaidh）、仙丘（the Shí）、乌克特·迪亚尔夫（Uct Dealv，「玉乳」）、仙境（Faery，作地名；与图安篇 Faery＝仙灵之族 请主代理统一）、永青之国（Land of the Ever Young）、提尔纳诺格（Tír na n-Og）、巴斯克内（Baiscne）；小节标题采「### I / I」合并行（EPUB 契约标题不进块） |
| 2026-09-08 | the-wooing-of-becfola.md | done | 新定名：Dermod（mac Ae）＝迪尔梅德（·麦克·艾）；Ae of Slane＝斯莱恩的艾；Crimthann＝克里姆坦；Ard-Rí＝至高王；Tara＝塔拉；Duffry＝达弗里；Cluain da chaillech＝克卢恩·达·卡列赫；Flann＝弗兰；Fedach／Dali＝费达赫／达利；Molasius of Devenish＝德文尼什的莫拉修斯；the Shí＝仙丘（同布兰篇）；Faery 作地名从布兰篇先例改「仙境」；Becfola 诨名「无嫁妆／薄妆」随文释义；节号罗马数字照搬入块（图安篇先例） |
| 2026-09-08 | ois-n-s-mother.md | done | 新定名：Oisín＝奥辛（首现「奥辛（Oisín）」，诨名「小鹿」）；Saeve＝赛芙（奥辛之母，即传统拼写 Sadb）；Fear Doirche＝费尔·多尔切（随文释「黑暗之人」）；Lochlann＝洛克兰（Lochlannachs＝洛克兰人）；Ben Edair／Ben Edar＝本·埃代尔；Ben Gulbain＝本·古尔本；Moy Lifé＝莫伊·利菲；Conán＝柯南；the Flower of Allen＝阿伦之花；Gariv Cronán＝加里夫·克罗南（诨名「嗡嗡粗嗓」the Rough Buzzer）；猎犬 Lomaire＝洛迈雷、Brod＝布罗德、Lomlu＝洛姆卢；the Men of God 的 Black Magician＝众神之民的黑魔法师；the High King＝至高王；Fianna-Finn 归并译「芬尼亚勇士团」；源文 Brah＝布兰、Vran／Heólan 为布兰／斯科兰呼格，随文按正名译；Faery 作地名译「仙境」（布兰篇先例）；小节标题「### I / I」合并行照布兰篇先例 |
| 2026-09-08 | the-boyhood-of-fionn.md | done | 新定名：Bovmall＝波芙玛尔；Lia Luachra＝丽娅·卢阿赫拉（简报作 Liad，从源文）；Mananánn＝玛纳南；Teigue＝泰格；Nuada＝努阿达；Ethlinn＝埃丝琳；Lugh of the Long Hand＝长臂卢格；Kerry＝凯里；Slieve Bloom＝斯利夫·布卢姆；Deimne＝代姆内；Connacht/Connaught＝康诺特；Conán Mael mac Morna＝柯南·梅尔·麦克·莫尔纳（Conán the Swearer＝起誓者柯南，Conán 从奥辛篇「柯南」）；Garra Duv mac Morna＝加拉·杜夫·麦克·莫尔纳（the Rough mac Morna＝「粗暴的麦克·莫尔纳」）；Art Og＝阿特·奥格（of the Hard Strokes＝「重击」）；the Galtees＝加尔蒂山；Fiacuil mac Cona＝菲亚库尔·麦克·科纳；Aillen mac Midna＝艾伦·麦克·米德纳（区别于 Allen＝阿伦）；Shí Finnachy＝芬纳希仙丘；Slieve Fuaid＝斯利夫·富阿德；Moy Lifé＝莫伊·利菲（从奥辛篇）；Lock Léin＝洛克·林；Finntraigh＝芬特拉；Boyne Water＝博因河；Finegas＝芬尼加斯；Salmon of Knowledge＝智慧鲑鱼（Nuts of Knowledge＝智慧坚果）；Shannon＝香农河；Suir＝苏尔河；Ana Lifé＝安娜·利菲；Tara of the Kings＝诸王的塔拉；Samhain＝萨温节；Ard-Rí/High King＝至高王；Conn of the Hundred Battles＝「百战」康恩；Art（康恩之子）＝阿特；Dagda Mor＝达格达·莫尔；Tir na n-Og, the Land of the Young＝提尔纳诺格·永青之国（Land of the Young 归「永青之国」）；Red Cith＝红发基斯；Luigne＝卢伊涅；Oisín＝奥辛（从奥辛篇）；Oscar＝奥斯卡；Dirim/mac-Reith＝迪里姆/麦克-雷斯；Birgha＝比尔加；Glen of the Mantle＝斗篷峡谷；Ard of Fire＝火之高地；Munster＝芒斯特；ogham＝欧甘文；timpan＝蒂姆潘琴；ollav＝大学者；tribes of Dana＝达南神族部族；Goll Mor mac Morna 归并术语表定名「戈尔·麦克·莫尔纳」；源文误拼 Balscne/Shl 按正字法译（巴斯克内/仙丘）；小节标题「### I / I」合并行照布兰篇先例 |
| 2026-09-08 | the-enchanted-cave-of-cesh-corran.md | done | 新定名：Cesh Corran＝克什科兰（标题定名）；Conaran＝科纳兰（Imidel＝伊米德尔）；四女 Caevóg＝卡沃格、Cuillen＝库伦、Iaran＝伊阿兰、Iarnach＝伊阿娜赫；地名 Legney＝莱格尼、Brefny＝布雷夫尼、Glen Dallan＝达兰峡谷、Carbury＝卡伯里、Kyle Conor＝凯尔·康纳、Moy Conal＝莫伊·科纳尔；mac Lugac＝麦克·卢加克；clann-Corcoran＝科克伦氏族、clann-Smól＝斯莫尔氏族；Cairell＝卡雷尔；whiskers＝颊须（区别 moustaches＝髭须）；源文误拼 Cesh Cotran／we llve 按正字法译；Goll mor mac Morna 归并「戈尔·麦克·莫尔纳」（芬恩篇先例）；Conán the Swearer＝「起誓者」柯南；小节标题「### I / I」合并行照布兰篇先例 |
| 2026-09-08 | the-little-brawl-at-allen.md | done | 新定名：Cairell Whiteskin＝白皮卡雷尔（诨名「白皮」，Cairell 从克什科兰篇「卡雷尔」）；Dermod of the Gay Face＝快活脸迪尔梅德（Dermod 从贝克福拉篇）；Fergus True-Lips＝真唇费格斯；mac Lugac of the Terrible Hand＝可怕之手麦克·卢加克（mac Lugac 从克什科兰篇）；clann-Morna＝莫尔纳氏族；史诗歌类 the Forts/Destructions/Raids/Wooings＝《堡寨》《焚毁》《袭掠》《求婚》；White Lochlann＝白洛克兰（即挪威，Lochlann 从奥辛篇）；battle of Cnocha＝克诺卡之战；Faelan＝费兰；Cormac mac Art＝科马克·麦克·阿特（Art 从芬恩篇「阿特」）；Ailve＝阿尔薇；Cairbre of Ana Lifé＝安娜·利菲的卡布雷（Ana Lifé 从芬恩篇）；Fintan (mac Bocna)＝芬坦（·麦克·博克纳），源文 Fiontan 同人同译；Flahri＝弗拉里；Feehal＝费哈尔；Rough Hair mac Morna＝乱发麦克·莫尔纳；Gara mac Morna＝加拉·麦克·莫尔纳（与芬恩篇 Garra Duv＝加拉·杜夫 同名归并）；沿用先成篇：Art og＝阿特·奥格·麦克·莫尔纳、Tara of the Kings＝诸王的塔拉、Tara＝塔拉、Lochlannachs＝洛克兰人；源文小节标题「### II3」之「3」为排版衍文，按罗马数字 II 照搬；小节标题「### I / I」合并行照布兰篇先例 |
| 2026-09-08 | the-carl-of-the-drab-coat.md | done | 新定名：the Carl of the Drab Coat＝褐衣卡尔（标题定名，Carl＝卡尔）；Cael of the Iron＝铁凯尔（Cael 从候选表「凯尔」）；Thessaly＝色萨利（King of Thessaly＝色萨利国王）；Slieve Luachra＝斯利夫·卢阿赫拉（the Hill of the Rushes 随文释「灯心草山」）；Rath Cruachan＝拉斯克鲁亨（the Shí of Rath Cruachan＝拉斯克鲁亨仙丘）；meal＝麦粉；seven leagues＝七里格；沿用先成篇：Ben Edair＝本·埃代尔（脚注锚点「本·埃代尔4（Ben Edair）」式）、Fianna＝芬尼亚勇士团、Conán＝柯南、Caelte mac Ronán＝卡尔特·麦克·罗南、Tara of the Kings＝诸王的塔拉、Cesh Corran＝克什科兰、Munster＝芒斯特、doom 小写作「劫数」；源文 *is* 斜体以语气体现；小节标题「### I / I」合并行照布兰篇先例 |
| 2026-09-08 | becuma-of-the-white-skin.md | done | 新定名：Becuma of the White Skin＝白肤贝库玛（标题定名）；Becuma Cneisgel＝贝库玛·克尼斯格尔；Eogan Inver＝埃奥甘·因弗；Labraid＝拉布拉德；Gadiar＝加迪亚尔；Manannán mac Lir＝玛纳南·麦克·利尔；the Many-Coloured Land＝斑斓之国；the Land of Wonder＝奇境；the Land of Promise＝应许之地；Eithne＝埃丝妮；Brisland Binn＝布里斯兰·宾；Brugh＝布鲁格；Angus Og／Angus mac an Og＝安格斯·奥格／安格斯·麦克·安·奥格；Cruachan Ahi＝克鲁亨·阿伊（Cruachan 从卡尔篇「拉斯克鲁亨」对齐）；Ethal Anbual＝埃塔尔·安布阿尔；Tailltin＝塔尔廷；Royal Meath＝王土米斯；Delvcaem＝德尔夫卡姆（Fair Shape 随文释「美好身形」）；Morgan＝摩根；Cromdes＝克罗姆德斯；Rigru＝里格鲁（Large-eyed 随文释「大眼」）；Lodan＝洛丹；Daire Degamra／Darè＝达雷；Segda＝塞格达（Sweet Speech 随文释「甜言」）；geasa＝盖萨（禁忌）；Curoi mac Darè＝库罗伊·麦克·达雷；Sliev Mis＝斯利夫·米斯；Eogabal＝埃戈瓦尔；Ainè＝艾妮；Inver Colpa＝因弗·科尔帕；Credè＝克蕾德（the Truly Beautiful＝「真美」）；Ailill of the Black Teeth＝黑牙阿伊利尔；Mongan Tender Blossom＝蒙根·嫩花；Sliav Saev＝斯利夫·塞夫；Dog Head＝狗首（the Dog Heads＝狗首人）；Sasana＝萨萨纳；Ir＝「爱尔」；coracle＝柳条小舟；沿用先成篇：「百战」康恩、阿特、芬恩、尤尔、至高王（Ard-Rí）、塔拉／诸王的塔拉、仙丘／仙境、康诺特、本·埃代尔、博因河、劫数（Doom）；源文 *Can* 斜体以语气体现；小节标题「### I / I」合并行照布兰篇先例 |

| 2026-09-08 | mongan-s-frenzy.md | done | 新定名：Mongan＝蒙根（从贝库玛篇先定，标题《蒙根的狂怒》）；Cairidè＝凯里德；Brótiarna the Flame Lady＝布罗蒂亚娜（火焰夫人）；Black Hag＝黑老妪；Fiachna Finn＝菲亚赫纳·芬、Fiachna Duv (mac Demain)＝菲亚赫纳·杜夫（·麦克·德曼）；Eolgarg Mor＝埃奥尔加格·莫尔（Big Eolgarg＝大埃奥尔加格）；Baltan＝巴尔坦；Murchertach＝穆尔切塔赫；Eogan＝埃奥甘；Neill＝尼尔；Dal Fiatach＝达尔·菲亚塔赫；Dun Fiathac＝邓·菲亚萨克；Condad Cerr＝康达德·切尔、Dal Riada＝达尔·里亚达、battle of Ard Carainn＝阿德·卡林之战；Ciaran the son of the Carpenter＝木匠之子基兰；Tuathal Maelgariv＝图阿尔·梅尔加里夫；Diarmait son of Cerrbel＝瑟尔贝尔之子迪尔梅德；Hill of Uisneach＝乌斯尼奇山；Branduv (son of Echach)＝布兰杜夫（埃卡赫之子）；An Dáv＝安·达夫、mac an Dáv＝麦克·安·达夫；Tibraidè＝蒂布拉德；Cell Camain＝凯尔·卡曼（the Moy of Cell Camain＝凯尔·卡曼草原）；Kevin Cochlach＝凯文·科克拉克；Hag of the Mill＝磨坊老妪；Brotar＝布罗塔尔；Ivell of the Shining Cheeks＝双颊生辉的伊薇尔；Ae the Beautiful＝美男子艾（Ae 从贝克福拉篇）；Rath Descirt of Bregia＝布里吉亚的拉斯·德斯卡特；Moy Linney＝莫伊·林尼；Lir＝利尔（利尔之子）；沿用先成篇：应许之地、王土米斯（贝库玛篇）、玛纳南（芬恩篇）、洛克兰／洛克兰人（奥辛篇）、莫伊·利菲（奥辛篇）、芒斯特／康诺特／伦斯特／阿尔斯特、劫数（Doom）、时光（Time）、仙境（Faery 作地名）、芬恩、至高王；两首歌谣保留 > 引用结构；年份 538／624 按「公元538年／624年」保留数字 |
| 2026-09-08 | endnotes.md | done | 尾注四条：Fionn 读音（Fewn，与 tune 押韵）、Oisín 读作 Usheen、Uail 之死版本不确且克诺卡在爱尔兰而非洛克兰、Ben Edair 即豪斯山（the Hill of Howth）；Fewn/tune/Usheen 保留原词；全部沿用术语表既定名，无新定名；全书 12/12 完结 |
