# 翻译计划（尖顶屋 / Pointed Roofs）

## 本计划信息

- **项目名称**：《尖顶屋》（多萝西·米勒·理查森）/ Pointed Roofs (Dorothy M. Richardson)
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

按 `prompts/翻译计划模板.md`「执行步骤」9 步推进（读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志）。本作品判定为中篇 → 连续模式，由主 agent 在自身上下文内逐章执行 9 步；单批受上下文限制时可分批续译。

## 篇目清单

| # | 篇名 | 源文 | 大小 | 状态 |
|---|------|------|------|------|
| 1 | 第一章 | chapter-1.md | 20.4KB | done |
| 2 | 第二章 | chapter-2.md | 15.4KB | done |
| 3 | 第三章 | chapter-3.md | 72.9KB | todo |
| 4 | 第四章 | chapter-4.md | 14.2KB | todo |
| 5 | 第五章 | chapter-5.md | 38.2KB | todo |
| 6 | 第六章 | chapter-6.md | 67.0KB | todo |
| 7 | 第七章 | chapter-7.md | 2.7KB | todo |
| 8 | 第八章 | chapter-8.md | 43.6KB | todo |
| 9 | 第九章 | chapter-9.md | 7.4KB | todo |
| 10 | 第十章 | chapter-10.md | 55.6KB | todo |

合计 10 章，约 334.8KB / 5.7 万英文词。

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-08-15 | chapter-1 | 20.4KB / exit 0 | 委派模式；26 块对照；风格对齐 chapter-2 黄金样本（米丽亚姆/弗劳莱恩小姐/“……”省略号）；新增术语：Saratoga trunk 萨拉托加大衣箱、Intermezzo 间奏曲、piquet 皮凯、rujabiba frills 噜噜巴巴褶边、goodney 老天鹅、Gooby 古比、Binks 宾克斯、basket plaits 篮式辫、Hinde's 欣德牌发夹、petersham belt 彼得沙姆腰带、rounders 圆场球、Lecky 莱基、Contemporary Review《当代评论》、Holy Family《圣家族》、Ungava《翁加瓦》、John Halifax《约翰·哈利法克斯》、Villette《维莱特》、Egmont《艾格蒙特》、Grand Ceremonial 大典礼 等 |
| 2026-08-15 | chapter-2 | 15.4KB / exit 0 | 委派模式；意识流文体，7 块对照；新增术语：Harwich 哈里奇、Sunlight Zeep 日光肥皂、Heller《不眠之夜》、Victoria Hotel 维多利亚饭店、Monsieur、La Maison déserte《荒宅》、Ellen Sharpe 埃伦·夏普、Babington 巴宾顿、Timmy 蒂米、Dawlish 道利什 等 |
| 2026-08-12 | - | 建项目 | 从 待翻译/ epub 提取 10 章正文、判断中篇/连续模式、建术语表初版（人物/地名/德法语词句）、生成队列 | 从 待翻译/ epub 提取 10 章正文、判断中篇/连续模式、建术语表初版（人物/地名/德法语词句）、生成队列 |
| 2026-08-15 | chapter-5 | 38.2KB / exit 0 | 委派模式；意识流文体，40 块对照；check_bilingual 通过（0 可疑错配）；新增术语：Kapellmeister Bossenberger 卡佩尔迈斯特·波森贝格、Minna 米娜、Anna 安娜、Kreipe 克赖佩、Georgstraße 格奥尔格大街、Elsa Speier 埃尔莎·施派尔、Dr. Dieckel 迪克尔医生、Stroodie 斯特鲁迪、Herr Pastor 牧师先生、Vorspielen 试奏、Jüngling 青年郎君、Apotheker 药剂师 等（已补入术语表） |
| 2026-08-15 | chapter-4 | 14.2KB / exit 0 | 委派模式；意识流文体，9 块对照；check_bilingual 通过（0 可疑错配）；德国教堂/英国教堂三章周日描写，大量宗教冥思独白；新增术语：Schlosskirche 宫殿教堂、Les Travailleurs de la Mer《海上劳工》、Lead, Kindly Light《慈光歌》、Cardinal Newman 纽曼红衣主教、Mr. Gladstone 格莱斯顿先生、Radical 激进派、schöne Predigt 优美的布道、Nun danket alle Gott 今感谢全体上帝（Now Thank We All Our God《今我们齐来感谢主》）、Hugo Wieland 雨果·维兰德、Erica Wieland 埃丽卡·维兰德、Marie 玛丽、Caritas 等（Vorspielen 译"演奏会"与 chapter-5"试奏"待统一） |
| 2026-08-15 | chapter-3 | 72.9KB / exit 0 | 委派模式；72.9KB 长篇按§7 分 4 段写入同一译文文件；21 块对照；意识流文体对齐 chapter-1/2；德语对白保留原文+括注，德语诗 Ein Blatt 保留原文+中译；术语表新增"第 3 章新增"节（Ulrica Hesse 乌尔丽卡·黑塞、Minna Blum 明娜·布卢姆、Elsa Speier 埃尔莎·施派尔、Gertrude Goldring 格特鲁德·戈德林、Frau Krause 克劳泽太太、Vorspielen 试奏会、Haarwaschen 洗头、Misunderstood《误解》、Ein Blatt《夏日里的一叶》等） |
| 2026-08-15 | chapter-7 | 2.7KB / exit 0 | 委派模式；短章，4 块对照；check_bilingual 通过（0 可疑错配）；餐桌收盘一幕，米丽亚姆与 Fräulein Pfaff 正面冲突（"wie Gräfinnen 像伯爵夫人"）；新增术语：wie Gräfinnen 像伯爵夫人（wie Gräfinnen）、the lift 升降机（餐梯）；人物均沿用术语表现有译法（Marie 玛丽、Clara 克拉拉等） |

| 2026-08-15 | chapter-6 | 67.0KB / exit 0 | 委派模式；67KB 长篇按§7 分 4 段写入同一译文文件；22 块对照；check_bilingual 通过（0 可疑错配）；286 源段落全覆盖核验；德语/法语对白与歌词保留原文+括注；术语表新增"第 6 章新增"节（Hoddenheim 霍登海姆、Der Spaziergang《散步》、Bienenkorb 蜂巢、Die Räuber《强盗》、Schwarzbrot 黑麦面包、Magd 女仆、Engländerin 英国女人、slommucky 邋遢、flountery 花哨飘飘 等） || 2026-08-15 | chapter-8 | 43.6KB / exit 0 | 委派模式；21 块对照（约 87KB 译文）；check_bilingual 通过（0 可疑错配、标题合并满足）；覆盖完整性经脚本逐段核对（0 漏段）；意识流文体对齐 chapter-1 黄金样本；德语学生歌/Sonnenschein 合唱/女管家低地德语（Ik kenne meine Tasse）保留原文+中译；Solveig 之歌（格里格）、坚信礼对话（weeped/cry）、雷雨夜、晨间花园棚屋与 Fräulein 平视一瞬；术语表已补"第 8 章新增"38 条；注意：Minna 译名 chapter-3 作"明娜"、chapter-5 起作"米娜"，本章沿用"米娜"，建议全书终校统一 |
| 2026-08-14 | chapter-9, chapter-10 | done ×2（全书 10/10 译完） | exit 0 |
