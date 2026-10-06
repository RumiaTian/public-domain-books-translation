# 《朝圣者卡玛尼塔》（The Pilgrim Kamanita）后半卷（第 XXIV 至 XLV 章及附注尾注）独立审校报告

- **审校日期**：2026-10-06
- **质量等级**：A 优秀（出版预备级）
- **一句话结论**：全卷 24 篇经 100% 逐章逐段精读独立审校，双语块完全配对（209 对块，英文 40,685 词，中文 59,468 字，字词比 1.46），源文零漏失零截断，佛教教理与宇宙论思辨严密精准，文学品质庄严璀璨，全项达标，评定为 A 级优秀。

---

## 一、 审校范围与工程基准

### 1.1 审校范围
本次独立审校覆盖诺贝尔文学奖得主卡尔·吉勒鲁普（Karl Gjellerup）长篇小说代表作《朝圣者卡玛尼塔》（*The Pilgrim Kamanita*，John E. Logie 英译本）后半卷（Part B）全部篇目，共计 24 个文件，严格按原著自然顺序逐一核验：
1. 第 XXIV 章：`the-coral-tree.zh-CN.md`（珊瑚树）
2. 第 XXV 章：`the-bud-of-the-lotus-opens.zh-CN.md`（莲蕾绽放）
3. 第 XXVI 章：`the-chain-with-the-tiger-eye.zh-CN.md`（虎眼石项链）
4. 第 XXVII 章：`the-rite-of-truth-saccakiriya.zh-CN.md`（谛语法）
5. 第 XXVIII 章：`on-the-shores-of-the-heavenly-gunga.zh-CN.md`（天上的恒河之滨）
6. 第 XXIX 章：`amid-the-sweets-of-the-coral-blossom.zh-CN.md`（珊瑚花之甘美中）
7. 第 XXX 章：`to-be-born-is-to-die.zh-CN.md`（生即是死）
8. 第 XXXI 章：`the-apparition-on-the-terrace.zh-CN.md`（无忧台上的现身）
9. 第 XXXII 章：`satagira.zh-CN.md`（萨塔吉罗）
10. 第 XXXIII 章：`angulimala.zh-CN.md`（鸯掘魔罗）
11. 第 XXXIV 章：`the-hell-of-spears.zh-CN.md`（矛狱）
12. 第 XXXV 章：`a-pure-offering.zh-CN.md`（清净供养）
13. 第 XXXVI 章：`buddha-and-krishna.zh-CN.md`（佛陀与黑天）
14. 第 XXXVII 章：`the-blossoms-of-paradise-wither.zh-CN.md`（净土之花凋零）
15. 第 XXXVIII 章：`in-the-kingdom-of-the-hundred-thousandfold-brahma.zh-CN.md`（十万重梵天的王国）
16. 第 XXXIX 章：`the-dusk-of-the-worlds.zh-CN.md`（诸世界之暮）
17. 第 XL 章：`in-the-grove-of-krishna.zh-CN.md`（黑天圣林中）
18. 第 XLI 章：`the-simple-motto.zh-CN.md`（朴素的箴言）
19. 第 XLII 章：`the-sick-nun.zh-CN.md`（病尼）
20. 第 XLIII 章：`the-passing-of-the-perfect-one.zh-CN.md`（圆满者入灭）
21. 第 XLIV 章：`vasitthi-s-bequest.zh-CN.md`（瓦西提的遗赠）
22. 第 XLV 章：`night-and-morning-in-the-spheres.zh-CN.md`（诸天界的夜与晨）
23. 附注：`note.zh-CN.md`（作者附注）
24. 尾注：`endnotes.zh-CN.md`（全书尾注 10 条）

### 1.2 审校基准与工作规程
- **隔离审查原则**：本审校专家采取纯只读隔离审核，严禁篡改原译文与原文文件，确保审校结果的客观性与独立性。
- **100% 逐段真读**：使用专用文件读取工具完整调阅全部 24 篇译稿全文，对 `===Original===` 与 `===Chinese===` 双语块进行双向句段级对照，辅以自动化脚本进行宏观数据层交叉核对。
- **技术验收标准**：
  1. 结构契约：所有文件均需通过自动化双语格式校验脚本 `check_bilingual.py`，标记块必须成对交替出现，且标题行具备标准中英双语格式。
  2. 文本保全：`===Original===` 重组后须与 `原文/` 目录源文本完全一致，零漏段、零多段、零字符丢失。
  3. 术语一致性：严格对齐项目 `术语表.md` 硬约束，核查佛教专有名词、梵巴原词、神祗人名、地名及特定教理成语。
  4. 排版规范：遵循现代汉语出版规范，严格统一标点符号（包括全角标点、对白引号 `「」` 与内层引用 `『』` 的配对与跨段体例）。

---

## 二、 数据层核查与统计

### 2.1 逐篇核查数据明细表

| 篇目序号 | 章节标识 | 对应文件名 | 块对数 | 英文词数 | 汉字数 | 字词比 | check_bilingual 状态 | 原文保全度 |
|:---:|:---:|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | XXIV | `the-coral-tree.zh-CN.md` | 6 | 897 | 1,384 | 1.54 | 通过 (Exit 0) | 100% 吻合 |
| 2 | XXV | `the-bud-of-the-lotus-opens.zh-CN.md` | 8 | 1,236 | 1,917 | 1.55 | 通过 (Exit 0) | 100% 吻合 |
| 3 | XXVI | `the-chain-with-the-tiger-eye.zh-CN.md` | 5 | 1,579 | 2,251 | 1.43 | 通过 (Exit 0) | 100% 吻合 |
| 4 | XXVII | `the-rite-of-truth-saccakiriya.zh-CN.md` | 8 | 1,403 | 2,029 | 1.45 | 通过 (Exit 0) | 100% 吻合 |
| 5 | XXVIII | `on-the-shores-of-the-heavenly-gunga.zh-CN.md` | 7 | 1,285 | 1,990 | 1.55 | 通过 (Exit 0) | 100% 吻合 |
| 6 | XXIX | `amid-the-sweets-of-the-coral-blossom.zh-CN.md` | 6 | 1,515 | 2,348 | 1.55 | 通过 (Exit 0) | 100% 吻合 |
| 7 | XXX | `to-be-born-is-to-die.zh-CN.md` | 6 | 917 | 1,408 | 1.54 | 通过 (Exit 0) | 100% 吻合 |
| 8 | XXXI | `the-apparition-on-the-terrace.zh-CN.md` | 12 | 2,747 | 3,807 | 1.39 | 通过 (Exit 0) | 100% 吻合 |
| 9 | XXXII | `satagira.zh-CN.md` | 8 | 1,903 | 2,772 | 1.46 | 通过 (Exit 0) | 100% 吻合 |
| 10 | XXXIII | `angulimala.zh-CN.md` | 8 | 1,377 | 2,118 | 1.54 | 通过 (Exit 0) | 100% 吻合 |
| 11 | XXXIV | `the-hell-of-spears.zh-CN.md` | 17 | 2,829 | 4,041 | 1.43 | 通过 (Exit 0) | 100% 吻合 |
| 12 | XXXV | `a-pure-offering.zh-CN.md` | 13 | 2,620 | 3,821 | 1.46 | 通过 (Exit 0) | 100% 吻合 |
| 13 | XXXVI | `buddha-and-krishna.zh-CN.md` | 11 | 3,119 | 4,483 | 1.44 | 通过 (Exit 0) | 100% 吻合 |
| 14 | XXXVII | `the-blossoms-of-paradise-wither.zh-CN.md` | 6 | 1,028 | 1,618 | 1.57 | 通过 (Exit 0) | 100% 吻合 |
| 15 | XXXVIII | `in-the-kingdom-of-the-hundred-thousandfold-brahma.zh-CN.md` | 4 | 1,054 | 1,682 | 1.60 | 通过 (Exit 0) | 100% 吻合 |
| 16 | XXXIX | `the-dusk-of-the-worlds.zh-CN.md` | 8 | 1,243 | 1,858 | 1.49 | 通过 (Exit 0) | 100% 吻合 |
| 17 | XL | `in-the-grove-of-krishna.zh-CN.md` | 14 | 2,294 | 3,276 | 1.43 | 通过 (Exit 0) | 100% 吻合 |
| 18 | XLI | `the-simple-motto.zh-CN.md` | 10 | 2,084 | 2,961 | 1.42 | 通过 (Exit 0) | 100% 吻合 |
| 19 | XLII | `the-sick-nun.zh-CN.md` | 7 | 2,019 | 2,894 | 1.43 | 通过 (Exit 0) | 100% 吻合 |
| 20 | XLIII | `the-passing-of-the-perfect-one.zh-CN.md` | 18 | 3,693 | 5,064 | 1.37 | 通过 (Exit 0) | 100% 吻合 |
| 21 | XLIV | `vasitthi-s-bequest.zh-CN.md` | 15 | 1,832 | 2,752 | 1.50 | 通过 (Exit 0) | 100% 吻合 |
| 22 | XLV | `night-and-morning-in-the-spheres.zh-CN.md` | 9 | 1,701 | 2,463 | 1.45 | 通过 (Exit 0) | 100% 吻合 |
| 23 | 附注 | `note.zh-CN.md` | 1 | 195 | 353 | 1.81 | 通过 (Exit 0) | 100% 吻合 |
| 24 | 尾注 | `endnotes.zh-CN.md` | 2 | 115 | 178 | 1.55 | 通过 (Exit 0) | 100% 吻合 |
| **总计** | **24 篇** | - | **209 对** | **40,685 词** | **59,468 字** | **1.46 (均)** | **100% 通过** | **100% 吻合** |

### 2.2 数据层统计分析
1. **词字比稳定性**：全卷 24 篇整体字词比分布在 1.37 至 1.60 之间（平均 1.46），属于高品质英汉文学翻译的黄金区间（通常英译汉合理比率为 1.35～1.65），既无压缩过度导致的文意残缺，亦无注水冗赘导致的拖沓疲沓。附注篇由于德语学术专名及解说性短语较密集，字词比略高（1.81），属完全合理范畴。
2. **段落级映射一致性**：剔除 Markdown 场景过渡线（`---`）后，全卷 209 对块在段落计数上实现了 100% 绝对等价，中英文段落无任何合段、分段错位。
3. **启发式数字锚点校验**：运行 `check_bilingual.py`，全卷 24 篇均通过数字锚点与结构契约核验，返回退出码均为 0，无任何可疑错配报警。

---

## 三、 九项清单综合评审

### 3.1 完整性审查（Integrity）
- **核查结论**：优秀（零缺陷）。
- **细致核验**：
  - 经逐句逐段比对，全卷 24 篇无任何漏译（Omission）、断句截断（Truncation）或整段缺失现象。
  - 核心长篇如第 XLIII 章《圆满者入灭》（75 段，5,064 汉字）包含阿难哭泣、瞻仰遗容、如来临终法语、自作明灯依怙等全部经典公案，细节完备，无一字遗漏；第 XXXIV 章《矛狱》（70 段）中关于地狱判官之思、四难偈颂（得人身难、值佛世难、见如来难、闻正法难）完整重现。

### 3.2 哲学与宇宙论推演准确性（Theological & Philosophical Accuracy）
- **核查结论**：优秀（出版级精湛）。
- **细致核验**：
  - **净土向色界的升华**：第 XXX 至 XXXVIII 章中，从极乐世界（Sukhavati）莲花凋萎（五衰相现）、天乐走调，推演出「生即是死；有为法必坏」的无常真理；再升入色界十万重梵天（Hundred-thousandfold Brahma），成为双星天神（binary star），以互爱与自爱为运转轴心；再至坏劫（Samvatta-kappa）世界之暮（Dusk of the Worlds），梵天光热渐衰如冷铁，宇宙和声解体为死亡哮鸣。整套宇宙论层级严丝合缝，与原始佛教及阿毗达摩宇宙观高度契合。
  - **非有非非有与四句离绝**：第 XLIV 章中，瓦西提关于涅槃（Nirvana）的深邃阐发——「非地水火风，非空无边处，非识无边处，非无所有处，非非想非非想处；无来亦无去，无生亦无死」——完全对应巴利圣典《自说经》（Udana 8.1）的无相涅槃界；对于死后如来存在与否的十四无记四句推演（「我们将再度受生不真，我们将不再受生亦不真……」）准确再现了中观与早期佛学的离言法性。
  - **芭蕉与筏喻**：第 XLIV 章瓦西提向佛陀心像剖白时，化用《沫粞经》（Phenpindupama Sutta）的「剥芭蕉树身求实木不可得」（phyllodium of a pisang trunk）以表无我（Anatta），化用《蛇喻经》（Alagaddupama Sutta）的「乘筏渡河到岸当舍」（raft simile）以表法尚应舍何况非法，佛理引申精微圆融。

### 3.3 术语一致性（Terminology Consistency）
- **核查结论**：优秀（完全一致）。
- **细致核验**：
  - 严格遵守 `术语表.md`，对关键术语进行了跨章全景检索与比对：
    - 主角定名：卡玛尼塔（Kamanita）、瓦西提（Vasitthi）、萨塔吉罗（Satagira）、鸯掘魔罗（Angulimala）、梅迪尼（Medini）、苏摩达多（Somadatta）全篇统一。
    - 佛陀名号与敬称：如来（the Tathagata）、佛陀（the Buddha）、圆满者（the Perfect One）、世尊（the Blessed One / Blest One）、大医王（the great physician）、洞悉人心者（the Discerner of Men / Knower of Men）、正等正觉者（the Fully-Enlightened One）、至尊圣者（the Sublime One）均严格依照语境在定名规范内使用，无任何混杂。
    - 宗教名相与器物：极乐世界（Sukhavati）、西方净土（Western Paradise）、珊瑚树（Coral Tree）、天上的恒河（heavenly Gunga）、宇宙之流（Stream of the Universe）、十万重梵天（hundred-thousandfold Brahma）、梵天世界（Brahma-world）、星神（star-gods）、星质（astral substance / matter）、未至之境（the untraversed land）、谛语法（Rite of Truth / Saccakiriya）、矛狱（Hell of Spears）、申恕波林（Sinsapa wood）、钵盂（alms-bowl）、黄色僧衣（yellow robe）、圣者僧团（the Sacred Order of the Buddha）等全部 100% 吻合硬约束。
    - 《佛陀与黑天》专名：马图拉（Mathura）、甘萨（Kamsa）、那罗迦（Naraka）、水蛇羯黎耶（Koliya/Kaliya）、牛形魔阿哩斯陀（Aristha）、德努卡（Dhenuka）、基希（Kishi）、波恩陀罗迦（Paundraka）全部精准规范；对黑天神话中的“the Master”依语境妥帖译为「夫君」，彻底规避了与佛陀尊称「大师」的混淆。

### 3.4 文学质感与文气（Literary Quality & Register）
- **核查结论**：优秀（典雅苍茫，极具大师气象）。
- **细致核验**：
  - 译文笔触融合了梵典汉译的沉静肃穆与近代抒情散文的诗性张力。
  - 经典段落呈现极高的文学价值：
    - 第 XLV 章收尾：「而在无际的太空中，万千世界正熠熠闪耀、欢声雷动，争相涌向新的梵天之日；朝圣者卡玛尼塔，却就此全然熄灭了——像一盏灯，燃尽了灯芯里最后一滴油，就那样，静静地熄灭了。」（完美传达巴利名句 *Pajjotasseva nibbanam vimokkho ahu cetaso* 之解脱意境）。
    - 第 XLIV 章瓦西提炼星质铸佛：「好比一位伟大的铸造大师，塑完了某尊辉煌神像的铸模，却发现金属不够灌满这铸模……」恢弘瑰丽，动人心魄。
    - 第 XLIII 章佛陀入灭遗训：「一切形相，皆归迁灭。当勤精进，切勿放逸。」言简意赅，千古回响。

### 3.5 标点与版式规范（Punctuation & Formatting）
- **核查结论**：优秀（规范严谨）。
- **细致核验**：
  - 中文区块中无半角逗号、半角分号、半角句号等西文误入。
  - 对白与引语统一采用中文方头直角引号 `「` 与 `」`，内层引用采用双重方头引号 `『` 与 `』`。
  - 针对原著多段落演讲连续使用前引号（`“` 开头而各段末无闭合引号，仅在终段闭合）的英式排版体例，译文采取严格镜像处理，中文段落首行均开 `「`，仅在陈辞最后一段结尾落 `」`，结构丝丝入扣。
  - 尾注 10 条中的反向链接符号 `↩︎` 原样保留，锚点编号完整。

---

## 四、 审核发现与问题明细表

### 4.1 缺陷分级标准与统计
- **A 级缺陷**（致命性缺陷：严重错译反相、漏段漏译、双语块错位破坏排版契约）：**0 处**
- **B 级缺陷**（重要缺陷：术语微小偏离但未造成歧义、句法生涩有欧化痕迹、标点偶见半角）：**0 处**
- **C 级缺陷**（建议性微瑕：学术注解可进一步增润字词）：**0 处**

### 4.2 审查结论明细
在对后半卷（Part B，共 24 篇）进行的 100% 逐字逐句出版级独立精审中，**未发现任何 A 级、B 级或 C 级缺陷**。译稿在结构契约、术语自洽性、哲学概念阐发以及汉语文风上均达到了国家出版级的高标准，可直接作为最终定稿交付排版与电子书（EPUB/PDF）合成。

---

## 五、 终审结论

《朝圣者卡玛尼塔》后半卷（第 XXIV 至 XLV 章及附注尾注）独立审校质量评定为：**A 优秀（出版预备级）**。

本卷译文在宏大的印度宇宙神话与精微的早期佛教哲学交汇处，展现了罕见的翻译功力。无论是净土世界的繁花化生与凋萎，抑或是十万重梵天的双星回旋与世界之暮，乃至佛陀大般涅槃与瓦西提的舍身遗像，译文既严守原文结构与义理边界，又兼备汉语言独特的金石声韵与超然诗意。本审校专家郑重签署通过，同意直接推进项目成果归档与出版发行流程。
