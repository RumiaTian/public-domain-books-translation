# 《古德伦》后半卷独立审校报告

- 审校日期：2026-10-23
- 质量等级：B级良好
- 一句话结论：后半卷全十八篇对照通读完毕，双语结构对齐严格无漏译，专有名词完全契合术语表，诗体叙事稳健流畅，仅第32章第6行存在1处段首残留标记，综合评定为B级

---

## 一、审校范围与工程基准

- 审校对象：《古德伦》（Gudrun）后半卷（Part B）
- 篇目清单：共计18篇独立双语对照文档
- 篇目详细列表：
  - 18-how-hartmut-and-ludwig-carried-away-gudrun.zh-CN.md：第十五诗章 哈特穆特与路德维希如何掳走古德伦（Tale XV）
  - 19-how-they-told-the-kings-that-gudrun-was-carried-off.zh-CN.md：第十六诗章 他们如何向诸王报信古德伦被掳（Tale XVI）
  - 20-how-hettel-with-his-friends-followed-after-the-normans.zh-CN.md：第十七诗章 黑特尔如何与友人们追赶诺曼人（Tale XVII）
  - 21-how-ludwig-slew-hettel-and-stole-away-in-the-night.zh-CN.md：第十八诗章 路德维希如何诛杀黑特尔并在夜色中潜逃（Tale XVIII）
  - 22-how-the-hegelings-went-home-to-their-land.zh-CN.md：第十九诗章 黑格林人如何归返他们的故土（Tale XIX）
  - 23-how-hartmut-and-ludwig-came-to-their-home.zh-CN.md：第二十诗章 哈特穆特与路德维希如何回到他们的家园（Tale XX）
  - 24-how-gudrun-must-wash-clothes-on-the-sea-sands.zh-CN.md：第二十一诗章 古德伦为何须在海边沙滩洗衣（Tale XXI）
  - 25-how-queen-hilda-sent-an-army-to-normandy.zh-CN.md：第二十二诗章 王后希尔达如何遣大军远征诺曼底（Tale XXII）
  - 26-how-the-hegelings-came-to-the-w-lpe-and-cast-anchor.zh-CN.md：第二十三诗章 黑格林人如何抵达维尔彭并抛锚泊舟（Tale XXIII）
  - 27-how-the-angel-in-the-shape-of-a-bird-brought-tidings-to-gudrun.zh-CN.md：第二十四诗章 化为鸟形的天使如何为古德伦带来佳音（Tale XXIV）
  - 28-how-ortwin-and-herwic-found-gudrun-washing-on-the-sands.zh-CN.md：第二十五诗章 奥特温与赫尔维克如何在沙滩上寻见洗衣的古德伦（Tale XXV）
  - 29-how-gudrun-said-she-would-wed-hartmut.zh-CN.md：第二十六诗章 古德伦如何假意应允嫁给哈特穆特（Tale XXVI）
  - 30-how-the-hegelings-attacked-the-castle-by-night.zh-CN.md：第二十七诗章 黑格林人如何趁夜突袭城堡（Tale XXVII）
  - 31-how-ortwin-and-hartmut-fought-before-the-castle.zh-CN.md：第二十八诗章 奥特温与哈特穆特如何在城堡前交锋（Tale XXVIII）
  - 32-how-hartmut-was-taken-prisoner.zh-CN.md：第二十九诗章 哈特穆特如何沦为俘虏（Tale XXIX）
  - 33-how-gudrun-was-brought-home-to-hilda.zh-CN.md：第三十诗章 古德伦如何被接回希尔达身边（Tale XXX）
  - 34-how-the-four-kings-were-wedded-in-hilda-s-land.zh-CN.md：第三十一诗章 四位国王如何在希尔达的国土上成婚（Tale XXXI）
  - 35-how-they-all-went-to-their-homes.zh-CN.md：第三十二诗章 众人如何各归各家（Tale XXXII）
- 工作模式：100% 逐块逐段对照通读，结合 check_bilingual.py 校验工程标记与结构契约，严守只读隔离，不改动任何原文与译文文件

---

## 二、主要缺陷与修改建议

### 发现的问题与建议
- 后半卷经逐段对照通读与脚本扫描，未发现A级致命缺陷（漏译、截断、严重逻辑反转均为0处）
- 发现B级格式瑕疵1处：
  - 章节定位：32-how-hartmut-was-taken-prisoner.zh-CN.md 第6行
  - 具体表现：段首残留编辑标记字符「@@@」，原文为「@@@黑格林人（Hegeling）攻占了城堡，老幼一概不留...」
  - 判定与影响：属于草稿编辑或校对残留标记，不影响正文诗节，但破坏了段落版面整洁
  - 修改建议：删除该行行首3个字符「@@@」，直接以「黑格林人（Hegeling）攻占了城堡...」起笔
- 句式与文风观察（C级）：
  - 跨节长句衔接良好，如第21章stanza 4-5、22章stanza 62-63、25章stanza 46-47、32章stanza 52-53与96-97、33章stanza 28-29等处的跨节从句嵌套，译文主谓宾重组得当，无断句断意现象

---

## 三、综合评审明细

- 完整性：全卷18篇均实现逐诗节逐半行完整对译，无跳段、无截断、无漏译，各章提要概括完整对应
- 准确性：主客体关系严谨清晰，战斗攻防与交战因果逻辑严密，无时间线倒错
- 术语与命名体系：严格遵照项目术语表执行，古德伦（Gudrun）、哈特穆特（Hartmut）、赫尔维克（Herwic）、奥特温（Ortwin）、路德维希（Ludwig）、格尔林德（Gerlind）、希尔达（Hilda）、黑特尔（Hettel）、瓦特（Wâ-te）、弗鲁特（Fru-te）、霍兰特（Horant）、奥特龙（Ortrun）、希尔德堡（Hildeburg）、赫尔加特（Hergart）、西格弗里德（Siegfried）、莫伦克（Morunc/Morung）、伊罗尔德（Irold）等核心人物名与维尔彭沙洲（Wülpensand）、卡西安（Kassian）、马特兰（Matelan）、阿尔扎比（Alzabie）、卡拉迪（Karadie）、西兰（Sealand）、奥特兰（Ortland）、丹麦兰（Daneland）、施图尔姆兰（Sturmisch/Sturmland）、摩尔兰（Moorland）等核心地名全局绝对一致，首次出现规范标注外文原名
- 文学质感与中世纪德语史诗风格：译文精准传达了玛丽·皮克林·尼科尔斯（Mary Pickering Nichols）英译底本的中古高地德语史诗韵律感，四行诗节节奏平稳匀称，沙洲浴血与城堡鏖战肃穆沉雄，雪滩浣衣哀婉动人，大婚休战庄重典雅
- 格式规范与标点：各章节标记对完全合规，标题采用中英合并格式，直角引号「」与英文双引号配对逻辑严密，除第32章第6行1处段首残留标记外，全篇无双星号加粗，无非法外文裸露，无多余空行，双语排版规范
