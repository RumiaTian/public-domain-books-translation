# Plan.md — joseph-conrad_suspense

## 本计划信息

- **项目名称**：joseph-conrad_suspense（《悬念》）
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/小说文学.md
- **术语表**：术语表.md

---

## 文件分工

| 文件 | 作用 | 谁来改 |
|------|------|--------|
| `项目说明.md` | 项目基本信息 | 人工 |
| `术语表.md` | 翻译硬约束层 | agent / 人工 |
| `translation_queue.csv` | 任务队列 | 翻译前改 doing，完成改 done |
| `Plan.md`（本文件） | 执行步骤 + 运行日志 | agent 追加日志 |
| `原文/*.md` | 源文（4 卷名页 + 15 章） | 不改 |
| `译文/*.zh-CN.md` | 译文产出 | 翻译 agent 产出 |

---

## 篇目清单（4 卷 15 章，未完成）

文件清单见 `translation_queue.csv`（19 行）。各卷章节序号独立重启。

| 卷 | 章 | 文件 |
|---|---|---|
| Part I | I–IV | part-1, 1-1 ~ 1-4 |
| Part II | I–VII | part-2, 2-1 ~ 2-7 |
| Part III | I–III | part-3, 3-1 ~ 3-3 |
| Part IV | I（全书未完） | part-4, 4-1（86.3KB，最长） |

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-08-04 | 建项目 | — | 19 文件提取完成（4卷名页+15章），领域=小说文学（康拉德遗作/拿破仑时代），术语表预填人物/地名/政治用语 |
| 2026-08-03 | part-1.md | done | 卷名页，仅标题「Part I / 第一卷」，无正文块；exit=0，0 错配 |
| 2026-08-03 | part-2.md | done | 卷名页，仅标题「Part II / 第二卷」，无正文块；exit=0，0 错配 |
| 2026-08-03 | 2-1.md | done | 21.0KB，卷二第I章；exit=0，20 对 Original/Chinese，0 可疑错配；补术语 Spire/Martel/Cantelucci/Nelson/Wellington/Keith/Sir Charles/Naples/Florence/Yorkshire/Jacobin |
| 2026-08-03 | 1-1.md | done | 26.6KB，卷一第I章；exit=0，11 对 Original/Chinese，0 可疑错配；补术语 Mole/felucca/signore/signorino/sbirri/Milord Keith/Buenos Aires/Piedmontese/Austrian |
| 2026-08-05 | 1-2.md | done | 23.6KB，卷一第II章；康拉德长段叙事（莱瑟姆家族史+达蒙一家伦敦流亡+贝尔纳与阿格莱絮语）；exit=0，39 对 Original/Chinese，0 可疑错配；修正 1 处英文残留 inspired；补术语 Medici/Artois/Billingsgate/Christendom/Bonaparte |
| 2026-08-05 | 2-4.md | done | 28.1KB，卷二第IV章；科斯莫在小客厅意外结识蒙特韦索伯爵（海利翁伯爵）——康拉德肖像式长段（染发/核桃色面孔/掷弹兵僵硬），印度发财冒险家话题、王政复辟下孤儿院之争、皮亚诺萨岛开发计划引出厄尔巴消息；exit=0，9 对 Original/Chinese，0 可疑错配；0 英文残留；补术语 Helion/Madame Bubna/Marquis/The Most Christian King/His Apostolic Majesty/Sindh/nabob/Restoration/Clelia/M. le Marquis/D’Armand/Island of Pianosa/Dey of Algiers/Barbary States/King of Piedmont |
| 2026-08-05 | 2-2.md | done | 45.3KB，卷二第II章；科斯莫忆巴黎社交→致函蒙特韦索伯爵夫人→登门重逢阿黛勒，阿格莱、克莱莉娅出场，拿破仑与维也纳会议之议；88.2KB 译文；exit=0，15 对 Original/Chinese，0 可疑错配；自检修复 2 处英文残留（grown-up/schoolboy）；补术语 Henrietta/Hollis/Mrs. R./Lady Jane/Palazzo Brignoli/Palazzo Rosso/Clelia/Marquis d’Armand/Queen of Sardinia/Vienna Congress |
| 2026-08-05 | 2-5.md | done | 22.4KB，卷二第V章；阿黛勒向科斯莫倾诉其与蒙特韦索伯爵（印度发财冒险家、爱尔兰团逃兵、自称将军、撒丁国王授衔）之婚姻始末——伦敦初识→主动求嫁以解父母之忧→蜜月排场与“东方式妒忌”丑剧→被逐→遭流亡圈诽谤迫害→复归→赴意寻“亲”之旅；45.2KB 译文；exit=0，8 对 Original/Chinese，0 可疑错配；0 英文残留（括注术语 coiffée en boucles/ancien régime/émigré/intrigue/Adèle de Montevesso/Madame Seppio/King of Sardinia/Court of Turin/plebeian/Bonaparte 合规）；补术语 Aglae/Madame Seppio/annulation/plebeian/poisoned robe/rabbit-skins dealer |
| 2026-08-05 | 2-6.md | done | 24.2KB，卷二第VI章；壁炉前夜谈，阿黛勒追述帝国年间乡间隐居、与蒙特韦索伯爵（海利翁伯爵）之名存实亡的婚姻、贝尔纳被收买为奸细、拿破仑在狄安娜画廊舞会上唯一一次与她搭话；命运/命运主宰之议；伯爵持烛送客穿越一连串空厅、前厅黝黑农妇式身影收尾；49.0KB 译文；exit=0，17 对 Original/Chinese，0 可疑错配；0 英文残留；沿用 2-2/2-4 译名（伯爵夫人=蒙特韦索夫人，Helion=海利翁伯爵，Lady William=威廉夫人，Countess Bubna=布布纳伯爵夫人）；首现标注 Empire/émigré/royalist/Destiny/Corsican/Bourbon dynasty/Tuileries/Princess of Baden/Galerie de Diane/Piedmont/the Russian campaign/the Emperor/sire/Count Helion/M. le Comte/Madame la Comtesse/Monsieur de Montevesso/Bernard/Aglae/Elba/Mr. Latham/the Man of Destiny/Mme. de Montevesso/Genoa |
| 2026-08-05 | 2-3.md | done | 38.0KB，卷二第III章；科斯莫在布林约利宫谒见达尔芒侯爵（法国驻都灵大使、阿黛勒之父）——侯爵追述流亡岁月中查尔斯爵士之资助、谢绝马德里大使任、赴维也纳议界之苦、保皇党对帝国胜利之复杂心境、厄尔巴岛囚禁拿破仑之近况；随后入小客厅会客，引见威廉·本蒂克夫人、布布纳将军、布布纳夫人、费拉蒂夫人等，又与克莱莉娅（杜拉佐）那"古怪姑娘"一番突兀对话，末尾循伯爵夫人眼色退入小起居室；76.4KB 译文；exit=1（仅 1 处假阳性：'98→九八年 为正当改写，非错配），18 对 Original/Chinese；0 真实英文残留（括注术语 Palazzo Brignoli/Marquis d'Armand/M. de Talleyrand/Sir Charles Stewart/Count Bubna/Lady William Bentick/Mr. Wycherley/Madame de Montevesso/Adèle d'Armand/Count Helion of Montevesso/Genoa/Elba/Yorkshire/India/Leghorn/Turin/Madrid/Vienna 及法语 mon enfant/Un grand dédaigneux/mon jeune ami/mon cher enfant/Venez/parfait galant homme 与意语 signorina 均合规）；补术语 Marquis d'Armand/Bernard/Count Helion of Montevesso/Henrietta Latham/Count Bubna/Lady William Bentick/Lord William/Louise Durazzo/Madame Ferrati/Mr. Wycherley/M. de Talleyrand/Sir Charles Stewart/Turin/Madrid/Vienna/Leghorn/India/Mediterranean/the Revolution/the Man of Elba/Palazzo Brignoli |
| 2026-08-05 | part-3.md | done | 卷名页，仅标题「Part III / 第三卷」，无正文块 |
| 2026-08-05 | part-4.md | done | 卷名页，仅标题「Part IV / 第四卷」，无正文块 |
| 2026-08-05 | 3-2.md | done | 15.5KB，卷三第II章；科斯莫黄昏回房写信（致亨利埃塔），佯装旅途见闻实则心绪不宁，附言补记拿破仑传闻（暗杀/绑架流言、维也纳会议之暴行、里窝那之议）；斯帕尔送信、主人苦笑惊仆；下楼遇马泰尔医生同桌进餐，医生借里维耶拉·迪·莱万特之路劝其赴里窝那、提议转让旅行马车，又借塔列朗亲王密友蒙特龙之口暗示拿破仑不能安分（「我们这儿可看不出这种必要」），并提醒厄尔巴岛之行不可迟误；末段科斯莫独坐房中，蒙特韦索夫人之容颜勾起莱瑟姆庄园藏画（鹅蛋脸圣女、左乳被匕首刺穿）的预言式记忆，惊惧出逃，经格拉齐亚尼府邸空厅、年迈上尉独饮之影，最终踏上去港口的路；31.0KB 译文；exit=0，9 对 Original/Chinese，0 可疑错配；0 英文残留（括注术语 Henrietta/Bonaparte/Livorno/Doctor Martel/Riviera di Levante/Cantelucci/signore/Mr. Latham/Elba/Vienna/Prince Talleyrand/Montrond/Duc d'Enghien/Madame de Montevesso/Lady Jane/Mrs. R./Latham Hall/Grazianis/the siege of Genoa 均合规）；沿用 2-2 译名 R 太太（Mrs. R.）、Lady Jane=简夫人；补术语 Riviera di Levante/Montrond/Duc d'Enghien/Grazianis |
| 2026-08-05 | 3-1.md | done | 20.9KB，卷三第I章；科斯莫别府邸夜归孤眠（首次尝孤独滋味、思父妹之隔）→晨与马泰尔医生同桌午餐长谈——医生自述二十年流浪（特兰西瓦尼亚三海杜克月夜之搏、犹太人毒香肠复仇）、论波佐·迪·博尔戈私仇之力与塔列朗讽拿破仑为「好品味之天生仇敌」，坎泰洛奇被唤来问意大利人何以爱拿破仑，答「是那个理想」；末段转医生视角：蒙特韦索伯爵引其入克莱莉娅病榻求逐「花花公鸡」（科斯莫）出热那亚，医生冷笑鄙夷，醒悟伯爵妒意方为真因；42.0KB 译文；exit=0，11 对 Original/Chinese，0 可疑错配；0 英文残留（括注术语 milord/Spire/Palazzo/Count Helion/Doctor Martel/Cantelucci/Mr. Latham/Latham Hall/Madrid/Moscow/Corsican/Transylvania/Haiduk/Bonaparte/Valence/Pozzo di Borgo/Elba/Talleyrand/Excellency/Signore/idea/Genoa/Livorno/Pollegrini/Count de Montevesso/Clelia/Marquis d'Armand/Boney/the Bourbons/Countess of Montevesso 均合规）；沿用 1-1~2-6 译名（Helion=海利翁伯爵，Clelia=克莱莉娅，Marquis d'Armand=达尔芒侯爵，Spire=斯帕尔，Doctor Martel=马泰尔医生，Cantelucci=坎泰洛奇），首现标注 Count de Montevesso/Talleyrand/Pozzo di Borgo/Countess of Montevesso/the Alliance/Alexander |
| 2026-08-05 | 2-7.md | done | 23.7KB，卷二第VII章（卷二终章）；前厅接续——老农妇（海利翁之姐）向伯爵诉说，引其上楼至偏僻旧宫深处，克莱莉娅（被传「中了邪」的侄女）僵卧床上、不肯作声；蒙特韦索伯爵（海利翁伯爵）支开众人与卡尔皮神父（Father Paul Carpi，诺维城开店人家出身、觊觎慈善机构主持神父之职）密谈——神权/帝权之议、厄尔巴岛拿破仑回返之谣、热那亚民心向法背皮埃蒙特；神父佯称「这是病」、提议请医，伯爵乘机欲私联方才同达尔芒侯爵议谈的医生，并从「欧洲营房到东方宫殿」的茫然里对克莱莉娅忽生父性柔肠；克莱莉娅爆发——痛斥黄发「女巫」舅母阿黛勒与众盛装贵妇、狂热告白今日所见英国青年「他真俊！我一定要把他弄到手」（呼应 2-3 奇遇），伯爵许以侯爵/伯爵亲事、嘱其缄默，神父与医生入门戛然收尾；47.6KB 译文；exit=0，20 对 Original/Chinese，0 可疑错配；0 英文残留（括注术语 Helion de Montevesso/Father Paul/Contessa/grandissimi signori/Bonsoir Abbé/Father Paul Carpi/Cosmo/M. le Comte/Monseigneur/M. le Marquis/Bernard/Patienza 及地名 Genoa/Rome/Paris/Vienna/Western Mediterranean/Novi 与政治用语 the Empire/the Revolution/Piedmontese、人名 Adèle 均合规）；自检移除 1 处不当括注（the Bishop 系普通名词头衔，非专有专名，已去括注）；沿用 2-2/2-4/2-6 译名（克莱莉娅=侄女、海利翁伯爵=舅父、阿黛勒=舅母、贝尔纳=仆、达尔芒侯爵=岳父）；补术语 Father Paul Carpi/Novi/the Bishop/Contessa/grandissimi signori/Maria/M. le Marquis（即达尔芒侯爵）/Patienza |
| 2026-08-05 | 3-3.md | done | 43.5KB，卷三第III章；马泰尔医生视角主线——科斯莫失踪（逃避旧画殉道圣女幻象出走）：坎泰洛奇入报，揭其烧炭党密谋者身份（侄女切卡之夫阿蒂利奥负文件南行，夜会切卡遭枪杀，密谋濒危）；医生与斯帕尔盘问（仆人因酒醉失察，约定候至四点）；医生独坐餐厅苦思蒙特韦索「妒夫」可怖之能事（暗喻科西嘉亡命徒/老农妇爪牙），决意走访鹰首狮身兽宫；入宫逢男仆睡卧，贝尔纳引见蒙特韦索夫人（侯爵病重不能见），呈交备忘录、自陈非卖力雇仆；夫人对宅中一切懵然若失林之童，医生以莱瑟姆之名试探并告失踪之事，夫人面窗惊问「您怀疑是一桩罪行」、自承「我惊骇万分」；克莱莉娅赤足闯入打断；末段贝尔纳阁楼探妻阿格莱——伦敦时多情天真的杂差已化作黑衣凝重老仆，阿格莱日受往事折磨而消瘦。85.0KB 译文；exit=0，23 对 Original/Chinese，0 可疑错配；自检修复 2 处英文残留（comparatively/aloud），1 处地名转译（Porto Ferraio→费拉约港）；沿用 1-1~3-2 译名（Cosmo=科斯莫，Adèle=阿黛勒，Spire=斯帕尔，Doctor Martel=马泰尔医生，Cantelucci=坎泰洛奇，Clelia=克莱莉娅，Bernard=贝尔纳，Aglae=阿格莱，Count Helion=海利翁伯爵，Marquis d'Armand=达尔芒侯爵，Madame de Montevesso=蒙特韦索夫人，Count de Montevesso=蒙特韦索伯爵，Mr. Latham=莱瑟姆先生，Elba=厄尔巴岛，Leghorn=里窝那，Yorkshire=约克郡，Genoa=热那亚，Jacobins=雅各宾派）；首现标注 the French Bourbons/St. Elmo/Checca/Attilio/Carbonari/ortolana/bestialita/poverino/milord/the Palazzo of the Griffins/Porto Ferraio/Madame la Comtesse/Monsieur de Jaucourt/Monsieur le Marquis/Adèle de Montevesso/Monsieur de Montevesso/Signorina Clelia/bergère/Le Jaloux/Molière |
| 2026-08-05 | 4-1.md | done | 86.3KB，卷四第I章（全书末章，康拉德未完成）；科斯莫夜归塔下遇密谋者低语→被巡警（巴博内一伙）误捕押往警卫室、拟渡港移交宪兵→港中阿蒂利奥（3-3 所传「遭枪杀」系误报，本章阿蒂利奥生还）率人驾舟劫救（船座板击昏二巡警、捞救落水老船夫）→藏双桅船头避海关十二桨大艇→逃出港湾、登接应三桅帆船；阿蒂利奥自述身世（南美海岸漂泊、平原隐士门徒、皮耶斯基家族、反多里亚家族密谋者血脉、信人人平等与意大利帝国、视厄尔巴岛上那个人为伟人皇帝）、力劝科斯莫随船 secret 出走里窝那方向（里维耶拉·迪·波南特本乡可护送回热那亚）；老船夫垂危仍掌舵「为整个意大利做一点事」、登帆船覆帆布而终；科斯莫问「我在这儿做什么」、阿蒂利奥答「他的星该是熄了——可谁又会因为它从天上熄了，便觉得少了什么呢？」收束（未完）；172.6KB 译文；exit=0，19 对 Original/Chinese，0 可疑错配，0 段落数错配；0 英文残留（括注术语 Genoa/Elba/Livorno/Casa Graziani/Paris/Piedmontese/Vienna/Riviera di Ponente/Count of Montevesso 及法意词 spadassin/sbirri/signore/Inglese/Permesso/Avanti/tartane/Voga, vecchio, voga/dogana/vecchio/giardiniera/furfante/ortolana/padrone/Per Dio/Va bene/Ah, Dio/Dio ne voglio/nobilissimo signore/milord Inglese/défaut d'armure/farouche/Excellency 与人名 Attilio/Cantelucci/Barbone/Pietro/Pieschi/Dorias/Cecchina/Madame de Montevesso 均合规）；首现标注 Attilio/Barbone/Cecchina/Pieschi/Dorias/Pietro/Casa Graziani/Riviera di Ponente；自检修复 1 处草稿英文残留（hardly）；卷四第I章标题「### I / I」；全书 15 章+4 卷名页（19 文件）译毕 |
