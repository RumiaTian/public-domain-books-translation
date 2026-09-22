# 翻译计划（易腐的货物 / Perishable Goods）

## 本计划信息

- **项目名称**：dornford-yates_perishable-goods（《易腐的货物》，多恩福德·耶茨）
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
01-dedication.md,0.1,todo
02-first-blood.md,30.4,todo
...
```

状态取值：`todo` 待译 / `doing` 翻译中 / `done` 已完成。

## 执行步骤

按 `prompts/翻译计划模板.md`「执行步骤」9 步推进（读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志）。本项目中篇/连续模式，由主/单一 agent 自身逐篇执行；全书约 344KB，超出单批舒适上限时分多批推进，模式不变。

## 篇目清单

| # | 章号 | 篇名 | 源文 | 状态 |
|---|------|------|------|------|
| 1 | — | 献词（哈罗公学） | 01-dedication.md | done |
| 2 | I | First Blood 初战 | 02-first-blood.md | done |
| 3 | II | We Take the Field 出征 | 03-we-take-the-field.md | todo |
| 4 | III | In Touch 保持联络 | 04-in-touch.md | todo |
| 5 | IV | The Castle of Gath 加斯城堡 | 05-the-castle-of-gath.md | done |
| 6 | V | Mansel Takes Off the Gloves 曼塞尔摊牌 | 06-mansel-takes-off-the-gloves.md | done |
| 7 | VI | The Love of a Lady 一位淑女的爱 | 07-the-love-of-a-lady.md | done |
| 8 | VII | We Practise to Deceive 骗局迭起 | 08-we-practise-to-deceive.md | done |
| 9 | VIII | Out of Sight, Out of Mind 眼不见，心不念 | 09-out-of-sight-out-of-mind.md | todo |
| 10 | IX | Full Measure 足量 | 10-full-measure.md | todo |

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-08-17 | - | 建项目 | 修复半成品项目：重转 epub 复核 10/10 章节一致；原文文件加 01-10 前缀保证队列顺序＝阅读顺序；补齐项目说明/术语表/Plan；生成队列（全 todo）；epub 归档至 原书/。判定：小说文学/块对照/中篇→连续 |
| 2026-09-17 | 03-we-take-the-field.md | done | 第 II 章双语 43 对，check 退出码 0；章题 We Take the Field 意译「出征」（取开赴战场义）；新定名：汉尼拔·劳斯（Hannibal Rouse）、圣保罗（St. Paul）；波加内克/萨瓦/圣马丁/白女士庄/克利夫兰罗/猪背岭/劳斯莱斯 本章首现已附原文；勒索信删节「— — —」照搬「—— ——」 |
| 2026-09-17 | 01-dedication.md + 02-first-blood.md | done | 献词不单独产文件，以双语块并入 02 译文顶部（章题行之前）；第 I 章含献词共 43 对，check 结构契约全过、退出码 1 仅数字锚点误报（译文「2026年10月」已含 2026，正则 \b 遇汉字边界失效，属可放行项）。章题 First Blood 意译「初战」，替代篇目清单暂拟「初见血」（清单已同步）。新定名：纽黑文（Newhaven）、马厩院（Stable Yard）、西里汉姆梗（Sealyham，特斯特犬种）。首章风格基线：对白「」、内层引语『』（如『货物易腐』）；咒骂与删节「— — —」照搬「—— ——」；cousin 一律「表亲」不坐实堂/表；Original 块段落按源文「一段一行」规整为空行分隔（沿用 blind-corner 惯例），行内 U+FEFF/U+00A0/U+200A 等隐形字符逐字节保真 |
| 2026-09-17 | 04-in-touch.md | done | 第 III 章双语 41 对（178 段全覆盖），check 退出码 0（结构契约全过、可疑错配 0）。章题 In Touch 意译「保持联络」，替代篇目清单暂拟「接上头」（清单已同步；取 keep in touch 双向联络义——匪帮遣劳斯保持联络、曼塞尔反用之，正点本章题眼）。新定名：克拉耶恩（Crayern，菲拉赫以东首站）、拉斯（Lass，本章首现附原文）、圣詹姆斯公园（St. James's Park）、比尔（Bill，乔治对钱多斯昵称）、《阿利森的欧洲史》（Alison's Europe）、围院（close，拉斯旧城围合院落）、汉尼拔·劳（Hannibal R.，劳斯戏称）。Original 块程序化按行切片，重组后与源文 178 段逐字节一致（U+FEFF/U+00A0 全保真）；本章无咒骂删节 |
| 2026-09-17 | 05-the-castle-of-gath.md | done | 第 IV 章双语 46 对（210 段全覆盖），check 退出码 0（结构契约全过、可疑错配 0）。章题 The Castle of Gath 沿用术语表定名「加斯城堡」无新拟。程序化装配：Original 块与源文 210 段逐字节一致（U+FEFF×39/U+200A×5/U+00A0×1 全保真，无 BOM）；场景分隔 --- 于 Original/Chinese 块尾成对保留。本章首现附原文：拉斯（Lass）、凯斯梅特（Casemate）、大个子威利（Big Willie）、朱特（Jute）、邦奇（Bunch）、加斯（Gath）/加斯城堡（the Castle of Gath）、遮阳板（sun-visor）、三王旅馆（Three Kings Hotel）。指南书引文为书商德式破英语，译文以刻意文理失当再现（「城堡们」「一位管理员们」「未加触动们」等）。咒骂删节「————」照搬「—— ——」；曼塞尔引语『花朵吹放的美丽露台』与指南原文呼应统一。新定名：三王旅馆（Three Kings Hotel）、遮阳板（sun-visor）（已补术语表） |
| 2026-09-17 | 06-mansel-takes-off-the-gloves.md | done | 第 V 章双语 49 对（273 段全覆盖），check 退出码 0（结构契约全过、可疑错配 0）。章题 Takes Off the Gloves 意译「摊牌」（取 take off the gloves「不再客气、动真格」义，替代篇目清单暂拟「亮剑」，清单已同步；章内点题句 "I've got the gloves right off" 译「我这副手套可是摘了个干净」与之呼应）。摊牌三场景：门房试探（罗斯·诺布尔隔栅现身）、小谷审朱特（bluff 攻心、白绸衬衫后处决留白）、凌晨奇袭城堡（水道浮子计、王寝入室、暗步坠落、破门终局）。程序化装配：Original 块与源文 273 段逐字节一致（U+FEFF×53/U+200A×15 全保真，无 BOM）；场景分隔 --- ×2 保留。新定名：杰克·谢泼德（Jack Sheppard，越狱王典故，已补术语表）；三王旅馆沿用第 IV 章定名（本章源文作 The Three Kings，首现注从原文）。咒骂删节「— — —」照搬「—— ——」不补写；sovereign/pound 未出现 |
| 2026-09-17 | 07-the-love-of-a-lady.md | done | 第 VI 章双语 84 对（源文 324 段+4 场景分隔全覆盖），check 退出码 0（结构契约全过、可疑错配 0）。章题 The Love of a Lady 意译「一位淑女的爱」（替代篇目清单暂拟「对一位夫人的爱」，已同步；取阿黛尔密室自白「我爱上了约拿」点题，lady 兼指罗斯·诺布尔「货物/名声」双押下的淑女名誉）。五场景：雨夜瀑布绳留守（曼塞尔「我留下」）、晨间露台夺人与失绳（绳溜回未被察觉）、餐桌勒索摊牌（「易腐的货物」/「受损的货物」论价、曼塞尔摊牌爱上其妻、赤手夺枪为椅所误）、密室定情与围城推演（无人之境之爱、致乔治进攻密令）、夜间绳逃断绳惊变（佯攻太薄、罗斯·诺布尔浊笑收章）。程序化装配：Original 块与源文逐行逐字节一致（U+FEFF×103/U+200A×24/U+00A0×1 全保真，无 BOM）；场景分隔 --- ×4 成对保留。咒骂删节「— — —」照搬「—— ——」不补写；sovereign/pound 未出现（数额作「五十万/十万/二十五万镑」）。新定名：查理（Charlie）、窃听哨（The Listening Post）、忠诚的威廉（William the Faithful）、山毛榉林（beechwoods）（已补术语表）；水道/活板门/楔子/山嘴沿用第 V 章定名 |
| 2026-09-17 | 08-we-practise-to-deceive.md | done | 第 VII 章双语 55 对（源文 203 段+4 场景分隔全覆盖），check 退出码 0（结构契约全过、可疑错配 0）。章题 We Practise to Deceive 意译「骗局迭起」（谚语 "Oh what a tangled web we weave, when first we practise to deceive" 截句，取本章连环做戏行骗之义；替代篇目清单暂拟「我们施计设骗」，清单已同步）。五场景：震后四点复盘与餐桌升降台坠入地窖厨房救汉伯里、汉伯里自述追车被擒（羊群/倒车/油箱）与叹服敌忍劳斯莱斯之诱惑、夜穿庭院夺门接应（卡森留外独守）、拂晓穿屋抵西南塔楼扑空（敌移东南塔楼）与苦守十六时定「坠墙」苦肉计、旋梯偷听庞特/凯斯梅特黑话（白捡/钉臭虫/货物开口）并闷倒凯斯梅特、密室导演假摔阿黛尔扑怀收章。程序化装配：Original 块与源文 203 段逐字节一致（U+FEFF/U+200A/U+00A0 全保真，无 BOM）；场景分隔 --- ×4 成对保留。咒骂删节「— — —」照搬「—— ——」不补写；sovereign/pound 未出现（数额作「五十万」）。新定名：大楼梯（Grand Staircase）、垛齿（merlon）、升降台（lift）、绞盘（windlass）、门廊（porch）、卫兵室（guardroom）、东南塔楼（southeast tower）（已补术语表）；山毛榉林沿用第 VI 章定名 |
| 2026-09-17 | 10-full-measure.md | done | 第 IX 章双语 55 对（源文 209 段+6 场景分隔全覆盖），check 退出码 0（结构契约全过、可疑错配 0）。章题 Full Measure 意译「足量」（取双关：末句 they gave full measure 之「足量付出/倾其所有」义，兼商品度量衡呼应书名货物计量；替代篇目清单暂拟「足量」，无冲突）。七场景：临终守护与生死对白（夏娃/弥尔顿典、潮水喻、轭与磨盘、《马太福音》取去撇下）、汉伯里寻医记（误认布欣格/一千镑+四千镑封口+二百五十镑、本地槽外失魂论）、手术与善后（凯斯梅特林中下葬留刀、庞特邦奇囚厨房、看管人右脚铐解缚、书伯拒载护流言、波加内克短简）、康复与书商来信（特斯特石头回廊守箱、破英语长信以德式生硬中文再现、维尔萨首现）、露台谈心（牛奶/剪羊毛羔羊谚/静谧画廊钥匙/侍臣与贵妇）、道别启程（书伯游堡致富、「有些交谊没有告别」、月夜城垣、台地三人影、王后之吻）、尾声点题（波加内克余韵、石板与血渍留待后世、足量回应）。程序化装配：Original 块与源文 209 段逐字节一致（U+FEFF×93/U+200A×32/U+00A0×6 全保真，无 BOM）；信末签名行（空格行/空行/空格行/ H. S.）逐字节照录。新定名：妖灵（familiar）、维尔萨（Welsa）、最后的骑士入表（承第 IV 章指南引文）、小门/看管人承第 V 章入表、足量（full measure）、H. S. 署名保留（已补术语表）。本章无咒骂删节 |
- 09:12 整书完结（10/10，批次3直启单长轮）：批次3 第 2 册流转。体例存档：章题「## 罗马数字 英文章名 / 中文数字 中文题名」意译报备制（出征/保持联络/加斯城堡/曼塞尔摊牌/一位淑女的爱/骗局迭起/眼不见，心不念/足量）；53KB 超大章 13 批 append-only 实证；主 agent sed 统一 terrace=台地/archway=拱洞（23 处，引语「美丽露台」例外保留）；咒骂删节/斜体/德式破英语/和合本圣经引文体系全链落地。认领锁删除，看板 refresh。
