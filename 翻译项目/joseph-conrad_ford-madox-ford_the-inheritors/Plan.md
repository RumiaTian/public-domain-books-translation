# Plan（《继承人》翻译计划）

> 从 `prompts/翻译计划模板.md` 复制建立。执行步骤、CSV 格式等通用规范见模板，此处为本书实例。

---

## 本计划信息

- **项目名称**：joseph-conrad_ford-madox-ford_the-inheritors（《继承人》，康拉德、福特合著）
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

> 执行步骤（读配置→取任务→读源文→翻译→自检→自动检查→回填状态→追加日志→循环）见 `prompts/翻译计划模板.md`「执行步骤」，本文件不重复；完成状态须双写（项目 CSV + 根表）。

---

## 篇目清单

| # | 篇名 | 源文 | 大小 | 状态 |
|---|------|------|------|------|
| 0 | 献词 | 01-dedication.md | 0.0KB | done |
| 0 | 题词 | 02-epigraph.md | 0.1KB | done |
| 1 | 第 I 章 | 03-i.md | 20.7KB | done |
| 2 | 第 II 章 | 04-ii.md | 12.2KB | done |
| 3 | 第 III 章 | 05-iii.md | 17.0KB | done |
| 4 | 第 IV 章 | 06-iv.md | 18.8KB | done |
| 5 | 第 V 章 | 07-v.md | 13.1KB | done |
| 6 | 第 VI 章 | 08-vi.md | 23.0KB | done |
| 7 | 第 VII 章 | 09-vii.md | 11.6KB | done |
| 8 | 第 VIII 章 | 10-viii.md | 17.9KB | done |
| 9 | 第 IX 章 | 11-ix.md | 13.9KB | done |
| 10 | 第 X 章 | 12-x.md | 22.4KB | done |
| 11 | 第 XI 章 | 13-xi.md | 19.0KB | done |
| 12 | 第 XII 章 | 14-xii.md | 15.1KB | done |
| 13 | 第 XIII 章 | 15-xiii.md | 20.6KB | done |
| 14 | 第 XIV 章 | 16-xiv.md | 22.5KB | done |
| 15 | 第 XV 章 | 17-xv.md | 26.1KB | done |
| 16 | 第 XVI 章 | 18-xvi.md | 15.4KB | done |
| 17 | 第 XVII 章 | 19-xvii.md | 21.5KB | done |
| 18 | 第 XVIII 章 | 20-xviii.md | 23.6KB | done |
| 19 | 第 XIX 章 | 21-xix.md | 10.3KB | done |

共 21 篇（献词 + 题词 + 19 章），源文合计约 345KB。全书单一叙事弧但章数多、章均 18KB，走委派模式；各章无标题，仅罗马数字编号。

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-09-08 | 全书 21/21（01-dedication ~ 21-xix） | done | 《继承人》整本完结。批次1主代理滚动验收：20/21 文件 rc=0；18-xvi rc=1 仅两处数字锚点假阳性（’78→一八七八年、Number 44→四十四号，已复核无错配）。术语表由主代理合并回填 160+ 条。终章四段连续引语镜像原文未闭引号惯例；承受大地点题语、ch1 丘陵初遇回闪闭环。 |
| 2026-09-08 | 04-ii.md | done | 新定名词：斯特林（Stelling）、凯特·温菲尔德（Kate Wingfield）、《博尔德罗》（Boldero）、《布兰菲尔德》（Blanfield）、赫克托·斯蒂尔（Hector Steele）、金克斯（Jinks）、沃特诺特（Whatnot，教区长绰号）、威尔金森（Wilkinson）、《肯辛顿》（the Kensington，杂志）、连载（feuilleton）、坎特伯雷（Canterbury）、柯达（Kodak） |
| 2026-09-08 | 01-dedication.md | done | 献词对象按术语表：鲍里斯；克里斯蒂娜 |
| 2026-09-08 | 02-epigraph.md | done | 新定名词：萨达纳帕勒斯（Sardanapalus） |
| 2026-09-08 | 03-i.md | done | 新定名词：多佛（Dover）、真福托马斯（Blessed Thomas）、切尔克斯人（Circassian）、约翰逊博士（Dr. Johnson）、伦敦佬诗派（cockney school of poetry）、乔克托人（Choctaw）、《浮士德博士》（Faustus）、贝尔哈里（Bell Harry，大教堂钟塔）、哈德夫斯（Hardves）、斯特林明尼斯（Stelling Minnis）；术语表既定词：第四维、第四维人、承受大地、卡伦 |
| 2026-09-08 | 05-iii.md | done | 新定名词：阿瑟（Arthur，叙述者名字首现）、查尔斯·格纳德（Charles Gurnard）、「旧道德买卖」（the Old Morality business）、鲸油（train-oil）、建国者（State Founder） |
| 2026-09-08 | 07-v.md | done | 新定名词：利（Lea，首现于译文）、波尔汉普顿（Polehampton，首现于译文）、豪登（Howden）、苏塞克斯（Sussex）、布卢姆斯伯里（Bloomsbury）、南安普敦街（Southampton Row） |
| 2026-09-08 | 06-iv.md | done | 新定名词：白金汉剧院（the Buckingham）、哈特利太太（Mrs. Hartly）、罗克福尔奶酪（Roquefort）、路易十五式（Louis Quinze）、华托（Watteau）、帕拉格拉夫俱乐部（the Paragraph Club）、斯特兰德（the Strand）、范妮·埃尔斯勒（Fanny Ellsler）、坎宁安（Cunningham）、阿德尔菲（the Adelphi）、美少年（beau jeune homme，法语短语夹注）、《杰克盖的房子》（the house that Jack built，童谣典故）；术语表既定词首现：埃文斯（Evans）、格兰特商号（Grant's）、中央新闻社（Central News）、外交大臣丘吉尔、条顿 |
| 2026-09-08 | 09-vii.md | done | 新定名词：《克伦威尔传》（Life of Cromwell）、克伦威尔（Cromwell）、奥利弗勋爵（the Lord Oliver）、老内尔（Old Noll，克伦威尔绰号）、严父角色（heavy father，戏剧行当）、《乡村墨丘利》（Mercurius Rusticus，十七世纪小册子）、假姐妹（pseudo-sister，呼应 ch6「She does me a great deal of good」）、提坦（titan）、皇家院士（Academician）、红桃K（the King of Hearts）、布鲁梅尔（Brummell）、史密森（Smithson，出版商）、法尔内塞的赫拉克勒斯（Farnese Hercules）、捉刀（ghost）、格陵兰体系（Greenland System） |
| 2026-09-08 | 08-vi.md | done | 新定名词：丘吉尔小姐（Miss Churchill，外交大臣之姑母）、格兰杰太太（Mrs. Granger，指老姑母）、埃钦厄姆（Etchingham，地名单独首现）、庄园宅第／埃钦厄姆庄园（the Manor house / Etchingham Manor）、斯图亚特王朝（the Stuarts）、正统派王位觊觎者（Legitimist pretenders）、『正统』（Legitimate，双关）、城堡主楼（donjon-keep）、堂妹（cousin）；术语表既定词首现：家庭女教师竞选传闻（Who starved her governess?）、持瓶人（bottle-handler） |
| 2026-09-08 | 11-ix.md | done | 新定名词：《双月刊》（the Bi-Monthly，ch15 复现）、『方方面面』（Aspects，短系列名）、选任大公（the Elective Grand Duke）、霍尔斯坦-劳内维茨（Holstein-Launewitz）、北极地区复兴会／S.R.A.R.（the Society for the Regeneration of the Arctic Regions）、阿斯顿（Aston，首任总督）、福克斯通（Folkestone）、圣但尼（St. Denis）、大饭店（the Grand）、拉丁区（the Quartier Latin）、出租马车（fiacre）、巴黎圣母院（Notre Dame）、伦勃朗（Rembrandt）、波先生（Mr. P.）、横贯格陵兰铁路（the Trans-Greenland railway，承接 ch3 译法）、格陵兰体系法语形（Système Groënlandais） |
| 2026-09-08 | 10-viii.md | done | 新定名词：阿瑟·爱德华兹（Arthur Edwards，小说家）、《哥达年鉴》（Almanac de Gotha）、格里姆斯比（Grimsby）、威廉·格纳德（William Gurnard）、横贯格陵兰铁路（Trans-Greenland Railway）、环球电报公司（All Round the World Cable Company）、泛欧铁路、探险与文明公司（Pan-European Railway, Exploration, and Civilisation Company）、国际贫民住房公司（International Housing of the Poor Company）、极北保护领（Hyperborean Protectorate）、失败事业沙龙（Salon des Causes Perdues）、圣日耳曼区（Faubourg Saint Germain）、白玫瑰同盟（White Rose League）、卡洛斯派（Carlists）、奥尔良派（Orleanists）、教皇黑党（Papal Blacks）、米迪峰（Dent du Midi）、佃户舞会（Tenants' Ball）、护国公（the Protector）、爱德华（Edward，丘吉尔之名）；术语表既定词首现：埃钦厄姆·格兰杰太太（Mrs. Etchingham Granger，老姑母称谓） |
| 2026-09-08 | 12-x.md | done | 新定名词：意大利人剧院街区（the Italiens）、新宫（the New Palace）、后台腔（coulisse，法语词夹注）、勒·格兰若／格兰若·埃辛冈（Le Grangeur / Grangeur Eschingan，女演员对「我」名字的法语误读）、猪猡（Peeg, peeg）、梭伦（Solon）、埃涅阿斯（Aeneas）、善意的人们（hominibus bonae voluntatis，拉丁语夹注）、打倒科涅（A bas Coignet）、歌剧院大道（Avenue de l'Opéra）、老红胡子（old Red-Beard，德·默施绰号）、布雷盖（Breguet's，餐馆）、德苏尔当（de Sourdam，奥地利使馆）、普吕伊维斯（Pluyvis）、德雷福斯案（the Affaire）、交趾支那（Cochin）、白衣神父（the Whites）、《红色评论》（Revue Rouge）、拉代（Radet，首现于译文）、圣女贞德（Joan of Arc）、里沃利街（Rue de Rivoli）、黎凡特人（Levantine）、《阿依达》（Aïda）、英国女人（Anglaise）、二位先生（Messieurs）；既定词沿用：圣日耳曼区（the F. St. Germain，承接 ch8 Faubourg Saint Germain） |
| 2026-09-08 | 13-xi.md | done | 新定名词：德·吕伊纳公爵（Duc de Luynes）、马尔索大街（Avenue Marceau）、苦难会神父（Passionist）、「格兰热沙龙」（Salon Grangeur）、郡望世家（county family）／非郡望人家（non-county persons）、寄膳宿房客（paying guest）、贼船（galère，法语夹注）、好血统（Bon sang ne，法语夹注）、我才不那么傻（pas si bête，法语夹注）、所谓（soi distant）、公寓（appartement，法语夹注）、霍尔斯坦人（the Holsteiner，承接 ch9 霍尔斯坦-劳内维茨）、埃辛冈-格兰若-r-r（Eschingan-Grangeur-r-r，承接 ch12-x 演员姐儿误读译法）；既定词沿用：《红色评论》、拉代、英国女人（Anglaise）、小个子记者（承接 ch12-x） |
| 2026-09-08 | 14-xii.md | done | 新定名词：吕伊纳公馆（Hôtel de Luynes，承接 ch13-xi 德·吕伊纳公爵译名）／格兰杰公馆（or Granger）、邮差（facteur，法语夹注）、那么就这么说定了（Alors, c'est entendu）、说定了（C'est entendu）、可是（mais）、好一个厉害的女人（Quelle femme!）、俊眼（beaux yeux，法语夹注）；既定词沿用：那套体系的监察人（Supervisor of the Système）、圣日耳曼区、正统派（Legitimists）、大革命（the Revolution）、承受大地 |
| 2026-09-08 | 15-xiii.md | done | 新定名词：汉普顿宫（Hampton Court）、塞维涅夫人（Madame de Sévigné）、镜厅（Salle des Glaces，法语夹注）、大学街（Rue de l'Université）、布洛涅林园（the Bois）、双座轿式马车（coupé，法语夹注）、「无忧宫」（Sans Souci，德·默施宅邸）、皮平苹果（pippin）、浪荡子（flaneurs）、陪护人（chaperon，法语夹注）、阿尔萨斯人（Alsatian）、哈尔德施罗特男爵（Baron de Halderschrodt）、格兰杰小姐（Miss Granger，那位姑娘的冒称称呼）、巴黎出版的美国《公报》（Paris-American Gazette）、「您的姐妹小姐」（mademoiselle votre soeur，法语夹注）、非国教（Dissent）；法语随文夹注：门房（portière）、上流社会（monde）、一家人似的随意（en famille）、晨衣（peignoir）、恰到好处的字眼（mot juste）、铺石路面（pavé）、那边（là bas）；金融行文：期票／贴现（bills / discount）；既定词沿用：摄取气氛（承接 ch2）、假姐妹（pseudo-sister）、圣日耳曼区、选任大公国、霍尔斯坦-劳内维茨 |
| 2026-09-08 | 16-xiv.md | done | 新定名词：黑色星期一（Black Monday）、詹姆斯爵士（Sir James）、梅雷迪思（Meredith，老姑母的律师）、德·萨布朗先生（Monsieur de Sabran）、现场勘验（constatation，法语夹注）、微醺（gris，法语夹注）、我的上帝（Mon Dieu，法语夹注）、Habet（拉丁语保留，括注「他完了」）、普鲁士近卫军（Prussian Guard）、鹅步（goose step）、狄安娜（Diana）、冬园（winter-garden）、棕榈温室（palm-house）、酒神狂女般的（maenadic）、联盟商行（allied firms）、那家美国报纸（the American paper）；既定词沿用：哈尔德施罗特男爵（承接 ch15-xiii）、格兰杰小姐（Miss Granger，那位姑娘冒称，承接 ch13-xi/ch15-xiii）、拧螺丝（put the screw，承接 ch15-xiii）、「姐妹」叙述加引号（承接 ch15-xiii）、出租马车（fiacre，承接 ch9） |
| 2026-09-08 | 17-xv.md | done | 新定名词：塔尔先生（Mr. Tull）、威洛比（Willoughby，埃菲的未婚夫）、埃菲（Effie，贵妇之女）、奥平顿鸡（Orpingtons，鸡种）、大彩帐（marquee）、家禽展／公鸡母鸡展（poultry show / cock-and-hen show）、地产管家（land steward）、义勇骑兵乐队（yeomanry band）、踏阶（stile）、犬蔷薇（dog-roses）、济贫院（workhouse）、教区救济（on the rates）、野猫骗局（wildcat schemes）、铁打的忠心（true blue）、保王党阴谋（Royalist plot）、「旧秩序正在更迭」（The old order changeth，丁尼生诗句）、往昔（temps jadis，法语夹注）；既定词沿用：《克伦威尔传》（承接 ch7）、人总得做这些事（承接 ch6）、《时辰报》、丘吉尔的小屋、斯林斯比、丘吉尔小姐、埃钦厄姆（承接 ch6） |
| 2026-09-08 | 18-xvi.md | done | 新定名词：英印人（Anglo-Indian）、布朗普顿斯先生（Mr. Bromptons）、肯沃兹太太（Mrs. Kenwards）、肯尼·格兰杰（Kenny Granger，叔叔、一族之长、姑母的丈夫）、博物馆（the Museum）、布鲁厄姆马车（brougham）、牛津街（Oxford Street）、贝德福德街（Bedford Row）、奇斯威克（Chiswick）、威廉斯（Williams）、沃林（Waring）、约翰逊（Johnson，四十四号）、设得兰披巾（Shetland shawl）、下策（pis aller，法语夹注）、华托房间（the Watteau room，承接 ch4 华托）、老庄稼汉（country hawbuck，福克斯口吻）；既定词沿用：报纸付印（put the paper to bed）、《时辰报》、《克伦威尔传》（承接 ch7）、坐骨神经痛（呼应索恩旧疾）、「姐妹」叙述加引号对白不加（承接 ch14/ch15 先例）、利（Lea）、索恩（Soane） |
| 2026-09-08 | 19-xvii.md | done | 新定名词：特派专员（the Special Commissioner，承接 ch12「特派员」）、杰克逊（Jackson，印刷工头）、桑威奇群岛（Sandwich Islands）、极乐群岛（the Islands of the Blest）、海滩拾荒客（beachcomber）、怀卡托号（S.S. Waikato）、德干（Deccan，刀）、说的是什么来着（Il s’agissait de……？法语夹注）、闹翻天（hats on the green）、掀翻苹果车（upset the apple cart）、该——死的（D——n 删节拼写镜像）；既定词沿用：家禽展（承接 ch15）、那正派（probity，承接 ch12）、一场病——对于我（承接 ch14）、部属（lieutenant，承接 ch12）、格陵兰体系（Système Groënlandais，承接 ch9）、C’est entendu（承接 ch12 不再括注）、承受大地、模范国家（承接 ch3）、索恩社论、报纸付印 |
| 2026-09-08 | 20-xviii.md | done | 新定名词：大英博物馆（British Museum）、格罗格拉姆（Grogram，下院领袖，Sir C. Grogram＝C·格罗格拉姆爵士）、德文波特（Devonport，选区）、下院领袖（Leader of the House）、纸带机（tape machine，俱乐部收报机）、报应之神涅墨西斯（Nemesis）、萨提尔（satyr，羊怪面具）、冥府般的幽暗（Cimmerian，意译）、方格镶嵌的石板地（tessellated pavement，意译）、那个被收买的人（the man who was got at）；既定词沿用：《克伦威尔传》（承接 ch7/ch16 博物馆摘录线）、双轮马车（hansom，承接 ch4）、布鲁厄姆马车（承接 ch16）、吸烟室、第四维人、德·默施的债券（debentures）、利（Lea）、假面「妹妹」（Sister is going to marry Gurnard，对白不加点破） |
| 2026-09-08 | 21-xix.md | done | 新定名词：米洛的维纳斯（Venus of Milo）、尼尼微（Nineveh）；新定短语：报丧钟（passing bell）、必然之势（the Inevitable）、瓦解机器（mighty engine of disintegration）、埃钦厄姆的格兰杰（the Granger of Etchingham）、『人在下面是会变瞎的』（One goes blind down here，福克斯引语，呼应 ch18『人就变得相当盲目了』）；既定词沿用：承受大地、正派（probity，承接 ch12）、旧秩序（承接 ch15 丁尼生典故）、曲折的阴谋（承接 ch12）、妹夫（承接 ch18 假妹妹嫁格纳德）、浩浩长天／云雀颤鸣（呼应 ch1 丘陵场景）；多段长引语镜像原标点（段首开引号不闭合） |
