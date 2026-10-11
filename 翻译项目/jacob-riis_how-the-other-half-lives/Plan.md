# 翻译计划（另一半人怎样生活）

## 本计划信息

- **项目名称**：另一半人怎样生活（雅各布·里斯）
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/学术著作.md
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

按 `prompts/翻译计划模板.md`「执行步骤」9 步推进（读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志）。委派模式下由子代理逐章执行，主 agent 调度。

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
| 2026-10-08 | 00-preface.md（序言 Preface） | done | 2 对块；双脚本通过；新增术语 newspaper man=报人 |
| 2026-10-08 | 01-epigraph.md（卷首诗 题词 Epigraph） | done | 1 对块；双脚本通过；无新增术语 |
| 2026-10-08 | 02-introduction.md（导言 Introduction） | done | 6 对块；双脚本通过；新增术语 Brooklyn=布鲁克林、tenant house=廉租公寓（变体拼法）、police court=治安法庭、workhouse=济贫院、rapid transit=快速交通、riot of 1863=1863年大暴乱 |
| 2026-10-08 | 03-genesis-of-the-tenement.md（第一章 廉租公寓的起源 Genesis of the Tenement） | done | 8 对块；双脚本通过；新增术语 rear house=后屋、Knickerbocker=尼克博克人、Gotham Court=哥谭院 等 15 条 |
| 2026-10-08 | 04-the-awakening.md（第二章 觉醒 The Awakening） | done | 5 对块；双脚本通过；新增术语 8 条（air-shaft=通风井、Sunday law=星期日法、cave-dwellers=穴居人、Council of Hygiene=卫生理事会、Subtreasury=国库分库、Annexed District=兼并区、Houston Street=休斯敦街、Westchester=威彻斯特） |
| 2026-10-08 | 05-the-mixed-crowd.md（第三章 混杂的人群 The Mixed Crowd） | done | 12 对块；双脚本通过；新增术语 the Battery=炮台、Little Italy=「小意大利」、Collect Pond=收集池、Cherry Street=樱桃街、Teuton=条顿人、Alderman=市议员、draft-riots=征兵暴乱 等 19 条 |
| 2026-10-08 | 07-the-italian-in-new-york.md | done | 摘要：双脚本过检回收（代理死于 [1308] 收尾阶段，译文 17.9KB 完整落盘、CSV 已自回填，调度方双脚本复核退出码均 0 后补记本行） |
| 2026-10-09 | 09-a-raid-on-the-stale-beer-dives.md（第七章 突击坏啤酒窟 A Raid on the Stale-Beer Dives） | done | 14 对块；双脚本通过；新增术语 Pearl Street=珍珠街、West Side=西区、Fourteenth Street=第十四街、two-cent restaurant=两分钱饭馆、sitters=「坐客」、sergeant=警佐、locust=洋槐木警棍、Revolvers=「回炉客」、banker=「银行家」、tough=恶棍、police-station lodging-room=警察局寄宿室、trampdom=流浪界 等 12 条 |
| 2026-10-09 | 08-the-bend.md（第六章 弯道区 The Bend） | done | 19 对块；双脚本通过；新增术语 Paradise Park=乐园公园、the House of Blazes=「火焰之屋」、Pasquale=帕斯夸莱、Antonia Candia=安东尼娅·坎迪亚、ristorante=意大利餐馆、standing room only=只有站票、crazy-house=疯人院、tobacco bureau=「烟草局」 等 8 条 |
| 2026-10-09 | 06-the-downtown-back-alleys.md（第四章 城中心的后巷 The Downtown Back-Alleys） | done | 21 对块；双脚本通过；新增术语 Blind Man’s Alley=盲人巷、Swamp Angels=沼泽天使、can racket=酒罐混战、growler=打酒桶、excise law=酒类许可法、Elevated Railroad=高架铁路、Seventh Ward=第七选区 等 37 条 |
| 2026-10-09 | 10-the-cheap-lodging-houses.md（第八章 廉价寄宿所 The Cheap Lodging-Houses） | done | 13 对块；双脚本通过；新增术语 cheap lodging-house=廉价寄宿所、Murray Hill=默里山、Washington Square=华盛顿广场、Grand Street=格兰德街、Jersey City=泽西城、Johnstown=约翰斯敦、the Windsor=「温莎」、Secret Police=秘密警察、City Missionary=城市传教士、New York Fagin=「纽约费金」、political boss=政治大佬、barrel=「钱桶」、ballot reform=选票改革、David Smith=戴维·史密斯、Edward Mulhearn=爱德华·马尔赫恩 等 15 条 |
| 2026-10-09 | 11-chinatown.md（第九章 唐人街 Chinatown） | done | 13 对块；双脚本通过；新增术语 Chay Yen Chong=查延庄、Won Lung & Co.=永隆公司、club=堂口、trade dollar=贸易银元、In God we trust=我们信仰上帝、Eighth Avenue=第八大道、reformatory=教养院、fire-escape=防火梯 等 8 条 |
| 2026-10-09 | 12-jewtown.md（第十章 「犹太镇」 Jewtown） | done | 16 对块；双脚本通过；新增术语 Essex Street=艾塞克斯街、Eldridge Street=埃尔德里奇街、Allen Street=艾伦街、First Avenue=第一大道、Gouverneur Slip=格弗努尔滑道、Pig-market=「猪市」、the Bay=「海湾」、Eastern Dispensary=东区分诊所、Semites=闪米特人、synagogue=犹太会堂、Talmudic school=塔木德学校、boarder=搭伙客、firebug=纵火贼、fence=「赃贩」、pullers-in=「拉客郎」、kaftan=长摆长袍、huckster=小贩、pedlar=货郎、Isaac Iacob=艾萨克·雅各布、Rachel=拉结、Nemesis=涅墨西斯 等 21 条 |
| 2026-10-09 | 术语仲裁 | done | fire-escape 双轨裁定全书统一「太平梯」（06 章先定名 + 4:1 多数）：11 章译文 1 处机械替换、术语表删重复条「防火梯」，双脚本复验退出码 0。本行由调度方记 |
| 2026-10-09 | 14-the-bohemians-tenement-house-cigarmaking.md（第十二章 波希米亚人——廉租公寓里的雪茄制造 The Bohemians—Tenement-House Cigarmaking） | done | 11 对块；双脚本通过；新增术语 Bohemian quarter=波希米亚人聚居区、Fifth Street=第五街、East Tenth Street=东第十街、Thirty-eighth Street=第三十八街、Fifty-fourth Street=第五十四街、Seventy-first Street=第七十一街、Seventy-second Street=第七十二街、Seventy-third Street=第七十三街、Chickering Hall=奇克林音乐厅、Court of Appeals=上诉法院、Czech=捷克人、cigarmaker=雪茄匠、tenement factory=廉租公寓工场、key money=「钥匙钱」、filler/wrapper=烟芯/外包叶、consumption=肺痨、ash-barrel=炉灰桶、bed-tick=床袋布、Thirty Years' War=三十年战争、Freethinkers=自由思想者、hardtack=硬面饼 等 21 条；firebug 对齐先定名「纵火贼」 |
| 2026-10-09 | 13-the-sweaters-of-jewtown.md（第十一章 「犹太镇」的血汗工头 The Sweaters of Jewtown） | done | 17 对块；双脚本通过；新增术语 suspender-maker=吊裤带工、cloak=披风、trade school=职业学校、colonization=移民垦殖、stoop=「门阶」、factory inspector=工厂检查员、buttonhole-maker=锁扣眼工、Family Entrance=「家庭入口」、divide=「大家平分」 等 9 条 |
| 2026-10-09 | 15-the-color-line-in-new-york.md（第十三章 纽约的肤色界线 The Color Line in New York） | done | 11 对块；双脚本通过；新增术语 color line=肤色界线、Tenth Census=第十次人口普查、house agent=房屋中介、once a colored house=「一朝有色屋，永远有色屋」、hen-ladder=鸡梯、fixin's=「配料」、claw-hammer coat=燕尾服、stiletto=匕首、Real Estate Record=《房地产记录》、Sixteenth Street=第十六街、Nineteenth Street=第十九街、Thirty-second Street=第三十二街、Thirty-third Street=第三十三街、Ninety-ninth Street=第九十九街 等 15 条 |
| 2026-10-09 | 17-the-problem-of-the-children.md（第十五章 孩子们的问题 The Problem of the Children） | done | 13 对块；双脚本通过；新增术语 North River=北河、Central Park=中央公园、Tenth Avenue=第十大道、Canon Taylor=泰勒法政牧师、horsecar=有轨马车、Truant Home=逃学儿童收容所、home-heathen=本土异教徒、Sunday-school=主日学校、matron=女舍监、McGinty=《麦金蒂》、Keeb of te Grass=「别踩草皮」 等 11 条 |
| 2026-10-09 | 18-waifs-of-the-city-s-slums.md（第十六章 城市贫民窟的流浪儿 Waifs of the City's Slums） | done | 8 对块；双脚本通过；新增术语 Foundling Asylum=育婴堂、Sisters of Charity=慈善修女会、Randall's Island=兰德尔岛、Infants' Hospital=婴儿医院、Morgue=陈尸所、Sister Irene's Asylum=艾琳修女育婴堂、Sixty-eighth Street=第六十八街、Public Charities=公共慈善局、baby-farming=婴儿农场、paregoric=复方樟脑酊、inanition=营养不良、Elbridge T. Gerry=埃尔布里奇·T·格里、Five Points Mission=五点区布道会、Five Points House of Industry=五点区工艺院、Day Nurseries=日间托儿所、"pay babies"=「寄养婴儿」、nurse-mother=乳母 等 18 条 |
| 2026-10-09 | 16-the-common-herd.md（第十四章 众生芸芸 The Common Herd） | done | 19 对块；双脚本通过（金额锚点段 2.50/10 照搬数字）；新增术语 Hell's Kitchen=地狱厨房、Frog Hollow=「蛙洼」、Tompkins Square=汤普金斯广场、Battle Row=「厮杀排」、"the village"=「村子」、Rag Gang=「破布帮」、flat=公寓、hoodlum=小流氓、"summer doctors"=「夏季医生」、Bread and Blood riots=「面包与鲜血」暴乱、dispossess warrant=收房令状、"Poor Man's Court"=「穷人的法庭」、rounders=「老油子」、instalment plan=分期付款、undertaker=殡仪商、City Cemetery=市立公墓、Poor Burying Ground=穷人墓园、the Sound=海峡、Ninth Avenue=第九大道、Vanderbilt=范德比尔特 等 26 条 |
| 2026-10-09 | 20-the-reign-of-rum.md（第十八章 朗姆酒当道 The Reign of Rum） | done | 6 对块；双脚本通过（统计数字 111/4,065/32,390/13,220/7,884/485 等照搬）；新增术语 Excise Board=酒类许可委员会、dramshop=零沽酒肆、precinct=警区、"Tub of Blood"=「血桶」、"Witches’ Broth"=「女巫汤」、"Plug Hat"=「大礼帽」、"Boodle Board"=「贿金委员会」、dancing-hell=跳舞地狱、"morgues"=「陈尸所」、pawnshop=当铺 等 10 条 |
| 2026-10-09 | 19-the-street-arab.md（第十七章 街头流浪儿 The Street Arab） | done | 16 对块；双脚本通过（金额 172,776.38/1,337.21 美元、统计 12,153/4,105/11,331/1,132/416/1,745 照搬；尾注 19 按两位数全角括号规则标作（19）；U+FEFF x7、U+00A0 x2 逐字保留）；新增术语 Newspaper Row=报馆街、Park Row=公园路、Printing House Square=印刷所广场、Duane Street=杜安街、Leonard Street=伦纳德街、Thirty-fifth Street=第三十五街、Forty-fourth Street=第四十四街、Sixty-seventh Street=第六十七街、Harlem Bridge=哈莱姆桥、Michigan=密歇根、Newsboys' Lodging House=报童寄宿所、New York Trade Schools=纽约工艺学校、Mrs. Astor=阿斯特夫人、Colonel Auchmuty=奥克穆蒂上校、Sing Sing=新新监狱、industrial school=工业学校、Insider=「内宿的」、upper ten=「上流十子」 等 18 条 |
| 2026-10-09 | 21-the-harvest-of-tares.md | done | 摘要：双脚本过检回收（代理死于 [1308] 收尾阶段，译文 50.4KB 完整落盘，调度方复核退出码均 0 后回填 done 并补记本行） |
| 2026-10-11 | 23-pauperism-in-the-tenements.md（第二十一章 廉租公寓里的贫困化 Pauperism in the Tenements） | done | 12 对块；双脚本通过（统计数字 135,595/31,000/5,169/2,594/1,474/612/2,633/947、金额 250/8,000,000 美元照搬，百分比按全书惯例作「百分之+数字」；U+FEFF x6、U+00A0 x1、斜体 *pauper* 逐字保留）；新增术语 Charity Organization Society=慈善组织协会（本章全书首现）、Almshouse=济贫院、the scrub=「擦洗婆」、Jewish Sabbath=犹太安息日、padrone system=「帕德罗内」制度、King’s Daughters’ Tenement-house Committee=「国王之女会」廉租公寓委员会、"friendly visitation"=「友好探访」、labor bureau=劳工介绍所、"gentleman tramp"=「绅士流浪汉」、Methodist=卫理公会教徒、"tribe of Ishmael"=「以实玛利部落」、Boston=波士顿、Philadelphia=费城、Hartford=哈特福德、Genoa=热那亚、Madison Avenue=麦迪逊大道、Masonis=马索尼一家、Celt=凯尔特人 等 18 条 |
| 2026-10-11 | 22-the-working-girls-of-new-york.md（第二十章 纽约的打工女孩 The Working Girls of New York） | done | 12 对块；双脚本通过（金额 $2/$4.50/$167/$125/$3,000/$1.75/$1.50、统计 150,000/25/75/11 照搬锚点；U+FEFF x7、hair space U+200A x2、斜体 *guessed*、弯引号逐字保留；诗行引文块按源文结构镜像）；新增术语 Working Women’s Society=劳动妇女协会、"Song of the Shirt"=《衬衫之歌》、State Board of Arbitration=州仲裁委员会、State Labor Bureau=州劳工局、Women’s Investigating Committee=妇女调查委员会、City Mission Society’s Monthly=《城市布道会月刊》、Girls’ Home=女子之家、saleswoman=女售货员、shirtmaker=衬衫女工、sewing-girl=缝纫女、calico wrappers=印花布晨衣、pin-money=零花钱、poorhouse=济贫院、starvation wages=饥饿工资、"paths of shame"=羞耻之路、Maine=缅因州 等 16 条 |
| 2026-10-11 | 24-the-wrecks-and-the-waste.md（第二十二章 沉沦者与虚耗 The Wrecks and the Waste） | done | 13 对块；双脚本通过（统计 22,477/1,419/4,913/3,694/13,813/14,000/138,332/38,600/9,765/553/48,918 与金额 $2,343,372/$4,409,550.94/$403,190/$7,156,112.94 照搬；尾注 22/23 按两位数全角括号规则标作（22）（23）；U+FEFF x9、U+200A x1 逐字保留，院长咒骂的破折号省略式照搬；术语对齐：Poverty Gap=「贫困谷」承第二十一章）；新增术语 almshouse=救济院（与 workhouse=济贫院分译，第二十三章两处已同步改齐）、Pauperdom=贫民界、the Nether Half=「下一半人」、Hart's Island=哈特岛、Ward's Island=沃德岛、Blackwell's Island Asylum=布莱克韦尔岛疯人院、Bellevue Hospital=贝尔维尤医院、Department of Charities and Correction=慈善与惩戒局、hell-box=「废铅字箱」、growler-gang=「打酒帮」、workhouse step=「济贫院步」、chain-gang=「锁链队」、Dr. Louis L. Seaman=路易斯·L·西曼医生 等 16 条 |
| 2026-10-11 | 25-the-man-with-the-knife.md（第二十三章 持刀者 The Man with the Knife） | done | 10 对块；双脚本通过（尾注 24 按两位数全角括号规则标作（24）；U+FEFF x6 逐字保留于 Original 块；斜体 *look bad* 译作 *看上去*；「大众对抗阶级」等引语照录）；新增术语 the man with the knife=持刀者、“dangerous classes”=「危险阶级」、Murderers’ Row=「凶杀排」、“the masses against the classes”=「大众对抗阶级」、brownstone front=褐石门面、madhouse=疯人院 等 6 条 |
| 2026-10-11 | 28-statistics-bearing-on-the-tenement-problem.md（统计附录 廉租公寓问题相关统计 Statistics Bearing on the Tenement Problem） | done | 9 对块（逐行镜像附录版式：3 段统计说明 + Police Statistics/Immigration/Tenements 三个表格标题行 + 3 条建筑条例）；双脚本通过（统计 25.19/26.76/1,575,073/1,482,273/79,358/28/1,111,082/1889/114.04/1,000/60/80/4/10/70/80 与拼写数词 seventy-eight/twelve 照搬，拼写数词作「百分之七十八/百分之十二」；U+2019 x2 逐字保留）；新增术语 sick-list=病员名单、corner tenement=街角廉租公寓、open court=露天庭院、rear yard=后院、apartment house=公寓楼 等 5 条 |
| 2026-10-11 | 26-what-has-been-done.md（第二十四章 已经做了什么 What Has Been Done） | done | 15 对块；双脚本通过（统计 14,872/468,492/21,000/32,390/1,093,701/37,316/2,630/1,250,000/1,068 照搬，城市人口比例作二十五分之一/四点五分之一/四分之一；U+FEFF x12、弯引号逐字保留，Original 块以脚本自源文逐字抽取）；新增术语 St. Antoine=圣安托万、Napoleon III=拿破仑三世、absentee landlord=在外房东、“Big Flat”=「大公寓」、“skin” tenements=「皮壳」廉租公寓、College Settlement=「大学睦邻社」、Neighborhood Guilds=邻里公会、stationary tubs=固定洗衣盆、wood-closets=柴房、housekeeper=管家/女管家、slough of despond=绝望泥沼、Murderers’ Alley=「凶手巷」（承第二十一章首译）、sanitary inspector=卫生检查员、junk shop=废品铺 等 14 条 |
| 2026-10-11 | 29-endnotes.md（尾注 Endnotes） | done | 27 对块（每条尾注一个对块，编号与尾注回链符 ↩︎ 照搬，体例同 Deledda 尾注样本）；双脚本通过（统计 69,111/42,028/两百栋、尺寸 10 × 12、6½ × 7、50 × 60 与金额 15/600/五美元照搬，百分比按全书惯例作「百分之+数字」；U+FEFF x3、U+00A0 x1、弯引号与斜体 *North American Review* 逐字保留于 Original 块；术语对齐：卫生理事会=承第二章、「废铅字箱」承第二十二章、《一个大城市的社会虚耗》承西曼医生条目、「国王之女会」承第二十一章、休斯敦街=承第二章）；新增术语 Sheriff Street=谢里夫街、multiple domicile=「多户合居」、coal-heaver=卸煤工、North American Review=《北美评论》、City Mission Report=《城市布道会报告》、American Prisons in the Tenth Census=《第十次人口普查中的美国监狱》、AAAS=美国科学促进会、King's Daughters' Tenement-house Relief Committee=「国王之女会」廉租公寓救济委员会 等 8 条 |
| 2026-10-11 | 30-list-of-illustrations.md（图版目录 List of Illustrations） | done | 43 对块（每条图题一行、Original 与源文逐字镜像的列表版式）；双脚本通过（U+FEFF x5 于 Original 块逐字保留并镜像于译文、弯引号弯撇号逐字保留、无页码数字；术语对齐：1863 图题承第三章原句、joint=馆子承第十一章、knee-pants/包工头作坊承第十三章、black-and-tan dive=黑白混杂酒窟与 downtown “morgue”=「陈尸所」承第二十章、growler gang=「打酒帮」承第二十二章、coal-heaver=卸煤工承尾注 17、盲人巷承第六章、两分钱饭馆/贫困谷/五点区工艺院/报童寄宿所等照术语表）；新增术语 Sebastopol=塞瓦斯托波尔、Jersey Street=泽西街、Riverside Buildings=「河畔楼」、A. T. White=A. T. 怀特、Charles F. Wingate=查尔斯·F·温盖特 等 5 条 |
| 2026-10-11 | 27-how-the-case-stands.md（第二十五章 现状如何 How the Case Stands） | done | 19 对块（八条「赤裸裸的事实」与三条「有效途径」两份排比清单各随引导段成块，--- 分节线独立成行，卷末诗人对句对块镜像源文行版式含衬行）；双脚本通过（$240,000/$285,000/$14/$6.25/218 户/1890 年号/25 × 100 英尺照搬，百分比作百分之六点七五/百分之五点五/百分之五六/百分之三四；U+FEFF x11、U+00A0 x5、弯引号弯撇号逐字保留于 Original 块，以脚本自源文逐字抽取）；新增术语 Ellen Collins=埃伦·柯林斯小姐、W. Bayard Cutting=W. 贝亚德·卡廷先生、Edwin R. A. Seligman=埃德温·R. A. 塞利格曼教授、A. T. White=A. T. 怀特先生、Sir Sydney Waterlow=悉尼·沃特洛爵士、Improved Dwellings Association=改良住宅协会、Tenement-house Building Company=廉租公寓建筑公司、East Seventy-second Street=东第七十二街、red tape=官样红线、governments=「公债」、doubting Thomas=多疑的多马、ash-chute=倒灰槽、ash-flue=倒灰井道、scullery=洗涤间、coal lift=运煤升降机、“institution character”=「机构色彩」、fair play=公平对待、beau ideal=完美典范 等 18 条 |
| 2026-10-11 | 全书完译 | done | 《另一半人怎样生活》31/31 全部过检完书：序言 + 卷首诗 + 导言 + 24 个正文章节（原书罗马数字 I-XXV）+ 统计附录 + 27 条尾注 + 43 条图版目录；历经 [1308] 额度中断多次（07/21 零补记回收、22 瞬死重派、06/08 重派）与 [1301] 内容审查误伤（另一项目），断点全部无损或最小损失恢复；术语表累计 400+ 条定名（纽约下东区地名/机构/族群/社会术语），fire-escape 与 almshouse/workhouse 两例跨章术语冲突均按先定名+语义辨析仲裁统一；本行由调度方记 |
