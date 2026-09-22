# 翻译计划（沃洛克风暴）

## 本计划信息

- **项目名称**：andre-norton_storm-over-warlock
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

## translation_queue.csv 格式

```
file,size_kb,status
01-disaster.md,19.2,todo
02-death-of-a-ship.md,19.6,todo
...
```

| 字段 | 含义 | 取值 |
|------|------|------|
| `file` | 源文文件名（在 `原文/` 目录下） | 如 `01-disaster.md` |
| `size_kb` | 源文大小（KB）。>50KB 为长文，按通用翻译引擎第七节分段 | 数字 |
| `status` | 翻译状态 | `todo` 待译 / `doing` 翻译中 / `done` 已完成 |

## 执行步骤

按 `prompts/翻译计划模板.md`「执行步骤」9 步推进（读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志）。

## 篇目清单

| # | 章题（罗马数字照搬） | 源文 | 状态 |
|---|------|------|------|
| 1 | I Disaster | 01-disaster.md | todo |
| 2 | II Death of a Ship | 02-death-of-a-ship.md | todo |
| 3 | III To Close Ranks | 03-to-close-ranks.md | todo |
| 4 | IV Sortie | 04-sortie.md | todo |
| 5 | V Pursuit | 05-pursuit.md | todo |
| 6 | VI The Hound | 06-the-hound.md | todo |
| 7 | VII Unwelcome Guide | 07-unwelcome-guide.md | todo |
| 8 | VIII Utgard | 08-utgard.md | todo |
| 9 | IX One Alone | 09-one-alone.md | todo |
| 10 | X A Trap for a Trapper | 10-a-trap-for-a-trapper.md | todo |
| 11 | XI The Witch | 11-the-witch.md | todo |
| 12 | XII The Veil of Illusion | 12-the-veil-of-illusion.md | todo |
| 13 | XIII He Who Dreams… | 13-he-who-dreams.md | todo |
| 14 | XIV Escape | 14-escape.md | todo |
| 15 | XV Dragon Slayer | 15-dragon-slayer.md | todo |
| 16 | XVI Third Prisoner | 16-third-prisoner.md | todo |
| 17 | XVII Throg Justice | 17-throg-justice.md | todo |
| 18 | XVIII Storm's Ending | 18-storm-s-ending.md | todo |

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
| 2026-09-06 | 01-disaster.md | done | 22 对块/44 段，check_bilingual 退出码 0（0 可疑）；定名沿用种子术语表，首现括注齐全，表末追加新词：Fadakar 法达卡、skitterer 疾窜兽、atomic torch 原子炬、bravo tablets 布拉沃口粮片、plate ships 碟形飞船、lake duck 湖鸭、S-E-Three S-E-三级、Sol's system 太阳系；源文 U+FEFF×21/U+200A×3 逐字保留 |
| 2026-09-06 | 02-death-of-a-ship.md | done | 23 对块/44 段，check_bilingual 退出码 0（0 可疑）；术语全按术语表；新定名（未入表，见交接报告）：Witch 女巫星、Wizard 男巫星、Emigrant Control 移民管理局、plasta 普拉斯塔、earth-wasp 土蜂、rider beam 引导波束，另 settlement board 定居委员会、cross-continent cargo carrier 跨洲货运机为描述性译法；斜体 *had* 保留（中文作 *得*）；源文 U+FEFF×19/U+200A×3 逐字保留 |
| 2026-09-06 | 04-sortie.md | done | 25 对块/51 段，check_bilingual 退出码 0（0 可疑）；术语全按术语表；新定名（未入表，见交接报告）：sortie（章题）出击、sling 投石索、throwing stick 投矛器、fire sparker 打火器、fjord 峡湾、raft 木筏、light plant 发光植物、willow-things 柳状植物、super-steel 超级钢、“deer”“鹿”、hound “猎犬”（斯罗格畜养之追踪兽，章末首现）；源文 U+FEFF×15/U+200A×6 逐字保留（Original 块自源文程序化切片） |
| 2026-09-06 | 03-to-close-ranks.md | done | 42 对块/79 段，check_bilingual 退出码 0（0 可疑）；术语全按术语表（沙恩/托尔瓦德/斯罗格人/甲虫脑袋/击晕枪/爆能枪/碟形飞船/克拉克鸟等）；新定名（未入表，见交接报告）：force ax / force-blade ax 力场斧（首现括注，他章无前例）、booster rocket 助推火箭、enter-atmosphere signal 入大气层信号、automatics 自动系统（降落）、concentrates 浓缩口粮、supply cache 补给窖藏（描述性）；章题 To Close Ranks 译「收拢阵线」；斜体 *had*/*was*/*not* 中文对应 *确实*/*真的*/*绝不能*；源文 U+FEFF×26/U+200A×9 逐字保留（Original 块自源文程序化切片，79 段逐一 verbatim 校验通过） |
| 2026-09-06 | 05-pursuit.md | done | 36 对块/75 段，check_bilingual 退出码 0（0 可疑）；术语全按术语表，猎犬/木筏/发光植物沿用 04 章定名、浓缩口粮沿用 03 章定名；新定名（未入表，见交接报告）：dumdum 达姆武器、light-willow 光柳、Cavern of the Veil 幕之洞窟、Odin 奥丁星系、Kulkulkan 库库尔坎星系、map case 地图盒、finger lock 指码锁、aerial survey 航测（描述性）；斜体 *if*/*must* 中文对应 *如果*/*必须*；源文 U+FEFF×44/U+200A×8 逐字保留（Original 块自源文程序化切片，75 段逐一 verbatim 校验通过） |
| 2026-09-06 | 06-the-hound.md | done | 33 对块/77 段，check_bilingual 退出码 0（0 可疑）；术语全按术语表（沙恩/托尔瓦德/斯罗格人/狼獾/“猎犬”带引号形态/击晕枪/爆能枪/原子炬/碟形飞船），跨章沿用：04 木筏/急流、03 力场斧/浓缩口粮片、05 地图盒/撑杆/瀑布（05 后成稿，按先定名者修正从其定名）；新定名（未入表，见交接报告）：force beam 力场光束、energy bolt 能量光束（描述性）、map case 地图盒（05 未括注，06 补首现括注）、jack-in-the-box 玩偶匣、toad-lizard 蟾蜍蜥蜴、the cut 裂谷/the slash 劈裂（描述性）；章题 The Hound 译「“猎犬”」；斜体 *was* 中文对应 *确实*；源文 U+FEFF×21/U+200A×2 逐字保留（Original 块自源文程序化切片，77 段逐一 verbatim 校验通过） |
| 2026-09-06 | 07-unwelcome-guide.md | done | 31 对块/82 段，check_bilingual 退出码 0（0 可疑）；术语全按术语表，跨章沿用：04 峡湾/木筏/发光植物/“猎犬”、05 骷髅山/绿幕/地图盒、03 浓缩口粮、01 原子炬/布拉沃口粮片、02 先遣侦察员/总部；新定名（未入表，见交接报告）：medallion 圆牌、the Archives 档案库、Fenniston 芬尼斯顿、Lorry 洛里、mind-controlled 精神受控者、plasta-flesh 普拉斯塔人造皮（沿用 plasta 定名）、badlands 荒原劣地/shingle 砾石滩/条图/“散发”等描述性译法；章题 Unwelcome Guide 译「不受欢迎的向导」；斜体 *this*/*I*/*did*/*after* 中文对应 *这个*/*我*/*偏偏*/*等*；源文 U+FEFF×40/U+200A×7 逐字保留（Original 块自源文程序化切片，82 段逐一 verbatim 校验通过） |
| 2026-09-06 | 08-utgard.md | done | 43 对块/66 段，check_bilingual 退出码 0（0 可疑）；术语全按术语表（沙恩/托尔瓦德/尤特加德/斯罗格人/“猎犬”/圆盘/狼獾/浓缩口粮），跨章沿用：04 峡湾、05 骷髅山/绿幕/幕之洞窟/木筏、02 侦察船、01 原子炬体系；新定名（未入表，见交接报告）：energy whip 能量鞭、Caldon mines 卡尔登矿区、Training Center 训练中心、bolt hole 逃生洞、flying things 沿用 05「会飞的东西」不另注、the Team 外勤队/Team stature 外勤队员身份（与 the Service 勘测队区分）、snout 兽吻/snout-passage 兽吻通道（描述性）、casual labor 临时工、labor Barracks 劳工营房（描述性）；章题 VIII Utgard 译「VIII 尤特加德」；斜体 *anything*/*had* 中文对应 *任何东西*/*确实*；源文 U+FEFF×17/U+200A×2/NBSP×1（“… storm coming.”）逐字保留（Original 块自源文程序化切片，66 段逐一 verbatim 校验通过） |
| 2026-09-06 | 10-a-trap-for-a-trapper.md | done | 24 对块/53 段，check_bilingual 退出码 0（0 可疑）；术语全按术语表（沙恩/托尔瓦德/塔吉/托吉/狼獾/斯罗格人/沃洛克/击晕枪/力场斧/圆盘/内谷），跨章沿用：08 独木舟/小舟/壳/浮木/骷髅山（skull-mountain「骷髅山」照用）、06 陷阱；新定名（未入表，见交接报告）：lagoon 潟湖、outrigger/outrigger canoe 舷外支架/舷外支架独木舟、rain tank 雨水箱、leather-headed bird 皮头鸟、spiny-tailed fish 刺尾鱼、moss-fungi 苔藓真菌（均首现括注，09 章并行未成稿，本章先定名待其沿用）；章题 A Trap for a Trapper 译「给设陷人的陷阱」（与正文 To trap the trapper「给设陷人设陷」呼应）；斜体 *had*/*they* 中文对应 *就是*/*他们*；源文 U+FEFF×13/U+200A×1（行 50 A trap 后 hair-space 序列）逐字保留（Original 块自源文程序化切片，53 段逐一 verbatim 校验通过） |
| 2026-09-06 | 09-one-alone.md | done | 25 对块/56 段，check_bilingual 退出码 0（0 可疑）；术语全按术语表（沙恩/托尔瓦德/尤特加德/斯罗格人/沃洛克/狼獾/塔吉/托吉/克拉克鸟/叉尾兽/圆盘/移民运输舰/巡逻舰队），跨章沿用：07 刻纹圆盘、08 独木舟、02 侦察船、05 移民运输舰、06 "猎犬"/沙暴；按先成稿者对齐 10 章定名：lagoon 潟湖（原拟环礁湖已改）、tank of rain 依 10 章 rain tank 雨水箱对齐为"一箱雨水"，独木舟/舷外支架/皮头鸟/砾石滩/高潮线与 10 章一致；新定名（未入表，见交接报告）：sea gate 海门（首现括注）、the reef 礁环（描述性，他章无前例）；章题 One Alone 译「独自一人」；斜体 *had* 中文对应 *非*/*当真*；源文 U+FEFF×16/U+200A×2 逐字保留（Original 块自源文程序化切片，56 段逐一 verbatim 校验通过） |
| 2026-09-06 | 11-the-witch.md | done | 50 对块/60 段，check_bilingual 退出码 0（0 可疑）；术语全按术语表（沙恩/塔吉/托吉/狼獾/斯罗格人/沃洛克人/内谷/击晕枪/力场斧/原子炬/独木舟/「梦」），按先成稿者对齐 09/10 章定名：海门（09）、潟湖（09/10）、舷外支架（10）、设陷人（10）；新定名（未入表，见交接报告）：Free Traders 自由商人、basic galactic speech 基础银河语（均首现括注）、snare 罗网/V 形头冠/龙首之人（描述性）；章题 XI The Witch 译「XI 女巫」；斜体 *must*/*man*/*Them* 中文对应 *非*/*人*/*他们*；源文 U+FEFF×44/U+200A×12/NBSP×0 逐字保留（Original 块自源文程序化切片，60 段逐一 verbatim 校验通过） |
| 2026-09-06 | 12-the-veil-of-illusion.md | done | 35 对块/62 段，check_bilingual 退出码 0（0 可疑）；术语全按术语表（沙恩/托尔瓦德/塔吉/托吉/狼獾/斯罗格人/沃洛克人/击晕枪/圆盘/幻象之幕），跨章沿用：05/07/08 绿幕·骷髅山·眼窝·鼻缝·会飞的东西、09 水道、07 刻纹圆盘（本章作圆盘）、07 席垫意象；新定名（未入表，见交接报告）：thoughtguider 导思者、Readers-of-the-rods 读签者、Sharers-of-my-visions 共享幻象的诸位、Old Ones 古老者、Rama 拉玛、star voyager 星际旅人、star-born one 星生者、man-who-thinks-without-a-guide 无导自思的人、initiates' road 入门者之路、tri-dee 三维影像、rods/slivers/needles 签/细签/签针（cast the rods 掷签）、jeweled pattern 珠光纹彩、bead-room 珠室（描述性）、Wise ones 诸位智者；章题 The Veil of Illusion 译「幻象之幕」；斜体 *your*/*not*/*was*/*all* 中文对应 *你*/*没能*/*有*/*全都*；源文 U+FEFF×22/U+200A×3 逐字保留（Original 块自源文程序化切片，62 段逐一 verbatim 校验通过） |
| 2026-09-06 | 13-he-who-dreams.md | done | 32 对块/78 单元（75 段+3 节 blockquote 诗），check_bilingual 退出码 0（0 可疑）；术语全按术语表（沙恩/托尔瓦德/加斯/兰蒂/洛加利/斯罗格人/翼蜥族/女巫/炽鸟/特拉夫/击晕枪/爆能枪/圆盘/骨圆牌（07）/垃圾场/「梦」），按先成稿者对齐并行章定名：12 章 tri-dee 三维影像→本章三维影像带（tri-dee tape）、water tunnel 水道→river tunnel 亦译水道、bowl of sticks 碗/细签/掷签→倾倒碗中细签；新定名（未入表，见交接报告）：Big Strike「大矿脉」酒馆、Ajax system 阿贾克斯星系（均首现括注）、witchery 巫术、Masters/Mistresses of illusion 幻术大师/幻术女师（「是女师」之纠）、class one status 一级评衔、Dream true or false「梦」之真伪（描述性）；托尔瓦德雾中吟唱三节诗保留 blockquote 译诗；斜体 *was*/*not*/*could*/*took*/*are* 中文对应 *确实*/*不*/*也*/*掳*/*真*；源文 U+FEFF×47/U+200A×9/NBSP×3 逐字保留（Original 块自源文程序化切片，86 非空行逐一 verbatim 校验通过） |
| 2026-09-06 | 14-escape.md | done | 30 对块/69 段，check_bilingual 退出码 0（0 可疑）；术语全按术语表（沙恩/托尔瓦德/斯罗格人/沃洛克/翼蜥族/沃洛克女巫/圆盘/叉尾兽/克拉克鸟/皮头鸟/狼獾/勘测队军官/幻象之幕），按先成稿者对齐并行章定名：12 幻象之幕、13 雾/迷雾体系、骨圆牌→圆盘（游动引路）、09 海门之外礁石意象；新定名（未入表，见交接报告）：cavern of the fog 雾之洞窟（与 05 幕之洞窟 Cavern of the Veil 区分）、monolith 独石、well/chimney 井/烟囱、control disk 控制圆盘、dragon slayer 屠龙者（呼应 15 章题）、fork-tail charm 弄兽/驭兽（描述性）；章题 XIV Escape 译「XIV 逃亡」；斜体 *was*/*slap-slap* 中文对应 *确实*/*有多深*/*啪嗒、啪嗒*；源文 U+FEFF×24/U+200A×3 逐字保留（Original 块自源文程序化切片，69 段逐一 verbatim 校验通过） |
| 2026-09-06 | 15-dragon-slayer.md | done | 42 对块/82 段，check_bilingual 退出码 0（0 可疑）；术语全按术语表（沙恩/兰蒂/托尔瓦德/塔吉/托吉/狼獾/斯罗格人/甲虫脑袋/翼蜥族/沃洛克/提尔的垃圾场/击晕枪/圆盘/幕之洞窟/洛加利/特拉夫/「梦」），按先成稿者对齐并行章定名：14 石板（the slab）/屠龙者/石柱/雾之洞窟（cavern of the fog，与本章幕之洞窟区分）、09 叉尾兽、12 珠光纹带、04 斯罗格“猎犬”、01 小熊模样；新定名（未入表，见交接报告）：warlock 双关首现括注「男巫（warlock）」、capital city 都城、shell-creature 壳兽、spiny collar 棘领、thought beams 思维波束、skin sheath 皮鞘（描述性）；战吼 Ayeeee 译「啊咿——！」；斜体 *what*/*us*/*did* 中文对应 *什么*/*我们*/*到底*；源文 U+FEFF×22/U+200A×1（underground 后 FEFF+200A+FEFF 序列）逐字保留（Original 块自源文程序化切片，82 段逐一 verbatim 校验通过） |
| 2026-09-06 | 16-third-prisoner.md | done | 32 对块/83 段，check_bilingual 退出码 0（0 可疑）；术语全按术语表（沙恩/兰蒂/托尔瓦德/斯罗格人/甲虫脑袋/翼蜥族/女巫/克拉克鸟/狼獾/塔吉/托吉/击晕枪/爆能枪/圆盘/特拉夫/垃圾场/骷髅山→骷髅（05/07）/「梦」/幻象之幕/落难的斯罗格人/勘测队军官），跨章沿用：12 星际旅人·掷签·细签·格局、13「梦」之真伪体系·雾、14 雾之洞窟（本章 cavern of the mist 同译）、08 鼻孔/05·12 鼻缝、11 磷光植物→磷光灌木、15 俘虏/落难的对译呼应；新定名（未入表，见交接报告）：Elder One 长者、Reachers 求索者、Trails of Seeking 求索之径、Reacher for Knowledge 求索知识者、Place of False Dreams 虚梦之地、First Awakening 初醒、Final Dream 终梦、Greatest Power 至大之力、air rider 飞骑、rock creatures 岩居生物、star man 星际人（均首现括注）、an elder among his kind 老资格（描述性，与「长者」区分）、smoke out/ smoked one 熏出洞/被熏的（双关保留）、dream store 梦藏；章题 XVI Third Prisoner 译「XVI 第三个俘虏」；斜体 *my*/*does*/*be* 中文对应 *我*/*确实*/*是*；源文 U+FEFF×34/U+200A×10/NBSP×0 逐字保留（Original 块自源文程序化切片，83 段逐一 verbatim 校验通过） |
| 2026-09-06 | 18-storm-s-ending.md | done | 50 对块/83 段，check_bilingual 退出码 0（0 可疑）；术语全按术语表（沙恩/兰蒂/托尔瓦德/塔吉/托吉/狼獾/斯罗格人/甲虫脑袋/翼蜥族/沃洛克/女巫星/圆盘/幻象之幕/外勤队/见习生），跨章沿用：04 通讯穹顶、02 引导波束（riding beam 同器）、05 骷髅·清剿·巡逻舰、15 长老·‘法力’·男巫、08 营房·外勤队员体系；新定名（未入表，见交接报告）：translator 翻译器（首现括注，器物源出 17 章）、the web （翻译器）蛛网、landing beam 着陆波束、fix point 定位点、embassy post 使馆驻点（均首现括注）、frame/framework 刑架、mop-up squad 清剿小队、wire rope 钢丝绳、wall seat 靠壁座椅、braid 绲带、skeleton crews 看守船员（描述性）；章题 XVIII Storm's Ending 译「XVIII 风暴的终局」；源文笔误照录（restored circulation, This / hung in his bounds）；源文 U+FEFF×37/U+200A×4/NBSP×1（Scorched! 句后）逐字保留（Original 块自源文程序化切片，83 段逐一 verbatim 校验通过） |
| 2026-09-06 | 17-throg-justice.md | done | 44 对块/72 段，check_bilingual 退出码 0（0 可疑）；术语全按术语表（沙恩/兰蒂/托尔瓦德/斯罗格人/甲虫脑袋/翼蜥族/沃洛克/垃圾场/圆盘/能量鞭/爆能枪/巡逻舰/运输舰/「梦」/三维影像），跨章沿用：04 通讯穹顶/通讯站、02 rider beam 引导波束（本章 guide beam 同物同译）、13 三维影像机（tri-dee）、洛加利/特拉夫（幻象之雾，13/14）、大陆（07/10）、密码（05）、骷髅山（05-08）；新定名（未入表，见交接报告）：force bar 力场棒（首现括注）、spotter beam broadcaster 定点波束发射机（首现括注）、mother ship 母舰、translator 翻译器、Mayday 保留原文首现括注「呼救信号」、fiction tapes 小说影像带、work tape 工作带（描述性）；章题 XVII Throg Justice 译「XVII 斯罗格人的正义」；源文 U+FEFF×43/U+200A×5/NBSP×2 逐字保留（Original 块自源文程序化切片，72 段逐一 verbatim 校验通过） |
| 2026-09-06 | 全书 18 章 | done 18/18（完结） | 批次1晚间整本完成（21:00 上锁）：01 定名篇串行（种子表已预填，38对块rc=0）后 3 路滚筒；18 章全过检（rc=0 居多，无误报类）；术语表滚合至100+条（Logally 备注经17章核证修正为垃圾场人类恶霸；女巫星/男巫星意译与沃洛克音译区分；求索者/至大之力等翼蜥族体系名成套）；源文笔误（then/than、gazed, at 等）均原样照录；删锁流转 |
