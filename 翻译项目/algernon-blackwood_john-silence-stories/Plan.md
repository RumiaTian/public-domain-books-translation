# 翻译计划（阿尔杰农·布莱克伍德《约翰·寂静医生的故事》）

## 本计划信息

- **项目名称**：《约翰·寂静医生的故事》（Algernon Blackwood, John Silence Stories）
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

按 `prompts/翻译计划模板.md`「执行步骤」9 步推进（读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志）。委派模式下由主 agent 派子代理逐篇执行。

## 篇目清单（依原书 spine 顺序 Case I–VI）

| # | Case | 篇名 | 源文 | 大小 | 状态 |
|---|------|------|------|------|------|
| 1 | I | A Psychical Invasion | a-psychical-invasion.md | 113.8KB | todo |
| 2 | II | Ancient Sorceries | ancient-sorceries.md | 104.3KB | todo |
| 3 | III | The Nemesis of Fire | the-nemesis-of-fire.md | 155.5KB | todo |
| 4 | IV | Secret Worship | secret-worship.md | 74.3KB | todo |
| 5 | V | The Camp of the Dog | the-camp-of-the-dog.md | 153.3KB | todo |
| 6 | VI | A Victim of Higher Space | a-victim-of-higher-space.md | 43.2KB | todo |

合计 6 篇，约 644.4KB。（状态由 `translation_queue.csv` 管理，此表为阅读参考。）

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-08-12 | — | 建项目 | 从 待翻译/algernon-blackwood_john-silence-stories.epub 提取 6 篇正文、建术语表初版、生成队列。短篇集，委派模式。 |
| 2026-08-13 | A Victim of Higher Space (a-victim-of-higher-space.md) | done，exit 0 | 43.2KB 长篇，分 4 段译（开篇接待+绿色书房／窥孔观察+马奇登场／马奇自述身世与高维经历／诊断+堵入口+唐豪瑟乐队+消失+电报）。check_bilingual.py 100 标记块（50 对 Original/Chinese），0 错配；完整性核对 140/140 段对齐。术语补充：窥孔(spyhole/peephole)、马厩巷(stable mews)、麻醉按钮(narcotic buttons)、德国乐队(German band)、白兰地(brandy)。本项目首篇完成译文，作为后续黄金样本对齐。 |
| 2026-08-13 | Secret Worship (secret-worship.md) | done，exit 1（数字锚点误报，已核验可接受） | 74.3KB 长篇，分 2 段译（哈里斯怀旧归校+秘密崇拜仪式至昏倒／废墟醒来+约翰·寂静护送揭秘+签名）。check_bilingual.py 92 标记块（46 对 Original/Chinese），标题合并格式满足；2 处可疑错配均为年份 '70→七〇年 的数字锚点误报，内容配对正确。术语补充：哈里斯(Harris)、卡尔克曼弟兄(Bruder Kalkmann)=Man of Chalk 白垩之人、施利曼/帕格尔/迈尔/吉辛等弟兄、阿斯莫德利乌斯(Asmodelius)=Hauptbruder 首席弟兄、Opfer（献祭/牺牲，关键剧情词保留德文原形）、索默劳(Sommerau)、霍恩贝格(Hornberg)、符腾堡/巴登、馈赠节(Beschehr-Fest)、弟兄室(Bruderstube)、玫瑰十字团(Rosicrucian)、空壳(shells)、加利利(Galilee)。Case IV 篇题罗马数字照搬。 |
| 2026-08-13 | Ancient Sorceries (ancient-sorceries.md) | done，exit 1（数字锚点误报，已核验可接受） | 104.3KB 超长篇，分 5 段译（标题+第I节火车下车入城+猫之气息／第II+III节全城窥伺+走廊邂逅+伊尔丝登场／第IV节伊尔丝引导+古城揭秘+前世公主女王幻象／第V节巫魔夜会+变猫+火逃／第VI节逃生自述+寂静医生考证巫术历史）。check_bilingual.py 166 标记块（83 对 Original/Chinese），标题合并格式满足；1 处可疑错配为年份 1700→一七〇〇年 的数字锚点误报，内容配对正确。术语补充：亚瑟·维赞(Arthur Vezin)、伊尔丝(Ilsé)、瑟比顿(Surbiton)、圣马丁教堂(St. Martin)、伊扎德(Iszard)、明斯基(Minski)、巫魔夜会(Witches' Sabbath)、变狼术(Lycanthropy)、马鞭草(vervain)、芸香(rue)、À cause du sommeil et à cause des chats（因为睡眠，也因为猫，关键警句保留法语原形）、salle à manger/religieuses 等法语保留。Case II 篇题罗马数字照搬。 |
| 2026-08-13 | The Camp of the Dog (the-camp-of-the-dog.md) | done，exit 0 | 153.3KB 超长篇，分 7 段译（标题+第I节登岛+人物登场+琼的不安预感／第II节营地日常+桑格里变野／第III节前半犬嚎+爪印+琼求留／第III节后半帐篷撕裂+围猎+夜观+决意电召寂静医生／第IV节寂静医生抵达+航海论"二重身"／第V节前半变狼症(lycanthropy)详解+维尔狼+反噬／第V节后半海雾之夜+狼人显形+琼梦游相迎+马洛尼开枪+反噬瘀伤+黎明团圆）。check_bilingual.py 256 标记块（128 对 Original/Chinese），标记成对满足、标题合并格式满足、0 错配。术语补充：琼·马洛尼(Joan Maloney)、蒂莫西·马洛尼牧师(Rev. Timothy Maloney)、彼得·桑格里(Peter Sangree)、哈伯德(Hubbard,叙述者)、瓦克斯霍尔姆(Waxholm)、斯凯戈德(Skägård)、副水手长(Bo'sun's Mate,马洛尼夫人营地绰号)、二重身(Double)、星光体(astral body)、欲望之身/情欲之身/微妙之身(Body of Desire/Passion Body/Subtle Body)、变狼症(lycanthropy)、狼人(werewolf)、维尔狼(Wehr Wolf)、反噬(repercussion)、僵厥(cataleptic)、梦游(somnambulism)、红皮肤印第安人(Red Indian)。Case V 篇题罗马数字照搬。 |
| 2026-08-13 | A Psychical Invasion (a-psychical-invasion.md) | done，exit 1（数字锚点误报，已核验可接受） | 113.8KB 超长篇，分 6 段译（标题+第I节西文森夫人引荐+寂静医生背景+登门彭德尔宅／第I节彭德尔夫人迎候+彭德尔自述+印度大麻实验开端／第I节药效体验+黑暗女人幻象+诊断+搬离计划+动物实验构想／第II节烟(Flame)猫(Smoke)详描+夜入凶宅／第II节动物灵敏感知+烟对隐形存在欢愉+焰惊惧+首次侵入／第II节入侵者带援军反扑+群猫幻象+黑暗面孔对决+心灵炼金术+焰失明+第III节结局考证1798年女囚历史+面孔辨识+焰复明）。check_bilingual.py 152 标记块（76 对 Original/Chinese），标记成对满足、标题合并格式满足；1 处可疑错配为年份 1798→一七九八年 的数字锚点误报，内容配对正确。术语补充：西文森夫人(Mrs. Sivendson)/瑞典姑娘(Svenska)、费利克斯·彭德尔(Felix Pender)、帕特尼荒原(Putney Heath)、帕特尼山(Putney Hill)、爱尔兰(Ireland)、印度大麻(Cannabis indica)、黑暗势力(Dark Powers)、迷障(glamour)、符印(sigils)、星界(astral region)、纽盖特刑案录(Newgate Calendar)、离体之灵(discarnate)、心灵炼金术(spiritual alchemy)、通话管(the tube)。Case I 篇题罗马数字照搬。全书首篇(Case I)，术语与黄金样本(a-victim-of-higher-space)对齐。 |
| 2026-08-13 | The Nemesis of Fire (the-nemesis-of-fire.md) | done，exit 0 | 155.5KB 超长篇，分 6 段译（标题+第I节前半火车赴宅+拉格上校登场+拉格小姐晚宴+热感／第I节后半上校夜述十二英亩林地怪事+二十年焚死旧案+近三周复发+月圆线索／第II节前半白日入林+护体外壳+烟柱+无形追猎+池塘现形+冲出林子+拉格小姐奔逃+洗衣房走水／第II节后半火元素灵揭秘+元素灵/魔法论+血祭显形方案+上校印度部落血祭见闻+半夜之约／第III节半夜洗衣房实验+红光+狗吠+附体+《死者之书》仪轨吟唱(奥西里斯/托特/荷鲁斯)+火形几何+古祭司之脸显形+火光一闪+驱散／第IV节晨起+卡之论+掘地道+墓室+木乃伊+四罐+圣甲虫失窃+拉格小姐爬入归还不翼而飞之圣甲虫+木乃伊起身+结局"燎焦了，也毁掉了"）。check_bilingual.py 292 标记块（146 对 Original/Chinese），标记成对满足、标题合并格式满足、0 错配；四节(### I/II/III/IV)齐全，结尾与原文"Scorched and blasted"对齐。术语补充：拉格上校(Colonel/Horace Wragge)、拉格小姐/拉格老太太(Miss Wragge)、斯特赖德(Stride,猎场看守)、庄园宅邸(the Manor House)、十二英亩林地(Twelve Acre Plantation/Wood)、德鲁伊之石(Druid stones)、火元素灵(fire elemental)/元素灵(Elemental)、触物感知(psychometry)、显形(materialisation)、利维(Levi,=Éliphas Lévi)、巴力(Baal)、雅兹迪(Yezidis)、尤利安皇帝(Emperor Julian)、木乃伊(mummy)、卡(Ka,埃及灵魂)、圣甲虫(scarabaeus)、五芒星(pentagrams)、《死者之书》(Book of the Dead)、奥西里斯(Osiris)/荷鲁斯(Horus,永恒的守望者)/托特(Thoth)/塞特(Set)/阿努比斯(Anubis,犬首之神)/太阳神拉的金舟(Boat of Ra)、底比斯(Thebes)、死亡之七殿(Seven Halls of Death)、火眼之神/烟面之神、D——/S——湾、克伦威尔(Cromwell)、滑铁卢车站(Waterloo)、皮卡迪利(Piccadilly)；哈伯德(Hubbard)叙述者沿用 the-camp-of-the-dog 既有译法，离体之灵(discarnate)/思想传感(thought-reading)沿用术语表。Case III 篇题罗马数字照搬。 |
