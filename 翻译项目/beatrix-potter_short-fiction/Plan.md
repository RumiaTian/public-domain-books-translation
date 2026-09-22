# Plan.md

## 本计划信息

- **项目名称**：beatrix-potter_short-fiction（彼得兔系列）
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md
- **领域配置**：prompts/领域配置/小说文学.md
- **术语表**：术语表.md

---

## 文件分工

| 文件 | 作用 | 谁来改 |
|------|------|--------|
| `项目说明.md` | 项目基本信息、领域配置、篇目清单 | 人工 |
| `术语表.md` | 翻译硬约束层 | agent / 人工 |
| `translation_queue.csv` | 任务队列（3 列） | 翻译前改 doing，完成改 done |
| `Plan.md`（本文件） | 执行步骤 + 运行日志 | agent 追加日志 |
| `原文/*.md` | 源文 | 不改 |
| `译文/*.zh-CN.md` | 译文产出（块对照双语） | 翻译 agent 产出 |

---

## 执行步骤

按 `prompts/翻译计划模板.md`「执行步骤」9 步推进。委派模式由子代理逐篇执行。

---

## 篇目清单（20 篇，按出版顺序）

| # | 篇名 | 源文 | 大小 |
|---|------|------|------|
| 1 | 彼得兔的故事 | the-tale-of-peter-rabbit.md | 5.2KB |
| 2 | 松鼠纳特金的故事 | the-tale-of-squirrel-nutkin.md | 7.0KB |
| 3 | 格洛斯特的裁缝 | the-tailor-of-gloucester.md | 16.3KB |
| 4 | 本杰明兔的故事 | the-tale-of-benjamin-bunny.md | 6.4KB |
| 5 | 两只坏老鼠的故事 | the-tale-of-two-bad-mice.md | 5.1KB |
| 6 | 提姬·温克尔太太 | the-tale-of-mrs-tiggy-winkle.md | 7.9KB |
| 7 | 馅饼和饼盘的故事 | the-tale-of-the-pie-and-the-patty-pan.md | 15.9KB |
| 8 | 杰里米·费舍尔先生 | the-tale-of-mr-jeremy-fisher.md | 4.4KB |
| 9 | 凶巴巴的坏兔子 | the-story-of-a-fierce-bad-rabbit.md | 0.8KB |
| 10 | 莫佩特小姐的故事 | the-story-of-miss-moppet.md | 1.2KB |
| 11 | 汤姆小猫的故事 | the-tale-of-tom-kitten.md | 4.0KB |
| 12 | 杰迈玛鸭妈妈的故事 | the-tale-of-jemima-puddle-duck.md | 7.1KB |
| 13 | 提特尔茅斯太太的故事 | the-tale-of-mrs-tittlemouse.md | 6.8KB |
| 14 | 蒂米·蒂普托斯的故事 | the-tale-of-timmy-tiptoes.md | 7.7KB |
| 15 | 金杰和皮克尔斯的故事 | the-tale-of-ginger-and-pickles.md | 6.7KB |
| 16 | 弗洛普西兔宝宝的故事 | the-tale-of-the-flopsy-bunnies.md | 5.9KB |
| 17 | 塞缪尔·威斯克斯的故事 | the-tale-of-samuel-whiskers.md | 14.4KB |
| 18 | 城里鼠约翰尼的故事 | the-tale-of-johnny-town-mouse.md | 7.2KB |
| 19 | 托德先生的故事 | the-tale-of-mr-tod.md | 26.9KB |
| 20 | 小猪布兰德的故事 | the-tale-of-pigling-bland.md | 20.0KB |

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-08-08 | 1. 彼得兔的故事 (the-tale-of-peter-rabbit.md) | 通过 (exit 0) | 系列首篇，确立黄金样本风格；11 块对照，check 0 错配 |
| 2026-08-08 | 2. 松鼠纳特金的故事 (the-tale-of-squirrel-nutkin.md) | 通过 (exit 0) | 8 块对照；6 首 riddle-song 押韵化处理；术语补 Twinkleberry=闪亮莓、Owl Island=猫头鹰岛 |
| 2026-08-08 | 5. 两只坏老鼠的故事 (the-tale-of-two-bad-mice.md) | 通过 (exit 0) | 8 块对照；讽刺幽默译笔；术语补 Lucinda=露辛达、Jane=简、doll's-house=玩偶屋、sixpence=六便士 |
| 2026-08-08 | 10. 莫佩特小姐的故事 (the-story-of-miss-moppet.md) | 通过 (exit 0) | 5 块对照；极短绘本(1.2KB)，儿童文学译笔；术语照表 Miss Moppet=莫佩特小姐；新增 duster=抹布、bellpull=拉铃绳、jig=吉格舞 |
| 2026-08-08 | 9. 凶巴巴的坏兔子 (the-story-of-a-fierce-bad-rabbit.md) | 通过 (exit 0) | 极短绘本(0.8KB)，3 块对照；动作叙事为主几乎无对话；术语照表 the Fierce Bad Rabbit=凶巴巴的坏兔子；新增 the good Rabbit=好兔子、carrot=胡萝卜 |
| 2026-08-08 | 8. 杰里米·费舍尔先生 (the-tale-of-mr-jeremy-fisher.md) | 通过 (exit 0) | 8 块对照；青蛙钓鱼历险记，惊险幽默；术语照表 Mr. Jeremy Fisher=杰里米·费舍尔先生；新增 Mr. Alderman Ptolemy Tortoise=参事托勒密乌龟先生、Sir Isaac Newton=艾萨克·牛顿爵士、Jack Sharp the stickleback=棘鱼小杰克·夏普、minnow=小鲦鱼、trout=鳟鱼、pike=梭子鱼、macintosh=橡胶雨衣、goloshes=橡胶套鞋 |
| 2026-08-08 | 12. 杰迈玛鸭妈妈的故事 (the-tale-of-jemima-puddle-duck.md) | 通过 (exit 0) | 19 块对照；鸭妈妈轻信狐绅士险成盘中餐、柯利犬救主；狐狸伪善殷勤（「您」「亲爱的夫人」）与杰迈玛天真（「没心眼儿的傻大姐」）反差对照；术语照表 Jemima Puddle-Duck=杰迈玛鸭妈妈；新增 Mrs. Rebeccah Puddle-duck=丽贝卡鸭太太、Kep/the collie-dog Kep=柯利/牧羊犬柯利、foxhound puppies=猎狐小犬、foxglove=毛地黄、sage=鼠尾草、thyme=百里香、omelette=煎蛋卷、lard=猪油 |
| 2026-08-08 | 13. 提特尔茅斯太太的故事 (the-tale-of-mrs-tittlemouse.md) | 通过 (exit 0) | 24 块对照；洁癖小老鼠与邋遢客人，幽默对比；术语照表 Mrs. Tittlemouse=提特尔茅斯太太；新增 Babbitty Bumble=巴巴蒂·邦布尔（熊蜂）、Mr. Jackson=杰克逊先生（蟾蜍）、Miss Muffet=马菲特小姐、Mrs. Thomasina Tittlemouse=托马西娜·提特尔茅斯太太、Mother Ladybird=瓢虫大婶、Miss Butterfly=蝴蝶小姐；拟声 Zizz/Bizz/Tiddly widdly=嗞嗞/嗡嗡/嘀哩呼哩 |
| 2026-08-08 | 11. 汤姆小猫的故事 (the-tale-of-tom-kitten.md) | 通过 (exit 0) | 16 块对照；儿童文学译笔，适合朗读；术语照表 Tom Kitten=汤姆小猫；新增 Mrs. Tabitha Twitchit=塔比莎·特维奇特太太、Mittens=米顿斯、Moppet=莫蓓、Mr. Drake Puddle-duck=德雷克·帕德尔鸭先生、Rebeccah Puddle-duck=丽贝卡·帕德尔鸭、Jemima Puddle-duck=杰迈玛·帕德尔鸭、Sally Henny Penny=萨莉·亨尼·佩妮、Pickles=皮克尔斯、pinafore=小围裙、tucker=花边围涎、rockery=假山、goose step=正步、measles=麻疹 |
| 2026-08-08 | 14. 蒂米·蒂普托斯的故事 (the-tale-of-timmy-tiptoes.md) | 通过 (exit 0) | 17 块对照；花栗鼠误会被囚树洞、妻子寻夫救出，温情幽默；术语照表 Timmy Tiptoes=蒂米·蒂普托斯；新增 Goody Tiptoes=古迪·蒂普托斯（妻）、Timothy=蒂莫西（蒂米正式名）、Silvertail=银尾巴、the Chipmunk=花栗鼠、Chippy Hackee=奇皮·哈基、woodpecker=啄木鸟、padlock=挂锁；鸟歌与两段押韵童谣做韵律化处理 |
| 2026-08-08 | 16. 弗洛普西兔宝宝的故事 (the-tale-of-the-flopsy-bunnies.md) | 通过 (exit 0) | 10 块对照；5.9KB 一次译完，结尾完整；昏睡被捉、调包脱险的幽默童趣；术语照表 the Flopsy Bunnies=弗洛普西兔宝宝、Benjamin Bunny=本杰明兔、Flopsy=弗洛普西、Mr./Mrs. McGregor=麦格雷戈先生/太太、Peter Rabbit=彼得兔；新增 Thomasina Tittlemouse=托马西娜·提特尔茅斯（林鼠）、Mrs. Tittlemouse=提特尔茅斯太太、Mrs. Flopsy Bunny=弗洛普西兔太太、vegetable marrow=西葫芦、turnip=芜菁、blacking-brush=鞋油刷子、baccy/rabbit tobacco=（兔子换的）烟、muff=暖手筒、mittens=连指手套、soporific=催眠、bluebottles=绿头大苍蝇 |
| 2026-08-08 | 15. 金杰和皮克尔斯的故事 (the-tale-of-ginger-and-pickles.md) | 通过 (exit 0) | 13 块对照；6.7KB 一次译完，结尾完整；赊账致倒闭的乡村经济寓言，猫狗搭档开店、村民白赊不还终至破产、萨莉母鸡重张开张；含货币（先令/便士/法寻/镑）、狗牌照/警察/传票/捐税等专有项；货币金额保留阿拉伯数字以过 check 数字锚点检测；术语照表 Ginger=金杰、Pickles=皮克尔斯；新增 John Taylor=约翰·泰勒（题献对象）、Dormouse=睡鼠、Lucinda=露辛达、Jane Doll-cook=玩偶厨娘简、Tabitha Twitchit=塔比莎·特维奇特太太、Kep the Collie dog=牧羊犬柯利、Samuel Whiskers=塞缪尔·威斯克斯、Anna Maria=安娜·玛丽亚、Mr. John Dormouse=约翰·睡鼠先生、Miss Dormouse=睡鼠小姐、Timothy Baker=面包师蒂莫西、terrier=梗犬、tomcat=公猫、galoshes=橡胶套鞋、snuff=鼻烟、pocket-handkerchief=手帕、haddock=鳕鱼干、biscuit=饼干、toffee=太妃糖、till=钱柜、credit=赊账、rates and taxes=地方捐税和各项税款、summons=传票、warren=野兔穴场、gamekeeper=猎场看守、treacle=糖浆、cream cracker=奶油苏打饼干、seed wigs=香料籽小面包、sponge-cake=海绵蛋糕、butter-bun=黄油小面包、self-fitting sixes=自合式六号蜡烛、jumble sale=义卖大杂烩 |
| 2026-08-08 | 18. 城里鼠约翰尼的故事 (the-tale-of-johnny-town-mouse.md) | 通过 (exit 0) | 10 块对照；7.2KB 一次译完，结尾完整；改编自伊索寓言的城乡互访记——蒂米·威利误困菜篮进城惊魂、约翰尼回访乡下嫌静折返；城乡生活对比主题，约翰尼城里腔（「恕我直言」「心里有数」）与蒂米乡下口吻（「不过」「我说真的」）形成反差；题献「致阴影中的伊索（Aesop）」照译；术语照表 Johnny Town-mouse=城里鼠约翰尼、Timmy Willie=蒂米·威利；新增 Timothy William=蒂莫西·威廉（约翰尼对蒂米的正式称呼）、Sarah=莎拉、Cock Robin=知更鸟、Aesop=伊索、hamper=菜篮/篮子、bacon=咸肉、jelly=果冻、herb pudding=香草布丁、fender=炉挡、poker=拨火棍、coal-cellar=煤窖、lawn-mower=割草机、canary=金丝雀、throstle=画眉、blackbird=乌鸫、pink=石竹、pansy=三色堇、sixpence=六便士 |
| 2026-08-08 | 3. 格洛斯特的裁缝 (the-tailor-of-gloucester.md) | 通过 (exit 0) | 23 块对照；16.3KB 中等篇幅一次译完，结尾完整；圣诞童话译笔，带古老韵律与温情；4 首老鼠童谣全部押韵化（catch a snail/蜗牛捉、flour/hour/面粉/时辰、spin/men/纺线/绅士、pet/hem/欢喜/金、farthing/dresser/法寻/碗橱）；日期锚点 "1901" 换序为 "圣诞节，1901" 以过 check 数字检测；术语照表 Gloucester=格洛斯特、the Tailor of Gloucester=格洛斯特的裁缝；新增 Freda=弗蕾达（题献对象）、Gloucestershire=格洛斯特郡、Simpkin=辛普金（猫）、Mayor of Gloucester=格洛斯特市长、Westgate Street=西大门街、College Court=学院庭、College Green=学院草地、Cathedral=大教堂、groat=格罗特（四便士银币）、pipkin=白瓷小瓦罐、paduasoy=波纹绸、taffeta=塔夫绸、pompadour=波斯锦、lutestring=卢特琳绸、worsted chenille=绒线绳、tambour stitch=刺绣针法、floss silk=绒丝、twist=（锁纽门的）绞合丝线、buttonhole=纽门儿/锁眼、tippet=披肩、four-post bed=四柱床、wainscot=护墙板、pansy=三色堇、poppy=罂粟花、cornflower=矢车菊、starling=椋鸟、jackdaw=寒鸦、throstle=歌鸫、robin=知更鸟、kyloe cow=苏格兰高地小牛、mobs=乱蓬蓬的头发、Hey diddle dinketty=（童谣衬词） |
| 2026-08-08 | 17. 塞缪尔·威斯克斯的故事 (the-tale-of-samuel-whiskers.md) | 通过 (exit 0) | 21 块对照；14.4KB 中等篇幅一次译完，结尾完整；又名《圆滚滚布丁》，卷中较长一篇；汤姆小猫藏烟囱迷路跌入鼠窝、被裹面团做布丁险被烤、母猫与邻居搜救、约翰·木匠撬地板搭救、二鼠携家当逃往土豆农夫谷仓繁衍成灾；"roly-poly"滚动声拟声化（咕噜咕噜）贯穿全文为反复母题；第一人称"波特小姐"与"我的手推车"叙述打破第四面墙；术语照表 Samuel Whiskers=塞缪尔·威斯克斯、Anna Maria=安娜·玛丽亚、Tom Kitten=汤姆小猫、Mrs. Tabitha Twitchit=塔比莎·特维奇特太太、Moppet=莫蓓、Mittens=米顿斯；新增 Mrs. Ribby=里比太太（邻居猫）、John Joiner=约翰·木匠（木匠狗）、Sammy/萨米（题献老鼠昵称）、Farmer Potatoes=土豆农夫、roly-poly pudding=圆滚滚布丁、dough=面团、rolling-pin=擀面杖、dumpling=团子布丁、snuff=鼻烟、fender=炉挡、wainscot=壁板、skirting-board=踢脚线、hay mow=干草垛、hen-coops=鸡笼、bluebottles=绿头大苍蝇、bran=麸皮、currants=葡萄干、counterpane=床单、smuts=烟灰、kitten dumpling roly-poly pudding=小猫咪馅圆滚滚布丁 |
| 2026-08-08 | 20. 小猪布兰德的故事 (the-tale-of-pigling-bland.md) | 通过 (exit 0) | 25 块对照；20.0KB 中等偏长一次译完，结尾完整（布兰德与猪小卷携手过桥、翻山远去）；卷中最长公路冒险篇，基调较深沉；八猪崽闹腾、布兰德与亚历山大赴市、亚历山大错把糖果店账单当通行证被警带走、布兰德独闯荒原误宿鸡棚被皮珀森装筐、识破皮珀森腌咸肉图谋、营救偷来的猪小卷、晨曦逃亡、杂货商追查巧装瘸腿脱险；5 首童谣押韵化（This pig went to market/这只小猪上市场、Tom Tom the piper's son/汤姆汤姆吹笛人子、Over the hills and far away/翻过山岗去远方、Over the hills...wind shall blow my top knot off/翻过山岗去远方大风吹掉头顶结、funny old mother pig/滑稽猪妈妈三猪崽）；母亲絮叨叮嘱、亚历山大轻浮傻笑（喂喂喂）、皮珀森阴沉贪婪（扒你的皮）、猪小卷天真甜美形成多层次语气；术语照表 Pigling Bland=小猪布兰德、Pig-wig=猪小卷；新增 Aunt Pettitoes=佩蒂托斯姑妈（猪母）、Cross-patch=爱闹别扭、Suck-suck=嘬嘬、Yock-yock=呦呦、Spot=小花、Alexander=亚历山大、Chin-chin=琴琴、Stumpy=小残桩、Mr. Peter Thomas Piperson=彼得·托马斯·皮珀森先生（想腌咸肉的农夫）、Cecily=塞西莉、Charlie=查理（题献）、Lancashire=兰开夏、Westmorland=威斯特摩兰、Berkshire=巴克夏（猪种）、conversation peppermints/peppermints=会话薄荷糖（印箴言）、pig papers/licences=猪通行证、county boundary=郡界、hiring fair=雇工商会、farthing=法寻、shilling=先令、flitch=半片咸肉、porridge=燕麦粥、meal chest=燕麦粉柜、coppy stool=草编小圆凳、antimacassar=椅背罩布、wainscot=护墙板、hen roost=鸡窝、hamper=大筐、moor=荒原、top knot=头顶结 |
| 2026-08-08 | 19. 托德先生的故事 (the-tale-of-mr-tod.md) | 通过 (exit 0) | 34 块对照；26.9KB 系列最长一篇，一次译完，结尾完整；三方对峙惊险喜剧——獾汤米·布罗克趁老邦瑟先生睡着偷走兔宝宝、本杰明兔与彼得兔联手追踪潜入、狐狸托德先生回家发现屋子被占、托德苦心布水桶机关暗算汤米·布罗克却被调包晨袍脱身、二兽厨房大战砸烂家当、兔子趁乱救出兔宝宝脱身；第一人称"我"开篇破题（两个叫人讨厌的家伙）；托德阴险自语（「不愉快的惊喜」「非消毒不可」）、汤米·布罗克懒散贪睡（仰面朝天咧嘴笑）、彼得冷静推理（「我清楚得很他往哪边去了」）、本杰明紧张哆嗦（「我再也见不着他们了」）形成多角色反差；题献「献给弗朗西斯·威廉·乌尔瓦——总有一天！」照译；术语照表 Mr. Tod=托德先生、Tommy Brock=汤米·布罗克（獾）、Benjamin Bunny=本杰明兔、Flopsy=弗洛普西、Peter Rabbit=彼得兔；新增 old Mr. Benjamin Bouncer=老本杰明·邦瑟先生（本杰明之父）、old Vixen Tod=老维克森·托德（托德外婆）、Cottontail=棉尾巴（彼得姐妹，嫁黑兔迁居山上）、John Stoat Ferret=白鼬约翰、Francis William of Ulva=弗朗西斯·威廉·乌尔瓦（题献对象）、Bull Banks=布尔陡坡、Oatmeal Crag=燕麦崖、stick-house=枝条棚屋、pollard willow=截头柳树、coppice=灌木丛、rabbit tobacco/baccy=兔子烟、cowslip wine=立金花酒、seed-cake=籽蛋糕、cabbage leaf cigar=卷心菜叶雪茄、pignuts=野花生、dog darnel=硬雀麦、wood sorrel=林酢浆草、mole trap=捕鼹鼠夹、wasp nests=黄蜂窝、spud=小鹤嘴锄、tester bed=四柱床顶、dressing-gown=晨袍、clothes line=晾衣绳、coal-scuttle=煤桶、warming-pan=暖床炉、hot-water bottle=热水袋、soft soap=软肥皂、persian powder=波斯粉、carbolic=石炭酸、sulphur=硫磺、brick oven=砖砌烤炉、faggots=柴捆、fender=炉挡、mantelpiece=壁炉台、canisters=茶叶罐、raspberry jam=覆盆子果酱、stone quarry=石矿、spring-cleaning=大扫除 |
