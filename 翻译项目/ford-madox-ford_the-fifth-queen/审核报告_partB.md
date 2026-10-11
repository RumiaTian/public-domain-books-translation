# 《第五王后》（The Fifth Queen）后半卷独立审校报告

- 审校日期：2026-10-11
- 质量等级：B 良好
- 一句话结论：后半卷整体文风古雅苍劲、人物对白生动传神、宏大宫廷与宗教争端意象表达精准，但第19章（21-chapter-19.zh-CN.md）存在大范围级联跨块排版错位（第28块至第41块）、单句漏译（第28块首句）以及拉丁诨名未遵术语表翻译而保留英文字符（第6块）等问题，综合评定为B良好并出具完整修复代码

## 一、全局评估与定级

- 综合质量评级：B 良好（实事求是定级，因第19章存在级联跨块排版错位与单句漏译缺陷，符合B级标准；出具完整修复方案，经修复后可达极优标准）
- 缺陷统计汇总：
  - A级致命缺陷（整章脱译、错位无法挽回）：0项
  - B级严重缺陷（排版级联错位漂移、单句漏译）：2项（第19章第28块至第41块级联跨块错位；第19章第28块首句漏译）
  - C级轻微缺陷（术语表未遵从与英文字符残留）：1项（第19章第6块巴恩斯博士诨名保留英文字符）
- 审校范围与工程基准：
  - 审校对象：后半卷共11个章节及分卷文件（12-chapter-11 至 22-chapter-20），全部位于译文目录下，排除 *.all.zh-CN.md
  - 篇目涵盖：
    - 12-chapter-11.zh-CN.md（第二部第4章：凯瑟琳与亨利八世花园纵论）共26块，550行
    - 13-chapter-12.zh-CN.md（第二部第5章：克伦威尔与主教派系深层权谋）共19块，443行
    - 14-chapter-13.zh-CN.md（第二部第6章：加德纳与诺福克密室博弈）共19块，407行
    - 15-chapter-14.zh-CN.md（第二部第7章：维里杜斯全面质询与宫廷审问）共68块，866行
    - 16-chapter-15.zh-CN.md（第二部第8章：夜行暗探与多重书信布局）共19块，399行
    - 17-chapter-16.zh-CN.md（第二部第9章：第二部终章、暴风雨前夕）共25块，349行
    - 18-part-3-the-king-moves.zh-CN.md（第三部分卷标头：第三部 国王行动了）分卷标题页，1行，块数0
    - 19-chapter-17.zh-CN.md（第三部第1章：汉普顿宫廷之变与新政风波）共14块，291行
    - 20-chapter-18.zh-CN.md（第三部第2章：亨利八世与诺福克密谋）共21块，274行
    - 21-chapter-19.zh-CN.md（第三部第3章：信使被执、刑讯阴影与密探博弈）共44块，837行
    - 22-chapter-20.zh-CN.md（第三部第4章：全书大结局、权臣落幕与王后入主）共51块，742行
  - 质量与工程量度指标：
    - 总双语对照块数：306块
    - 逐块精读通读覆盖率：100%（共计306块，逐块严格对照阅读，无遗漏跳读）
    - 章末截断发生率：0%（11个文件末尾段落全部完好，全书收束严密）
    - 原文译文文件只读保护隔离遵循率：100%（未擅自修改任何现有源文件与译文文件）

## 二、九项清单逐项核查结论

- 语义错配：存在1处系统性错配（第19章第28块至第41块，由于上一块尾句或尾段侵占下一块首句或首段，导致连续14个块的中文译文与对应英文原文产生整体位移与归属漂移）
- 整段漏译：存在1处单句漏译（第19章第28块首句原文“Katharine hung her head and meditated for a space.”在对应中文块中完全遗漏脱落）
- 章末截断：完全合格（后半卷11个文件全部通读至文末，包括第20章全书终局“克伦威尔朝前迈出一步。……他静默而立，身形矮小而庞大”等收束段落均严密咬合，无截断残缺）
- 重大数字错译：完全合格（包括第11章的九点与四名侍从、第14章的十四天与七个郡、第19章的十五封信、六点、四个穿灰斗篷的人、五处田庄、四十分钟与十分钟等关键数字，核查全部精确对应）
- 术语表违规：存在1处违规（第19章第6块将巴恩斯博士诨名“Antoninus Anglicanus”直译保留拉丁英文，违背术语表第640条指定的“安东尼努斯·安格利卡努斯”）
- 同名异译：完全合格（凯瑟琳·霍华德、诺福克、加德纳、维里杜斯、克伦威尔、查普伊斯、卡尔佩珀等核心人物译名贯穿始终保持高度统一）
- 英文单词残留：存在1处轻微残留（第19章第6块遗留“Antoninus Anglicanus”，其余章节所含古典拉丁引文均附标准六角括号〔〕中文释义，未见英文正文脱译残留）
- 语义误译：未见重大语义扭曲，整体词句理解深入透彻，复杂长句拆分得当
- 风格与流畅度：优良（精准传达了福特·马多克斯·福特原著幽深、阴冷、机变百出的都铎王朝权谋氛围，人物对话古风盎然且性格鲜明，叙事铺陈节奏极为洗练有力）

## 三、缺陷清单与修复方案

- 缺陷一（B级·第19章第28块至第41块级联跨块排版错位与第28块首句漏译）
  - 问题定位：译文/21-chapter-19.zh-CN.md，第522行至第787行（对应第28块至第41块）
  - 现象描述：
    - 第28块译文遗漏首句“Katharine hung her head and meditated for a space.”（凯瑟琳垂下头，沉吟了片刻），且末尾错误带入属于第29块首句的译文““收回您的誓言！”凯瑟琳喊道”
    - 第29块译文末尾错误带入属于第30块首句的译文“凯瑟琳在情感的震颤中强自镇定，玛丽公主干巴巴地说：”
    - 第30块译文末尾错误带入属于第31块首句的译文““好丫头，”玛丽公主说。“我做你的奴仆：不过，能到手几分便收几分吧。””
    - 第31块译文末尾错误包含了原本属于第32块首段的整段译文“内德·普因斯一路走去，少不得经过大使的宅子……”
    - 第32块译文因首段被前一块侵占，仅剩四人拦路对白，且末尾错误带入属于第33块首句的译文“普因斯把披风向肩后一甩，手按剑柄”
    - 第33块至第40块依次顺延错位一个自然段
    - 第41块末尾错误带入第42块首句译文““你肯拿你自己的脑袋押上么？””，导致该句在第41块末与第42块首重复出现；自第42块起对照恢复正常
  - 修复方案与代码实现：严格按原文块边界剥离并归位各段译文，补齐第28块遗漏首句，清除第41块冗余重复句，完整替换代码如下：

```markdown
===Original===
Katharine hung her head and meditated for a space.

“No, before God,” she said earnestly, “I think you judge me wrong. I think I am not as you think me. I think that I do seek no ends of my own.”

The Lady Mary raised her eyebrows and snickered ironically.

“But of this I am very certain,” Katharine said. She spoke more earnestly, seeming to plead: “If I thought that I were grown a self-seeker, by Mars who changed Alectryon to a cock, and by Pallas Athene who changed Arachne to a spider﻿—if I were so changed, I would get me gone from this place. But here is a thing that I may do. If you will aid me to do it I will stay. If you will not I will get me gone.”

“Good wench,” Mary answered, “let us say for the sake of peace that thou art honest.﻿ ﻿… Yet I have sworn by other gods than thine that never will I do aught that shall be of aid, comfort or succour to my father’s cause.”
===Chinese===
凯瑟琳垂下头，沉吟了片刻。

“不，上帝在上，”她恳切地说，“我想您看错了我。我想我不是您料想的那种人。我想我确实不曾营谋一己的私图。”

玛丽公主扬起眉，讥诮地嗤笑了一声。

“可有一件事我万分确信，”凯瑟琳说。她说得更恳切了，几乎是哀求：“倘若我认定自己已长成一个营私之人——凭那把阿勒克特里翁（Alectryon）变成公鸡的玛尔斯，凭那把阿拉喀涅（Arachne）变成蜘蛛的帕拉斯·雅典娜（Pallas Athene）起誓——倘若我变了质，我必自行离开此地。可这里有一件我做得来的事。您若肯助我做成，我便留下。您若不肯，我便走。”

“好丫头，”玛丽答道，“为了太平起见，就算你心术端正。……可我发的誓，奉的是别的神，不是你那几位：但凡于我父王之业有补益、有宽慰、有救助的事，我一概不做。”

===Original===
“Take back your oaths!” Katharine cried.

“For thee!” Mary said. “Wench, thou hast brought me food: thou hast served me in the matter of letters. I might only with great trouble get another so to serve me. But, by Mars and Pallas and all the constellation of the deities, thou mightest get thee to Hell’s flames or ever I would take back an oath.”

“Oh, madness,” Katharine cried out. “Oh, mad frenzy of one whom the gods would destroy.” Three times before she had reined in her anger: now she stretched out her hands with her habitual gesture of pitiful despair. Her eyes looked straight before her, and, as she inclined her knees, the folds of her grey dress bent round her on the floor.

“Here I have pleaded with you, and you have gibed me with the love of the King. Here I have been earnest with you, and you have mocked. God help me!” she sobbed, with a catch in her throat. “Here is rest, peace and the blessing of God offered to this land. Here is a province that is offered back to the Mother of God and the dear hosts of heaven. Here might we bring an erring King back to the right way, a sinful man back unto his God. But you, for a parcel of wrongs of your own.﻿ ﻿…”

“Now hold thy peace,” Mary said, between anger and irony. “Here is a matter of a farthing or two. Be the letter written, and kiss upon it.”
===Chinese===
“收回您的誓言！”凯瑟琳喊道。

“为你才肯么！”玛丽说。“丫头，你给我带过吃食：书信的事上，你也服侍过我。再寻一个这样服侍我的人，须得大费周章。可是，凭玛尔斯、帕拉斯和满天星宿的众神祇，你就是堕入地狱的烈焰，我也断不收回一句誓言。”

“哦，疯狂，”凯瑟琳失声喊道。“哦，诸神欲毁之人的癫狂啊。”此前她已三次勒住怒火：此刻她伸出双手，摆出那惯常的哀怜而绝望的姿势。她的眼睛直望着前方，双膝缓缓屈下，灰裙的褶裥在地板上向她周身弯拢。

“我在这里向您恳求，您却拿国王的爱来讥诮我。我在这里与您披肝沥胆，您却百般嘲弄。上帝救我！”她喉咙里哽了一下，呜咽道。“此刻，安宁、太平与上帝的祝福，正呈给这片国土。此刻，一省之地，正待奉还给天主之母和天上亲爱的众军。此刻，我们本可把迷途的国王领回正道，把有罪的人领回他的上帝面前。可您，为着自己那一包私怨。……”

“好了，闭上嘴吧，”玛丽说，半是恼怒，半是讥诮。“不过一两个法新的小事。信照写，写完亲一记作数。”

===Original===
Katharine stayed herself in the tremor of her emotions, and the Lady Mary said drily:

“Be the letter written. But thou shalt write it. I have sworn that I will do nothing to give this King ease.”

“But my writing.﻿ ﻿…” Katharine began.

“Thou shalt write,” Mary interrupted her harshly. “If thou wilt have this King at peace for a space that Cromwell may fall, why I am at one with thee. For this King is such a palterer that without this knave at his back I might have had him down ten years ago. Therefore, thou shalt write, and I will countersign the words.”

“That were to write thyself,” Katharine said.
===Chinese===
凯瑟琳在情感的震颤中强自镇定，玛丽公主干巴巴地说：

“信是要写的。可落笔的须是你。我发过誓：凡是能给这国王宽解的事，我一概不为。”

“可由我执笔。……”凯瑟琳开口道。

“由你来写，”玛丽粗暴地打断她。“你若要让这国王安分一个时期，好教克伦威尔倒台，那我和你正是一条心。因为这国王最会支吾迁延，若没有这恶棍在背后撑着，十年前我早把他扳倒了。所以，由你来写，我在字句下副署。”

“那等于是您亲笔了，”凯瑟琳说。

===Original===
“Good wench,” the Lady Mary said. “I am thy slave: but take what thou canst get.”

Towards six of the next day young Poins clambered in at Katharine Howard’s window and stood, pale, dripping with rain and his teeth chattering, between Cicely Elliott and her old knight.

“The letter,” he said. “They have taken thy letter. My advancement is at an end!” And he fell upon the floor.

Going jauntily along the Hampton Street, he had been filled, that afternoon, with visions of advancement. Drifts of rain hid the osiers across the river and made the mud ooze in over the laces of his shoes. The tall white and black house, where the Emperor’s ambassador had his lodgings, leaned in all its newness over the path, and the water from its gutters fell right into the river, making a bridge above a passer’s head. The little cookshop, with its feet, as it were, in the water, made a small hut nestling down beneath the shadow of the great house. It was much used by Chapuys’ grooms, trencher boys and javelin men, because the cook was a Fleming, and had a comfortable hand in stewing eels.
===Chinese===
“好丫头，”玛丽公主说。“我做你的奴仆：不过，能到手几分便收几分吧。”

次日将近六点，小普因斯从凯瑟琳·霍华德的窗口爬了进来，站在西西莉·埃利奥特和她的老骑士中间，脸色发白，浑身雨淋，牙齿捉对儿打战。

“信，”他说。“他们把您的信截走了。我的前程完了！”说完他扑倒在地板上。

那天下午，他一路神气活现地走在汉普顿街上，满脑子都是高升的幻梦。一阵阵雨幕遮没了河对岸的柳丛，泥浆从鞋带上漫进来。皇帝大使下榻的那座高大的黑白两色楼房，通身簇新，俯临在小径上方，檐槽的水直落河中，在过路人头顶上架起一道水桥。那家小吃食铺仿佛双脚踏在水里，像间小屋，蜷伏在大宅的阴影底下。查普伊斯的马夫、端盘侍童和持矛侍从常来照顾生意，因为掌勺的厨子是个法兰德斯人，炖起鳗鱼来，有一手叫人舒坦的好功夫。

===Original===
Ned Poins must pass the ambassador’s house in his walk, but in under the dark archway there stood four men sheltering, in grey cloaks that reached to their feet. Stepping gingerly on the brick causeway that led down to the barge-steps, they came and stood before the young man, three being in a line together and one a little to the side. He hardly looked at them because he was thinking: “This afternoon I will say to my sister Margot: ‘Fifteen letters I have carried for thy great persons. I have carried them with secrecy and speed. Now, by Cock, I will be advanced to ancient.’ ” He had imagined his sister pleading with him to be patient, and himself stamping with his foot and swearing that he would be advanced instantly.

The solitary one of the four men barred his way, and said:

“No further! You go back with us!”
===Chinese===
内德·普因斯一路走去，少不得经过大使的宅子；可幽暗的拱门底下正立着四个避雨的人，灰斗篷直垂到脚面。他们踩着通向游船码头的砖道，小心翼翼地走过来，在这少年面前站定：三个并作一排，一个稍稍偏在一旁。他几乎没有看他们一眼，因为他心里正盘算着：“今天下午我要对玛戈妹妹说：‘我为你的那些大人物送了十五封信。我送得又机密又麻利。如今，凭老天，我要升掌旗官了。’”他已经预想好了妹妹劝他耐心、他自己跺着脚赌咒必须立刻升迁的光景。

那四人中独站一旁的一个拦住去路，说：

“走不得再远了！你跟我们回去！”

===Original===
Poins swung his cape back and touched his sword-hilt.

“You will have your neck stretched if you stay me,” he said.

The other loosened his cloak which had covered him up to the nose. He showed a mocking mouth, a long red beard that blew aside in a wild gust of the weather, and displayed on his breast the lion badge of the Lord Privy Seal.

“An you will not come you shall be carried!” he said.

“Nick Throckmorton,” Poins answered, “I will slit thy weazand! I am on a greater errand than thine.”
===Chinese===
普因斯把披风向肩后一甩，手按剑柄。

“你敢拦我，管叫你脖颈吃绞索、拉得老长，”他说。

对方解开一直掩到鼻端的斗篷，露出一张含讥带诮的嘴、一部让狂风吹向一边的火红长须，又亮出胸前的御玺大臣狮纹徽记。

“你若不肯走，就被人抬着走！”他说。

“尼克·斯罗克莫顿，”普因斯回声道，“我要割断你的咽喉！我身负的差使比你的大。”

===Original===
It was strong in his mind that he was bearing a letter for the King’s Highness. The other three laid hands swiftly upon him, and a wet cloak flapped over his head. They had his elbows bound together behind his back before his eyes again had the river and the muddy path to look upon. Throckmorton grinned sardonically, and they forced him along in the mud. The rain fell down; his cloak was gone. And then a great dread entered into his simple mind. It kept running through his head:

“I was carrying a letter for the King﻿—I was carrying a letter for the King!” but his addled brains would bear his thoughts no further until he was cast loose in the very room of Privy Seal himself. They had used him very roughly, and he staggered back against the wall, gasping for breath and weeping with rage and fear.

Privy Seal stood before the fire; his eyes lifted a little but he said nothing at all. Throckmorton took a dagger from the chain round his neck, and cut the bag from the boy’s girdle. Still smiling sardonically, he placed it in Privy Seal’s fat hands.

“Here is the great secret,” he said. “I took it even in the gates of Chapuys.”
===Chinese===
他心里笃定得很：他这是在替国王陛下送信。另外三人飞快地朝他下手，一条湿斗篷啪地罩上他的头。等他的眼睛重新看得见河水和泥泞的小路，他的双肘早已被反绑在背后。斯罗克莫顿讥诮地一咧嘴，他们押着他在泥里深一脚浅一脚。雨不停地下；他的披风也没了。这时，一阵巨大的恐惧钻进他单纯的头脑。那念头在脑子里转个不住：

“我是在给国王送信——我是在给国王送信！”可他那团乱麻似的脑子，再也驮不动别的念头，直到他被松了绑，扔进御玺大臣本人的房间。他们下手极粗，他踉跄着退到墙根，大口喘气，又怒又怕地哭了出来。

御玺大臣立在炉火前；眼睛略抬了抬，却一言不发。斯罗克莫顿从颈间链子上取下一柄匕首，把布袋从少年腰间割下。他面上仍挂着讥诮的笑，把袋子搁进御玺大臣肥厚的手里。

“天大的机密在这里了，”他说。“我就在查普伊斯的家门口把它截了下来。”

===Original===
Privy Seal started a little and cried, “Ah!” The boy would have spoken, but he feared even to cry out; his eyes were starting from his head, and his breath came in great gusts that shook him. Privy Seal sat down in a large chair by the fire and considered for a moment. Then he slowly drew out the crumpled ball of paper. Here at last he held the Lady Mary utterly in his power; here at last, at the eleventh hour, he had a new opportunity to show to the King his vigilance, his power, and how necessary he was to the safety of the realm. He had been beginning to despair; Winchester was to confess the King that night. Now he held them.﻿ ﻿…

“I have been diligent,” Throckmorton said. “I had had the Lady Mary set in the room that has a spyhole beside a rose in the ceiling. So I saw the writing of this letter.”

Cromwell said, “Ah!” He had pulled the paper apart, smoothed it across his knee, and looked at it attentively. Then he held it close to the fire, for no blank paper could trouble the Privy Seal. This was a child’s trick at best.

In the warmth faint lines became visible on the paper; they darkened and darkened beneath his intent eyes. Behind his back Throckmorton, with his immense beard and sardonic eyes, rubbed his hands and smiled. Privy Seal’s fingers trembled, but he gave no further sign.
===Chinese===
御玺大臣微微一震，喊出一声“啊！”那少年想要说话，可他连喊都不敢喊；他双眼凸出眼眶，喘气一口接一口，浑身发颤。御玺大臣在炉边的大椅里坐下，沉吟了片刻。随后他缓缓抽出那团皱纸。到了这一步，玛丽公主终于全然落进他的掌心；到了这一步，在最后关头，他终于又得着一个新机会，可以向国王显一显自己的警觉、自己的权势，以及自己对这王国的安危何等要紧。他本来已经开始绝望；温彻斯特当夜就要去听国王的忏悔了。而此刻，他们全在他手里。……

“我办事勤谨，”斯罗克莫顿说。“我早让人把玛丽公主安置在那间屋里——天花板的玫瑰饰旁开着一个窥孔。这封信是怎样写下的，我都看在眼里。”

克伦威尔说了声“啊！”。他已把纸摊开，在膝头抚平，细细端详。随后他把纸凑近炉火——区区一张白纸，可难不倒御玺大臣。这至多是孩童的把戏。

热气一熏，纸上显出淡淡的字迹；在他专注的目光底下，颜色越烘越深。他背后，斯罗克莫顿搓着手直笑，一部浓髯，满眼讥诮。御玺大臣的手指发起颤来，却不露别的形迹。

===Original===
Suddenly he cried, “What!” and then, “Both women! both.﻿ ﻿…”

He fell back in the chair, and the sudden quaver of his face, the deep breath that he drew, showed his immense joy.

“God of my heart! Both women!” he said again.

The rain hurled itself with a great rustling against the casement. Though it was so early, it was already nearly dark. Cromwell sat up suddenly and pointed at the boy.
===Chinese===
他突然喊出声：“什么！”接着又是一声：“两个女人！都是。……”

他仰面倒回椅中，脸上骤然一颤，又深深吸进一口气，透出他巨大的欢喜。

“我心中的上帝啊！两个女人！”他又说了一遍。

雨挟着大片簌簌之声扑向窗扉。天时虽早，天色却已近乎昏黑。克伦威尔猛然坐直，手指着那少年。

===Original===
“Take that rat away!” he said. “Set him in irons, and come back here.”

Throckmorton caught the quivering boy by the ear and led him out at the door. He took him down a small stair that opened behind a curtain. At the stair-foot he pulled open a small, heavy door. He still held his dagger, and he cut the ropes that tied Poins’ elbows. With a sudden alacrity and a grin of malice he kicked him violently.

“Get you gone to your mistress,” he said.

Poins stood for a moment, wavering on his feet. He slipped miserably in the mud of the park, and suddenly he ran. His grey, straining form disappeared round the end of the dark buildings, and then Throckmorton waved a hand at the grey sky and laughed noiselessly. Thomas Cromwell was making notes in his tablets when his spy reentered the room, with the raindrops glistening in his beard.
===Chinese===
“把那耗子带走！”他说。“给他戴上镣铐，你再回这里来。”

斯罗克莫顿揪住打颤少年的耳朵，把他带出门去。他领他走下一道开在帘幔后的小楼梯，在梯脚拉开一扇沉重的小门。他手里仍握着匕首，割断了捆绑普因斯双肘的绳子，随即陡然一阵麻利，狞笑着狠狠踹了他一脚。

“滚回你女主子那儿去，”他说。

普因斯站了一会儿，脚下直晃。他可怜巴巴地在园子的泥地里打滑，忽然撒腿跑了起来。他那灰色的、拼命奔逃的身影绕过黑魆魆的建筑尽头不见了，斯罗克莫顿这才朝灰色的天空挥一挥手，无声地笑了。托马斯·克伦威尔正在记事板上写着记事，他的密探重新进屋来，髯须上雨珠闪亮。

===Original===
“Here are some notes for you,” Cromwell said. He rose to his feet with a swift and intense energy. “I have given you five farms. Now I go to the King.”

Throckmorton spoke gently.

“You are overeager,” he said. “It is early to go to the King’s Highness. We may find much more yet.”

“It is already late,” Cromwell said.

“Sir,” Throckmorton urged, “consider that the King is much affected to this lady. Consider that this letter contains nothing that is treasonable; rather it urges peace upon the King’s enemies.”
===Chinese===
“这几条记事给你，”克伦威尔说。他浑身带着一股迅疾而炽烈的劲头，霍地立起。“我已赏了你五处田庄。现在我这就去见国王。”

斯罗克莫顿放软了声气。

“您太心急了，”他说。“这时候就去见国王陛下，还早。咱们兴许还能再掘出许多来。”

“已经迟了，”克伦威尔说。

“爵爷，”斯罗克莫顿进言道，“您想想，国王对这位贵妇迷恋得很。您想想，这封信里没有一句叛国的话；反倒是在劝国王的敌人息兵。”

===Original===
“Aye,” said Cromwell; “but it is written covertly to the King’s enemies.”

“That, it is true, is a treason,” Throckmorton said; “but it is very certain that the Lady Mary hath written letters very much more hateful. By questioning this boy that we have in gaol, by gaoling this Lady Katharine﻿—why, we shall put her to the thumbscrews!﻿—by gaol and by thumbscrew, we shall gar her to set her hand to another make of confession. Then you may go to the King’s Highness.”

“Nick Throckmorton,” Cromwell said, “Winchester hath tonight the King’s ear.﻿ ﻿…”

“Sir,” Throckmorton answered, and a tremble in his calm voice showed his eagerness, “I beseech you to give my words your thoughts. Winchester hath the King’s ear for the moment; but I will get you letters wherein these ladies shall reveal Winchester for the traitor that we know him to be. Listen to me.﻿ ﻿…” He paused and let his crafty eyes run over his master’s face. “Let this matter be for an hour. See you, you shall make a warrant to take this Lady Katharine.”

He paused and appeared to reflect.
===Chinese===
“是啊，”克伦威尔说，“可它终究是暗地里写给国王的敌人的。”

“这确实算得叛国，”斯罗克莫顿说，“可千真万确，玛丽公主写过的信，罪过多比这重。把押在牢里的这小子提来一审，再把这位凯瑟琳贵妇下到狱里——嗐，咱们给她上拇指夹！——凭牢狱加刑具，管教她亲笔另招一份口供。到那时，您再去找国王陛下不迟。”

“尼克·斯罗克莫顿，”克伦威尔说，“今夜国王的耳朵归温彻斯特。……”

“爵爷，”斯罗克莫顿答道，平静的嗓音里一丝颤动泄露了他的急切，“求您把我的话放在心上掂量掂量。温彻斯特眼下占着国王的耳朵；可我能替您弄来书信，叫这两位贵妇亲手揭出温彻斯特——揭出那个我们心里有数的叛贼。您听我说。……”他顿住，让那双狡黠的眼睛在主人脸上溜了一遍。“这事且搁上一个钟头。您瞧着：您来签一道手令，把这位凯瑟琳贵妇拿问。”

他顿了顿，像是思量。

===Original===
“In an hour she shall be here. Give me leave to use my thumbscrews.﻿ ﻿…”

“Aye, but Winchester,” Cromwell said.

“Why,” Throckmorton answered confidently, “in an hour, too, Winchester shall be with the King in the King’s Privy Chapel. There will be a make of prayers; ten minutes to that. There shall be Gardiner talking to the King against your lordship; ten minutes to that. And, Winchester being craven, it shall cost him twice ten minutes to come to begging your lordship’s head of the King, if ever he dare to beg it. But he never shall.”

Cromwell said, “Well, well!”

“There we have forty minutes,” Throckmorton said. He licked his lips and held his long beard in his hand carefully, as if it had been a bird. “But give me ten minutes to do my will upon this lady’s body, and ten to write down what she shall confess. Then, if it take your lordship ten minutes to dress yourself finely, you shall have still ten in which you shall show the King how his Winchester is traitor to him.”
===Chinese===
“一个钟头之内，她准到这里。请许我动用拇指夹。……”

“是啊，可温彻斯特那边呢，”克伦威尔说。

“嗐，”斯罗克莫顿胸有成竹地答道，“一个钟头之后，温彻斯特也一样会同国王待在国王的御用礼拜堂里。须得行一通祈祷；那占去十分钟。接着是加德纳在国王面前数说大人；又十分钟。再者，温彻斯特是个懦夫，就算他真敢开这个口，从进谗走到向国王乞请大人的首级那一地步，还得再破费两个十分钟。可他万万不敢。”

克伦威尔说：“唔，好，好！”

“这样我们手头就有四十分钟，”斯罗克莫顿说。他舔了舔嘴唇，小心翼翼地把长髯托在手里，像捧着一只鸟。“但请给我十分钟，让我在这位贵妇身上行我的手段；再给十分钟，录下她的口供。然后，大人若用十分钟把自己穿戴体面，您还整整剩下十分钟，正好向国王揭明：他的温彻斯特是怎样一个叛贼。”

===Original===
Cromwell considered for a minute; his lips twitched cautiously the one above the other.

“This is a great matter,” he said. He paused again. “If this lady should not confess! And it is very certain that the King affects her.”

“Give me ten minutes of her company,” the spy answered.

Cromwell considered again.

“You are very certain,” he said; and then:
===Chinese===
克伦威尔沉吟了一分钟；两片嘴唇小心地一上一下互相挪动。

“这是件天大的事，”他说。他又顿了顿。“万一这贵妇不招呢！而国王宠爱她，这是千真万确的。”

“给我十分钟同她相处，”密探答道。

克伦威尔又沉吟起来。

“你很有把握，”他说；接着又道：
```

- 缺陷二（C级·第19章第6块术语表违规与英文字符残留）
  - 问题定位：译文/21-chapter-19.zh-CN.md，第97行（对应第6块）
  - 现象描述：原文为“nicknamed Antoninus Anglicanus”，译文译为“诨名 Antoninus Anglicanus〔拉丁语，意为英格兰的安东尼努斯〕”，违反术语表第640条指定的规范译名“安东尼努斯·安格利卡努斯”，且残留未汉化英文字符
  - 修复方案与代码实现：
    - 将第97行整行替换为：就在她叔祖诺福克公爵派人传见她的那一天，国王与那个异端巴恩斯博士——诨名“安东尼努斯·安格利卡努斯”〔意为英格兰的安东尼努斯〕——会了面

## 四、后续处理建议

- 针对第19章的级联排版错位及漏译，由后续集成阶段执行上述提供的修复代码，严禁在审校阶段破坏只读隔离原则
- 针对第19章第6块的诨名规范，同步进行修正替换
- 整体后半卷在完成上述针对性修复后，全卷质量即达极优水准，可顺利并入全书终审及合流发布
