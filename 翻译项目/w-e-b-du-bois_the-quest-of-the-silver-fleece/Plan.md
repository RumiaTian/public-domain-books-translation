# Plan.md — w-e-b-du-bois_the-quest-of-the-silver-fleece

## 本计划信息

- **项目名称**：w-e-b-du-bois_the-quest-of-the-silver-fleece（《银色羊毛的追寻》）
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
| `原文/*.md` | 源文（题词 + 作者序 + 38 章 = 40 文件） | 不改 |
| `译文/*.zh-CN.md` | 译文产出（块对照双语） | 翻译 agent 产出 |

---

## 篇目清单

| # | 章名 | 源文 | 大小 | 状态 |
|---|------|------|------|------|
| - | Dedication（题词） | dedication.md | 0.2KB | todo |
| - | Note（作者序） | note.md | 0.7KB | todo |
| 1 | I Dreams | dreams.md | 11.2KB | todo |
| 2 | II The School | the-school.md | 6.5KB | todo |
| 3 | III Miss Mary Taylor | miss-mary-taylor.md | 10.3KB | todo |
| 4 | IV Town | town.md | 16.4KB | todo |
| 5 | V Zora | zora.md | 14.5KB | todo |
| 6 | VI Cotton | cotton.md | 18.5KB | todo |
| 7 | VII The Place of Dreams | the-place-of-dreams.md | 21.2KB | todo |
| 8 | VIII Mr. Harry Cresswell | mr-harry-cresswell.md | 13.9KB | todo |
| 9 | IX The Planting | the-planting.md | 16.2KB | todo |
| 10 | X Mr. Taylor Calls | mr-taylor-calls.md | 26.6KB | todo |
| 11 | XI The Flowering of the Fleece | the-flowering-of-the-fleece.md | 15.8KB | todo |
| 12 | XII The Promise | the-promise.md | 24.2KB | todo |
| 13 | XIII Mrs. Grey Gives a Dinner | mrs-grey-gives-a-dinner.md | 8.7KB | todo |
| 14 | XIV Love | love.md | 9.4KB | todo |
| 15 | XV Revelation | revelation.md | 21.2KB | todo |
| 16 | XVI The Great Refusal | the-great-refusal.md | 14.2KB | todo |
| 17 | XVII The Rape of the Fleece | the-rape-of-the-fleece.md | 12.9KB | todo |
| 18 | XVIII The Cotton Corner | the-cotton-corner.md | 15.3KB | todo |
| 19 | XIX The Dying of Elspeth | the-dying-of-elspeth.md | 18.6KB | todo |
| 20 | XX The Weaving of the Silver Fleece | the-weaving-of-the-silver-fleece.md | 14.6KB | todo |
| 21 | XXI The Marriage Morning | the-marriage-morning.md | 13.2KB | todo |
| 22 | XXII Miss Caroline Wynn | miss-caroline-wynn.md | 18.2KB | todo |
| 23 | XXIII The Training of Zora | the-training-of-zora.md | 12.9KB | todo |
| 24 | XXIV The Education of Alwyn | the-education-of-alwyn.md | 19.5KB | todo |
| 25 | XXV The Campaign | the-campaign.md | 23.3KB | todo |
| 26 | XXVI Congressman Cresswell | congressman-cresswell.md | 16.9KB | todo |
| 27 | XXVII The Vision of Zora | the-vision-of-zora.md | 15.0KB | todo |
| 28 | XXVIII The Annunciation | the-annunciation.md | 13.5KB | todo |
| 29 | XXIX A Master of Fate | a-master-of-fate.md | 19.7KB | todo |
| 30 | XXX The Return of Zora | the-return-of-zora.md | 16.0KB | todo |
| 31 | XXXI A Parting of Ways | a-parting-of-ways.md | 27.3KB | todo |
| 32 | XXXII Zora's Way | zora-s-way.md | 12.2KB | todo |
| 33 | XXXIII The Buying of the Swamp | the-buying-of-the-swamp.md | 20.4KB | todo |
| 34 | XXXIV The Return of Alwyn | the-return-of-alwyn.md | 20.2KB | todo |
| 35 | XXXV The Cotton Mill | the-cotton-mill.md | 19.2KB | todo |
| 36 | XXXVI The Land | the-land.md | 22.9KB | todo |
| 37 | XXXVII The Mob | the-mob.md | 11.8KB | todo |
| 38 | XXXVIII Atonement | atonement.md | 12.6KB | todo |

> 全部单章 <50KB，无需分段。全书约 626KB。

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-08-03 | 建项目 | — | 题词+作者序+38 章提取完成，领域=小说文学，术语表含种族用语处理策略 |
| 2026-08-03 | Dedication（题词） | 通过 | 1对块，献词，诗意处理 |
| 2026-08-03 | Note（作者序） | 通过 | 1对块，结构满足；1处日期数字锚点误报（1911→汉字） |
| 2026-08-03 | I Dreams | 通过 | 11对块，check_bilingual 退出码0；诗化开篇，布莱斯与佐拉初遇；佐拉方言译为质朴乡野中文 |
| 2026-08-03 | II The School | 通过 | 8对块，退出码0；史密斯小姐与范德普尔太太对话；首处种族蔑称「小猴子」加译注 |
| 2026-08-03 | III Miss Mary Taylor | 通过 | 13对块，退出码0；玛丽·泰勒初识棉花之美；原文有1处重复段落已合并去重 |
| 2026-08-03 | IV Town | 通过 | 20对块，退出码0；镇上众生相；考德威尔蔑称「黑鬼」加注；佐拉首次登场对峙泰勒 |
| 2026-08-03 | V Zora | 通过 | 19对块，退出码0；佐拉成长、学认字、与布莱斯定下银羊毛之约；红裙子登场 |
| 2026-08-03 | VI Cotton | 通过 | 20对块，退出码0；视角转北方资本（泰利/伊斯特利/格雷太太）；金融托拉斯阴谋；darkies/niggers蔑称加注 |
| 2026-08-03 | VII The Place of Dreams | 通过 | 26对块，退出码0；泰勒小姐对Bles的暗示、佐拉偷别针事件；梦居之地（沼泽秘岛）被发现 |
| 2026-08-03 | VIII Mr. Harry Cresswell | 通过 | 16对块，退出码0；克雷斯韦尔父子种族主义对话；哈里施压学校、与Bles路上对峙 |
| 2026-08-03 | IX The Planting | 通过 | 20对块，退出码0；佐拉偷骡开垦梦之田；圣母像与纯洁之诺；埃尔斯贝思午夜播种巫术仪式 |
| 2026-08-03 | X Mr. Taylor Calls | 通过 | 30对块，退出码0；约翰·泰勒南下与克雷斯韦尔家结盟；金融托拉斯全貌；泰勒被海伦吸引 |
| 2026-08-03 | XI The Flowering of the Fleece | 通过 | 16对块，退出码0；佐拉蜕变、白裙登场；银羊毛开花；史密斯小姐收到不祥的信 |
| 2026-08-03 | XII The Promise | 通过 | 32对块，结构满足；1处金额数字误报（50万/75万→汉字）；格雷捐助、黑人来求助、史密斯落入抵押陷阱 |
| 2026-08-03 | XIII Mrs. Grey Gives a Dinner | 通过 | 10对块，退出码0；查尔斯·史密斯出卖原则；晚宴上南北合流、黑人教育虚伪辩论 |
| 2026-08-03 | XIV Love | 通过 | 8对块，退出码0；暴雨救羊毛之谜（佐拉挖渠）；佐拉病危康复；两人相爱，全书情感高潮 |
| 2026-08-03 | XV Revelation | 通过 | 25对块，退出码0；考察团撞见恋人、克雷斯韦尔污蔑；布莱斯质问佐拉、两人决裂（全书悲剧转折） |
| 2026-08-03 | XVI The Great Refusal | 通过 | 15对块，退出码0；史密斯小姐拒绝格雷附带克雷斯韦尔控制的捐助（全书道义高潮）；痛斥玛丽·泰勒 |
| 2026-08-03 | XVII The Rape of the Fleece | 通过 | 13对块，退出码0；圣诞发饷众生相；银羊毛被克雷斯韦尔家掠夺；佐拉觉醒、决意寻路 |
| 2026-08-03 | XVIII The Cotton Corner | 通过 | 16对块，退出码0；棉价大起大落、农民同盟被北方资本操纵囤积；克雷斯韦尔赌赢五十万 |
| 2026-08-03 | XIX The Dying of Elspeth | 通过 | 44对块，退出码0；哈里求婚玛丽、玛丽应允；埃尔斯贝思临终、巫者送终；佐拉守尸、暴徒破门而逃（全书神秘—惊悚高潮） |
| 2026-08-03 | XX The Weaving of the Silver Fleece | 通过 | 29对块，退出码0；银羊毛被运往北方做嫁衣、约翰·泰勒电报暗藏命运；佐拉沦入纵酒狂欢被史密斯救回；史密斯托付佐拉予范德普尔太太、点明『求的是他的敬重』 |
| 2026-08-03 | XXI The Marriage Morning | 通过 | 28对块，退出码0；佐拉入范德普尔府为侍女、绣嫁衣识破银羊毛归己；复活节双人婚礼（海伦穿巴黎华服、玛丽穿银羊毛）；佐拉匿银羊毛于雪松箱、藏沼泽 |
| 2026-08-03 | XXII Miss Caroline Wynn | 通过 | 31对块，退出码0；布莱斯北上华盛顿谋财政部文书、识卡罗琳·怀恩；史密斯参议员政治交易内幕；斯蒂林斯引布莱斯入黑人上流社会、怀恩小姐召蒂尔斯韦尔敌意 |
| 2026-08-03 | XXIII The Training of Zora | 通过 | 26对块，退出码0；佐拉随范德普尔太太赴纽约、城如沼泽之悟；范德普尔太太与玛丽议佐拉前途、伊斯特利以法国大使位图谋其影响力；佐拉埋首书海、遍游古今世界 |
| 2026-08-03 | XXIV The Education of Alwyn | 通过 | 28对块，退出码0；怀恩小姐调教阿尔文衣仪、引其入华盛顿黑人上流社会；伯特利文学会阿尔文即席演说震动全场；怀恩自述法官旧事、坦陈对世道之不信任 |
| 2026-08-03 | XXV The Campaign | 通过 | 37对块，退出码0；大选内幕（伊斯特利图范德普尔驻法大使、共和党笼络黑人选票）；阿尔文被推为黑人演说领袖、助共和党胜选；史密斯许以高位、怀恩求婚成功（布莱斯俯首时见佐拉之面） |
| 2026-08-03 | XXVI Congressman Cresswell | 通过 | 27对块，退出码0；哈里买官进国会、玛丽空守华宅；斯蒂林斯与蒂尔斯韦尔结盟构陷阿尔文（诱其演说激怒南方、废其任命）；范德普尔太太力保阿尔文、闻其订婚而惊、佐拉闭门 |
| 2026-08-03 | XXVII The Vision of Zora | 通过 | 24对块，退出码0；佐拉夜入小教堂闻道重生、立誓回南方为族人；范德普尔太太定五年之约助佐拉游学、许助阿尔文登财务长；玛丽入公民俱乐部、社区会议初识佐拉与怀恩 |
| 2026-08-03 | XXVIII The Annunciation | 通过 | 22对块，退出码0；就职典礼两场舞会（白人舞会与黑人舞会对照、玛丽再见布莱斯）；伊斯特利南下布局（毙教育法案、保棉花联合体）；哈里逼玛丽退出公民俱乐部、玛丽报喜有孕 |
| 2026-08-03 | XXIX A Master of Fate | 通过 | 35对块，退出码0；史密斯揭蒂尔斯韦尔/斯蒂林斯构陷局、欲怀恩牵制阿尔文；匿名诗信（亨利《不可征服》）点醒阿尔文；毕业典礼阿尔文怒攻本党、财务长任命被否、斯蒂林斯上位；怀恩弃阿尔文转订婚斯蒂林斯（全书道德抉择高潮） |
| 2026-08-03 | XXX The Return of Zora | 通过 | 26对块，退出码0；范德普尔太太以谎言换得驻法大使、佐拉失望别离（携银色羊毛与支票）；佐拉南下火车受辱亲历种族隔离之苦；归校与史密斯小姐重逢、学校凋敝待救 |
| 2026-08-03 | XXXI A Parting of Ways | 通过 | 39对块，退出码0；玛丽产后获知不能再育（子嗣之罪追三四代）、立誓以牺牲赎罪；操持全南方艺术展谋丈夫驻法大使；怀恩（已嫁斯蒂林斯）参展夺魁揭种族歧视；玛丽夜追丈夫至妓院、昏厥；哈里逐妻回阿拉巴马 |
| 2026-08-03 | XXXII Zora’s Way | 通过 | 23对块，退出码0；佐拉归乡目睹种植园暴政（烧物逼签、鞭打犁童）、立志护卫黑人女性；史密斯小姐坦陈学校抵押将倾；范德普尔支票揭盅一万块、佐拉立意买下沼泽建自由社区 |
| 2026-08-03 | XXXIII The Buying of the Swamp | 通过 | 30对块，退出码0；佐拉以一千定金五十元/亩购沼泽二百亩（藏九千）；琼斯牧师忌恨中伤致佃户爽约；神秘老者（送终之巫）夜降布道会斥众、率众连夜开荒二十亩；埃尔斯贝思小屋幻灭、布莱斯归 |
| 2026-08-03 | XXXIV The Return of Alwyn | 通过 | 25对块，退出码0；布莱斯车站偶遇玛丽、闻佐拉南下归乡受召回农场；玛丽误解阿尔文情意、上校持鞭破门、佐拉奔走救场解围（携衣篮现身）；阿尔文求婚被佐拉平静拒绝 |
| 2026-08-03 | XXXV The Cotton Mill | 通过 | 29对块，退出码0；图姆斯维尔建棉纺厂、泰勒『以黑制白以白制黑』的劳工平衡术；白人劳工夺权但仍受黑人竞争威胁、种族裂痕加深；佐拉领布莱斯参观『我的大学』、坦陈复兴土地大计 |
| 2026-08-03 | XXXVI The Land | 通过 | 31对块，退出码0；佃户聚议入伙农场、约翰逊告密作梗；佐拉自辩无律师胜诉（泰勒法庭倒戈证克雷斯韦尔有意签约）；上校败诉迁怒泰勒、转而煽动警长科尔顿种族仇恨（黑鬼需要教训）；全书政治经济斗争白热化 |
| 2026-08-03 | XXXVII The Mob | 通过 | 20对块，退出码0；埃玛学成归来护理、泰勒送伤童入院化解厂方索赔；警长煽动暴民夜袭学校、佐拉布火阵守夜化解；次日约翰逊告密、罗布与约翰逊被私刑吊死松树（全书悲剧高潮） |
| 2026-08-03 | XXXVIII Atonement | 通过 | 22对块，退出码0；克雷斯韦尔上校临终认外孙女埃玛、忏悔私刑之罪而逝；遗赠学校二十万、佐拉以圣洁成全布莱斯与『另一人』、终悟彼此相爱；布莱斯求婚（全书圆满收束）+ 跋诗『放我的族人走』。**全书40篇全部译完** |
