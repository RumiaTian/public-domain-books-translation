# 翻译计划：线索（The Clue）

## 本计划信息

- **项目名称**：carolyn-wells_the-clue
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/小说文学.md
- **术语表**：术语表.md
- **执行模式**：委派（长篇；见 WORKFLOW.md「单篇翻译流程」）

## 执行步骤

单篇 9 步（读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志）以 `prompts/翻译计划模板.md`「执行步骤」为准，本文件不重复。委派模式下由主 agent 派单，子代理简报含黄金样本与前章末尾。

## 篇目清单

由 `translation_queue.csv` 管理（24 章，约 352KB）。文件名 01-24 前缀即阅读顺序。

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-09-09 | 01-the-van-normans.md | done | 68 段 16 块，check rc=0；原文侧逐字一致（NBSP×10/FEFF×16 保留） |
| 2026-09-09 | 02-miss-morton-arrives.md | done | 96 段 17 块，check rc=0；原文侧逐字一致（FEFF×7/NBSP×6/thin×3 保留）；新登场人物均已括注：费森登、莫顿小姐、多萝西·伯特、西塞莉·杜皮伊、玛丽、梅普尔顿旅馆 |
| 2026-09-09 | 04-suicide-or.md | done | 80 段 16 块，check rc=0；原文侧逐字一致（FEFF×7 含标题 2 个/NBSP×12 保留）；亨特（Hunt）全书首现已括注；伦纳德/希尔斯首现于第 3 章故未注 |
| 2026-09-09 | 03-a-cry-in-the-night.md | done | 75 段 15 块，check rc=0；原文侧逐字一致（FEFF×15/NBSP×12/hair space×2 保留，源即 LF）；首现括注：哈里斯、希尔斯医生、伦纳德医生、新泽西州；新术语建议补录术语表：Venetian dagger→威尼斯匕首、county physician→县医官、A Cry in the Night→暗夜惊呼 |
| 2026-09-09 | 05-a-case-for-the-coroner.md | done | 77 段 15 块，check rc=0；原文侧逐字一致（FEFF×8/NBSP×20 保留，源即 LF）；本章无全书首现人名故未括注（沿用第 3、4 章全书首现原则）；「written confession/the written paper」统一作「字条」与第 3 章对齐，「county physician」作「县医生」与第 3 章正文对齐；章题 V. A Case for the Coroner→五　交由验尸官的案子（与章末点题句呼应） |
| 2026-09-09 | 06-fessenden-comes.md | done | 89 段 15 块，check rc=0；原文侧逐字一致（FEFF×9/NBSP×16/hair space×1 保留，源即 LF）；首现括注：本森验尸官、马卡姆小姐、卡尔顿太太（斯凯勒之母）；「字条」「县医生」「验尸审讯」沿用第 3-5 章对齐；章题 VI. Fessenden Comes→六　费森登到来 |
| 2026-09-09 | 07-mr-benson-s-questions.md | done | 59 段 12 块，check rc=0；原文侧逐字一致（FEFF×5/NBSP×15 含标题 1 个，源即 LF）；「Coroner Benson」统一作「本森验尸官」与第 6 章首现括注对齐、「Mr. Benson」作「本森先生」（8+7 处与源文一一对应），「字条」「县医生」沿用第 3-6 章对齐；源文 "Doctor Hill's theory" 系原书排印之误（Hills），照实译作希尔斯医生；章题 VII Mr. Benson's Questions→七　本森先生的讯问 |
| 2026-09-09 | 08-a-soft-lead-pencil.md | done | 87 段 22 块，check rc=0；原文侧逐字一致（NBSP×19/FEFF×2 保留，源即 LF）；本章人物均已于前章首现括注故未注；「字条」「本森验尸官」「本森先生」「自杀」「临终自白」沿用第 3-7 章对齐；章题 VIII. A Soft Lead Pencil→八　一支软铅铅笔（章题即破案关键线索）；新术语建议补录术语表：coroner's jury→验尸陪审团、rustic arbor→乡野趣味的凉亭 |
| 2026-09-09 | 09-the-will.md | done | 95 段 19 块，check rc=0；原文侧逐字一致（FEFF×3/NBSP×24 保留，源即 LF）；首现括注：皮博迪律师（Lawyer Peabody，新登场）、伊丽莎白·莫顿（Elizabeth Morton 之名全书首现）；「本森验尸官/本森先生」「管家哈里斯」「验尸审讯」「验尸陪审团」沿用第 3-8 章对齐，「notes」区分处理：马德琳当晚欲写/西塞莉代复的社交短简作「便条」与第 8 章对齐（自杀遗书「字条」本章不涉及）；理查德遗嘱条款译法与第 1 章背景叙述呼应；章题 IX The Will→九　遗嘱；新术语建议补录术语表：Lawyer Peabody→皮博迪律师、stenographer→速记员、latchkey→弹簧锁钥匙、residuary fortune→剩余财产 |
| 2026-09-09 | 10-some-testimony.md | done | 107 段 20 块，check rc=0；原文侧逐字一致（NBSP×22/FEFF×15 保留，源即 LF）；本章人物均已于前章首现故未注；「字条」「本森验尸官」（2 处）「本森先生」（10 处，均与源文一一对应）「自白」「便条」（西塞莉社交短简，与第 9 章对齐）沿用第 3-9 章对齐；hall 按位置分译「走廊/大厅」与第 3 章对齐；玛丽法语 m'seu/monsieur→先生、*Mon Dieu!* 保留法语原样与第 3 章对齐；章题 X Some Testimony→十　几份证词；新术语建议补录术语表：bellboy→侍应生、ice water→冰水 |
| 2026-09-09 | 11-i-decline-to-say.md | done | 96 段 19 块，check rc=0；原文侧逐字一致（FEFF×5/NBSP×27 保留，源即 LF）；首现括注：地方检察官（district attorney，全书首现，2 处对应）；「弹簧锁钥匙」（4 处，与 latchkey 一一对应）沿用第 9 章对齐，「字条」「本森验尸官」（3 处，与 Coroner Benson 一一对应）「本森先生」「存放贺礼的屋子」「验尸审讯」沿用第 3-9 章对齐；拒证短语分层：decline to answer→拒绝回答、I decline to do so→我拒绝奉告、章题点题句 I decline to say→我拒绝回答；源文首句 "questioned next When" 系原书排印脱句号，照实保留；章题 XI “I Decline to Say”→十一　「我拒绝回答」；新术语建议补录术语表：district attorney→地方检察官 |
| 2026-09-09 | 12-dorothy-burt.md | done | 80 段 19 块，check rc=0；原文侧逐字一致（FEFF×23/NBSP×7/hair space×1 保留，源即 LF，UTF-8 无 BOM）；本章人物均已于前章首现括注故未注（多萝西·伯特见第 2 章）；「缠人的玫瑰花蕾/玫瑰花蕾姑娘」沿用第 5 章定译、「字条」及引文「我爱S.，可他并不爱我。」沿用第 3-9 章对齐、「弹簧锁钥匙」「大客厅」「花匠伙计」「裁纸刀」「大厅」（hall 按位置，与第 3/10 章对齐）沿用前章；rose-garden→玫瑰园、sitting-room→起居室、（太太的）companion→女伴均本章全书首现（普通名词不注，仅记译法）；斜体标记按第 8 章惯例不保留、语气自见；章题 XII Dorothy Burt→十二　多萝西·伯特；新术语建议补录术语表：clinging rosebud→缠人的玫瑰花蕾、rose-garden→玫瑰园、sitting-room→起居室 |
| 2026-09-09 | 13-an-interview-with-cicely.md | done | 104 段 19 块，check rc=0；原文侧逐字一致（NBSP×21/FEFF×15 保留，源即 LF）；本章人物均已于前章首现括注故未注（多萝西·伯特见第 2 章）；「字条」「遗言」「十一点半/十一点一刻」「凭栏/楼梯栏杆」沿用第 3-12 章对齐，（太太的）companion→女伴与第 12 章对齐；斜体标记按 01-10 章主流惯例保留（*S*、*她*、*当然* 等）；Fessenden 对杜皮伊小姐由「您」转「你」（对应原文 “只有真话” 后的逼问）；源文 "Cicely eyes dropped" 系原书排印之误（Cicely’s），照实译作西塞莉的眼睛；章题 XIII An Interview with Cicely→十三　与西塞莉的一席谈；新术语建议补录术语表：无 |
| 2026-09-09 | 14-the-carleton-household.md | done | 77 段 18 块，check rc=0；原文侧逐字一致（FEFF×25/NBSP×9 保留，源即 LF，UTF-8 无 BOM）；本章人物均已于前章首现括注故未注（卡尔顿太太见第 6 章、多萝西·伯特见第 2 章）；「缠人的玫瑰花蕾」沿用第 5/12 章定译、「玫瑰园」「女伴」「伯特小姐」「十一点一刻/十一点半」「书房」「验尸审讯」「客厅」沿用第 3-13 章对齐；拒证句 I refuse to state→我拒绝回答，与第 11 章点题句呼应；卡尔顿私室焚毁之 notes 作「短笺」，与「字条」（自杀遗书）「便条」（社交短简）区分；斜体（*never*/*Could*/*were*/*that*）按主流惯例不保留、以语气词（决计/到底）自见；章题 XIV The Carleton Household→十四　卡尔顿家；新术语建议补录术语表：den→私室 |
| 2026-09-09 | 15-fessenden-s-detective-work.md | done | 81 段 20 块，check rc=0；原文侧逐字一致（FEFF×21/NBSP×21 保留，源即 LF，UTF-8 无 BOM）；本章人物均已于前章首现括注故未注；「字条」「大客厅」「花匠伙计」「书房」「起居室」沿用第 3-14 章对齐；玛丽法语 m’sieur/monsieur→先生与第 10 章对齐、mademoiselle→小姐；莫顿小姐焚毁之 papers 作「文件」（指向遗嘱，与第 14 章「短笺」区分）；马卡姆太太称谓敬「您」、费森登对基蒂称「你」与前章人称分层一致；斜体（*years*/*now*/*possible* 等）按主流惯例不保留、语气自见；章题 XV Fessenden’s Detective Work→十五　费森登的侦探功夫；新术语建议补录术语表：Rose of Dawn→破晓的玫瑰（费森登对基蒂的爱称） |
| 2026-09-09 | 16-searching-for-clues.md | done | 93 段 25 块，check rc=0；原文侧逐字一致（FEFF×7/NBSP×8/hair space×1/星标×4 保留，源即 LF，UTF-8 无 BOM）；首现括注：泰勒先生（Mr. Taylor，全书首现）、鲍西娅（Portia，莎剧典故意译）、香口珠（cachou，口含清口气之小糖珠）；「本森验尸官/本森先生」与源文一一对应，「书房」「客厅」「hall 按位置译大厅」「起居室」「侍应生」「冰水」「一条小小的线索」沿用前章对齐；斜体 *amusement*/*was* 原文侧照抄、中文侧不出现星标以措辞体现（2026-09-09 全书裁定）；侍应生口语硬币 quarter→两毛五、dime→一毛；Mr. Smarty-Cat Detective→自作聪明的猫儿大侦探（戏语意译）；章题 XVI Searching for Clues→十六　搜寻线索；新术语建议补录术语表：cachou→香口珠、Portia→鲍西娅 |
| 2026-09-09 | 【批次1暂停】16/24 竇 done（终检 16 文件 rc=0） | paused | 用户指令切换其他批次；17-24 均为 todo 未派发；认领锁保留待批次1下次断点续作；体例裁定：中文侧无星标 |
2026-09-10 | 17-miss-morton-s-statements | 双语块 31 对（127 段全对照）| check_bilingual 通过(exit 0)，术语沿用术语表（莫顿小姐/本森验尸官/玫瑰园/证人席/女伴兼社交秘书），无人名新现需注音
2026-09-10 | 18-carleton-is-frank | 双语块 22 对（67 段全对照）| check_bilingual 通过(exit 0)，原文侧逐字一致（FEFF×7/NBSP×2 保留，源即 LF 无空行，UTF-8 无 BOM）；术语沿用术语表（香口珠/地方检察官/梅普尔顿/玫瑰园/女伴/哈里斯/亨特先生/费尔班克斯），本章无新人名首现；新译名：reliquary→圣物盒、（婚礼）floral bower→花亭、exclusive opportunity→独有机缘、circumstantial evidence→环境证据；斜体 *know*/*don’t* 原文侧照抄、中文侧无星标（2026-09-09 裁定）；章题 XVIII Carleton Is Frank→十八　卡尔顿袒露实情；备注：认领时 doing 曾被外部还原为 todo（疑 OneDrive 同步），终态 done 已复核；新术语建议补录术语表：reliquary→圣物盒、floral bower→花亭、exclusive opportunity→独有机缘
2026-09-10 | 19-the-truth-about-miss-burt | 双语块 18 对（57 段全对照）| check_bilingual 通过(exit 0)，自检原文侧 57 段逐字一致（FEFF/NBSP 原样保留，UTF-8 无 BOM）；术语沿用术语表（多萝西·伯特/杜皮伊小姐/莫顿小姐/亨特/哈里斯/本森先生/验尸审讯/字条/玫瑰园）；notes 分层沿用第 13/14 章裁定：自杀遗书及 S.字条作「字条」、卡尔顿私人信件作「短笺」、社交应酬作「便条」；首现括注：圣物盒（reliquary，对齐第 18 章定译）、费尔班克斯侦探（Detective Fairbanks，全书首现）；前接 18 章结尾「推心置腹」语境（18 章尚为 todo，衔接待主 agent 对齐）；斜体（*did*/*ought*/*naive*）不保留星标、以语气自见；章题 XIX The Truth About Miss Burt→十九　伯特小姐的实情；新术语建议补录术语表：reliquary→圣物盒（与第 18 章一致）
2026-09-10 | 20-cicely-s-flight | 双语块 22 对（89 段全对照）| check_bilingual 通过(exit 0)，术语沿用术语表（本森先生/费尔班克斯/杜皮伊小姐/基蒂·弗伦奇/起居室/范·诺曼宅邸/梅普尔顿/玛丽法语 m’sieu→先生），原文侧逐字一致（FEFF×3/NBSP×14 保留，UTF-8 无 BOM）；首现括注：圣物匣（reliquary）；Grand Central Station→大中央车站、Waldorf→华尔道夫饭店（通行译法，前后两现一致）；电报引语保留 blockquote 结构、M./C. 缩写照源；斜体 *could*/*is*/*not* 中文侧不保留、以措辞体现（全书裁定）；新术语建议补录术语表：reliquary→圣物匣、Grand Central Station→大中央车站、Waldorf→华尔道夫饭店、hot box→轴箱发热
2026-09-10 | 21-a-successful-pursuit | 双语块 21 对（82 段全对照）| check_bilingual 通过(exit 0)，原文侧 82 段逐字一致（FEFF×3/NBSP×25 保留，UTF-8 无 BOM）；术语沿用术语表（杜皮伊小姐/亨特先生/验尸官本森/费尔班克斯/莫顿小姐/基蒂·弗伦奇/汤姆·威拉德/玛迪/梅普尔顿/哈里斯/验尸审讯）；首现括注：弗莱明·斯通（Fleming Stone，全书首现提名）；Grand Central Station→大中央车站对齐第 20 章；baluster→楼梯栏杆；斜体 *I*/*am*/*was*/*almost* 原文侧照抄、中文侧无星标（2026-09-09 裁定）；章题 XXI A Successful Pursuit→二十一　一场成功的追踪；备注：认领后 CSV 曾被并行写报错，重读后仅改本行，done 已复核
2026-09-10 | 22-a-talk-with-miss-morton | 双语块 14 对（60 段全对照）| check_bilingual 通过(exit 0)，原文侧 60 段逐字一致（FEFF×18/NBSP×8 保留，源即 LF 无空行，UTF-8 无 BOM）；术语沿用术语表（香口珠/弗伦奇小姐/玛迪/莫顿小姐/多萝西·伯特/费尔班克斯/验尸审讯/证人席/玫瑰园/女伴/卡尔顿太太/范·诺曼宅邸）；首现括注：弗莱明·斯通（Fleming Stone，正文首次提及、第 23 章登场）；记事册（memorandum book）对齐第 17 章「私人小记事册」；斜体 *could*/*knew*/*did* 中文侧不保留、以措辞体现（全书裁定）；you're a brick→您真是个大好人（口语意译）、rolling stone 意象直译保留；章题 XXII A Talk with Miss Morton→二十二　与莫顿小姐的一次谈话；备注：认领后 CSV 曾因并行写 20/21 章 done 而刷新，本行 doing 保留完好，终态 done 已复核
2026-09-10 | 23-fleming-stone | 双语块 24 对（72 段全对照）| check_bilingual 通过(exit 0)，原文侧 72 段逐字一致（NBSP×29/FEFF×2 保留，源即 LF 无空行，UTF-8 无 BOM）；术语沿用术语表（弗莱明·斯通/费森登/基蒂·弗伦奇/莫顿小姐/汤姆·威拉德/斯凯勒·卡尔顿/本森先生/费尔班克斯先生/哈里斯/杜皮伊小姐/香口珠/弹簧锁钥匙/起居室/范·诺曼宅邸）；房间名沿用全书既定：library→书房、drawing-room→客厅、hall→大厅、cellar→地窖；首现括注：瘦子吉姆（Slim Jim）、灰渣滑槽（ash-chute）；新译名：andirons→柴架、hearth→炉床；斜体 *anything* 原文侧照抄、中文侧无星标以语气自见（2026-09-09 裁定）；章题 XXIII Fleming Stone→二十三　弗莱明·斯通；新术语建议补录术语表：Slim Jim→瘦子吉姆、ash-chute→灰渣滑槽、andirons→柴架
2026-09-10 | 24-a-confession | 双语块 17 对（68 段全对照，全书末章）| check_bilingual 通过(exit 0)、可疑段落错配 0，自检原文侧 68 段逐字节一致（FEFF/NBSP 原样保留，UTF-8 无 BOM）；术语沿用术语表（香口珠/灰渣滑槽/特里普/泰勒先生/亨特/希尔斯医生/验尸官本森先生/莫顿小姐/玛迪/梅普尔顿旅馆/浪荡子/游廊/字条）；房间名沿用全书既定：library→书房、drawing-room→客厅、hall→大厅、cellar→地窖；parlor 本章为房间名首现，译「会客室」以与客厅区分；本章无新人名首现故无括注；斜体 *he*/*did*/*had* 原文侧照抄、中文侧无星标（2026-09-09 裁定）；结尾 tiny clue→一条小小的线索点题；drummers→旅行推销员、boiler manhole→锅炉人孔、scapegrace→浪荡子（对齐术语表）；章题 XXIV A Confession→二十四　自白；备注：全书 24 章至此全部 done；新术语建议补录术语表：boiler manhole→锅炉人孔、handspring→跟斗
