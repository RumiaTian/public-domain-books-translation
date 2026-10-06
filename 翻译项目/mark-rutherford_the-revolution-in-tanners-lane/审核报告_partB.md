# 《坦纳巷的革命》（The Revolution in Tanner's Lane）后半卷（第 XIV 至 XXVII 章及尾注）独立审校报告

- **审校日期**：2026-10-06
- **质量等级**：B 良好
- **一句话结论**：后半卷 15 篇译文（原文 41,203 词，译文 61,176 汉字，136 对双语块）文风沉郁凝练、宗派世相与圣经考据极佳，唯在第 XIV 与 XVI 章查出 2 处源文分块时截落的段落级漏译，实事求是定为 B 良好，并提供精确定位与无缝补正代码。

---

## 一、 审校范围与工程基准

### 1. 审校对象与绝对路径
- **工程根目录**：`/Users/hantiantian/Downloads/LittleThings/public-domain-books-translation/翻译项目/mark-rutherford_the-revolution-in-tanners-lane`
- **术语规范基准**：`/Users/hantiantian/Downloads/LittleThings/public-domain-books-translation/翻译项目/mark-rutherford_the-revolution-in-tanners-lane/术语表.md`
- **译文比对目录**：`/Users/hantiantian/Downloads/LittleThings/public-domain-books-translation/翻译项目/mark-rutherford_the-revolution-in-tanners-lane/译文`
- **底本原文目录**：`/Users/hantiantian/Downloads/LittleThings/public-domain-books-translation/翻译项目/mark-rutherford_the-revolution-in-tanners-lane/原文`
- **审校报告产出**：`/Users/hantiantian/Downloads/LittleThings/public-domain-books-translation/翻译项目/mark-rutherford_the-revolution-in-tanners-lane/审核报告_partB.md`

### 2. 篇目覆盖范围（共 15 篇，无一遗漏）
按小说自然章节顺序，100% 逐章逐段精读核对：
1. `the-school-of-adversity-the-sixth-form-thereof.zh-CN.md`（第十四章 苦难的学校：及其最高年级）
2. `end-of-the-beginning.zh-CN.md`（第十五章 开端之终）
3. `cowfold.zh-CN.md`（第十六章 考福尔德）
4. `when-wilt-thou-arise-out-of-thy-sleep-yet-a-little-sleep.zh-CN.md`（第十七章 你何时睡醒呢？再睡片时）
5. `a-religious-picnic.zh-CN.md`（第十八章 宗教野餐）
6. `the-kingdom-of-heaven-is-like-unto-leaven.zh-CN.md`（第十九章 「天国好像面酵」）
7. `the-reverend-thomas-broad-s-exposition-of-romans-8-7.zh-CN.md`（第二十章 托马斯·布罗德牧师讲解《罗马书》八章七节）
8. `the-wisdom-of-the-serpent.zh-CN.md`（第二十一章 蛇的智慧）
9. `the-oracle-warns-after-the-event.zh-CN.md`（第二十二章 神谕示警——总在事后）
10. `further-development.zh-CN.md`（第二十三章 事态的进一步展开）
11. `i-came-not-to-send-peace-but-a-sword.zh-CN.md`（第二十四章 「我来并不是叫地上太平，乃是叫地上动刀兵」）
12. `and-a-man-s-foes-shall-be-they-of-his-own-household.zh-CN.md`（第二十五章 人的仇敌就是自己家里的人）
13. `a-professional-consultation.zh-CN.md`（第二十六章 专业咨询）
14. `mr-broad-s-last-church-meeting-latimer-chapel.zh-CN.md`（第二十七章 布罗德先生最后一次教会会议——拉蒂默礼拜堂）
15. `endnotes.zh-CN.md`（尾注：引诗与古典校注）

### 3. 只读隔离与把关原则
本审校严格恪守出版级外部独立复核规范，执行「只读隔离」红线，未改动任何原译文件。通过自动化全量比对脚本（基于 `difflib` 与字符流分析）结合资深审校肉眼精读，逐行核查语义准确度、宗派历史背景、人物性格刻画与标点符号规范。

---

## 二、 数据层核查与统计

### 1. 各章双语分块与字符统计表

| 章号 | 章节中文标题 | 译文文件名 | 块数 | 原文词数 (块/原档) | 译文汉字数 | 汉字/词比 | 原文吻合度与数据对齐 |
|:---:|:---|:---|:---:|:---:|:---:|:---:|:---|
| **XIV** | 第十四章 苦难的学校：及其最高年级 | `the-school-of-adversity-the-sixth-form-thereof.zh-CN.md` | 19 | 4,932 / 4,961 | 7,156 | 1.45 | 块内缺漏 1 处对话起首句（20 词） |
| **XV** | 第十五章 开端之终 | `end-of-the-beginning.zh-CN.md` | 10 | 2,080 / 2,085 | 3,016 | 1.45 | 100% 完整吻合 |
| **XVI** | 第十六章 考福尔德 | `cowfold.zh-CN.md` | 6 | 4,533 / 4,580 | 6,646 | 1.47 | 块内缺漏 1 处叙事段落（47 词） |
| **XVII** | 第十七章 你何时睡醒呢？再睡片时 | `when-wilt-thou-arise-out-of-thy-sleep-yet-a-little-sleep.zh-CN.md` | 8 | 2,268 / 2,281 | 3,541 | 1.56 | 100% 完整吻合 |
| **XVIII** | 第十八章 宗教野餐 | `a-religious-picnic.zh-CN.md` | 8 | 2,688 / 2,692 | 4,037 | 1.50 | 100% 完整吻合 |
| **XIX** | 第十九章 「天国好像面酵」 | `the-kingdom-of-heaven-is-like-unto-leaven.zh-CN.md` | 2 | 1,528 / 1,537 | 2,374 | 1.55 | 100% 完整吻合 |
| **XX** | 第二十章 托马斯·布罗德牧师讲解《罗马书》八章七节 | `the-reverend-thomas-broad-s-exposition-of-romans-8-7.zh-CN.md` | 11 | 2,125 / 2,136 | 3,192 | 1.50 | 100% 完整吻合 |
| **XXI** | 第二十一章 蛇的智慧 | `the-wisdom-of-the-serpent.zh-CN.md` | 5 | 1,244 / 1,260 | 2,071 | 1.66 | 100% 完整吻合 |
| **XXII** | 第二十二章 神谕示警——总在事后 | `the-oracle-warns-after-the-event.zh-CN.md` | 13 | 2,887 / 2,894 | 3,906 | 1.35 | 100% 完整吻合 |
| **XXIII** | 第二十三章 事态的进一步展开 | `further-development.zh-CN.md` | 10 | 2,338 / 2,341 | 3,461 | 1.48 | 100% 完整吻合 |
| **XXIV** | 第二十四章 「我来并不是叫地上太平，乃是叫地上动刀兵」 | `i-came-not-to-send-peace-but-a-sword.zh-CN.md` | 17 | 5,644 / 5,654 | 8,416 | 1.49 | 100% 完整吻合 |
| **XXV** | 第二十五章 人的仇敌就是自己家里的人 | `and-a-man-s-foes-shall-be-they-of-his-own-household.zh-CN.md` | 9 | 2,731 / 2,744 | 3,925 | 1.44 | 100% 完整吻合 |
| **XXVI** | 第二十六章 专业咨询 | `a-professional-consultation.zh-CN.md` | 9 | 2,723 / 2,727 | 4,118 | 1.51 | 100% 完整吻合 |
| **XXVII** | 第二十七章 布罗德先生最后一次教会会议——拉蒂默礼拜堂 | `mr-broad-s-last-church-meeting-latimer-chapel.zh-CN.md` | 7 | 3,326 / 3,335 | 5,019 | 1.51 | 100% 完整吻合 |
| **Endnotes** | 尾注 | `endnotes.zh-CN.md` | 2 | 156 / 157 | 298 | 1.91 | 100% 完整吻合 |
| **合计** | **后半卷 15 篇全集** | — | **136** | **41,203 / 41,384** | **61,176** | **1.48** | **2 处块切分截落，其余 13 篇完好** |

### 2. 数据层综合分析
1. **块标记成对完备性**：15 个文件中的 `===Original===` 和 `===Chinese===` 标记严格对称（每个文件各有 19、10、6、8、8、2、11、5、13、10、17、9、9、7、2 对，合计 136 对），没有出现任何标记错位、空块、未闭合或多余的标头。
2. **容量与展开比一致性**：全卷汉字数与英文词数比稳定在 1.35～1.66 之间（整卷均值 1.48），尾注因包含双语字词对译及苏格兰古英语注释，展开比达 1.91，整体比例高度均衡，不存在恶性扩译或大面积萎缩。
3. **差异源头排查**：第 XIV 章（差异 29 词，其中章节标题 9 词，缺失正文 20 词）与第 XVI 章（差异 47 词，全为缺失正文）在底本分块阶段发生脱落，直接导致块内原文和对应译文缺失。

---

## 三、 九项清单综合评审

### 1. 完整性与覆盖度（Integrity & Completeness）
- **核查结论**：**良好（发现 2 处局部脱落）**。
- **排查结果**：除第 XIV 章和第 XVI 章各存在一处由于上游分块切分遗漏引起的脱文之外，其余 13 篇译文与原文保持 100% 全覆盖对齐，未发现任何截断、跨段错位、尾部丢失或遗漏诗节的情况。

### 2. 语义准确性与忠实度（Accuracy & Fidelity）
- **核查结论**：**极优**。
- **细部考察**：
  - 第 XIV 章济贫院冷酷体制、老看护工詹金斯一生的麻木苍白，译文准确传达了作者对英国旧济贫制度（Poor Law）的锥心之痛。
  - 第 XVI 章对考福尔德省城日常的世态白描（正餐与茶点的生活转折点、小镇的茶桌心理学、杂货铺与五金店的兼业现象），精准细腻，绝无含糊。
  - 第 XX 章托马斯讲道中所谓「救赎的形而上学」（metaphysics of Redemption）与通俗化「加大拉的猪」的讽刺对比、波琳以小剪刀刻下十字的烈性反击，语义拿捏分毫不差。
  - 第 XXIV 章撒迦利亚与青年乔治关于「起义 vs 无休止辩论」的思想交锋，译文沉郁雄健，极富政治哲理深度。

### 3. 术语一致性与专名规范（Terminology & Consistency）
- **核查结论**：**完全合规**。
- **执行情况**：
  - 核心主角与配角：撒迦利亚·科尔曼（Zachariah Coleman）、让·凯约（Jean Caillaud）、波琳（Pauline）、梅特兰少校（Major Maitland）、纳丁（Nadin）、卡特太太（Mrs. Carter）全书统一。
  - 考福尔德人物群像：约翰·布罗德牧师（Reverend John Broad）、布罗德太太（Mrs. Broad，原弗拉维尔博士之女）、托马斯·布罗德（Thomas Broad / 汤米 Tommy / 汤姆 Tom）、普丽西拉（Priscilla）、特里福莎（Tryphosa）、艾萨克·艾伦（Isaac Allen）、乔治·艾伦（George Allen）、范妮·艾伦（Fanny Allen）、巴顿保姆（Nurse Barton）、布舍尔弟兄（Brother Bushel）、韦恩赖特弟兄（Brother Wainwright）、斯科顿弟兄（Brother Scotton）前后丝丝入扣。
  - 地名与名胜：考福尔德（Cowfold）、坦纳斯巷（Tanner's Lane）、拉蒂默礼拜堂（Latimer Chapel）、北街（North Street）、肖特树林（Shott Woods）、希普盖特（Sheepgate）、哈克斯顿绿地（Hackston Green）、布尔斯克罗斯（Bull's Cross）、黑乡（Black Country）、皮丁戈尔德（Piddingfold）、乔治与蓝野猪旅馆（George and Blue Boar）完全遵循 `术语表.md`。
  - 宗教宗派与机构：独立派（Independents）、卫斯理宗（Wesleyan）、严格浸信会（strict Baptist）、琐珥（Zoar）、反律法主义（Antinomian）、国教会（the Establishment）。

### 4. 典故与圣经引文考证（Biblical & Classical Allusions）
- **核查结论**：**极优**。
- **考据亮点**：
  - **圣经经文与和合本对勘**：
    - 申 12:13：「你要谨慎，不可在你所看中的各处献燔祭」（第 XXIV 章）
    - 罗 8:7：「原来体贴肉体的，就是与神为仇……也是不能服」（第 XX 章）
    - 太 10:34：「我来并不是叫地上太平，乃是叫地上动刀兵」（第 XXIV 章）
    - 太 10:36：「人的仇敌就是自己家里的人」（第 XXV 章）
    - 彼后 1:10：「务要殷勤，使你所蒙的恩召和拣选坚定不移」（第 XXIV 章）
    - 出 32:26：「凡属耶和华的，都要到我这里来」（第 XXIV 章）
    - 加 2:20：「我已经与基督同钉十字架……现在活着的不再是我，乃是基督在我里面活着」（第 XXVII 章）
    - 林前 14:8：「号筒发的声音无定」（第 XXVII 章）
  - **古典文学神学双关**：
    - 第 XXVII 章核心神学概念 `at*one*ment` 巧妙拆解为「救赎（Atonement）……原是一种『合而为一』（at-*one*-ment）」，精准还原了怀特对维多利亚晚期新神学思潮的深刻捕捉。
    - 第 XXVI 章拉丁语成语 `via media` 译为「中间路线」，刻画出布罗德牧师和稀泥的狡黠。
    - 第 XXIV 章托马斯·厄·肯培《效法基督》（*Imitation of Christ*）引语译文肃穆静谧，极见功力。
    - 第 XXV 章约翰逊博士《闲散者》（*The Idler*）引言援引罗马皇帝奥古斯都谢幕典故，典雅渊雅。

### 5. 语言文学质感与文体风格（Literary Quality & Style）
- **核查结论**：**极优**。
- **质感评价**：怀特（Mark Rutherford）特有的内敛、克制、省察、省去多余形容词的清教徒式散文在中文里得到了纯正还原。剔除了当下翻译腔中泛滥的各种生硬连词与套话，句式短促有力，节奏沉稳。
  - 例如第 XXII 章写乔治人生的头一个失眠之夜：「头一个不眠之夜是何等的纪元啊——那一夜，命运之神头一回猛拧我们一把，把我们从对生命的热爱里拧松下来；那一夜，我们头一回对自己说：世上还有比死更坏的事！」（*What an epoch is the first sleepless night—the night when the first wrench has been given us by the Destinies to loosen us from the love of life; when we have first said to ourselves that there are worse things than death!*）
  - 又如第 XXIV 章波琳的论殉道名段：「然而殉道的至高一式，甚至不是为着一项事业而活，而是没有事业也照样活下去，只因活着是你的本分。倘若你蒙召为一桩大真理作证，那么在火焰里唱歌是容易的。是啊，是啊，乔治先生，我要封圣的圣徒，不是那些为事业殉道的人，而是那些根本没有事业的人。」文学感染力极强。

### 6. 对话口吻与阶层性格还原（Dialogue & Characterization）
- **核查结论**：**极优**。
- **人物声音辨识度**：
  - **老巴顿保姆**的乡野口吻（用「俺」「玩意儿」「张狂作态、眼高于顶」）与朴素温情跃然纸上；
  - **布舍尔弟兄**因脖子短、说话断断续续摇头晃脑的农民腔（「俺跟着布舍尔弟兄，*俺*是跟着的」「俺反对一切文书」）栩栩如生；
  - **布罗德牧师**张口闭口分条列目、随时引经据典自卫的假道学官僚嘴脸令人拍案叫绝；
  - **普丽西拉**的娇怯迟钝、不知世事，与乔治谈关税时的鸡同鸭讲，生活化讽刺意味十足。

### 7. 标点与格式排版规范（Punctuation & Formatting）
- **核查结论**：**完全达标**。
- **规范核验**：
  - 中文文本内半角标点检出为 0；
  - 直角引号「」与内层双引号『』层级严整，全卷配对数完全一致；
  - 英文括号 `(...)` 在正文中仅用于首次专有名词对照附注，符合 `术语表.md` 规定；
  - 书名号《》、引文块 `>` 排版规范统一。

### 8. 结构对齐与块完整性（Structural Alignment）
- **核查结论**：**优**。
- 136 个分块严格保持 `===Original===` 与 `===Chinese===` 上下对应，无错位串行。第 XIV 与 XVI 章的两处脱落发生在分块生成阶段（源文本被截留），属于「块内容漏句」，而非「分块结构错位」。

### 9. 总体出版预备度与工程交付标准（Publication Readiness）
- **综合评定**：全卷 15 篇具备极高的出版底稿品质；只需将本报告第四节中提供的两处精确定位代码打入对应文件，Part B 即可 100% 无瑕达到出版预备级（Grade A）。

---

## 四、 审核发现与问题明细表

在本次全量逐段精读独立审校中，严格按质检门禁识别出 **2 处 A 级缺陷（文本漏译/源文漏块）**，未发现严重误译或术语冲突。具体定位与无缝修复补丁如下：

---

### 问题 1：【A 级缺陷 · 句子与对话导言漏译】第 XIV 章
- **文件路径**：`the-school-of-adversity-the-sixth-form-thereof.zh-CN.md`
- **定位坐标**：第 15 块（约第 309-324 行之间）
- **缺陷说明**：
  在底本中，撒迦利亚在屋外星空下漫步回屋后，原本有夫妻二人次日傍晚相对默坐、丈夫首先发话询问的交代：
  `The next evening, after they had sat dumb for some moments, he said, “My dear, you don’t seem well.”`
  译文文件在切分分块时，第 15 块的 `===Original===` 突兀地直接跳到妻子的回答：
  `“I am not well, as you know. You yourself don’t seem well.”`
  对应第 15 块的 `===Chinese===` 也直接跳到：
  `「我不好，你是知道的。你自己看上去也不好。」`
  导致前情起因与撒迦利亚的发话完全缺失，语境衔接断裂。
- **原文遗漏内容**：
  ```text
  The next evening, after they had sat dumb for some moments, he said, “My dear, you don’t seem well.”
  ```
- **拟补正译文**：
  ```text
  第二天傍晚，他们相对默坐了片刻，他说：「亲爱的，你身子好像不舒服。」
  ```
- **建议修复方案**：
  将第 15 块的 `===Original===` 及 `===Chinese===` 首部修正为包含此句：
  ```markdown
  ===Original===
  The next evening, after they had sat dumb for some moments, he said, “My dear, you don’t seem well.”

  “I am not well, as you know. You yourself don’t seem well.”

  ===Chinese===
  第二天傍晚，他们相对默坐了片刻，他说：「亲爱的，你身子好像不舒服。」

  「我不好，你是知道的。你自己看上去也不好。」
  ```

---

### 问题 2：【A 级缺陷 · 关键叙事段落漏译】第 XVI 章
- **文件路径**：`cowfold.zh-CN.md`
- **定位坐标**：第 6 块（约第 58-61 行之间）
- **缺陷说明**：
  在讲述安妮女王时代的故主与门第悬殊的平民妻子成婚、并立方尖碑悼念亡妻的段落中，底本原文在「...casting her in the scale, father, mother, and friends were as gossamer.」之后紧接着有两整句交代其妻子恰于成婚整两年之日离世、青年伯爵痛失至爱形单影只的关键叙事背景：
  `She died two years after the wedding—to the very day. Rich in her love, he had never taken a thought to propitiate anybody, nor to make friends with the Mammon of Unrighteousness; and when she suddenly departed, he turned round and found himself alone.`
  而在译文文件的第 6 块中，英文 `===Original===` 和中文 `===Chinese===` 均被截断遗漏，译文直接从「父母亲友轻得如同蛛丝」跳到了「他非但不去叩世人的门」，读者在尚未得知妻子去世的情况下读到后文，叙事因果与方尖碑立碑动机产生脱节。
- **原文遗漏内容**：
  ```text
  She died two years after the wedding—to the very day. Rich in her love, he had never taken a thought to propitiate anybody, nor to make friends with the Mammon of Unrighteousness, and when she suddenly departed, he turned round and found himself alone.
  ```
- **拟补正译文**：
  ```text
  成婚整整两年的那一天，她撒手人寰。因有她的爱，他已别无所求，从不曾动念讨好任何人，也不曾去结交不义的钱财；而当她猝然离世，他转过身来，发现只剩自己形单影只。
  ```
- **建议修复方案**：
  在第 6 块中定位该处，将中英对应位置补齐：
  ```markdown
  ===Original===
  He had made enemies of them all; but he won his wife, and, casting her in the scale, father, mother, and friends were as gossamer. She died two years after the wedding—to the very day. Rich in her love, he had never taken a thought to propitiate anybody, nor to make friends with the Mammon of Unrighteousness, and when she suddenly departed, he turned round and found himself alone. So far from knocking at men’s doors, he more fiercely hated those who now, touched with pity, would gladly have welcomed him.

  ===Chinese===
  他同他们统统结了怨；但他赢得了妻子，把她往天平上一放，父母亲友轻得如同蛛丝。成婚整整两年的那一天，她撒手人寰。因有她的爱，他已别无所求，从不曾动念讨好任何人，也不曾去结交不义的钱财；而当她猝然离世，他转过身来，发现只剩自己形单影只。他非但不去叩世人的门，反倒更狠地恨那些如今动了怜悯、巴不断欢迎他的人。
  ```

---

## 五、 审校结论

《坦纳巷的革命》后半卷（Part B，第 XIV 至 XXVII 章及尾注，共 15 篇）展现了极为罕见的文学造诣与严谨的宗派历史功底，全卷人物对白生动传神，圣经与古典文学引典考据无可挑剔，标点格式完全符合出版工程规范。

鉴于在第 XIV 章与第 XVI 章发现了两处由于早期分块截断导致的段落/句子级漏译，严格依照审校标准实事求是地评定为 **B 良好**。上述两处问题均已在报告中给出了精确定位与标准补齐代码，修复完成后全卷可直接进入出版定稿程序。
