# 《自治市司库》（The Borough Treasurer）前半卷（第 1 至 15 章）独立审校报告

- **审校日期**：2026-10-06
- **审校范围**：Part A（第 1 至 15 章，共 15 篇，chapter-1 至 chapter-15）
- **质量等级**：B 良好（出版修定级）
- **一句话结论**：全卷 15 章共 185 个双语块、英文 35,513 词、汉字 57,964 字；古典英伦悬疑探案风格醇正雅达，案情逻辑与术语严密，唯第 8 章遗漏对白 2 段（67 词）、第 10 章缺失 2 处闭合双引号，实事求是定级为 B 良好，已附精确定位与修复代码。

---

## 一、 审校范围与工程基准

### 1. 审校篇目与路径
本报告涵盖 J. S. Fletcher 侦探悬疑名作《自治市司库》（*The Borough Treasurer*）前半卷（Part A）全部 15 个章节：
- 译文目录：`译文/chapter-1.zh-CN.md` 至 `译文/chapter-15.zh-CN.md`
- 原文目录：`原文/chapter-1.md` 至 `原文/chapter-15.md`
- 术语基准：`术语表.md`

### 2. 审校原则与隔离红线
- **只读隔离红线**：本审校全程恪守只读红线，严禁擅自修改原文与译文文件，所有核查结论与修正建议全部收录于本报告。
- **100% 逐章精读**：使用 `view_file` 顺次对指定 15 章进行了 100% 逐行逐块全文肉眼精读与核验，杜绝跳读、抽样或仅核对首尾段。
- **自动化工程辅助**：结合 Python 脚本完成双语块交替对齐、源文覆盖率比对、英汉标点符码平衡、专有名词与高频术语一致性扫描。

---

## 二、 数据层核查与统计

### 1. 逐章数据统计明细表

| 章节编号 | 章节标题 | 对照块数 | 英文词数 | 汉字数 | 汉英比 | 原文吻合度 |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|
| 第 1 章 | I. Blackmail / 第一章 敲诈 | 14 | 2,340 | 4,067 | 1.74 | 100% 吻合 |
| 第 2 章 | II. Crime—and Success / 第二章 罪恶——与成功 | 9 | 2,423 | 3,846 | 1.59 | 100% 吻合 |
| 第 3 章 | III. Murder / 三 谋杀 | 10 | 2,486 | 3,823 | 1.54 | 100% 吻合 |
| 第 4 章 | IV. The Pine Wood / 四 松林 | 10 | 2,374 | 3,691 | 1.55 | 100% 吻合 |
| 第 5 章 | V. The Cord / 五 绳索 | 16 | 2,766 | 4,242 | 1.53 | 100% 吻合 |
| 第 6 章 | VI. The Mayor / 六 市长 | 14 | 2,120 | 3,362 | 1.59 | 100% 吻合 |
| 第 7 章 | VII. Night Work / 七 夜工 | 16 | 2,448 | 3,860 | 1.58 | 100% 吻合 |
| 第 8 章 | VIII. Retained for the Defence / 八 受聘辩护 | 18 | 2,579 | 4,326 | 1.68 | 漏 2 段 (67 词) |
| 第 9 章 | IX. Antecedents / 九 来历 | 15 | 1,919 | 3,298 | 1.72 | 100% 吻合 |
| 第 10 章 | X. The Hole in the Thatch / 十 草顶上的洞 | 7 | 2,556 | 4,256 | 1.67 | 100% 吻合 |
| 第 11 章 | XI. Christopher Pett / 十一 克里斯托弗·佩特 | 14 | 2,454 | 4,076 | 1.66 | 100% 吻合 |
| 第 12 章 | XII. Parental Anxiety / 十二 父亲的焦虑 | 12 | 2,345 | 3,904 | 1.66 | 100% 吻合 |
| 第 13 章 | XIII. The Anonymous Letter / 十三 匿名信 | 12 | 2,278 | 4,041 | 1.77 | 100% 吻合 |
| 第 14 章 | XIV. The Sheet of Figures / 十四 一纸数字 | 8 | 2,487 | 3,867 | 1.55 | 100% 吻合 |
| 第 15 章 | XV. One Thing Leads to Another / 十五 一环扣一环 | 10 | 1,938 | 3,305 | 1.71 | 100% 吻合 |
| **全卷合计** | **Part A（1~15 章总计）** | **185 对** | **35,513** | **57,964** | **1.63** | **除第 8 章缺 2 段外 100% 吻合** |

### 2. 数据层综合分析
1. **结构完备性**：15 卷译文文件的双语块标记 `===Original===` 与 `===Chinese===` 全部交替成对出现，共 185 个对照块，结构对齐度 100%，无断层、无孤立块或标签拼写错误。
2. **文本覆盖率**：原本 1~15 章共 35,580 词。译文文件中提取的英文块为 35,513 词，差额 67 词为第 8 章第 5 对照块内遗漏的对话段落。除该处外，其余 14 个章节的英文块与原书全文本字字吻合。
3. **汉英扩展比**：全卷汉字总数为 57,964，综合汉英比例为 1.63:1。各章汉英比稳定在 1.53 ~ 1.77 之间，符合英汉文学翻译的自然延展区间，既无过分缩写省略，亦无冗余膨胀。

---

## 三、 九项清单综合评审

### 1. 完整性（Completeness）
- **核查结论**：第 1~7 章、第 9~15 章全部 100% 完整，无漏译、无截断、无掉段；
- **异常项**：第 8 章第 5 块末尾遗漏马拉柳与哈伯勒的 2 段争辩对白（英文 67 词），详见第四节 [DEF-A-01]。

### 2. 事实准确性与案情逻辑（Accuracy & Case Logic）
- **关键案情数字**：
  - 房租账目（ch1）：年租 25 镑、季租 6 镑 5 先令（twenty-five pounds a year is six pound five a quarter），核对精确；
  - 斯通纳薪资（ch14）：每周两镑十二先令六便士（two pounds twelve shillings and sixpence per week），换算与行文准确；
  - 遇害现金与首饰（ch4/5/7）：基特利怀表约合 100 镑、身上搜出 20 多镑沙弗林与半沙弗林金币、兑付 5 镑面额钞票数张，数字前后丝丝入扣；
  - 匿名悬赏金（ch13）：挂号信内附 6 张 150 镑面额英格兰银行新钞共计 900 镑；悬赏告示 500 镑，如无果则加倍；
  - 30 年前互助会侵吞案（ch14/15）：侵吞本金 2,000 镑；纸上分别测算 30 年 3.5% 与 5% 单利以及复利金额；
- **案发时间线与在场证明**：
  - 遇害时间：晚 9:00 至 9:15 之间；
  - 科瑟斯通离家时间：晚 8:50 至 9:55（约 1 个小时），10:00 归家并在客厅遇客；
  - 马拉柳打牌时间：晚 10:00 赴诺思罗普议员宅邸打惠斯特牌；
  - 诺思罗普穿过肖山时间：晚 9:45；
  - 警局初审：次日清晨 6:00 抓获哈伯勒，上午 11:00 治安法庭过堂。
  - 各章节时间线在译文中严丝合缝，毫厘不爽。

### 3. 术语一致性（Terminology Consistency）
对照 `术语表.md` 进行全量跨章检索，重点术语完全统一：
- **主要人物**：
  - Anthony Mallalieu 统一为「安东尼·马拉柳」；
  - Milford Cotherstone 统一为「米尔福德·科瑟斯通」；
  - Gifford Brereton 统一为「吉福德·布里尔顿」；
  - Windle Bent 统一为「温德尔·本特」；
  - Kitely 统一为「基特利」；
  - John Harborough / Gentleman Jack 统一为「约翰·哈伯勒」/「绅士杰克」；
  - Avice 统一为「艾维丝」；
  - Herbert Stoner / Bert 统一为「赫伯特·斯通纳」/「伯特」；
  - Miss Pett / Christopher Pett 统一为「佩特小姐」/「克里斯托弗·佩特」；
  - David Myler / Dave 统一为「戴维·迈勒」/「戴夫」；
  - Pursey 统一为「珀西」。
- **地理专名**：
  - Highmarket 统一为「海马基特」；
  - Highmarket Shawl / the Shawl 统一为「海马基特肖山」/「肖山」；
  - Wilchester 统一为「威尔切斯特」；
  - Norcaster 统一为「诺卡斯特」；
  - Darlington 统一为「达灵顿」；
  - High Gill Junction 统一为「海吉尔枢纽站」。
- **官职与机构专名**：
  - Borough Treasurer 在指代科瑟斯通的市政职务时统一为「市政财政官」，在指代 30 年前建房互助会职位时作「司库」，区分合理契合语境；
  - superintendent 统一为「警司」（未出现混淆为警察局长或警督）；
  - police sergeant 统一为「警佐」；
  - magistrate / chief magistrate 统一为「治安法官」/「首席治安官」；
  - Town Clerk 统一为「市镇书记官」；
  - Assizes 统一为「巡回法庭」（威尔切斯特巡回法庭 / 诺卡斯特巡回法庭）；
  - police-court 统一为「治安法庭」；
  - coroner / inquest 统一为「验尸官」/「死因审讯」；
  - barrister / solicitor 严格区分译为「出庭律师」与「事务律师」。

### 4. 文学品质与文风调性（Literary Texture & Tone）
- **叙述腔调**：呈现出典型的英伦古典侦探小说质感，典雅沉稳、练达洗练。例如写科瑟斯通在黑暗办公室中的惊恐心绪、写肖山松林夜间案发现场的清冷压抑，笔触极富沉浸感与出版级文学张力。
- **对白生动度与身份拟合**：
  - 马拉柳的对白透着市侩巨贾的粗中有细、威严自满与内心防范；
  - 科瑟斯通言语急促、神经过敏、焦灼不安，人物跃然纸上；
  - 布里尔顿言辞清峻敏捷，兼具青年绅士的朝气与出庭大律师的缜密；
  - 佩特小姐阴沉乖戾、话带机锋、装聋作哑的市井老妇嘴脸惟妙惟肖；
  - 珀西老先生的高门小民怀旧口吻与小商人打诨自然鲜活。

### 5. 格式规范与标点符码（Typography & Formatting）
- **标点符号**：全面采用符合 GB/T 15834 规范的现代汉语标点（全角引号、逗号、句号、冒号、破折号）；
- **英汉混排**：首现专名采用「中文名（English）」标准括号格式，全角圆括号内保留原文字样，无乱码，无直角单双引号混杂；
- **异常项**：第 10 章第 1 块中文译文结尾处存在 2 处未闭合后引号，详见第四节 [DEF-B-01]。

### 6. 错别字与语病（Grammar & Typos）
- 全卷 5.7 万余字无任何低级错别字、倒装语病或机器翻译的翻译腔（translationese），成语与文雅短语运用妥帖自然（如“众望所归”、“如释重负”、“心照不宣”、“水落石出”等）。

### 7. 专有文化背景还原（Cultural Nuance）
- **英式制度背景**：如 "meat tea" 准确传达为以肉食为主食的英格兰北部黄昏茶点大餐；
- **司法风俗**：如 "special licence" 特许结婚证、"running-knot" 活结、"Thuggeeism" 印度图吉教派扼杀勒杀手法、"Dodson & Fogg" 狄更斯《匹克威克外传》诉讼掮客典故，均处理得圆润贴切，且附带恰当的阐释性融入。

### 8. 叙事连贯性与伏笔追踪（Narrative Consistency）
- 核心伏笔脉络完全贯通：从第 1 章基特利登门以 30 年前威尔切斯特旧案勒索，到第 10 章记事簿神秘代号（`M. & C. v. S.B. cir. 81`），到第 11 章手电筒来源追查与剪贴簿遗赠，再到第 14/15 章斯通纳发现草稿纸演算并远赴达灵顿由珀西老人口中揭开当年马洛斯与奇德福思（Mallows & Chidforth）案真相，线索严密闭环，前后照应无缝。

### 9. 检校隔离红线恪守情况（Isolation Compliance）
- 审校过程严格恪守只读红线，未对原译文做任何原地篡改，所有审核成果均完整结集于本独立报告中。

---

## 四、 审核发现与问题明细表

本审校在 100% 精读核对中共发现 **1 处 A 级缺陷（漏译段落）** 和 **1 处 B 级缺陷（标点未闭合）**，无 C 级缺陷。具体明细及修复方案如下：

---

### [DEF-A-01] 第 8 章：对白遗漏 2 个段落（67 英文词）

- **章节位置**：`译文/chapter-8.zh-CN.md`
- **缺陷级别**：A 级（漏译 / 漏段）
- **行号定位**：第 111~135 行（对照块第 5 块）
- **问题分析**：在哈伯勒与马拉柳在警局对峙的高潮部分，原书接在哈伯勒自辩词“...I could prove my innocence down to the ground! There!”之后，尚有马拉柳的反问及哈伯勒的激烈反驳两段。译文文件的 `===Original===` 与 `===Chinese===` 同步遗漏了这两段，直接跳到了下一块“随本特和布里尔顿从肖山下来的那名警察...”。

#### 原文遗漏文本（67 词）：
```text
“And you won’t say that word?” asked Mallalieu.

“I shan’t! Why? Because it’s not necessary. Why!” demanded Harborough, laughing with an expresssion of genuine contempt. “What is there against me? Naught! As I say, there’s law in this country—there’s such a thing as a jury. Do you believe that any jury would convict a man on what you’ve got? It’s utter nonsense!”
```

#### 建议补全出版级译文：
```text
“你不肯吐那个字？”马拉柳问。

“我不吐！为什么？因为没那个必要。为什么！”哈伯勒逼问道，发出一阵真切轻蔑的笑声。“有什么证据能治我的罪？没有！正如我说的，这个国家是有王法的——还有陪审团呢。你们凭手头那点东西，就信哪家陪审团会给人定罪？简直荒唐透顶！”
```

#### 修复代码补丁参考（针对 `chapter-8.zh-CN.md` 第 111 至 135 行）：
```markdown
<<<<
===Original===

“No!” he answered. “I shan’t say! The truth’ll come out in good time without that. It’s not necessary for me to say. Where I was during the night is my business—nobody else’s.”

“You’ll not tell?” asked Mallalieu.

“I shan’t tell,” replied Harborough.

“You’re in danger, you know,” said Mallalieu.

“In your opinion,” responded Harborough, doggedly. “Not in mine! There’s law in this country. You can arrest me, if you like—but you’ll have your work set to prove that I killed yon old man. No, sir! But—” here he paused, and looking round him, laughed almost maliciously “—but I’ll tell you what I’ll do,” he went on. “I’ll tell you this, if it’ll do you any good—if I liked to say the word, I could prove my innocence down to the ground! There!”

===Chinese===

“不！”他答道。“我不说！不靠这个，真相到时候自会水落石出。我没有必要说。我夜里在哪儿是我自己的事——与旁人无干。”

“你不肯说？”马拉柳问。

“我不说，”哈伯勒答。

“你知道，你这是在往险地里走，”马拉柳说。

“那是你们的看法，”哈伯勒执拗地答道。“不是我的！这个国家是有王法的。你们要愿意，尽可以逮捕我——可要证明是我杀了那个老头儿，你们可得下一番死工夫。不，先生！不过——”说到这里他顿住，环顾四周，笑得近乎不怀好意，“——不过我可以告诉你们我打算怎么办，”他接着说。“要是这话对你们有什么用处，我就说这么一句——只要我肯吐一个字，我就能把我的清白证个底朝天！就这样！”
====
===Original===

“No!” he answered. “I shan’t say! The truth’ll come out in good time without that. It’s not necessary for me to say. Where I was during the night is my business—nobody else’s.”

“You’ll not tell?” asked Mallalieu.

“I shan’t tell,” replied Harborough.

“You’re in danger, you know,” said Mallalieu.

“In your opinion,” responded Harborough, doggedly. “Not in mine! There’s law in this country. You can arrest me, if you like—but you’ll have your work set to prove that I killed yon old man. No, sir! But—” here he paused, and looking round him, laughed almost maliciously “—but I’ll tell you what I’ll do,” he went on. “I’ll tell you this, if it’ll do you any good—if I liked to say the word, I could prove my innocence down to the ground! There!”

“And you won’t say that word?” asked Mallalieu.

“I shan’t! Why? Because it’s not necessary. Why!” demanded Harborough, laughing with an expresssion of genuine contempt. “What is there against me? Naught! As I say, there’s law in this country—there’s such a thing as a jury. Do you believe that any jury would convict a man on what you’ve got? It’s utter nonsense!”

===Chinese===

“不！”他答道。“我不说！不靠这个，真相到时候自会水落石出。我没有必要说。我夜里在哪儿是我自己的事——与旁人无干。”

“你不肯说？”马拉柳问。

“我不说，”哈伯勒答。

“你知道，你这是在往险地里走，”马拉柳说。

“那是你们的看法，”哈伯勒执拗地答道。“不是我的！这个国家是有王法的。你们要愿意，尽可以逮捕我——可要证明是我杀了那个老头儿，你们可得下一番死工夫。不，先生！不过——”说到这里他顿住，环顾四周，笑得近乎不怀好意，“——不过我可以告诉你们我打算怎么办，”他接着说。“要是这话对你们有什么用处，我就说这么一句——只要我肯吐一个字，我就能把我的清白证个底朝天！就这样！”

“你不肯吐那个字？”马拉柳问。

“我不吐！为什么？因为没那个必要。为什么！”哈伯勒逼问道，发出一阵真切轻蔑的笑声。“有什么证据能治我的罪？没有！正如我说的，这个国家是有王法的——还有陪审团呢。你们凭手头那点东西，就信哪家陪审团会给人定罪？简直荒唐透顶！”
>>>>
```

---

### [DEF-B-01] 第 10 章：对白末尾缺失闭合双引号（2 处）

- **章节位置**：`译文/chapter-10.zh-CN.md`
- **缺陷级别**：B 级（格式与排版标点缺陷）
- **行号定位**：第 14 行与第 15 行末尾（对照块第 1 块）
- **问题分析**：本特对白段落末尾与布里尔顿长对白段落末尾均遗漏了闭合双引号 `”`，导致全段引语呈现未闭合状态。

#### 现有文本：
```text
第14行末：...吃烤羊肉，深信不疑是佩特小姐掐死了她的东家！
第15行末：...纯粹为了一时兴起的念头就动了手。
```

#### 建议修复后文本：
```text
第14行末：...吃烤羊肉，深信不疑是佩特小姐掐死了她的东家！”
第15行末：...纯粹为了一时兴起的念头就动了手。”
```

#### 修复代码补丁参考（针对 `chapter-10.zh-CN.md` 第 11 至 18 行）：
```markdown
<<<<
===Chinese===

治安法庭的庭审散场之后，本特（Bent）领着客人回家吃饭，流露出一股强烈而可喜的好奇心。跟所有设法挤进老法院旁听的镇民一样，他对布里尔顿（Brereton）盘问佩特小姐（Miss Pett）的那一番交锋大感兴趣。此刻他就想知道：那到底是什么意思，有什么讲究，跟这桩案子的真正关联又在哪里？
“你该不会是说，你当真疑心那个古怪干瘦的小老太婆吧！”两人在本特的单身汉餐桌旁落座时，他满腹狐疑地嚷道。“可是——你那副神情还真像是在疑心她——连嗓音里都设法掺进了几分这意思！我的好老兄！——这会儿，海马基特（Highmarket）一半的自作聪明之士正坐下来吃烤羊肉，深信不疑是佩特小姐掐死了她的东家！
“哦，为什么不能疑心？”布里尔顿不动声色地问。“说真的，只要正视事实，疑心佩特小姐的理由，跟疑心哈伯勒（Harborough）的理由本来就一样多。十之八九，他们俩都跟你一样清白。就算有那么些对哈伯勒不利的难看证据，可也有一个推定——由她亲口说出的话推出来的——佩特小姐指望着从这老头子的死里得些好处。她是个身板结实、精瘦干练的女人，你又跟我说基特利（Kitely）近来已有些衰弱——你要知道，她未必就杀不了他。亲爱的老兄，杀人的往往是最不像会杀人的人，缘由也千奇百怪：不乏十分体面的女性——就像佩特小姐这样的——纯粹为了一时兴起的念头就动了手。
“你当真疑心她？”本特追问道。“我就是要知道这个。”
“这正是我偏不告诉你的。”布里尔顿答道，笑声颇为和善。“我只告诉你一点：依我看，这桩凶案要么简单得出奇，要么复杂透顶。稍安勿躁——比方说，等克里斯托弗·佩特先生（Mr. Christopher Pett）带着那份遗嘱到了再说。到那时，咱们就能往前推进一大步了。”
====
===Chinese===

治安法庭的庭审散场之后，本特（Bent）领着客人回家吃饭，流露出一股强烈而可喜的好奇心。跟所有设法挤进老法院旁听的镇民一样，他对布里尔顿（Brereton）盘问佩特小姐（Miss Pett）的那一番交锋大感兴趣。此刻他就想知道：那到底是什么意思，有什么讲究，跟这桩案子的真正关联又在哪里？
“你该不会是说，你当真疑心那个古怪干瘦的小老太婆吧！”两人在本特的单身汉餐桌旁落座时，他满腹狐疑地嚷道。“可是——你那副神情还真像是在疑心她——连嗓音里都设法掺进了几分这意思！我的好老兄！——这会儿，海马基特（Highmarket）一半的自作聪明之士正坐下来吃烤羊肉，深信不疑是佩特小姐掐死了她的东家！”
“哦，为什么不能疑心？”布里尔顿不动声色地问。“说真的，只要正视事实，疑心佩特小姐的理由，跟疑心哈伯勒（Harborough）的理由本来就一样多。十之八九，他们俩都跟你一样清白。就算有那么些对哈伯勒不利的难看证据，可也有一个推定——由她亲口说出的话推出来的——佩特小姐指望着从这老头子的死里得些好处。她是个身板结实、精瘦干练的女人，你又跟我说基特利（Kitely）近来已有些衰弱——你要知道，她未必就杀不了他。亲爱的老兄，杀人的往往是最不像会杀人的人，缘由也千奇百怪：不乏十分体面的女性——就像佩特小姐这样的——纯粹为了一时兴起的念头就动了手。”
“你当真疑心她？”本特追问道。“我就是要知道这个。”
“这正是我偏不告诉你的。”布里尔顿答道，笑声颇为和善。“我只告诉你一点：依我看，这桩凶案要么简单得出奇，要么复杂透顶。稍安勿躁——比方说，等克里斯托弗·佩特先生（Mr. Christopher Pett）带着那份遗嘱到了再说。到那时，咱们就能往前推进一大步了。”
>>>>
```

---

## 五、 终审结论与评定等级

1. **定级结论**：依据严苛的国家出版级审校标准，因第 8 章存在 1 处段落漏译（A 级缺陷），且第 10 章存在 1 处标点未闭合（B 级缺陷），本前半卷综合评定为 **B 良好（出版修定级）**。
2. **整改建议**：本报告已提供 100% 精确的修复代码与补译译文。合成脚本或主审责任编辑只需采纳上述两个针对性补丁，即可将全卷质量一举推进至 **A 优秀（出版预备级）**。
