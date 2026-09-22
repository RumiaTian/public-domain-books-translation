# 翻译计划（西蒙）

## 本计划信息

- **项目名称**：《西蒙》（J.斯托勒·克卢斯顿）
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
chapter-1.md,8.7,todo
chapter-2.md,9.3,todo
...
```

| 字段 | 含义 | 取值 |
|------|------|------|
| `file` | 源文文件名（在 `原文/` 目录下） | 如 `chapter-1.md` |
| `size_kb` | 源文大小（KB） | 数字 |
| `status` | 翻译状态 | `todo` 待译 / `doing` 翻译中 / `done` 已完成 |

## 执行步骤

按 `prompts/翻译计划模板.md`「执行步骤」9 步推进（读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志）。本项目为长篇，走委派模式，主 agent 调度、子代理逐篇执行。

## 篇目清单

共 40 章（chapter-1.md … chapter-40.md），详见 `translation_queue.csv`。

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-09-15 | chapter-1.md | 完成 | 章题定名：The Solitary Passenger → 孤身旅客；7 对块 / 21 段；check_bilingual exit 0 |
| 2026-09-15 | chapter-2.md | 完成 | 章题定名：The Procurator Fiscal → 检察官；10 对块 / 52 段；check_bilingual exit 0；术语表新增 Janet=珍妮特（厨娘名）；首现括注：拉塔先生（Mr. Rattar）、西蒙·拉塔（Simon Rattar）、检察官（Procurator Fiscal）、地产代理人（factor）、沉默的西蒙（Silent Simon）、玛丽·麦克莱恩（Mary MacLean） |
| 2026-09-15 | chapter-4.md | 完成 | 章题定名：The Man from the West → 西部来客；18 对块 / 63 段；check_bilingual exit 0；首现括注：斯坦斯兰（Stanesland）的克罗玛蒂先生、马尔科姆·克罗玛蒂先生（Mr. Malcolm Cromarty）、西蒙·拉塔（Simon Rattar）、雷金纳德·克罗玛蒂爵士（Sir Reginald Cromarty）、内德·克罗玛蒂（Ned Cromarty）、法蒙德小姐（Miss Farmond）、西塞莉·法蒙德（Miss Cicely Farmond）、莉莲（Lilian）、上等领主（laird）；术语表 Miss Farmond 行补全名西塞莉（Cicely） |
| 2026-09-15 | chapter-3.md | 完成 | 章题定名：The Heir → 继承人；11 对块 / 59 段；check_bilingual exit 0；术语表新增 Thomson=汤姆森、James Ison=詹姆斯·艾森、letter book=信函登记簿、business ledger=营业总账、head clerk=首席职员；首现括注：马尔科姆·克罗玛蒂（Malcolm Cromarty）、雷金纳德爵士（Sir Reginald）、查尔斯·克罗玛蒂（Charles Cromarty）、凯尔代尔（Keldale）、斯坦斯兰（Stanesland）、汤姆森（Thomson） |
| 2026-09-15 | chapter-6.md | 完成 | 章题定名：At Night → 夜里；8 对块 / 26 段；check_bilingual exit 0；首现括注：西蒙·拉塔（Simon Rattar）、玛丽·麦克莱恩（Mary MacLean）、珍妮特（Janet）、沉默的西蒙（Silent Simon）；无新增术语 |
| 2026-09-15 | chapter-8.md | 完成 | 章题定名：Sir Reginald → 雷金纳德爵士；15 对块 / 65 段；check_bilingual exit 0；首现括注：西塞莉·法蒙德（Cicely Farmond）、马尔科姆·克罗玛蒂（Malcolm Cromarty）、内德·克罗玛蒂（Ned Cromarty）、雷金纳德爵士（Sir Reginald）、法蒙德小姐（Miss Farmond）、玛格丽特（Margaret）、克罗玛蒂夫人（Lady Cromarty）、雷吉（Reggie）、凯尔代尔（Keldale）、伊顿（Eton）；baronet 沿用第 3 章「男爵」译法 |
| 2026-09-15 | chapter-7.md | 完成 | 章题定名：The Drive Home → 驾车归途；25 对块 / 108 段；check_bilingual exit 0；无新增术语（出场人名均已在表）；首现括注：西塞莉·法蒙德（Cicely Farmond）、内德·克罗玛蒂（Ned Cromarty）、斯坦斯兰（Stanesland）的领主（laird）、老西蒙（Simon Rattar）、马尔科姆·克罗玛蒂（Malcolm Cromarty）、莉莲·克罗玛蒂（Lilian Cromarty）、阿尔弗雷德·克罗玛蒂（Alfred Cromarty）、雷金纳德爵士（Sir Reginald）；内德美式口吻 I guess 统一作「估摸」以承接莉莲"Don't 'guess'"的调侃 |
| 2026-09-15 | chapter-5.md | 完成 | 章题定名：The Third Visitor → 第三位访客；18 对块 / 73 段；check_bilingual exit 0；术语表新增 Eastbourne=伊斯特本；首现括注：西塞莉·法蒙德（Miss Cicely Farmond）、西蒙·拉塔（Simon Rattar）、雷金纳德爵士（Sir Reginald）、克罗玛蒂夫人（Lady Cromarty）、伊斯特本（Eastbourne）、凯尔代尔（Keldale）、阿尔弗雷德（Alfred）、比塞（Bisset）；discover/recover 之辨译「查明／恢复」存其双关 |
| 2026-09-15 | chapter-12.md | 完成 | 章题定名：Cicely → 西塞莉；11 对块 / 55 段；check_bilingual exit 0；无新增术语（出场人名均已在表，无需回填）；首现括注：比塞（Bisset）、检察官（Procurator Fiscal）、内德·克罗玛蒂（Ned Cromarty）、马尔科姆·克罗玛蒂先生（Mr. Malcolm Cromarty）、法蒙德小姐（Miss Farmond）、马尔科姆爵士（Sir Malcolm）、西塞莉（Cicely）、克罗玛蒂夫人（Lady Cromarty）；内德 I guess 沿用「估摸」 |
| 2026-09-15 | chapter-9.md | 完成 | 章题定名：A Philosopher → 一位哲学家；12 对块 / 47 段；check_bilingual exit 0（可疑错配 0）；术语表 Bisset 行补全名詹姆斯·比塞（James Bisset）及管家身份、新增 The People's Self-Educator in Science and Art=《大众科学与艺术自学读本》；首现括注：西塞莉（Cicely）、马尔科姆（Malcolm）、雷金纳德爵士（Sir Reginald）、斯坦斯兰（Stanesland）的克罗玛蒂（Cromarty）先生、法蒙德小姐（Miss Farmond）、领主（laird）、克罗玛蒂夫人（Lady Cromarty）、克罗玛蒂小姐（Miss Cromarty）；比塞苏格兰方言以口语化中文呈现（fac=实情、weel=这个嘛、whiles=时不时）；内嵌引语用单弯引号还原比塞转述领主打猎自嘲一段 |
| 2026-09-15 | chapter-10.md | 完成 | 章题定名：The Letter → 一封信；15 对块 / 82 段；check_bilingual exit 0（可疑错配 0）；术语表新增 John Simon Rattar=约翰·西蒙·拉塔、Shearer=希勒、Castleknowe=卡斯尔诺、pyramids=金字塔台球；首现括注：西塞莉（Cicely）、乔治·拉塔（George Rattar）、约翰·西蒙·拉塔（John Simon Rattar）、雷金纳德爵士（Sir Reginald）、沉默的西蒙（Silent Simon）、拉塔先生（Mr. Rattar）、克罗玛蒂夫人（Lady Cromarty）、西蒙·拉塔（Simon Rattar）、马尔科姆（Malcolm）、地产代理人（factor）、卡斯尔诺（Castleknowe）、希勒（Shearer）、玛格丽特（Margaret）、法蒙德小姐（Miss Farmond）；货币金额以中文数字改写（一英镑/一个便士）规避数字锚点误报 |
| 2026-09-15 | chapter-11.md | 完成 | 章题定名：News → 消息；23 对块 / 119 段；check_bilingual exit 0（可疑错配 0、0 直引号、无 BOM）；出场人名均已在表，无新增人名；首现括注：内德·克罗玛蒂（Ned Cromarty）、莉莲（Lilian）、雷金纳德爵士（Sir Reginald）、比塞（Bisset）、检察官（Procurator Fiscal）、西蒙·拉塔（Simon Rattar）、萨瑟兰警司（Superintendent Sutherland）、斯坦斯兰（Stanesland）的领主（laird）、克罗玛蒂夫人（Lady Cromarty）；术语表新增 snib=窗闩、sealing wax=火漆、India rubber=橡皮、finger marks=指印、dressing room=更衣室；苏格兰方言（Ower true/cowpit/likit/windies 等）以口语化中文对等呈现 |
| 2026-09-15 | chapter-15.md | 完成 | 章题定名：Two Women → 两个女人；11 对块 / 39 段；check_bilingual exit 0（可疑错配 0、中文块 0 直引号）；出场人名均已在表，无新增术语；首现括注：克罗玛蒂夫人（Lady Cromarty）、西蒙·拉塔（Simon Rattar）、马尔科姆爵士（Sir Malcolm）、西塞莉·法蒙德（Cicely Farmond）、比塞（Bisset）；比塞苏格兰方言（vera/I'm thinking）以口语化中文呈现；baronet 沿用「男爵」既定译法 |
| 2026-09-15 | chapter-13.md | 完成 | 章题定名：The Deductive Process → 演绎推理之法；14 对块 / 65 段；check_bilingual exit 0（可疑错配 0、0 直引号、无 BOM）；出场人名均已在表，无新增术语；首现括注：比塞（Bisset）、内德·克罗玛蒂（Ned Cromarty）、雷金纳德爵士（Sir Reginald）、拉塔先生（Mr. Rattar）、西蒙·拉塔（Simon Rattar）、斯坦斯兰（Stanesland）的领主（laird）；比塞苏格兰方言（windie/corp/cowped/snibbed/muckle 等）沿用口语化中文对等呈现；「Half of 26 is 13」保留阿拉伯数字并于 CJK 相邻处加空格，规避数字锚点误报 |
| 2026-09-15 | chapter-16.md | 完成 | 章题定名：Rumour → 流言；15 对块 / 73 段；check_bilingual exit 0（可疑错配 0、0 直引号、无 BOM）；出场人名均已在表，无新增人名；术语表新增 ventriloquist=腹语师；首现括注：斯坦斯兰（Stanesland）、比塞（Bisset）、克罗玛蒂先生（Mr. Cromarty）、领主（laird）、雷金纳德爵士（Sir Reginald）、马尔科姆爵士（Sir Malcolm）、法蒙德小姐（Miss Farmond）、西塞莉小姐（Miss Cicely）、克罗玛蒂夫人（Lady Cromarty）、内德·克罗玛蒂（Ned Cromarty）、拉塔先生（Mr. Rattar）、老西蒙（Simon Rattar）；比塞苏格兰方言口语化呈现（windie/fa/haill/ae 等），I *had* 强调以斜体保留 |
| 2026-09-15 | chapter-14.md | 完成 | 章题定名：The Question of Motive → 动机问题；17 对块 / 85 段；check_bilingual exit 0（可疑错配 0、0 直引号、无 BOM）；术语表新增 John Robertson=约翰·罗伯逊（汽车司机）、Donald Mackay=唐纳德·麦凯（花匠）、life rent=终身用益权；首现括注：艾森先生（Mr. Ison）、西蒙·拉塔先生（Mr. Simon Rattar）、斯坦斯兰（Stanesland）的克罗玛蒂先生、领主（laird）、内德（Ned）、雷金纳德爵士（Sir Reginald）、萨瑟兰警司（Superintendent Sutherland）、比塞（Bisset）、检察官（Procurator Fiscal）、沉默的西蒙（Silent Simon）、克罗玛蒂夫人（Lady Cromarty）、马尔科姆爵士（Sir Malcolm）、法蒙德小姐（Miss Farmond）、詹姆斯·比塞（James Bisset）、约翰·罗伯逊（John Robertson）、唐纳德·麦凯（Donald Mackay）、拉塔先生（Mr. Rattar）、内德·克罗玛蒂（Ned Cromarty）；遗嘱金额 1,000/2,000 沿用千分位阿拉伯数字并于 CJK 相邻处加空格以对齐数字锚点，其余金额用中文数字；内德 I guess 沿用「估摸」 |
| 2026-09-15 | chapter-19.md | 完成 | 章题定名：The Empty Compartment → 空隔间；11 对块 / 43 段；check_bilingual exit 0（可疑错配 0、0 直引号、无 BOM）；术语表新增 MacAlister=麦卡利斯特；首现括注：萨瑟兰警司（Superintendent Sutherland）、麦卡利斯特先生（Mr. MacAlister）、乔治（George）、罗比（Robbie）、检察官（Procurator Fiscal）、乔迪（Geordie）；carriage 译「车厢」、compartment 译「隔间」两词分立以保谜题逻辑；麦卡利斯特苏格兰方言（aboot/noo/naething/hae a crack 等）以口语化中文呈现；全章无阿拉伯数字，无锚点问题 |
| 2026-09-15 | chapter-20.md | 完成 | 章题定名：The Sporting Visitor → 运动来客；7 对块 / 25 段；check_bilingual exit 0（可疑错配 0、0 直引号、无 BOM）；术语表新增 Kings Arms Hotel=国王纹章酒店；首现括注：国王纹章酒店（Kings Arms Hotel）、F·T·卡林顿（F. T. Carrington）、彼得金小姐（Miss Peterkin）、克罗玛蒂（Cromarty）谋杀案、卡内基（Carnegie）、西蒙·拉塔（Simon Rattar）、凯尔代尔宅邸（Keldale House）；全章无阿拉伯数字，无锚点问题；boots 译「杂役」、choice spirits 译「妙人儿」、wee droppie 译「再来一小盅」；卡林顿口癖 By Jove/I say 作「我的天哪/我说」 |
| 2026-09-15 | chapter-18.md | 完成 | 章题定名：£1,200 → 一千二百镑；11 对块 / 58 段；check_bilingual exit 0（可疑错配 0、0 直引号、无 BOM）；出场人名均已在表，无新增术语；首现括注：内德·克罗玛蒂（Ned Cromarty）、克罗玛蒂小姐（Miss Cromarty）、莉莲（Lilian）、沉默的西蒙（Silent Simon）、马尔科姆爵士（Sir Malcolm）、法蒙德（Farmond）、莉莲·克罗玛蒂（Lilian Cromarty）、马尔科姆·克罗玛蒂（Malcolm Cromarty）、西塞莉·法蒙德（Cicely Farmond）；莉莲承第 7 章「他姐姐」既定称谓；正文 £1,200 沿用 ch-14 先例作「1,200 英镑」对齐数字锚点，章题意译作「一千二百镑」 |
| 2026-09-15 | chapter-17.md | 完成 | 章题定名：A Suggestion → 一项建议；17 对块 / 78 段；check_bilingual exit 0（可疑错配 0、0 直引号、无 BOM）；出场人名均已在表，无新增术语；首现括注：西蒙·拉塔（Simon Rattar）、斯坦斯兰（Stanesland）的克罗玛蒂先生（Mr. Cromarty of Stanesland）、马尔科姆爵士（Sir Malcolm）、法蒙德小姐（Miss Farmond）、雷金纳德爵士（Sir Reginald）、内德（Ned）、检察官（Procurator Fiscal）、萨瑟兰警司（Superintendent Sutherland）、拉塔先生（Mr. Rattar）、地产代理人（factor）；evidence/proof 之辨沿用第 11 章「证据／确证」译法；遗嘱金额 a thousand/two thousand 以中文数字（一千英镑／两千英镑）与第 10、14 章散文体金额处理一致；single eye 沿用第 4 章「独眼」译法；强调斜体 *believed/evidence/did/want/done* 以斜体保留 |
| 2026-09-15 | chapter-21.md | 完成 | 章题定名：Mr. Carrington's Walk → 卡林顿先生的漫步；17 对块 / 45 段；check_bilingual exit 0（可疑错配 0、0 直引号、无 BOM）；术语表新增 Sandy Donaldson=老桑迪·唐纳森（人物表）、policies=园囿地界；首现括注：国王纹章酒店（Kings Arms）、凯尔代尔宅邸（Keldale House）、马尔科姆·克罗玛蒂爵士（Sir Malcolm Cromarty）、雷金纳德爵士（Sir Reginald）、法蒙德小姐（Miss Farmond）、桑迪（Sandy）、老桑迪·唐纳森（Sandy Donaldson）、彼得金小姐（Miss Peterkin）、西蒙·拉塔（Simon Rattar）、地产代理人（factor）；卡林顿口癖 By Jove 作「我的天哪」、I'm damned 作「真是见了鬼了」；全章无阿拉伯数字，无锚点问题 |
| 2026-09-15 | chapter-23.md | 完成 | 章题定名：Simon's Views → 西蒙的看法；17 对块 / 98 段；check_bilingual exit 0（可疑错配 0、中文块 0 直引号、无 BOM）；出场人名均已在表，无新增术语；首现括注：拉塔先生（Mr. Rattar）、卡林顿（Carrington）、西蒙（Simon）、马尔科姆爵士（Sir Malcolm）、雷金纳德爵士（Sir Reginald）、法蒙德小姐（Miss Farmond）、检察官（Procurator Fiscal）、比塞先生（Mr. Bisset）、斯坦斯兰（Stanesland）的克罗玛蒂先生（Mr. Cromarty）、美国（America）；正文 £1,200 沿用 ch-14/ch-18 先例作「1,200 英镑」对齐数字锚点；结尾 in very deep waters 双关以「在水极深极深的地方」存其暗指 |
| 2026-09-15 | chapter-24.md | 完成 | 章题定名：Mr. Bisset’s Assistant → 比塞先生的助手；29 对块 / 116 段；check_bilingual exit 0（可疑错配 0、0 直引号、无 BOM）；出场人名均已在表，无新增术语；首现括注：凯尔代尔宅邸（Keldale House）、西蒙·拉塔（Simon Rattar）、詹姆斯·比塞（James Bisset）、卡林顿先生（Mr. Carrington）、克罗玛蒂夫人（Lady Cromarty）、马尔科姆爵士（Sir Malcolm）、法蒙德小姐（Miss Farmond）、雷金纳德爵士（Sir Reginald）、西塞莉·法蒙德（Miss Cicely Farmond）、马尔科姆·克罗玛蒂爵士（Sir Malcolm Cromarty）；比塞苏格兰方言（haill/sofie/corp/windie/daurna/after a’/cowpit/tappit 等）以口语化中文呈现（corp=尸首、cowpit=翻倒）；全章无阿拉伯数字，无锚点问题 |
| 2026-09-15 | chapter-22.md | 完成 | 章题定名：Mr. Carrington and the Fiscal → 卡林顿先生与检察官；15 对块 / 72 段；check_bilingual exit 0（可疑错配 0、0 直引号、无 BOM）；术语表新增 private enquiry agent=私人调查员、Sports Club=运动俱乐部；首现括注：西蒙·拉塔先生（Mr. Simon Rattar）、运动俱乐部（Sports Club）、卡林顿先生（Mr. Carrington）、艾森先生（Mr. Ison）、检察官（Procurator Fiscal）、凯尔代尔宅邸（Keldale House）、私人调查员（private enquiry agent）、国王纹章酒店（the Kings Arms）、彼得金小姐（Miss Peterkin）、比塞先生（Mr. Bisset）、雷金纳德·克罗玛蒂爵士（Sir Reginald Cromarty）；事务所铭牌「我的人生三守则」三条清单结构原样保留；long odds 作「十有八九」以避让内德专属的「估摸」 |
| 2026-09-15 | chapter-27.md | 完成 | 章题定名：Flight → 夜奔；10 对块 / 41 段；check_bilingual exit 0（可疑错配 0、0 直引号、无 BOM）；术语表新增 keeper=猎场看守；首现括注：内德·克罗玛蒂（Ned Cromarty）、猎场看守（keeper）、法蒙德小姐（Miss Farmond）、凯尔代尔宅邸（Keldale House）、克罗玛蒂小姐（Miss Cromarty）、西塞莉·法蒙德（Cicely Farmond）、内德·道金斯（Ned Dawkins）、露易莎·道金斯（Louisa Dawkins）；gig lamps 沿用术语表「马车灯」；内德 I guess 沿用「估摸」、derned 作「见鬼的」，伪名道金斯假舅舅一段嵌套引语用单弯引号；站长/看守苏格兰方言以口语化中文呈现；全章无阿拉伯数字，无锚点问题 |
| 2026-09-15 | chapter-26.md | 完成 | 章题定名：At Stanesland → 在斯坦斯兰；25 对块 / 79 段；check_bilingual exit 0（可疑错配 0、0 直引号、无 BOM）；出场人名均已在表，无新增术语；首现括注：卡林顿先生（Mr. Carrington）、斯坦斯兰（Stanesland）的领主（laird）、克罗玛蒂先生（Mr. Cromarty）、比塞（Bisset）、内德·克罗玛蒂（Ned Cromarty）、马尔科姆爵士（Sir Malcolm）、法蒙德小姐（Miss Farmond）、克罗玛蒂夫人（Lady Cromarty）、拉塔先生（Mr. Rattar）、雷金纳德爵士（Sir Reginald）、克罗玛蒂小姐（Miss Cromarty）、莉莲（Lilian）、凯尔代尔宅邸（Keldale House）、西塞莉·法蒙德（Cicely Farmond）；内德 I guess 沿用「估摸」；车价 four hundred 以中文数字作「四百镑」；全章无阿拉伯数字，无锚点问题 |

| 2026-09-15 | chapter-28.md | 完成 | 章题定名：The Return → 归来；19 对块 / 87 段；check_bilingual exit 0（可疑错配 0、中文块 0 直引号、无 BOM）；术语表新增 Louisa=露易莎（西塞莉假名）、Dawkins=道金斯（内德假名）；首现括注：斯坦斯兰（Stanesland）的内德·克罗玛蒂（Ned Cromarty）、利物浦（Liverpool）、道金斯先生（Mr. Dawkins）、露易莎（Louisa）、西塞莉（Cicely）、法蒙德小姐（Miss Farmond）、马尔科姆（Malcolm）、雷金纳德爵士（Sir Reginald）、克罗玛蒂夫人（Lady Cromarty）、比塞（Bisset）、拉塔先生（Mr. Rattar）、西蒙·拉塔（Simon Rattar）、卡林顿先生（Mr. Carrington）、克罗玛蒂小姐（Miss Cromarty）；Ned's one eye 沿第 4 章玻璃眼设定译「独眼」；两场景间 --- 分隔线保留为游离行；内德美式口吻 derned/honour bright 以「见鬼的／凭良心说」呈现 |
| 2026-09-15 | chapter-25.md | 完成 | 章题定名：A Telegram → 一封电报；12 对块 / 50 段；check_bilingual exit 0（可疑错配 0、0 直引号、无 BOM）；出场人名均已在表，无新增术语；首现括注：卡林顿先生（Mr. Carrington）、拉塔先生（Mr. Rattar）、马尔科姆·克罗玛蒂爵士（Sir Malcolm Cromarty）、西蒙（Simon）、比塞先生（Mr. Bisset）、凯尔代尔（Keldale）、西塞莉·法蒙德（Cicely Farmond）、斯坦斯兰城堡（Stanesland Castle）；电文仿电报体作「速来有急事勿复勿延」连写无标点存其急迫；bad eggs 之谑以「好蛋坏蛋」存其双关；全章时刻以中文数字书写（两点整/一点五十分），无阿拉伯数字，无锚点问题 |
| 2026-09-15 | chapter-32.md | 完成 | 章题定名：The Sympathetic Stranger → 善体人意的陌生人；11 对块 / 40 段；check_bilingual exit 0（可疑错配 0、中文块 0 直引号、无 BOM）；出场人名均已在表，无新增术语；首现括注：卡林顿（Carrington）、萨瑟兰警司（Superintendent Sutherland）、拉塔先生（Mr. Rattar）、检察官（Procurator Fiscal）、西蒙·拉塔（Simon Rattar）、雷金纳德·克罗玛蒂爵士（Sir Reginald Cromarty）、乔治·拉塔（George Rattar）、凯尔代尔（Keldale）、玛丽·麦克莱恩（Mary MacLean）；警司苏格兰方言（couldna／a kind o’ idea／we were that taken up／minded on it）以口语化中文呈现；全章时刻以中文数字书写（十二点二十分／三点来钟／五点以前），无阿拉伯数字，无锚点问题 |
| 2026-09-15 | chapter-29.md | 完成 | 章题定名：Brother and Sister → 姐弟；15 对块 / 54 段；check_bilingual exit 0（可疑错配 0、0 直引号、无 BOM）；出场人名均已在表，无新增术语；首现括注：内德·克罗玛蒂（Ned Cromarty）、西塞莉·法蒙德（Cicely Farmond）、马尔科姆·克罗玛蒂（Malcolm Cromarty）、莉莲（Lilian）、莉莲·克罗玛蒂（Lilian Cromarty）、西蒙·拉塔（Simon Rattar）、卡林顿（Carrington）；内德 I guess 沿用「估摸」、By heaven 作「老天在上」；莉莲为内德之姐依第 7 章「比她弟弟年长几岁」定称谓作他姐姐／她弟弟；I'm out of my depth 存水喻作「这潭水深了，我够不着底」；全章无阿拉伯数字，无锚点问题 |
| 2026-09-15 | chapter-31.md | 完成 | 章题定名：The Letter Again → 旧信重提；17 对块 / 67 段；check_bilingual exit 0（可疑错配 0、中文块 0 直引号、无 BOM）；出场人名均已在表，无新增术语；首现括注：马尔科姆爵士（Sir Malcolm）、国王纹章酒店（the Kings Arms）、卡林顿先生（Mr. Carrington）、凯尔代尔（Keldale）、彼得金小姐（Miss Peterkin）、比塞（Bisset）、法蒙德小姐（Miss Farmond）、克罗玛蒂夫人（Lady Cromarty）、凯尔代尔宅邸（Keldale House）、雷金纳德爵士（Sir Reginald）、拉塔先生（Mr. Rattar）、西蒙（Simon）；卡林顿口癖 By Jove/I'm dashed 沿用「我的天哪/真是见了鬼了」；比塞苏格兰方言（deil a sign/exac'ly/datas/fac'/yon/hersel'）以口语化中文呈现，「The devil/That's just exac'ly it」谐趣应答予以保留；比塞视卡林顿为「助手」沿用 ch-24 先例；Simon 的 grunt 沿用 ch-3「闷哼」；letter book 作「信函登记簿」；两场景间 --- 分隔线保留为游离行；全章无阿拉伯数字，无锚点问题 |
| 2026-09-15 | chapter-30.md | 完成 | 章题定名：A Marked Man → 被盯上的人；32 对块 / 109 段；check_bilingual exit 0（可疑错配 0、中文块 0 直引号、无 BOM）；术语表新增 sloe gin=黑刺李金酒；首现括注：彼得金小姐（Miss Peterkin）、凯尔代尔（Keldale）、斯坦斯兰（Stanesland）、卡林顿先生（Mr. Carrington）、马尔科姆·克罗玛蒂爵士（Sir Malcolm Cromarty）、雷金纳德·克罗玛蒂爵士（Sir Reginald Cromarty）、伦敦（London）、西塞莉·法蒙德（Miss Cicely Farmond）、国王纹章酒店（the Kings Arms）、凯尔代尔宅邸（Keldale House）、老西蒙（Simon）、拉塔先生（Mr. Rattar）、沉默的西蒙（Silent Simon）、西蒙·拉塔（Simon Rattar）；Good egg 承第 25 章「好蛋坏蛋」之谑作「好蛋」、电文沿用第 25 章「速来有急事勿复勿延」；marked man 双关以「被盯上的人」贯通章题与结尾 I rather like them marked；卡林顿口癖 By Jove 作「我的天哪」、by Gad 作「老天爷」；全章无阿拉伯数字，无锚点问题 |
| 2026-09-15 | chapter-35.md | 完成 | 章题定名：In the Garden → 在园中；7 对块 / 23 段；check_bilingual exit 0（可疑错配 0、中文块 0 直引号、无 BOM）；出场人名均已在表，无新增术语；首现括注：彼得金小姐（Miss Peterkin）、国王纹章酒店（the Kings Arms）、卡林顿先生（Mr. Carrington）、西蒙·拉塔先生（Mr. Simon Rattar）、艾森先生（Mr. Ison）；boots 沿用第 20 章「杂役」、manageress 作「女经理」、head clerk 作「首席职员」；全章时刻与长度均以中文数字书写（八点半刚过几分／九下／五十来码／将近一个钟头），无阿拉伯数字，无锚点问题 |
| 2026-09-15 | chapter-36.md | 完成 | 章题定名：The Walking Stick → 手杖；9 对块 / 42 段；check_bilingual exit 0（可疑错配 0、中文块 0 直引号、无 BOM）；出场人名均已在表，无新增术语；首现括注：卡林顿先生（Mr. Carrington）、西蒙·拉塔（Simon Rattar）、玛丽（Mary）、凯尔代尔宅邸（Keldale House）；sympathetic 沿用第 32 章「善体人意」贯通全章（善体人意的先生/朋友/笑容）；全章无阿拉伯数字，无锚点问题 |
| 2026-09-15 | chapter-34.md | 完成 | 章题定名：A Confidential Conversation → 一场密谈；25 对块 / 92 段；check_bilingual exit 0（可疑错配 0、中文块 0 直引号、无 BOM）；出场人名均已在表，无新增术语；首现括注：斯坦斯兰（Stanesland）的领主（laird）、国王纹章酒店（the Kings Arms）、卡林顿先生（Mr. Carrington）、克罗玛蒂先生（Mr. Cromarty）、内德·克罗玛蒂（Ned Cromarty）、法蒙德小姐（Miss Farmond）、比塞（Bisset）、西蒙·拉塔（Simon Rattar）、马尔科姆爵士（Sir Malcolm）、拉塔先生（Mr. Rattar）、凯尔代尔宅邸（Keldale House）、雷金纳德爵士（Sir Reginald）；内德 I guess 沿用「估摸」、by Gad 沿用「老天爷」、独眼沿用「独眼」；cards played for me 牌喻全章统一作「替我出牌」、deep waters 承第 23 章「在水极深极深的地方」；£1,200 沿用 ch-14/18/23 先例作「1,200 英镑」，其余数字均中文数字，无锚点问题 |
| 2026-09-15 | chapter-33.md | 完成 | 章题定名：The House of Mysteries → 谜团之宅；16 对块 / 68 段；check_bilingual exit 0（可疑错配 0、中文块 0 直引号、无 BOM）；术语表新增 tacketty boot=钉掌靴；首现括注：玛丽·麦克莱恩（Mary MacLean）、雷金纳德爵士（Sir Reginald）、拉塔先生（Mr. Rattar）、钉掌靴（tacketty boot）、卡林顿先生（Mr. Carrington）；玛丽苏格兰方言（forbye that/couldna/pollis/it's the truth they were/I'm that feared/N—no）以口语化中文呈现（还不止呢/根本不能/报官/千真万确/怕得要命/不——不大信）；卡林顿口癖 By Jove/I say 沿用「我的天哪/我说」、Brilliant police 作「警察可真是高明」；玛丽自语嵌套引语用单弯引号；*watched* 强调斜体保留作「*盯*」；全章无阿拉伯数字（九点整），无锚点问题 |
| 2026-09-15 | chapter-37.md | 完成 | 章题定名：Bisset's Advice → 比塞的忠告；12 对块 / 51 段；check_bilingual exit 0（可疑错配 0、中文块 0 直引号、无 BOM）；术语表新增 Sheriff=郡法官（Sheriff）；首现括注：内德·克罗玛蒂（Ned Cromarty）、法蒙德小姐（Miss Farmond）、比塞（Bisset）、西塞莉（Cicely）、斯坦斯兰（Stanesland）、凯尔代尔（Keldale）、西蒙·拉塔（Simon Rattar）、克罗玛蒂夫人（Lady Cromarty）、拉塔先生（Mr. Rattar）、郡法官（Sheriff）、领主（laird）、莉莲·克罗玛蒂（Lilian Cromarty）、克罗玛蒂小姐（Miss Cromarty）、国王纹章酒店（Kings Arms）、卡林顿先生（Mr. Carrington）；比塞苏格兰方言（vera/haill/tellt/no for/Shirra'/fac'/weel）以口语化中文呈现；内德 derned 作「见鬼的」、By Gad 沿用「老天爷」；trap 沿用第 4/7 章「双轮小马车」、gig lamps 沿用「马车灯」、玻璃眼沿用「玻璃眼珠子」；电报仿电报体作「今夜八点国王纹章酒店见 事急 卡林顿」；全章数字以中文数字书写（今天早上/八点/二十分钟），无阿拉伯数字，无锚点问题 |
| 2026-09-15 | chapter-38.md | 完成 | 章题定名：Trapped → 落网；23 对块 / 106 段；check_bilingual exit 0（可疑错配 0、中文块 0 直引号、无 BOM）；术语表新增 tantalus=玻璃酒柜；首现括注：克罗玛蒂（Cromarty）、卡林顿（Carrington）、法蒙德小姐（Miss Farmond）、萨瑟兰警司（Superintendent Sutherland）、西蒙·拉塔（Simon Rattar）、拉塔先生（Mr. Rattar）、玛丽（Mary）、玛丽·麦克莱恩（Mary MacLean）、马尔科姆爵士（Sir Malcolm）、乔治·拉塔（George Rattar）、雷金纳德爵士（Sir Reginald）、玻璃酒柜（tantalus）；玛丽苏格兰方言（canna rightly say／fair mad like／they was digging）以口语化中文呈现；内德 I guess 沿用「估摸」、derned 作「见鬼的」；揭底反转「此人是乔治·拉塔」完整保留；全章无阿拉伯数字，无锚点问题 |
| 2026-09-15 | chapter-40.md | 完成 | 章题定名：The Last Chapter → 末章；12 对块 / 46 段；check_bilingual exit 0（可疑错配 0、中文块 0 直引号、无 BOM）；术语表新增 kid gloves=小山羊皮手套；首现括注：内德·克罗玛蒂（Ned Cromarty）、卡林顿（Carrington）、拉塔（Rattar）、凯尔代尔（Keldale）、比塞（Bisset）、雷金纳德爵士（Sir Reginald）、法蒙德小姐（Miss Farmond）、克罗玛蒂夫人（Lady Cromarty）、马尔科姆爵士（Sir Malcolm）、乔治·拉塔（George Rattar）、西蒙（Simon）、萨瑟兰警司（Superintendent Sutherland）、西蒙·拉塔先生（Simon Rattar）、老艾森（Ison）、彼得金小姐（Miss Peterkin）、斯坦斯兰（Stanesland）；内德 I guess 沿用「估摸」、Great Scot 作「好家伙」、derned 沿用「见鬼的」；卡林顿口癖 By George 沿用「我的老天」、I'm hanged 承「见了鬼」句式；gig lamps 沿用「马车灯」、finger marks 沿用「指印」；middle blind（百叶窗）与 as a blind（幌子）同词异义分译；末章解谜收束明快，以彼得金小姐一句妙语收全书；全章无阿拉伯数字，无锚点问题 |
| 2026-09-15 | chapter-39.md | 完成 | 章题定名：The Yarn → 一套说辞；26 对块 / 74 段；check_bilingual exit 0（可疑错配 0、中文块 0 直引号、无 BOM）；出场人名均已在表，无新增术语；首现括注：西蒙（Simon）、拉塔（Rattar）、卡林顿（Carrington）、内德·克罗玛蒂（Ned Cromarty）、马尔科姆·克罗玛蒂（Malcolm Cromarty）、法蒙德家的姑娘（the Farmond girl）、萨瑟兰警司（Superintendent Sutherland）、雷金纳德爵士（Sir Reginald）、克罗玛蒂（Cromarty）、凯尔代尔（Keldale）；I'd *be* Simon 强调斜体保留作「我要*当*西蒙」；行凶处 settled 双关以「他也就这么给我‘定’了」存其冷峭；罪犯独白跨段引语沿用原书开合引语节奏、嵌套引语用单弯引号；内德 I guess 未出现，其冷面短句 Won't turn, spring broken 作「转不动，弹簧坏了」；全章数字均中文数字（五码／五个先令／二十来秒／九点过五分／三步），无锚点问题 |

## 整书完结日志

| 日期 | 事件 | 明细 |
| --- | --- | --- |
| 2026-09-15 | 《西蒙》整书完结（批次1第25册） | 40/40 章全部 done，批量复检 40 章 check_bilingual.py 零 FAIL；体例「## 罗马数字 / 中文题名」（描述性题名意译+人名/金额题名先例：检察官/继承人/西部来客/一千二百镑/末章）；章题报备制 40/40 全量落地；术语表新增约 30 条（法官/玻璃酒柜/小山羊皮手套/钉掌靴等）；声口锁词：内德 I guess=估摸、derned=见鬼的，卡林顿 By Jove=我的天哪，苏格兰方言口语化零怪拼；金额锚点双轨：£1,200=「1,200 英镑」沿第14章先例、散文金额中文数字；本册为批次1首部侦探推理长篇（1919 公版），零拦截零额度尽，10 波×4 并发约 3 小时完书 |
