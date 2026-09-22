# 翻译计划（克拉克·阿什顿·史密斯短篇科幻奇幻集）

## 本计划信息

- **项目名称**：克拉克·阿什顿·史密斯短篇科幻奇幻集
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

按 `prompts/翻译计划模板.md`「执行步骤」9 步推进（读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志）。本集为短篇集，走委派模式：主 agent 调度，子代理逐篇执行。注意 marooned-in-andromeda（68.5KB）、the-end-of-the-story（40.0KB）为长文，子代理须按通用翻译引擎第七节分段产出、严防末尾截断。

## 篇目清单

| # | 篇名 | 源文 | 大小 | 题材 |
|---|------|------|------|------|
| 1 | The Malay Krise | the-malay-krise.md | 4.5KB | 马来冒险 |
| 2 | The Ghost of Mohammed Din | the-ghost-of-mohammed-din.md | 14.7KB | 印度怪奇 |
| 3 | The Mahout | the-mahout.md | 13.4KB | 印度冒险 |
| 4 | The Raja and the Tiger | the-raja-and-the-tiger.md | 13.3KB | 印度冒险 |
| 5 | The Last Incantation | the-last-incantation.md | 10.8KB | 波塞冬尼斯·奇幻 |
| 6 | The Abominations of Yondo | the-abominations-of-yondo.md | 14.4KB | 怪奇 |
| 7 | The Ninth Skeleton | the-ninth-skeleton.md | 10.3KB | 怪奇 |
| 8 | The End of the Story | the-end-of-the-story.md | 40.0KB | 阿维罗涅·奇幻（长文） |
| 9 | Sadastor | sadastor.md | 7.3KB | 怪奇·神话 |
| 10 | The Phantoms of the Fire | the-phantoms-of-the-fire.md | 11.5KB | 边疆怪谈 |
| 11 | Marooned in Andromeda | marooned-in-andromeda.md | 68.5KB | 科幻（长文） |
| 12 | The Uncharted Isle | the-uncharted-isle.md | 24.2KB | 怪奇 |

> 篇目顺序见 `translation_queue.csv`（gen_project_files 按自然键排序）。

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-08-12 | - | 建项目 | 从 待翻译/clark-ashton-smith_short-fiction.epub 提取 12 篇正文、建术语表初版（含阿维罗涅/许珀玻瑞亚/波塞冬尼斯/雍多等架空世界译名）、生成队列 |
| 2026-08-12 | the-malay-krise (8978B,9对块) | done | exit 0; 委派子代理。首篇黄金样本,定巴洛克颓靡怪奇风格基线(适度平衡早期冒险题材叙事节奏) |
| 2026-08-12 | sadastor (15663B,9对块) | done | exit 0; 委派子代理。恶魔沙尔纳迪斯给塞壬利斯皮尔讲故事;神话专名(拉弥亚/塞壬/蛇怪/曼陀罗/塔耳塔洛斯/皮同)遵表 |
| 2026-08-12 | the-ghost-of-mohammed-din (30233B,21对块) | done | exit 0; 委派子代理(自行补术语表)。新词:Ali Bagh 阿里·巴格/Hyderabad 海得拉巴/Bombay 孟买/charpoy 查尔帕伊绳床/punkah 布风扇 等 |
| 2026-08-12 | the-mahout (27524B,21对块) | done | exit 0; 委派子代理。新词:ankus 象钩/howdah 象舆/musth 狂象之症/Kshatriya 刹帝利。注:Raja 作象名时译「拉贾」、作头衔时译「王公」消歧 |
| 2026-08-12 | the-ninth-skeleton (21596B,15对块) | done | exit 0; 委派子代理(自行补术语表)。新词:Guenevere 桂妮薇儿/Eld 洪荒/witches' sabbat 巫魔夜会 |
| 2026-08-12 | the-abominations-of-yondo (29959B,18对块) | done | exit 0; 委派子代理。新词:Ong 昂(狮首之神)/mysteriarchs 秘仪教长/hashish-dream 哈希什迷梦/charnel-house 藏骨堂/lich 尸鬼。建议 Ong=昂 补入术语表神祇条目 |
| 2026-08-13 | the-phantoms-of-the-fire (24116B,21对块) | done | exit 0; 委派子代理。加州边疆怪谈,写实散文+乡村口语对白(Gosh/wuz/ye 等)。新词:Samuel Slocum 塞缪尔·斯洛克姆/Bill 比尔(乔纳斯幼子)/El Dorado 埃尔多拉多/Mission·Muscat 弥赛·麝香葡萄/manzanita 熊果木。源文"A man in calico"按上下文(后文 her/女人/玛蒂尔达)判为 woman 之误植,译作女人 |
| 2026-08-13 | the-last-incantation (10.8KB,8对块) | done | exit 0; 委派子代理。波塞冬尼斯死灵法师马利格里斯召亡记;专名(Malygris 马利格里斯/Nylissa 妮莉莎/Susran 苏斯兰/Meros 梅罗斯/Zemander 泽曼德/Poseidonis/Hyperborea/Atlantis/Lethe 忘川)遵表。法器词:cockodrill 鳄鱼/crotali 响板/thuribles 香炉/pentacles 五芒星/philtre 迷情之剂/electrum 琥珀金/balas-rubies 巴拉斯红宝石。源文"too subtle to he named"按 he→be 误植译。无新术语表补词 | |
| 2026-08-13 | the-raja-and-the-tiger (13595B,20对块) | done | exit 1(数字锚点误报,120°/98°译为华氏一百二十/九十八度); 委派子代理。印度冒险:英国驻扎官本特利遭王公琼布·辛格推下深渊谋害,反被猛虎所救、王公自食其果。遵表术语(Bently/Chumbu Singh/Lal Das/Shaitanabad/Nahargarh/Rajput/Raja/Sahib);新词:British Resident 英国驻扎官/gadi 加迪(宝座)/kinkhab 金卡布/Jain 耆那教/Arhat 阿罗汉/nullah 干沟/peristyle 列柱廊 |
| 2026-08-13 | the-uncharted-isle (24.2KB,30对块) | done | exit 0; 委派子代理。太平洋时空错位孤岛怪谈:大副马克·欧文海难漂流至海图未载之岛,遇迷失族群(浑天仪/星盘/历象碑/古海图)与活体神像献祭,携桨逃归无人置信。遵表术语(Mark Irwin/Captain Melville/Callao/Wellington/Easter Island/Lemuria/Mu/armillary/astrolabe/parapegm/fern-palm/cycad/araucaria);新词:Southern Cross 南十字座/calenture 发热性谵妄/Tyrian 推罗紫/Mongolian 蒙古人种/limbo 林勃狱 |
| 2026-08-13 | marooned-in-andromeda (68.5KB,47对块) | done | exit 1(数字锚点误报:7个罗马数字章节标题 I–VII 按术语表"罗马数字照搬不译"留原样,故无"/"分隔,核验后可接受); 委派子代理,按§7分7段写入(标题+第I章/II/III/IV/V/VI/VII)。早期星际科幻:沃尔马船长将三名叛变者罗弗顿·戴明·亚当斯弃于仙女座δ行星,历食肉植物·独眼侏儒·多嘴多眼潭怪·巨囊鸟·植物克拉肯诸劫,亚当斯葬身草木怪物,终由悔悟的沃尔马接回。遵表术语(Roverton/Deming/Adams/Volmar/Andromeda);新词:Alton Jasper 阿尔顿·贾斯珀(大副/天文学家)/Delta Andromedae 仙女座δ/Alpha Centauri 半人马座α/Allen Farquhar 艾伦·法夸尔/space-flier 飞船/pterodactyl 翼手龙/anaconda 水蚺/kraken 海怪克拉肯/Noctiluca 夜光虫/Animaculae 微小生物 |
| 2026-08-13 | the-end-of-the-story (40.0KB,41对块) | done | exit 1(数字锚点误报:1798年份,译文作"1798年11月"含原数字,核验后可接受); 委派子代理。补全截断结尾(首译触[1301]中断,译文在第137行"As I entered the grove..."处截断,补译第143–193行共15对块:妮赛娅宫殿/拉弥亚真相/希莱尔驱魔/穆兰写下记述/计划重返伪焰堡)。遵表术语(佩里贡/伪焰堡/妮赛娅/希莱尔/穆兰/阿维罗涅/维奥纳/拉弥亚);新词:Nycea 妮赛娅/Apollonius of Tyana 提亚纳的阿波罗尼乌斯/aspergillus 洒圣水器/Doric 多立克/onyx 缟玛瑙/porphyry 斑岩 |
