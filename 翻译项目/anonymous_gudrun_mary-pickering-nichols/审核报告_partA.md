# 《古德伦》前半卷独立审校报告

- 审校日期：2026-10-23
- 质量等级：A级优秀
- 一句话结论：前半卷全十七篇对照通读完毕，双语结构对齐严格无脱漏，核心专名完全契合术语表，诗体叙事凝练古雅且具中世纪德语史诗质感，综合评定为A级

---

## 一、审校范围与工程基准

- 审校对象：《古德伦》（Gudrun）前半卷（Part A）
- 篇目清单：共计17篇独立双语对照文档
- 篇目详细列表：
  - 01-preface.zh-CN.md：前言（Preface）
  - 02-names-of-persons.zh-CN.md：人名表（Names of Persons）
  - 03-names-of-places.zh-CN.md：地名表（Names of Places）
  - 04-how-hagen-was-carried-off-by-the-griffin.zh-CN.md：第一诗章 哈根如何被狮鹫掳走（Tale I）
  - 05-how-hagen-slew-the-griffin.zh-CN.md：第二诗章 哈根如何诛杀狮鹫（Tale II）
  - 06-how-hagen-sailed-to-his-home.zh-CN.md：第三诗章 哈根扬帆归故里（Tale III）
  - 07-how-hagen-was-met-by-his-father-and-mother.zh-CN.md：第四诗章 哈根如何与父母相会（Tale IV）
  - 08-how-w-te-was-sent-to-ireland-as-a-suitor.zh-CN.md：第五诗章 瓦特如何奉命前往爱尔兰求亲（Tale V）
  - 09-how-sweetly-horant-sang.zh-CN.md：第六诗章 霍兰特唱得何等甜美（Tale VI）
  - 10-how-the-maidens-came-to-see-the-ship-and-were-carried-to-hettel-s-kingdom.zh-CN.md：第七诗章 少女们如何来看船并被载往黑特尔的王国（Tale VII）
  - 11-how-hagen-followed-his-daughter.zh-CN.md：第八诗章 哈根如何追赶他的女儿（Tale VIII）
  - 12-how-gudrun-was-sought-by-siegfried.zh-CN.md：第九诗章 西格弗里德如何求娶古德伦（Tale IX）
  - 13-how-hartmut-sent-to-woo-gudrun.zh-CN.md：第十诗章 哈特穆特如何遣使向古德伦求亲（Tale X）
  - 14-how-herwic-sent-to-seek-gudrun-and-how-hartmut-came-himself.zh-CN.md：第十一诗章 赫尔维克如何遣使求娶古德伦、哈特穆特如何亲自前来（Tale XI）
  - 15-how-herwic-made-war-on-hettel-and-how-gudrun-was-betrothed-to-him.zh-CN.md：第十二诗章 赫尔维克如何向黑特尔兴兵，古德伦如何与他订婚（Tale XII）
  - 16-how-siegfried-made-war-against-herwic.zh-CN.md：第十三诗章 西格弗里德如何向赫尔维克兴兵（Tale XIII）
  - 17-how-hettel-sent-tidings-from-herwic-s-land.zh-CN.md：第十四诗章 黑特尔如何从赫尔维克的国土传来音讯（Tale XIV）
- 工作模式：100% 逐块逐段对照精读，结合 check_bilingual.py 校验工程标记与结构契约，严守只读隔离，不改动任何原文与译文文件

---

## 二、主要缺陷与修改建议

### 发现的问题与建议
- 前半卷经逐段对照通读与脚本扫描，未发现A级重大缺陷（漏译、截断、严重逻辑反转均为0处）
- 未发现B级格式硬伤与术语违规，标记对齐率100%，专有名词完全受控
- 长对话续引标记严格遵守多节承接规则，行内无非法外文裸露，无重复段落

---

## 三、综合评审明细

- 完整性：全卷17篇均实现逐诗节逐半行完整对译，无跳段、无截断、无漏译，序言与名表信息完整对应
- 准确性：主客体关系清晰明确，无时间线与因果反转；比武、海战、交锋之动作描写动词选用准确到位
- 术语与命名体系：严格遵照项目术语表执行，古德伦（Gudrun）、哈根（Hagen）、希尔达（Hilda）、黑特尔（Hettel）、奥特温（Ortwin）、哈特穆特（Hartmut）、赫尔维克（Herwic）、西格弗里德（Siegfried）、路德维希（Ludwig）、格尔林德（Gerlind）、瓦特（Wâ-te）、弗鲁特（Fru-te）、霍兰特（Horant）、莫伦克（Morunc）、伊罗尔德（Irold）、西格班德（Sigeband）、乌特（U-te）、格尔（Ger）、希尔德堡（Hildeburg）、黑格林（Hegeling）、施图尔姆兰（Sturmland）、奥特兰（Ortland）、丹麦兰（Daneland）、摩尔兰（Moorland）、西兰（Sealand）、迪特马什（Dietmarsch）、尼夫兰（Nifland）、阿尔扎比（Alzabie）、加拉迪（Garadie）、巴利安（Ballian）、卡迪根（Cardigan）、士瓦本（Suabia）等核心专有名词全局绝对一致，首次出现规范标注外文原名
- 文学质感与中世纪德语史诗风格：译文精准传达了玛丽·皮克林·尼科尔斯（Mary Pickering Nichols）英译底本的中古高地德语史诗韵律感，四行诗节节奏明快稳健，措辞庄重典雅，战斗场面悲壮肃穆，宫廷仪礼与相思唱和语调得体
- 格式规范与标点：各章节标记对完全合规，标题采用中英合并格式，直角引号「」与英文双引号配对逻辑严密，无双星号加粗，无多余空行，双语排版整饬纯净
