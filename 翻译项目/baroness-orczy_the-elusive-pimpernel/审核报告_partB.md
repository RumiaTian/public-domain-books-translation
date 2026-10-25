# 《难捕的红花侠》后半卷独立审校报告

- 审校日期：2026-10-23
- 质量等级：B 良好
- 一句话结论：全卷无漏译与逻辑反转等重大缺陷，文学质感上乘，但存在个别字词错译、加粗格式违规、外文主次倒置及第33章标题格式残缺等瑕疵，建议按明细修订后定稿

---

## 一、审校范围与工程基准

- 审校对象：《难捕的红花侠》后半卷（Part B）
- 篇目清单：共计18篇，覆盖第18章至第35章：
  - chapter-18.zh-CN.md（XVIII. 六号牢房）
  - chapter-19.zh-CN.md（XIX. 弱者的力量）
  - chapter-20.zh-CN.md（XX. 大捷）
  - chapter-21.zh-CN.md（XXI. 悬念）
  - chapter-22.zh-CN.md（XXII. 并非死亡）
  - chapter-23.zh-CN.md（XXIII. 人质）
  - chapter-24.zh-CN.md（XXIV. 同僚）
  - chapter-25.zh-CN.md（XXV. 意外）
  - chapter-26.zh-CN.md（XXVI. 交易的条件）
  - chapter-27.zh-CN.md（XXVII. 抉择）
  - chapter-28.zh-CN.md（XXVIII. 午夜守望）
  - chapter-29.zh-CN.md（XXIX. 国家庆典）
  - chapter-30.zh-CN.md（XXX. 巡游）
  - chapter-31.zh-CN.md（XXXI. 最后部署）
  - chapter-32.zh-CN.md（XXXII. 那封信）
  - chapter-33.zh-CN.md（XXXIII. 英国间谍）
  - chapter-34.zh-CN.md（XXXIV. 晚祷钟）
  - chapter-35.zh-CN.md（XXXV. 玛格丽特）
- 工作模式：100%逐块逐段对照通读，严守只读隔离，未修改原文与译文任何文件
- 校验工具：结合 scripts/check_bilingual.py 完成双语标记对齐与启发式语义校验，18篇双语块结构完全配对闭合

---

## 二、主要缺陷与修改建议

### 发现的问题与建议

- 第18章（chapter-18.zh-CN.md）第199行：
  - 原文：The figure was slender and almost wizened, the thin shoulders round with an habitual stoop, the lean shanks were encased in a pair of much-darned, coarse black stockings
  - 现译：那身形瘦小，几乎干瘪，瘦削的肩膀因为常年佝偻而溜圆，两条细胞上套着一双补丁摞补丁的粗黑长袜
  - 问题定位：实质性别字与错译硬伤，将 lean shanks（细瘦的小腿或细胫）误译为「两条细胞上」，语义不通
  - 修改建议：建议将「两条细胞上」修改为「两条细腿上」或「两条瘦削的小腿上」

- 第18章（chapter-18.zh-CN.md）第91行：
  - 原文：she was conscious of the same pleasant voice softly droning Paters and Aves close to her ear
  - 现译：她始终意识着那个和悦的嗓音在耳边低低地、单调地诵着一篇篇《主祷文》和《圣母经》
  - 问题定位：术语一致性违规，后文各章（第19章第163行、第29章第21行、第33章第50行、第35章第128行）及术语表新增词条统一采用天主教传统译名《天主经》，此处单独使用了新教译名《主祷文》
  - 修改建议：建议将《主祷文》修改为《天主经》以保持全书术语一致

- 第22章（chapter-22.zh-CN.md）第115行：
  - 原文：“Now then, calotin,” said the first soldier with an oath
  - 现译：「行了，*calotin*（教士佬），」头一个士兵啐了句粗话
  - 问题定位：外文暴露在中文括号外且主次倒置，违背译文为主体、外文附注括号的规范
  - 修改建议：建议调整为「行了，『教士佬』（*calotin*），」

- 第25章（chapter-25.zh-CN.md）第273行：
  - 原文：Passons, Monsieur
  - 现译：*Passons*（言归正传），先生
  - 问题定位：外文暴露在中文括号外且主次倒置
  - 修改建议：建议调整为「言归正传（*passons*），先生」

- 第26章（chapter-26.zh-CN.md）第158行：
  - 原文包含 Citizen Chauvelin 加粗标识
  - 现译：肖夫兰公民一词带有双星号加粗标记
  - 问题定位：格式规范违规，译文直接使用了 Markdown 加粗语法（连续双星号），违反全书禁止加粗格式的工程规范
  - 修改建议：建议去掉加粗语法，修改为平铺格式「肖夫兰公民——」或带引号格式

- 第29章（chapter-29.zh-CN.md）第415行：
  - 原文：There were to be Pierrots and Pierettes, Harlequins and English clowns, aristocrats and goddesses!
  - 现译：要有皮埃罗（Pierrot）和皮埃蕾特（Pierrette），有阿尔莱坎（Harlequin）和英国小丑，有贵族和女神！
  - 问题定位：同名异译与术语表违规，术语表已明确 Harlequin 定名为「哈利昆」（见第30章第35行「哈利昆」），此处译为法文读音「阿尔莱坎」；同句中 Pierrette 亦与术语表定名「皮埃罗特」产生歧异
  - 修改建议：建议将「阿尔莱坎」统一为「哈利昆」，「皮埃蕾特」统一为「皮埃罗特」

- 第32章（chapter-32.zh-CN.md）第57行、第59行、第75行：
  - 原文：calotin
  - 现译：剩不下一个*calotin*（教士佬） / *calotin*（教士佬）有的是 / 那老*calotin*（教士佬）
  - 问题定位：外文暴露在中文括号外且主次倒置
  - 修改建议：建议一律调整为「『教士佬』（*calotin*）」

- 第33章（chapter-33.zh-CN.md）第1行至第20行：
  - 原文与现译：章节标题仅作 XXXIII 且正文首块内残留篇名
  - 问题定位：章节标题结构格式违规与标记契约受损，未遵循全书通行的双语合并标题规范，致使英文标题残留在 Original 块内、中文标题残留在 Chinese 块内
  - 修改建议：建议将首行标题修正为「## XXXIII. The English Spy / XXXIII. 英国间谍」，并同步从 Original 和 Chinese 双语正文块起始处删除坠入正文的孤立章节名行
  - 同章第162行亦再次出现「阿尔莱坎」，建议一并修正为「哈利昆」
  - 同章第248行「带这*calotin*（教士佬）去敲晚祷钟」，建议一并修正外文倒置为「带这『教士佬』（*calotin*）去敲晚祷钟」

---

## 三、综合评审明细

- 完整性：全卷18篇经逐段仔细对照，双语标记对齐严丝合缝，无任何遗漏段落、无截断、无漏译，结构完整度达到100%
- 准确性：整体译文理解深入，对英国贵族与法国革命政权之间的殊死博弈把握准确，人物心理刻画精微，除第18章一处字词层面的别字（细胞误译）外，全卷未见主客体颠倒、时间线反转或因果逻辑错乱等严重语义缺陷
- 术语与命名体系：核心人物与专有名词（如珀西、玛格丽特、肖夫兰、布洛涅、加约勒、理性女神、晚祷钟、白日梦号、洛伦佐·琴奇之剑、坦普尔监狱等）在18个章节中高度一致，仅存在极个别章节间的词条细微偏差（主祷文与天主经、哈利昆与阿尔莱坎），经本报告指出后极易修正闭环
- 文学质感与历史浪漫冒险小说风格：译文展现出极高水准的十九世纪历史浪漫传奇译风，对奥希女男爵原作特有的讽刺笔调、英伦贵族式漫不经心的傲慢幽默、恐怖统治时期的血雨腥风与群众狂热心理展现得淋漓尽致，长句节奏张弛有度，修辞与对话文采斐然
- 格式规范与标点：各篇普遍遵循了双语对照工程契约，引语与长段对话递进嵌套标点规范，但第26章出现了一处双星号加粗语法硬伤，数个章节存在外文置于中文括号外的倒置排版，第33章标题未规范合并，这些格式瑕疵在修订后即可完全达到定稿出版级标准