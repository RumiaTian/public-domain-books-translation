# 翻译计划（《幻境》——乔治·麦克唐纳）

## 本计划信息

- **项目名称**：《幻境》（George MacDonald, *Phantastes: A Faerie Romance for Men and Women*, 1858）
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

按 `prompts/翻译计划模板.md`「执行步骤」9 步推进（读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志）。本内容形态为「长篇」，走委派模式，每篇下沉到一次性子代理执行。

## 篇目清单

共 25 章（罗马数字 I–XXV，章名仅罗马数字、无英文标题），外加卷首三则合并题词。详见 `translation_queue.csv`。

| # | 章 | 源文 | 大小 | 状态 |
|---|----|------|------|------|
| 0 | 卷首题词（斯宾塞／诺瓦利斯／门与窗） | 00-epigraphs.md | 1.4KB | todo |
| I | | chapter-1.md | 8.1KB | todo |
| II | | chapter-2.md | 3.3KB | todo |
| III | | chapter-3.md | 24.2KB | todo |
| IV | | chapter-4.md | 20.5KB | todo |
| V | | chapter-5.md | 15.3KB | todo |
| VI | | chapter-6.md | 14.6KB | todo |
| VII | | chapter-7.md | 16.0KB | todo |
| VIII | | chapter-8.md | 7.2KB | todo |
| IX | | chapter-9.md | 12.5KB | todo |
| X | | chapter-10.md | 15.3KB | todo |
| XI | | chapter-11.md | 12.2KB | todo |
| XII | | chapter-12.md | 14.2KB | todo |
| XIII | （Cosmo's Story 故事中故事） | chapter-13.md | 45.0KB | todo |
| XIV | | chapter-14.md | 13.7KB | todo |
| XV | | chapter-15.md | 7.3KB | todo |
| XVI | | chapter-16.md | 3.2KB | todo |
| XVII | | chapter-17.md | 9.9KB | todo |
| XVIII | | chapter-18.md | 9.1KB | todo |
| XIX | | chapter-19.md | 32.4KB | todo |
| XX | | chapter-20.md | 17.2KB | todo |
| XXI | | chapter-21.md | 10.4KB | todo |
| XXII | | chapter-22.md | 16.0KB | todo |
| XXIII | | chapter-23.md | 26.0KB | todo |
| XXIV | | chapter-24.md | 6.5KB | todo |
| XXV | | chapter-25.md | 6.2KB | todo |

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
| 2026-09-10 | chapter-2.md（第二章） | 3 对双语块，check_bilingual 通过（exit 0） | 诺瓦利斯德语题词按「两存之」原则在译文块保留原样、语义由英译行中译承载；Fairy Land=仙境、罗马数字章名照搬；本篇为全书首批译文之一，风格基调（诗意典雅）已立 |
| 2026-09-10 | 00-epigraphs.md（卷首三则题词） | 3 对双语块，check_bilingual 通过（exit 0） | 新书首篇：斯宾塞诗体题词保留分行镜像，诺瓦利斯德语题词（无英译附文）径以典雅中文译出，古英语题词以带古意中文传达；Phantastes 首现标注原文、依术语表作「幻境」 |
| 2026-09-10 | chapter-1.md（第一章） | 9 对双语块，check_bilingual 通过（exit 0，可疑错配 0 处） | 首章立基调：章首柯尔律治式诗体题词逐行镜像；术语全数落位（secretary=书桌、Fairy Land=仙境、Anodos=阿诺多斯、Uncle Ralph=拉尔夫叔父，均首现附原文）；小妇人化形为白衣淑女一段叙事抒情节奏照原样保留；章名罗马数字照搬，标题合并为「I / 第一章」 |
| 2026-09-10 | chapter-4.md（第四章） | 13 对双语块，check_bilingual 通过（exit 0，可疑错配 0 处） | 中古英语题词「When bale is att hyest, boote is nyest」以带古意中文传达；山毛榉女神之歌分行镜像；术语落位：the Ash=梣树、beech-tree=山毛榉、goblin=妖怪、gnomes=地精、Fairy Land=仙境；梣树手影／尸面／贪眼等魔影先声段保留原文阴郁质感；源文内嵌 U+FEFF 杂符在对照镜像中剔除 |
| 2026-09-10 | chapter-5.md（第五章） | 10 对双语块，check_bilingual 通过（exit 0，可疑错配 0 处） | 斯宾塞诗体题词与中古英语联句（Sche was as whyt as lylye yn May）逐行镜像、以带古意中文传达；唤大理石少女三首歌分行镜像源文「单空格行＋空行」结构；术语落位：antenatal tomb=未生之墓、alabaster=雪花石膏、Pygmalion=皮格马利翁、Ariel=爱丽儿、Niobe=倪俄柏、Orpheus=俄耳甫斯（均首现附原文）、the lady of the beech-tree=山毛榉女神；源文内嵌 U+FEFF 杂符在对照镜像中剔除 |
| 2026-09-10 | chapter-6.md（第六章） | 13 对双语块，check_bilingual 通过（exit 0，可疑错配 0 处） | 诺瓦利斯德语题词依 chapter-2 体例原样两存、附英译径译中文；「Thy red lips」残句与唤白衣女郎之歌均逐行镜像源文「单空格行＋空行」结构；术语落位：Sir Percival=珀西瓦尔爵士、the Maiden of the Alder-tree=赤杨树少女（均首现附原文）、the marble lady=大理石少女、girdle of beech-leaves=山毛榉叶腰带、the Ash=梣树、Gorgon-head=戈耳工之头；锈甲骑士段以阴郁典雅色调呼应第四章梣树宿怨；源文内嵌 U+FEFF 杂符剔除 |
| 2026-09-10 | chapter-8.md（第八章） | 5 对双语块，check_bilingual 通过（exit 0，可疑错配 0 处） | 歌德《浮士德》式德语题词依 chapter-2/6 体例：原文块德英两存，译文块德语原样保留、中译由英译行承载；老妪黑暗独白的古体英语（abideth/doth/yea）以带古意中文传达；「眼睛与对象进入真实的关系」「趋近迅疾而抵达迟迟」等奇诡段落保留原文哲思质感；魔影初附按未定名阶段统一作「影子」，与术语表「自第十一章起方为魔影」的分期一致；食人妖（ogre）满口白牙的揭示段落保留惊悚顿悟节奏 |
| 2026-09-11 09:11 | chapter-3 | 29对 | [1308]额度中断前已落盘，主Agent过检代验收回填done |
| 2026-09-10 | chapter-11.md（第十一章） | 8 对双语块，check_bilingual 通过（exit 0，可疑错配 0 处） | 自本章起影子按术语表分期定名「魔影」，「Shadow of me!」呼语作「我这属身的魔影」，『shadow of light/shadow of darkness』泛指处保留「影子」以存光影对仗；华兹华斯体题词七行逐行镜像并保留 high/Uplifted 跨行；术语落位：Queen of Fairy Land=仙国女王、the fairy bath=仙家浴池、porphyry=斑岩、jasper=碧玉、lapis lazuli=青金石、agate=玛瑙、mile=英里照搬原词、alabaster=雪花石膏；藏书室「读即代入」段保留哲思质感；源文内嵌 U+FEFF 杂符剔除 |
| 2026-09-11 09:21 | chapter-10.md（第十章） | 10 对双语块，check_bilingual 通过（exit 0，可疑错配 0 处） | 麦克唐纳自作诗体题词四行逐行镜像源文「单空格行＋空行」结构；影子按第八章既定分期：本章魔影仍属身未脱，统一作「影子」，泛指树影同；术语落位：goblin-fairies=妖怪仙灵、the Spirit of the Earth=大地之灵、the Church of Darkness=黑暗教堂（均首现附原文）、the fairy palace=仙宫、The Chamber of Sir Anodos=阿诺多斯爵士之室（铭文加粗保留）；porphyry=斑岩与第十一章一致；倒影与魔镜议论段保留原文哲思质感 |
| 2026-09-11 09:22 | chapter-9.md（第九章） | 8 对双语块，check_bilingual 通过（exit 0，可疑错配 0 处） | [1308]断点重派，前次子代理额度中断未落盘，本次从头完整翻译；柯尔律治《抑郁颂》诗体题词按既定「单空格行＋空行」结构分行镜像；影子按第十一章前分期统一作「影子」（魔影零出现）；术语落位：Fairy Land=仙境、palace of Fairy Land=仙宫、Alder-maiden=赤杨树少女（承第六章）、armor/mail=甲胄/锁子甲、closet=壁橱、focal distance=焦距；源文 10 处 U+FEFF 杂符剔除；少女晶球段落保留原文哀恸复沓节奏 |
| 2026-09-11 09:23 | chapter-7.md（第七章） | 15 对双语块，check_bilingual 通过（exit 0，可疑错配 0 处） | [1308]断点重派，前次子代理额度中断未落盘，本次从头完整翻译；安德鲁爵士歌谣题词的中古英语拼写（sayes/Ime/slain/againe）按既定「单空格行＋空行」结构逐行镜像、以带古意中文传达；术语落位：Fairy Land=仙境、the lady of the marble=大理石少女（承第五六章）、the Ash=梣树、the white lady=白衣女郎、Hop-o'-my-Thumb=小拇指（首现附原文）、mile=英里照搬原词、Midsummer-eve=仲夏前夜、The History of Graciosa and Percinet=《格蕾西奥莎与珀西内的故事》（首现附原文）；农家晚宴对白按人物口吻分流（农夫憨谐、其子讥诮、小姑娘稚气）；源文内嵌 U+FEFF 杂符剔除 |
| 2026-09-11 09:30 | chapter-14.md（第十四章） | 11 对双语块，check_bilingual 通过（exit 0，可疑错配 0 处） | 莎翁《泰尔亲王佩力克尔斯》五行题词逐行镜像（罗马数字章名照搬「## XIV / 第十四章」体例；源文题词行内杂散空白归一）；术语落位：fairy palace=仙宫、the white lady=白衣女郎、marble beauty/marble queen 承「大理石」、my lady of the cave=我的岩穴女郎、alabaster=雪花石膏、demon/missing demon 统一「魔影」、Touch Not!=勿触！（金字铭文保留引块）；十二石像厅、梦的揭示与空基座诸段保留神秘感知与哲思质感；源文 1 处 U+FEFF 杂符剔除 |
| 2026-09-11 09:34 | chapter-15.md（第十五章） | 19 对双语块，check_bilingual 通过（exit 0，可疑错配 0 处） | 全章主体为一首 128 行自作颂歌（16 组八行诗节），逐行镜像源文「单空格行＋空行」结构、组间直连；标题照搬「## XV / 第十五章」体例；术语落位：Isis=伊西丝（首现附原文）、Pan=潘神（首现附原文）、statue-halls=雕像之殿、presence 统一「临在」，承第十四章空基座白足光晕与舞群石像化意象；斜体强调（*Dumb art thou?*／*me*）中文镜像保留；源文 3 处 U+FEFF 杂符剔除 |
| 2026-09-11 09:36 | chapter-12.md（第十二章） | 24 对双语块，check_bilingual 通过（exit 0，可疑错配 0 处） | 章首题词与书中两首长诗逐行镜像，源文「单空格行＋空行」OCR 痕迹归一为紧凑引块（与第十一章体例一致）；罗马数字章名照搬「## XII / 第十二章」体例；无翼女人／不映影之水／蛋形穹天等意象沿用前章「仙家浴池」「仙国女王」语汇；snowdrop=雪花莲；源文 U+FEFF 杂符剥离 |
| 2026-09-10 | chapter-16.md（第十六章） | 2 对双语块，check_bilingual 通过（exit 0，可疑错配 0 处） | 德语题词（歌德《普洛塞庇娜》，附英译）依 chapter-2/6/8 体例：原文块德英两存、译文块德语原样保留、中译由英译行承载（四行对四行镜像）；罗马数字章名照搬「## XVI / 第十六章」体例；源文题词杂散空白行与 2 处 U+FEFF 杂符剔除归一（承 chapter-14 黄金样本）；术语落位：fairy palace=仙宫、the white lady=白衣女郎、statue/pedestal=石像/基座（承十四章）、corridor=长廊、the Queen=女王；「你不该碰我！」嗔责、石门穿丘与无门荒丘墓碑的骤变段落保留原文急转节奏 |
| 2026-09-11 09:52 | chapter-13.md（第十三章·科斯莫的故事） | 32 对双语块，check_bilingual 通过（exit 0，可疑错配 0 处） | 45KB 大章按场景 17 分片 append-only 落盘后合并；题词（I saw a ship 情歌两节）承 ch11/12 体例归一为紧凑引块逐行镜像；罗马数字章名照搬「## XIII / 第十三章」体例；嵌入故事叙事口吻独立：术语落位 Cosmo von Wehrstahl=科斯莫·冯·韦尔施塔尔（首现附原文）、University of Prague=布拉格大学、Albertus Magnus=大阿尔伯特、Cornelius Agrippa=科内利斯·阿格里帕、Princess von Hohenweiss=冯·霍恩魏斯公主、von Steinwald=冯·施泰因瓦尔德、Lisa=莉莎、Moldau=伏尔塔瓦河（首现均附原文）、the mirror 统一「魔镜」、the couch 统一「长榻」、charmed circle=法圈；「如对着镜子观看，模糊不清」保留哥林多前书典故语感；源文 3 处「---」场景分隔对应保留；挥剑砸镜、霹雳夺镜、桥上月下死别诸段保留急转节奏与挽歌质感 |
| 2026-09-10 | chapter-18.md（第十八章） | 6 对双语块，check_bilingual 通过（exit 0，可疑错配 0 处） | 9.1KB 小章一次成文；题词德（诺瓦利斯）英两存，逐行照原文散行格式镜像（空格行保留）；罗马数字章名照搬「## XVIII / 第十八章」体例；术语落位：the white lady=白衣女郎、Fairy Land=仙境、the beech-tree=山毛榉、the goblin Selfishness/the angel Love=「自私」这妖怪／「爱」那天使；无数字锚点问题，源文弯引号与 3 处 U+FEFF 原样保留 |
| 2026-09-11 09:49 | chapter-17.md（第十七章） | 16 对双语块，check_bilingual 通过（exit 0，可疑错配 0 处） | 德语题词（歌德，附英译）依 chapter-2/6/8/16 体例：原文块德英两存、译文块德语原样保留、中译由英译行承载（四行对四行镜像，源文「单空格行＋空行」诗节结构照搬）；罗马数字章名照搬「## XVII / 第十七章」体例；妖怪拟唱的嘲弄歌与两首自作劝慰歌谣（四节＋三节）逐行镜像；术语落位：the white lady=白衣女郎、fairy palace=仙宫、white hall of Phantasy=幻想的白殿（承十五章）、goblins=妖怪、august presence 承「临在」、Kobolds=科博尔德（首现附原文）、Anodos=阿诺多斯（本章首现附原文）；妖怪哄笑群像与丑妇美颜骤变两场保留怪诞与急转节奏；源文 3 处 U+FEFF 杂符剔除 |
2026-09-10 | chapter-19.md | 64 对双语块 | 通过（exit 0，可疑错配 0 处） | 罗马数字章名照搬「## XIX / 第十九章」体例；诺瓦利斯德语题词依 chapter-2/6/8/16 体例两存之（德语原样保留、中译由英译行承载）；152 行民谣（Sir Aglovaile 与鬼新娘）逐行镜像、叠句斜体保留、行首悬挂引号照搬；术语落位：Fairy Land=仙境、the red mark=红色印记、the door of Dismay=畏惧之门、the door of Sighs=叹息之门（首现附原文）、the door of the Timeless=无时之门（首现附原文）、the knight of the soiled armor=铠甲蒙尘的骑士（首现附原文）、Sir Aglovaile=阿格洛维尔爵士（首现附原文）、Adelaide=阿德莱德（首现附原文）；方屋四门（第二/三/四门）、谷仓人间插曲、镜前会客厅、宗族墓穴教堂诸场与五首安慰短歌全部译出；源文「单空格行＋空行」诗节结构规范化为连续 > 诗行 |
| 2026-09-10 | chapter-21.md（第二十一章） | 12 对双语块，check_bilingual 通过（exit 0，可疑错配 0 处） | 罗马数字章名照搬「## XXI / 第二十一章」体例；圣经式题词（I put my life in my hands）单行镜像；终曲歌五节逐行镜像，源文「单空格行＋空行」诗节结构依 ch11/12 体例归一为紧凑引块，首末两节 pain/noise of life 之异文照原样保留；术语落位：the giants=巨人、the Shadow=魔影（承十一章后定名，章首「旧魔影」呼应其复返）、Fairy Land=仙境、Sir Gawain=高文爵士（首现附原文）、mare's sons=母马之子（高文爵士典故直译存典）、princes=两位王子、rapier=细剑、sabre=马刀、battle-axe=战斧、two-handed sword=双手大剑、mace=钉头锤（首现附原文）、gorget/cuirass=护喉/胸甲、dub me knight=册封骑士、the lists=武斗；对话引号用「」；源文 1 处 U+FEFF 杂符剔除 |
2026-09-10 | chapter-22.md（第二十二章） | 11 对双语块，check_bilingual 通过（exit 0，可疑错配 0 处） | 罗马数字章名照搬「## XXII / 第二十二章」体例；章首德语题词（Niemand hat meine Gestalt als der *Ich*.，附英译）依 chapter-2/6/8/16/19 体例：原文块德英两存，译文块德语原样保留、中译由英译行承载；两首歌谣（大地母亲之歌 30 行、别歌 8 行两节）逐行镜像，源文「单空格行＋空行」OCR 痕迹归一为紧凑引块（承 ch11/12 体例）；术语落位：Fairy Land=仙境、the Shadow=魔影（承十一章后定名）、the Fairy Queen=仙国女王、the woman of the beech-tree=山毛榉女神（承第四章）、the giants=巨人、Sir Galahad=加拉哈德爵士（首现附原文）、globe=玻璃球（首现附原文）；对话引号用「」；镜面骑士囚塔、褪甲去骑士号、「但愿丢失的是我的魔影」与章末三问诸段保留原文哲思质感；源文无 U+FEFF 杂符
2026-09-10 | chapter-20.md（第二十章） | 15 对双语块，check_bilingual 通过（exit 0，可疑错配 0 处） | 罗马数字章名照搬「## XX / 第二十章」体例；章首斯宾塞《仙后》双节古体题词（hadst/doth/hart/vertuous 等古拼写）逐行镜像、以带古意中文传达；章中两首自作歌谣（国王与独子十节、贵妇三节）依 ch11/12 体例将源文「单空格行＋空行」诗节结构归一为紧凑引块逐行镜像，歌中跨行台词行首悬挂引号归一；对话引号用「」、转述内引语用『』，长者转述智者妇人一节多段未闭合引号按源文样式照搬；术语落位：the giants=巨人、wise woman in the cottage=智慧老妪（承方屋一线）、turret=角楼、isthmus=地峡（承第十九章）；锻炉铸剑、镜中示人、双歌连泪诸段保留原文叙事质感；源文 2 处 U+FEFF 杂符剔除

2026-09-10 | chapter-23.md（第二十三章） | 30 对双语块 | 通过（exit 0，可疑错配 0 处） | 罗马数字章名照搬「## XXIII / 第二十三章」体例；章首双题词（锡德尼箴言单行、罗伊顿悼锡德尼四行古体诗 kinde/lookes）逐行镜像、以带古意中文传达；骑士战歌六节 24 行逐行镜像、归一为紧凑引块（承 ch11/12 体例）；26KB 较大章按场景 4 分片 append-only 落盘后合并；术语落位：the knight of the soiled armor=铠甲蒙尘的骑士（承第十九章既定译名，首现附原文）、the lady of the marble=大理石少女（承第五六七章）、the white lady=白衣女郎、squire=侍从、battle-axe=战斧（承第二十一章）、hermit=隐士（首现）、yew=紫杉（首现）；「 Knight and squire must share the labor」内转述引语用『』；源文题词与歌谣「单空格行＋空行」结构归一，第 79-118 行段界缺失的连排长段按对白边界重新分段并使原文块与译文块逐段对齐；无两位以上数字锚点，源文 3 处 U+FEFF 杂符剔除
2026-09-10 | chapter-25.md（第二十五章·终章） | 5 对双语块，check_bilingual 通过（exit 0，可疑错配 0 处） | 全书末章；罗马数字章名照搬「## XXV / 第二十五章」体例；章首诺瓦利斯德语题词（附英译）依 chapter-2/6/8/16/19 体例两存之：译文块德语原样保留、中译由英译行承载；中古英语题词（modres gate/knocke/Leve mother，《农夫皮尔斯》体古拼写）逐行镜像、以带古意中文传达；术语落位：Fairy Land=仙境、the Shadow=魔影（终章得脱）、my Ideal=我的「理想」（全题主旨句「出门寻理想、失魔影而归」）、the castle=城堡、my sisters=妹妹们（归来迎接）、the wise woman/the ancient woman=智慧老妪、the cottage（four-square）=方屋、the door of Dismay=畏惧之门、the red mark/the red sign=红色印记、beech-tree=山毛榉、Anodos=阿诺多斯（承首章，不再括注）；内转述引语用『』、斜体 *Farewell* 镜像作「*别了*」；源文题词区「单空格行＋空行」结构与 U+FEFF 杂符归一剔除
2026-09-10 | chapter-24.md（第二十四章·死亡之章） | 8 对双语块，check_bilingual 通过（exit 0，可疑错配 0 处） | 罗马数字章名照搬「## XXIV / 第二十四章」体例；章首双题词（单行箴言 We are ne'er like angels till our passions die ＋十行论死亡与言说之诗 This wretched Inn…）逐行镜像，源文「单空格行＋空行」结构依 chapter-23 体例照搬（> 首行＋前导空格行），斜体强调（*Inn*/*Dwelling-Place*/*Step*/*Race*/*Live*/*Be*/*things*/*words*/*pictures* 与两处 *Behold…*）中文镜像保留；术语落位：the knight=骑士、the lady=女郎（承第二十三章）、primrose=报春花（承第三四章）、bluebell=蓝铃花（首现）、the land of Death=死亡之国、the realms of lofty Death=崇高的死亡之疆域、the helpers=帮助者们（首现）；对话引号用「」；阿诺多斯死后续在（棺中听葬、入报春花得吻、云端悟爱与飘临城池）诸段保留挽歌与沉思质感，章末「重返肉身」骤转节奏照原文；源文 2 处 U+FEFF 杂符（chariot 段破折号旁）剔除归一

2026-09-10 | 整书完结（26/26 篇全部 done） | 批次1 删锁流转 | 全书体例：罗马数字章名合并单行「## XX / 第XX章」；外语题词两存之（原文块原样保留、中译由英译行承载）；歌谣「单空格行＋空行」结构归一为紧凑引块逐行镜像；对话引号「」、转述内引语『』。核心术语：Anodos=阿诺多斯、Fairy Land=仙境、the Shadow=魔影、the white lady=白衣女郎、the cottage（four-square）=方屋、the wise woman=智慧老妪、the door of Dismay=畏惧之门、the red mark=红色印记、the beech-tree=山毛榉、the knights of the soiled armor=铠甲蒙尘的骑士
