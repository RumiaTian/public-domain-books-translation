# Plan：Fred Gross Stories

## 本计划信息

- **项目名称**：ring-lardner_fred-gross-stories
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md
- **领域配置**：prompts/领域配置/小说文学.md
- **术语表**：术语表.md

## 文件分工

| 文件 | 作用 | 谁来改 |
|------|------|--------|
| `项目说明.md` | 项目基本信息、领域配置、方言处理策略 | 人工 |
| `术语表.md` | 翻译硬约束层 | agent / 人工 |
| `translation_queue.csv` | 任务队列（file,size_kb,status） | 翻译前 doing，完成 done |
| `Plan.md`（本文件） | 执行步骤 + 运行日志 | agent 追加日志 |
| `原文/*.md` | 源文 | 不改 |
| `译文/*.zh-CN.md` | 译文产出 | 翻译 agent 产出 |

## 执行步骤

按 `prompts/翻译计划模板.md`「执行步骤」9 步推进。

## 运行日志

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-08-05 | - | 项目建立 | 7 篇，短篇集/委派/小说文学；方言处理见项目说明 |
| 2026-08-05 | fore.md | done | 38.3KB，Fred Gross 方言书信（标题《Fore! / 开球！》，9 封写给弟弟查利的信，讲述入会高尔夫俱乐部到被骗酒账、退会、又转去公共球场；主题：自吹自擂的反讽喜剧）；44 对 Original/Chinese，25 处可疑错配（全部为 \$150/\$50/63杆 等数字被改写成中文数字一百五十/五十/六十三所致的启发式误报，逐块核对配对正确）；6 处英文残留（shinty/hardly/driver/brassy/click/masher/putter/tea/high ball/forfeit）已全部改入括号内作术语参考或意译，复扫 0 残留 |
| 2026-08-05 | the-last-laugh.md | done | 31.8KB→约 62KB 译文；Fred Gross 方言短篇（书信体，7 封致查利老弟的信）；主题：郊区小市民 Fred 被汉密尔顿/卡本特两家冷落后报复，借「办聚会不请」与「雇副治安官突袭对方桥牌赌局」出气，终章「笑到最后」反讽；38 对 Original/Chinese，0 可疑错配；方言用「咧/哩/寻思/咋/啥」+ 口语化语法 + 偶用不规范用词模拟，正式请柬块保留正式腔与 F.A. 缩写以映衬原文反差；check_bilingual exit 0 |
| 2026-08-05 | uncivil-war.md | done | 36.8KB→约 70.7KB 译文；Fred Gross 方言书信（标题《Uncivil War / 野蛮内战》，8 封 1920s 致查利老弟的信）；主题：左邻马丁、右邻汉密尔顿的「邻里战争」——猫翻垃圾桶→情人节辱骂卡→天花牌→爆胎→电话骚扰→门挂丧纱→消防队冲水，结尾揭穿幕后黑手原是马丁、与汉密尔顿和解；54 对 Original/Chinese，11 处可疑错配（全部为 \$.01/\$1.60/\$.80、日期 12/14/15/18/20、人数 16/18、10 a clock、40 cts 等数字按中文数字书写所致的启发式误报，逐块核对配对正确）；5 处英文残留（supposed/ballet/Martins/4 hundred club）已全部改写意译，复扫 0 残留；check_bilingual 结构契约满足（exit≠0 仅因数字启发式误报）；方言用「咧/咋/啥/咱/寻思」+口语化语法+偶用近音/不规范用词模拟 Fred 半文盲口吻 |
| 2026-08-05 | own-your-own-home.md | done | 41.6KB→约 78.0KB 译文；Fred Gross 方言书信（标题《Own Your Own Home / 自置居所》，17 封 1920s 致查利老弟的信，5月→次年6月）；主题：郊区买房盖屋血泪史——立雄心买地→银行吃利息佣金→地基挖反→包工头撂挑子换木匠→门窗打不开屋顶漏雨地窖进水，预算 \$3,700 翻成 \$5,300，结尾反讽「有孩子的人家就这一种活法」；17 对 Original/Chinese，2 处可疑错配（全部为日期 Nov.29/Feb.24 在中文写作「11月29日/2月24日」时数字被中文字符包围致 \b 边界失效的启发式误报，逐块核对配对与日期均正确）；6 处英文均为故意保留的方言关键词括号参考（warranty deed/2 cotes/graded/mary xmas/plumer/2 storys）以再现 Fred 半文白拼写趣味，非泄露；check_bilingual 结构契约满足（exit≠0 仅因数字边界启发式误报）；方言用「咧/咋/啥/咱/寻思/得咧/撒脚丫子」+口语化语法+偶用近音/不规范用词+契约式长句模拟 Fred 憨直啰嗦的半文盲口吻 |
| 2026-08-05 | war-bribes.md | done | 35.4KB→约 68KB 译文；Fred Gross 方言短篇（书信体，10 封致查利老弟的信，8月→11月）；主题：一战末期股市投机狂热——娃娃染百日咳、跟兄弟借 100 块被拒，转头听信「战争贿赂」war bribes（一战中军火相关股票）的内线消息，连炒鲁姆利/麦克斯韦/坩埚钢铁等股票，被保证金制度套牢赔光，反被岳父靠「卖空」伯利恒钢铁净赚 3 万 5；38 对 Original/Chinese，28 处可疑错配（全部为 \$/股数/日期/百分比等数字被改写成中文数字一百/五十/八十五等所致的启发式误报，逐块核对配对正确）；方言用「咧/啦/哩/寻思/咋/啥」+口语化语法+大量 Lardner 错别字（epidermis/simpsons/leppersy/billius/bethleham steal/Gen. Moders/crucial steal/octopus/night mayor/prophets/sky rockit/panicks/bond fire/contrakters/fliver 等）以中文括注「他写成 X／他管 Y 叫 Z」保留谐音/误用笑点；英文残留全部在括注内作术语参考，复扫 0 残留；check_bilingual 结构契约满足（exit≠0 仅因 28 处启发式数字误报） |
| 2026-08-05 | the-swift-six.md | done | 38.5KB→约 73.8KB 译文；Fred Gross 方言书信（标题《The Swift Six / 迅捷六型》，11 封致查利老弟的信，1月→次年5月）；主题：立誓攒钱戒烟戒酒→妻子要买钢琴→转而冲动定下迅捷六型汽车→交车一拖再拖→发动机冻裂、电池踩坏、无照驾驶冲向人群、轮胎被同事放气、整车自燃、最后车被偷，结尾反讽夸钢琴比汽车强；65 对 Original/Chinese，27 处可疑错配（全部为 $600/$550/$490/$60/$110/$250/$20/$16/$7.50/$11/$30/$40/$150/$849 与日期 22/24/27/15 等数字改写成中文六百/五百五十/四百九十/六十/一百一十/二百五十/二十/十六/七块五/十一/三十/四十/一百五十/八百四十九与「一月二十二日」等所致的启发式误报，逐块核对配对与段落数均一致）；0 处英文残留（Swift Six/Detroit/Chi/Wabash ave./Marshall and Field/Sherlock/limousine/flivver/Over the Waves/Jerry Donahue/LaSalle st./Ogden ave./dodge/saxon 6/Mrs. Grundy/Crusoe 等专有名词与术语均置于中文全角括号内作参考，复扫 0 残留）；段落数 65/65 配对一致，源文末段 **F. A. Gross**. 与译文末段对应；方言用「咧/咋/啥/咱/寻思/麻利儿/捣鼓/撒脚丫子」+ 口语化语法 + 偶用近音/不规范用词模拟 Fred 憨直啰嗦的半文盲口吻 |
| 2026-08-05 | welcome-to-our-city.md | done | 36.5KB→约 71KB 译文；Fred Gross 方言书信（标题《Welcome to Our City / 欢迎来到咱们这座城》，13 封 1920s 致查利老弟的信，7月→11月）；主题：郊区新城社交受挫记——盖房漏水油漆味→格蕾丝拜客误把丈夫警探名片当自家名片递出被当女侦探→Fred 瞒着妻子请汉密尔顿/卡彭特两家吃饭遭放鸽子→误收本该给汉密尔顿家的慈善舞会请帖，硬闯舞会被委员会当众驱赶险些动武→卡里一家翻脸→终章与卡里一家及新来的柯蒂斯夫妇和好、决定扎根；14 对 Original/Chinese，13 处可疑错配（全部为日期 Jul.24/Aug.13/16/31/Sep.14/18/Oct.3/8/11/18/22/Nov.1 改写为「七月二十四日」等中文数字、及金额 \$20→二十/\$50→五毛/\$100→一百/\$1,000→一千/45 yrs.→四十五 等数字被中文字符包围致 \b 边界失效的启发式误报，逐块核对配对与数字均正确）；5 处英文均为故意保留的方言关键词括号参考（divers suit/angel worms/opra house/gat/welsh rabbit/rummy/cinch/Belgiums/sucker）以再现 Fred 半文白拼写与双关趣味，非泄露；check_bilingual 结构契约满足（exit≠0 仅因数字边界启发式误报）；方言用「咧/咋/啥/咱/寻思/得咧/撒脚丫子」+口语化语法+偶用近音/不规范用词+长句啰嗦模拟 Fred 憨直自吹的半文盲口吻，与 fore/the-last-laugh/uncivil-war/own-your-own-home 一致 |
