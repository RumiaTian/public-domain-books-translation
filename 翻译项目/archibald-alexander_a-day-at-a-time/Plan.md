# 翻译计划（Plan.md）— archibald-alexander_a-day-at-a-time

---

## 本计划信息

- **项目名称**：archibald-alexander_a-day-at-a-time（一天一天地过／A Day at a Time, and Other Talks on Life and Religion）
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/小说文学.md
- **术语表**：术语表.md

---

## 文件分工

| 文件 | 作用 | 谁来改 |
|------|------|--------|
| `项目说明.md` | 项目基本信息、领域配置、篇目清单 | 人工 |
| `术语表.md` | 翻译硬约束层。每篇译完补充新词 | agent / 人工 |
| `translation_queue.csv` | 任务队列。每行一文件，`file, size_kb, status` 三列 | 翻译前改 doing，完成后改 done |
| `Plan.md`（本文件） | 执行步骤 + 运行日志 | agent 追加日志 |
| `原文/*.md` | 源文 | 不改 |
| `译文/*.zh-CN.md` | 译文产出（块对照双语） | 翻译 agent 产出 |

---

## translation_queue.csv 格式

```
file,size_kb,status
00-dedication.md,0.2,todo
00-epigraph.md,0.2,todo
01-a-day-at-a-time.md,7.6,todo
...
```

| 字段 | 含义 | 取值 |
|------|------|------|
| `file` | 源文文件名（在 `原文/` 目录下） | 如 `01-a-day-at-a-time.md` |
| `size_kb` | 源文大小（KB）。>50KB 为长文，按通用翻译引擎第七节分段 | 数字 |
| `status` | 翻译状态 | `todo` 待译 / `doing` 翻译中 / `done` 已完成 |

---

## 执行步骤（agent 按此推进，两种模式共用）

> **谁执行**由 `项目说明.md` 的「内容形态」字段决定（见 `WORKFLOW.md`「判断内容形态」）：本项目为短篇集，走**委派模式**，由子代理逐篇执行本流程。无论谁执行，这 9 步不变。

### 1. 读配置（每次翻译前必读）
```
1. 本项目 Plan.md（本文件）
2. 项目说明.md
3. 术语表.md
4. prompts/通用翻译引擎.md
5. prompts/领域配置/小说文学.md
6. 译文/ 下任意一篇已完成的 .zh-CN.md（作为风格黄金样本，照此风格译；无则跳过）
```

### 2. 取任务
读 `translation_queue.csv`，取第一个 `status=todo` 的行。先 `ls 译文/` 检查该篇译文是否已存在：
- 已存在 → 直接改 `done`，跳到步骤 8。
- 不存在 → 把该行 `status` 改为 `doing` 并保存 CSV，继续。

### 3. 读源文
读 `原文/对应文件名`。

### 4. 翻译
产出到 `译文/对应文件名去.md加.zh-CN.md`。

**双语对照格式、标记规则、完整性禁令**：见 `prompts/通用翻译引擎.md` 第五、六节（标记成对、标题合并「英文 / 中文」、不跳过不缩写、UTF-8 无 BOM）。此处不重复。

**本流程专有提醒**：
- 逐块对照原文，绝不漏译、不合并段落、不缩写、不总结，尤其结尾别截断。
- 严守术语表：遇表内源词必译为指定译法。新词自行确定统一译法，首次附原文「中文（English）」。
- 圣经引文按和合本译出；出处行照排不译；`Prayer` 译「祈祷」；`Amen.` 译「阿们。」
- 人名/语气/风格全文一致（各篇独立，但同一人物典故跨篇须与术语表统一），照黄金样本风格译。
- 长文（源文 >50KB）分段处理见通用翻译引擎第七节（本书各篇均 <10KB，无需分段）。

### 5. 自检
- 完整性：源文每一段都在译文 Original 块中出现，末尾无截断。
- 块对称：Original/Chinese 数量相等，每块内段数对应。
- 标题格式：全部「英文 / 中文」合并。
- 术语一致：抽查 5 个术语词，全文译法统一。
- 不满足则改到满足。

### 6. 自动检查
```
python scripts/check_bilingual.py 译文/对应篇名.zh-CN.md
```
结构契约满足（标记成对、标题合并格式、可疑错配少）则继续；有违规回步骤 4 修订。

### 7. 回填状态（双写）
检查通过后，`status` 从 `doing` 改 `done`，改两处：
- ① 项目 `translation_queue.csv` 该行；
- ② 根 `translation_queue.csv` 中 `<本项目名>,<本篇名>` 那一行（`WORKFLOW.md`「双写状态」）。

### 8. 追加日志
在本文件「运行日志」追加一行。

### 9. 循环
回到步骤 2，取下一篇 `todo`，直到全部 `done`。委派模式下由主 agent 决定是否继续派单（见 `WORKFLOW.md`「委派模式调度循环」）。

---

## 篇目清单

| # | 篇名 | 源文 | 状态 |
|---|------|------|------|
| 0 | 献词 | 00-dedication.md | todo |
| 0 | 题词 | 00-epigraph.md | todo |
| I | A Day at a Time | 01-a-day-at-a-time.md | todo |
| II | God in the Wheels | 02-god-in-the-wheels.md | todo |
| III | A Triple Best | 03-a-triple-best.md | todo |
| IV | Finical Farming | 04-finical-farming.md | todo |
| V | The Doctor | 05-the-doctor.md | todo |
| VI | Well and Now | 06-well-and-now.md | todo |
| VII | The “Washen Face” in War Time | 07-the-washen-face-in-war-time.md | todo |
| VIII | The Real Martha | 08-the-real-martha.md | todo |
| IX | Our Unearned Increment | 09-our-unearned-increment.md | todo |
| X | Smoking Wicks | 10-smoking-wicks.md | todo |
| XI | Culpable Goodness | 11-culpable-goodness.md | todo |
| XII | A Khaki Virtue | 12-a-khaki-virtue.md | todo |
| XIII | The Overcoming of Panic | 13-the-overcoming-of-panic.md | todo |
| XIV | The Day’s Darg | 14-the-day-s-darg.md | todo |
| XV | Gashmu the Gossip | 15-gashmu-the-gossip.md | todo |
| XVI | God in Front | 16-god-in-front.md | todo |
| XVII | “Unbelief Kept Quiet” | 17-unbelief-kept-quiet.md | todo |
| XVIII | The Equipment of Joy | 18-the-equipment-of-joy.md | todo |
| XIX | The God of the Unlovable Man | 19-the-god-of-the-unlovable-man.md | todo |
| XX | Under the Juniper Tree | 20-under-the-juniper-tree.md | todo |
| XXI | Instructing the Cabin Boy | 21-instructing-the-cabin-boy.md | todo |
| XXII | God’s Door of Hope | 22-god-s-door-of-hope.md | todo |
| XXIII | Now-a-Days | 23-now-a-days.md | todo |
| XXIV | Roundabout Roads | 24-roundabout-roads.md | todo |
| XXV | The Extravagance of Love | 25-the-extravagance-of-love.md | todo |
| XXVI | The Art of “Doing Without” | 26-the-art-of-doing-without.md | todo |
| XXVII | Wonder | 27-wonder.md | todo |
| XXVIII | The Fatherhood of God | 28-the-fatherhood-of-god.md | todo |
| XXIX | The Unreturning Brave | 29-the-unreturning-brave.md | todo |
| XXX | The Sacrament of Sunset | 30-the-sacrament-of-sunset.md | todo |
| — | Endnotes（尾注） | 31-endnotes.md | todo |

（权威清单以 `translation_queue.csv` 为准）

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
| 2026-09-10 | 00-epigraph.md（题词） | 双语 1 对，check_bilingual 通过（exit 0） | 首篇产出；E. B. Browning 按术语表译「勃朗宁夫人」并首现附原文；诗行结构与源文逐行镜像 |
| 2026-09-10 | 00-dedication.md（献词） | 双语 2 对，check_bilingual 通过（exit 0） | 新书首章；Sir John R. Jellicoe 按术语表译「约翰·杰利科爵士」首现附原文；G.C.B.、K.C.V.O. 照搬；逐行镜像源文行式 |
| 2026-09-10 | 01-a-day-at-a-time.md（I 一天一天地过） | 双语 8 对，check_bilingual 通过（exit 0） | 书名句申 33:25 与太 6:34 按术语表和合本译法锁死；R. D. Blackmore、Mark Rutherford 首现附原文；this great conflict 译「大冲突」、the war 译「大战」；33:27 按和合本「永生的神是你的居所」；引诗、Prayer/阿们照项目说明行式 |
| 2026-09-10 | 02-god-in-the-wheels.md（II 轮中的上帝） | 双语 7 对，check_bilingual 通过（exit 0） | 吉卜林（Rudyard Kipling）、麦卡安德鲁（Macandrew）、帕斯卡（Pascal）首现附原文；结 1:21 题词译「生命的灵在轮中」，出处行照排不译；「双胞胎怪物」按术语表；太 6:9 依和合本「我们在天上的父」；叙述用「上帝」、祈祷呼格依经文语域用「神」；Prayer→祈祷、Amen→阿们照项目说明 |
| 2026-09-10 | 03-a-triple-best.md（III 三重最好） | 双语 6 对，check_bilingual 通过（exit 0） | 乔治·斯蒂芬森（George Stephenson）、卡莱尔（Carlyle）、乔治·艾略特／埃莫斯·巴顿牧师／《教区生活场景》首现附原文；罗 1:17 题词依和合本「义人必因信得生」、出处行照排不译；三重格言锁定「凡事务求最好／逢人想着最好／对己盼望最好」并贯穿全篇；可 14 章香膏两段引文依和合本；「该撒家里的圣徒」按术语表；Prayer→祈祷、Amen.→阿们。 |
| 2026-09-10 | 04-finical-farming.md（IV 过分讲究的耕作） | 双语 6 对，check_bilingual 通过（exit 0） | 传 11:4 题词与 11:6 引文依和合本（「看风的必不撒种，望云的必不收割」「早晨要撒你的种，晚上也不要歇你的手」），出处行照排不译；Agricola 首现附原文「阿格里科拉（Agricola）」；the Preacher＝传道者、the wise man＝智慧人依和合本用语；叙述用「上帝」、经文语境用「神」（依术语表与第 II 篇体例）；「O Lord and Master」译「我们的主、我们的夫子」依约 13:13 称谓对；Prayer→祈祷、Amen→阿们照项目说明行式 |
| 2026-09-10 | 05-the-doctor.md（V 医生） | 双语 7 对，check_bilingual 通过（exit 0） | 太 9:12 题词依和合本「康健的人用不着医生，有病的人才用得着」，出处行照排不译；马修·阿诺德（Matthew Arnold）、贝斯纳尔格林（Bethnal Green）、卢克·菲尔兹（Luke Fildes）首现附原文；阿诺德诗引三行逐行镜像；可 10:45 回声「不是要受人服事，乃是要服事人……作多人的赎价」与可 5:34「平平安安地去吧」依和合本语汇；Good Physician 锁定「良医」；叙述用「上帝」（依第 02、04 篇体例）；Prayer→祈祷、Amen→阿们照项目说明行式 |
| 2026-09-10 | 06-well-and-now.md（VI 做好，趁现在） | 双语 5 对，check_bilingual 通过（exit 0） | 传 9:10 题词与正文重引依和合本「凡你手所当作的事，要尽力去做」，出处行照排不译；西 3:23 依和合本「无论做什么，都要从心里做，像是给主做的」；「黑夜将到」（约 9:4）与「拯救的日子」（林后 6:2）依和合本；奥丽芙·施赖纳（Olive Schreiner）／《梦想》、史蒂文森（Stevenson）、巴格肖特（Bagshot）首现附原文；the Preacher＝传道者；叙述用「上帝」、祈祷呼格用「神」；Prayer→祈祷、Amen.→阿们。照项目说明行式 |
| 2026-09-10 | 07-the-washen-face-in-war-time.md（VII 战时的「洗净的脸」） | 双语 9 对，check_bilingual 通过（exit 0） | 创 43:31 题词与正文重引依和合本「他洗了脸出来，勉强隐忍，吩咐人摆饭」，43:30「急忙寻找可哭之地」「进入自己的屋里，哭了一场」依和合本；太 20:28「多人赎价」依和合本；washen face＝洗净的脸（washen face）方言首现附原文加注，cult of the washen face＝洗净脸的风尚；Lowell＝洛威尔首现附原文，诗节引文按 > 前缀原行式照排；叙述用「上帝」、祈祷呼格用「神」；Prayer→祈祷、Amen.→阿们。照项目说明行式 |
| 2026-09-10 | 08-the-real-martha.md（VIII 真正的马大） | 双语 10 对，check_bilingual 通过（exit 0） | 路 10:42 R.V. 边注题词照排出处行，正文重译「需要的不过几样，甚或只有一样」；Martha／Mary／Lazarus／Bethany 首现附原文，按和合本「马大／马利亚／拉撒路／伯大尼」；约 11:5 引文依和合本「耶稣素来爱马大和她妹子并拉撒路」；Authorised Version＝《钦定本》、King James' translators＝钦定本的译者；the Master 统一「主」；祈祷呼格用「神」，For Thy Name's sake 仿前篇作「为你名的缘故求」；Prayer→祈祷、Amen.→阿们。照项目说明行式 |
| 2026-09-10 | 10-smoking-wicks.md（X 将残的灯火） | 双语 9 对，check_bilingual 通过（exit 0） | 赛 42:3 题词依和合本「将残的灯火，他不吹灭」（呼应「压伤的芦苇，他不折断」语域），出处行照排不译；正文重引 dimly-burning wick 统一「将残的灯火」；约 6:37 依和合本「到我这里来的，我总不丢弃他」；Zaccheus＝撒该按和合本；John Owen＝约翰·欧文首现附原文；两处诗节引文按 > 前缀原行式照排、逐行镜像；fruits of the Spirit＝圣灵的果子（加 5:22 语汇）；叙述用「上帝」、祈祷呼格用「神」、For Jesus's sake 仿前篇作「奉耶稣的名求」；Prayer→祈祷、Amen.→阿们。照项目说明行式 |
| 2026-09-10 | 09-our-unearned-increment.md（IX 不劳而获的增益） | 双语 8 对，check_bilingual 通过（exit 0） | 诗 127:2 题词按作者所倡变体读法译出并保留括注「（在他们睡时）」，出处行照排不译；正文重引统一「上帝在他所爱的人睡时赐给他们」；Providence／providence 统一「眷护」；埃及旷野双隐士橄榄树典故、蜡烛两头烧（太 6 语域）照译；叙述用「上帝」、祈祷呼格用「神」；三十倍、六十倍（可 4 语汇）依和合本；Prayer→祈祷、Amen.→阿们。照项目说明行式 |
| 2026-09-10 | 11-culpable-goodness.md（XI 可责的善行） | 双语 8 对，check_bilingual 通过（exit 0） | 罗 14:16 题词依和合本「不可叫你的善被人毁谤」，出处行照排不译；三大病根锁定「好论断／极端／冷淡」并首现附原文；腓 4:5 依和合本「当叫众人知道你们谦让的心」，太 22:37、太 5:41、西 3:23 依和合本语汇（「尽心爱主你的神」「同他走二里」「从心里做，像是给主做的」）；Robert Louis Stevenson、Ian Maclaren、Bunyan、Dr. Dale of Birmingham、Keble 按术语表首现附原文；crank＝怪人、righteous overmuch＝行义过分（传 7:16 语汇）；call a spade a spade 以「是铲子就说铲子」保留双关；源文引诗硬换行规范化为 > 逐行式（仿第 VII 篇先例）；叙述用「上帝」、祈祷呼格用「神」、For Thy Name's sake 作「为你名的缘故求」；Prayer→祈祷、Amen.→阿们。照项目说明行式 |
| 2026-09-10 | 13-the-overcoming-of-panic.md（XIII 克服恐慌） | 双语 8 对，check_bilingual 通过（exit 0） | 耶 40:6 题词与正文内引统一依和合本「境内剩下的民」语汇；耶 9:2 内引「惟愿我在旷野有行路人住宿之处，使我可以离开我的民出去」；a great gulf fixed 呼应和合本「深渊限定」（路 16:26）；endure hardness 统一「忍受艰难」呼应提后 2:3 精兵语汇；祷文 Thou sendest no man a warfare upon his own charges 用林前 9:7「自备粮饷」语汇；西蒙兹（J. A. Symonds）首现附原文；claustrophobia 病征意译「惧怕封闭」；叙述用「上帝」、祷告经文语域用「神」；Prayer→祈祷、Amen.→阿们。照项目说明行式 |
| 2026-09-10 | 15-gashmu-the-gossip.md（XV 传闲话的基善） | 双语 10 对，check_bilingual 通过（exit 0） | 尼 6:6 题词「Gashmu saith it」依术语表作「是基善说的」，出处行照排不译；Gashmu＝基善首现附原文（和合本基善，Geshem 变体），Sanballat＝参巴拉、Nehemiah＝尼希米按和合本；诗 91 语汇「黑夜行的瘟疫／午间灭人的毒病」；赛 32:2「疲乏之地大磐石的影子」；亚瑟王圆桌骑士誓约按术语表「不进谗言，也不听谗言」；Vestigia nulla retrorsum 照搬加注「（来路无痕）」；Sir Walter Scott＝沃尔特·司各特爵士首现附原文；源文引诗空格缩进+空行交错规范化为 > 逐行式（仿第 VII、XI 篇先例）；叙述用「上帝」、祈祷呼格用「神」；For Thy Name's sake 仿前篇作「为你名的缘故求」；Prayer→祈祷、Amen.→阿们。照项目说明行式 |
| 2026-09-10 | 12-a-khaki-virtue.md（XII 卡其美德） | 双语 7 对，check_bilingual 通过（exit 0） | 林后 9:7 题词依和合本「神喜爱捐得乐意的人」（经文语域用「神」），出处行照排不译；标题 A Khaki Virtue 按术语表作「卡其美德」；cheerfulness／cheerful 全篇统一「快乐／快乐的」（题词经文「捐得乐意」除外）；tholing 按术语表意译加注「硬扛（tholing）」；Bunyan's Christian＝班扬笔下的基督徒（Christian）首现附原文，与泛指基督徒区分；Goldsmith＝哥尔德斯密斯（Goldsmith）首现附原文，carols as he goes＝「且行且唱」；God's in His Heaven＝「上帝在他的天上」（勃朗宁语）；cheerfulness is twice blessed 化用《威尼斯商人》作「双重的祝福：它祝福那拥有的人，也祝福那看见的人」；章末祈祷系史蒂文森祷文引文，整段作 > 引用块照项目说明行式，署名行「— R. L. Stevenson.」照排不译，引文内 Amen 译「阿们。」；源文引诗空格缩进+空行交错规范化为 > 逐行式（仿第 VII、XI、XV 篇先例）；叙述用「上帝」；Prayer→祈祷 |
| 2026-09-10 | 14-the-day-s-darg.md（XIV 一天的活计） | 双语 8 对，check_bilingual 通过（exit 0） | 林前 10:31 题词依和合本「你们无论做什么，都要为荣耀神而行」，出处行照排不译；darg 按术语表作「一天的活计」，标题保留原文（The Day’s Darg），正文 our day’s work 呼应译「我们一天的活计」；出 20:9 依和合本「六日要劳碌做你一切的工」；帖撒罗尼迦人／使徒保罗／彼得按和合本；Van Dyke＝范戴克（Van Dyke）首现附原文；未载经卷语录「举起石头，你就必寻见我；劈开木头，我就在那里」与范戴克诗末行统一译法；源文引诗空格缩进+空行交错规范化为 > 逐行式（仿第 VII、XI、XV 篇先例）；the Master 按术语表统一「主」；叙述用「上帝」、题词经文语域用「神」；Prayer→祈祷、Amen.→阿们。照项目说明行式 |
| 2026-09-10 | 17-unbelief-kept-quiet.md（XVII 按捺住的不信） | 双语 9 对，check_bilingual 通过（exit 0） | 提前 6:12 题词依和合本「你要为真道打那美好的仗」，出处行照排不译；章题 Unbelief Kept Quiet 与勃朗宁引诗 perpetual unbelief kept quiet 统一呼应，引诗作「永远都在的不信／被按捺得不动声色」，标题作「按捺住的不信」；Michael 按和合本作「米迦勒」；林后 7:5 依和合本「外有争战，内有惧怕」；来 12:2「信心的创始成终者」、弗 6:13「在磨难的日子……成就了一切，还能站立得住」照和合本语汇；「向山举目」（诗 121）、「信仰并不是眼见」（林后 5:7）用和合本语域；源文引诗空格缩进+空行交错规范化为 > 逐行式（仿第 VII、XI、XIV 篇先例）；叙述与祈祷用「上帝」；Prayer→祈祷、Amen.→阿们。 |
| 2026-09-10 | 16-god-in-front.md（XVI 上帝行在前头） | 双语 6 对（题词 1、正文 4、祈祷 1），check_bilingual 通过（exit 0，无可疑错配） | 诗 21:3 题词依和合本首句「你以美福迎接他」，出处行照排不译；prevent 古义全篇统一「先行迎接／行在前头」（呼应章末祈祷 Thou goest before us＝「祢在我们众人的前头行」）；奥利弗·洛奇爵士（Sir Oliver Lodge）、马可·奥勒留（Marcus Aurelius）、马克·拉瑟福德（Mark Rutherford）、赫胥黎（T. H. Huxley）、奥利弗·温德尔·霍姆斯（Oliver Wendell Holmes）首现附原文；Huxley 的 Lay Sermons 译《俗世讲道集》附原文斜体；华兹华斯、柯勒律治、拜伦、雪莱、济慈通行译名；约 14:2「我去原是为你们预备地方去」、麻雀句太 10:29 语汇依和合本；door of splendid hope 呼应术语表「希望之门」译「一扇辉煌的希望之门」；源文 OCR 笔误 percursor 在原文块订正为 precursor，并清除零宽不可见字符（U+FEFF 等）；叙述用「上帝」、祈祷呼格用「祢」；Prayer→祈祷、Amen.→阿们。照项目说明行式 |
| 2026-09-10 | 19-the-god-of-the-unlovable-man.md（XIX 不可爱之人的神） | 双语 7 对（题词 1、正文 5、祈祷 1），check_bilingual 通过（exit 0，无可疑错配） | 诗 46:11 题词依和合本「雅各的神是我们的避难所」，出处行照排；雅各／亚伯拉罕／以撒／以扫按和合本；亨利·德拉蒙德（Henry Drummond）、赫兹里特（Hazlitt）、乔治·艾略特（George Eliot）首现附原文；Index Expurgatorius（私人黑名单）拉丁照搬加注；the Evangel 按术语表作「福音」；浪子比喻语汇归路加福音 15 章和合本；叙述与祈祷用「上帝」、经文语域用「神」；Prayer→祈祷、Amen.→阿们。照项目说明行式 |
| 2026-09-10 | 18-the-equipment-of-joy.md（XVIII 喜乐的装备） | 双语 11 对（题词 1、正文 8、引诗 1、祈祷 1），check_bilingual 通过（exit 0，无可疑错配） | 尼 8:10 题词与文中重引均依和合本「靠耶和华而得的喜乐是你们的力量」，出处行照排；the joy of the Lord 概念性表述统一「靠主而得的喜乐」；「我的主，我的神」「救恩之乐」依和合本语汇；史蒂文森（Stevenson）首现附原文；£100 保留数字作 100 英镑（消数字锚点误报）；引诗规范化为 > 逐行式并清除 U+FEFF 零宽字符与原诗散行；叙述用「上帝」、经文语域用「神」、祈祷呼格用「祢」；Prayer→祈祷、Amen.→阿们。照项目说明行式 |
| 2026-09-10 | 20-under-the-juniper-tree.md（XX 罗腾树下） | 双语块 5 对（题词 1、正文 3、祈祷 1），check_bilingual 通过（exit 0，无可疑错配） | 王上 19:4 题词依和合本「以利亚自己在旷野走了一日的路程，来到一棵罗腾树下，就坐在那里求死」，出处行照排；juniper tree 统一「罗腾树」；reaction 统一「反弹」；班扬典故依术语表「美宫／乐土／屈辱谷」，火箭依和合本弗 6:16；变像山、彼得雅各约翰依和合本；伊恩·麦克拉伦（Ian Maclaren）、互助会（Friendly Societies）首现附原文；诗 103:14、林后 12:9 祈祷引语依和合本；叙述用「上帝」、祈祷呼格用「祢」；Prayer→祈祷、Amen.→阿们。照项目说明行式 |
| 2026-09-10 | 21-instructing-the-cabin-boy.md（XXI 教导舱童） | 双语 10 对（题词 1、正文 8、祈祷 1），check_bilingual 通过（exit 0，无可疑错配） | 约 7:17 题词依和合本「人若立志遵着他的旨意行，就必晓得这教训」，出处行照排不译；路 17:14「他们去的时候就洁净了」依和合本；约翰·卫斯理（John Wesley）《日记》、佐治亚（Georgia）依术语表；托马斯·卡莱尔（Thomas Carlyle）引语「任何一种怀疑，不借着行动，就无法除去」；肯缪尔子爵（Viscount Kenmure）首现附原文；cabin boy 统一「舱童」，与篇题一致；「信仰……失了味」呼应和合本盐失味意象；Wesley《日记》日记体引文照原意译出；叙述用「上帝」、经文语域用「神」、祈祷呼格用「祢」；Prayer→祈祷、Amen.→阿们。照项目说明行式 |
| 2026-09-10 | 22-god-s-door-of-hope.md（XXII 上帝的希望之门） | 双语 7 对（题词 1、正文 4、诗 1、祈祷 1），check_bilingual 通过（exit 0，无可疑错配） | 何 2:15 题词依和合本「亚割谷作为指望的门」，出处行照排；Achor→亚割、亚割谷首现附原文，字义「连累」从和合本书 7:26 小注；Achan→亚干；door of hope 统一「希望之门」；诗 119:71「我受苦是与我有益」依和合本；诗 55:6 化用「但愿我有鸽子的翅膀」；Despond→灰心沼依术语表；梅洛里亚岛、比萨、热那亚、东波士顿、冠达码头依术语表，菲利普斯·布鲁克斯（Phillips Brooks）、马西森博士（George Matheson）首现附原文；引诗（I walked a mile with Pleasure/Sorrow）规范化为 > 逐行式；「我们的主、我们的夫子」沿用第 04 篇定名；叙述用「上帝」、经文语域用「神」、祈祷呼格用「祢」；Prayer→祈祷、Amen.→阿们。照项目说明行式 |
| 2026-09-10 | 25-the-extravagance-of-love.md（XXV 爱的挥霍） | 双语 5 对（题词 1、正文 3、祈祷 1），check_bilingual 通过（exit 0，无可疑错配） | 约 12:5 题词依和合本「这香膏为什么不卖三十两银子周济穷人呢？」，出处行照排；约 12:6「并不是挂念穷人，乃因他是个贼，又带着钱囊」依和合本；太 26:12「她是为我安葬做的」、路 7:47「她的爱多」、寡妇两个小钱依和合本；extravagance 统一「挥霍」，alabaster box 依和合本「玉瓶」，widow's cruse 译「寡妇的油瓶」；马利亚、犹大依术语表；叙述用「上帝」、祈祷呼格用「祢」；Prayer→祈祷、Amen.→阿们。照项目说明行式 |
| 2026-09-10 | 24-roundabout-roads.md（XXIV 迂回之路） | 双语 7 对（题词 1、正文 5、引诗 1、祈祷 1），check_bilingual 通过（exit 0，无可疑错配） | 代下 18:33 题词依和合本「有一人随便开弓」，出处行照排；Ahab→亚哈依术语表；drew a bow at a venture 全篇统一「随便开弓」，Hebrew in his simplicity 译「在他浑然无意之中」前后呼应；太 25:40「作在……身上」、加 6:2「互相担当重担」、一杯凉水（太 10:42）、「凡丧掉生命的，必救活生命」（路 17:33）依和合本语汇；圣尼古拉（St. Nicholas）、圣卡西安（St. Cassianus）依术语表，the Master 统一「主」；引诗（He kept his lamp still lighted）规范化为 > 逐行式并清除源文散行空行；叙述用「上帝」、祈祷呼格用「祢」；Prayer→祈祷、Amen.→阿们。照项目说明行式 |
| 2026-09-10 | 23-now-a-days.md（XXIII 如今） | 双语 8 对（题词 1、正文 6、祈祷 1），check_bilingual 通过（exit 0，无可疑错配） | 撒上 25:10 题词依和合本「近来悖逆主人奔逃的仆人甚多」，出处行照排；章题眼 Nowadays 全篇统一「如今」；拿八、大卫依术语表撒上 25 典故；churl 依和合本撒上 25:3 语汇「凶恶愚顽」；可 6:3「这不是那木匠么？」、路 17:20「神的国来到，不是眼所能见的」依和合本；H. G. 格雷厄姆（H. G. Graham）《十八世纪苏格兰社会生活》（Social Life in Scotland in the Eighteenth Century）首现附原文；尾注标记 today.1 数字照搬（对应尾注 Written in February）；清除源文 U+FEFF 零宽字符；叙述用「上帝」、经文语域用「神」、祈祷呼格用「祢」；Prayer→祈祷、Amen.→阿们。照项目说明行式 |
| 2026-09-10 | 27-wonder.md（XXVII 惊奇） | 双语 6 对（题词 1、正文 4、祈祷 1），check_bilingual 通过（exit 0，无可疑错配） | 出 3:3 题词依和合本「我要过去看这大异象」，出处行照排；章题眼 wonder 全篇统一「惊奇」；罗斯金（Ruskin）茅屋/沃里克城堡语、乔治·艾略特（George Eliot）「上帝所赐给我们认识之物中最神圣者」、勃朗宁夫人（Mrs. Browning）「每日最安静之需要的高度」、约翰·凯尔曼（John Kelman）首现附原文；工匠方言句 awfu' wee God 意译「未免太小啦」保留口语；祈祷内诗 8:4「顾念/眷顾」、约壹 3:1「神的儿女」、诗 139:6、诗 95:6 依和合本语汇，the Lord our Maker 依称谓统一作「造我们的主」；清除源文 U+2060 词连接符；叙述用「上帝」、经文语域用「神」、祈祷呼格用「祢」；Prayer→祈祷、Amen.→阿们。照项目说明行式 |
| 2026-09-10 | 26-the-art-of-doing-without.md（XXVI 「忍受缺乏」的艺术） | 双语 8 对（题词 1、正文 5、引诗 1、祈祷 1），check_bilingual 通过（exit 0，无可疑错配） | 腓 4:12 题词依和合本「我知道怎样处卑贱，也知道怎样处丰富」，出处行照排；篇题眼 doing without 全篇统一「忍受缺乏」；路 12:15 化用「人的生命……在乎家道丰富」、太 6:33 化用「先求」依和合本语汇；卡莱尔（Thomas Carlyle）、史蒂文森（R. L. Stevenson）、《伊利亚特》（Iliad）、劳伦斯弟兄（Brother Lawrence）、布莱顿的罗伯逊（Robertson of Brighton）、霍勒斯·布什内尔（Horace Bushnell）首现附原文；引诗（better to walk in the dark with God）规范化为 > 逐行式并清除源文散行空行；叙述用「上帝」、祈祷呼格用「祢」；Prayer→祈祷、Amen.→阿们。照项目说明行式 |
| 2026-09-10 | 28-the-fatherhood-of-god.md（XXVIII 上帝的父性） | 双语 8 对（题词 1、正文 5、引诗 1、祈祷 1），check_bilingual 通过（exit 0，无可疑错配） | 路 11:13 题词依和合本「你们虽然不好，尚且知道拿好东西给儿女」（节引作「你们虽然不好，尚且知道……何况……你们的天父」），出处行照排；诗 103:12 化用「东离西有多远」、林前 13:4「恒久忍耐，又有恩慈」、罗 4:18「无可指望的时候仍怀着指望」、路 15 浪子典故（醒悟过来）、路 11:11「谁有儿子求饼，反给他石头呢」依和合本语汇；long-suffering 双关以「恒久忍耐/长久的受苦」对应保留；亨利·德拉蒙德（Henry Drummond）、考文垂·帕特莫尔（Coventry Patmore）《玩具》（"The Toys"）依术语表首现附原文；Bethankit 苏格兰方言意译加注「谢恩祷（Bethankit）」；引诗（Patmore The Toys 末节）规范化为 > 逐行式，清除源文 U+FEFF/U+200A 隐形字符与散行空行；叙述用「上帝」、经文语域用「神」、祈祷呼格用「祢」；Prayer→祈祷、Amen.→阿们。，Through Jesus Christ our Lord 依第 01 篇定式「奉耶稣基督我们的主求。阿们。」 |
| 2026-09-10 | 29-the-unreturning-brave.md（XXIX 不归的勇士） | 双语 9 对（题词 1、正文 6、引诗 1、祈祷 1），check_bilingual 通过（exit 0，无可疑错配） | 太 16:25 题词依和合本「凡为我丧掉生命的，必得着生命」，出处行照排；伯 14:14「人若死了岂能再活呢」、诗 23「死荫的幽谷/可安歇的水边」、歌 2:17「天起凉风，日影飞去」、太 20:28「舍命，作多人的赎价」依和合本语汇；约翰·海（John Hay）《派克县歌谣》（Pike County Ballads）、吉姆·布拉德索（Jim Bludso）、「草原美人号」（Prairie Belle）依术语表首现附原文；引诗（Jim Bludso 末两行）规范化为 > 逐行式，清除源文 U+FEFF 零宽字符与散行空行；chaplain 统一「随军牧师」、War Office 译「陆军部」；叙述用「上帝」、祈祷呼格用「祢」；Prayer→祈祷、Amen.→阿们。照项目说明行式 |
| 2026-09-10 | 31-endnotes.md（尾注） | 双语 2 对（尾注 2 条），check_bilingual 通过（exit 0，无可疑错配） | 全书末篇；两条作者自注照译：数字锚点 1./2. 与回链符号「↩︎」照搬；尾注 1 Written in February 译「写于二月」（对应第 XXIII 篇 today.1）；尾注 2 威廉·罗伯逊·尼科尔爵士（Sir Wm. Robertson Nicoll）《当伤员回家时》（"When the Wounded Go Home"）依术语表首现附原文，a tender and courageous message 译「一则温柔而勇敢的信息」；标题合并为单行 Endnotes / 尾注 |
| 2026-09-10 | 30-the-sacrament-of-sunset.md（XXX 日落圣礼） | 双语 8 对（题词 1、正文 5、引诗 1、祈祷 1），check_bilingual 通过（exit 0，无可疑错配） | 诗 19:1 题词依和合本「诸天述说神的荣耀」，出处行照排；诗 104:2 化用「铺张穹苍如铺张幔子」、诗 19:5「为太阳安设帐幕」、约 9:4「黑夜将到」、徒 17:27 化用「揣摩」依和合本语汇；罗斯金（John Ruskin）天空为悦人而行之语、艾尔郡（Ayrshire）海岸、阿伦岛（Arran）依术语表首现附原文；丁尼生化用「那已死之日温柔的风致」（Break, Break, Break）；引诗（长日终鸣晚祷钟之古谚）规范化为 > 逐行式，清除源文散行空行；叙述用「上帝」、经文语域用「神」、祈祷呼格用「祢」；Prayer→祈祷、Amen.→阿们。照项目说明行式 |
