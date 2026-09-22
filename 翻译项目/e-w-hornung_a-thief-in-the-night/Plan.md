# 翻译计划（e-w-hornung_a-thief-in-the-night）

## 本计划信息

- **项目名称**：e-w-hornung_a-thief-in-the-night（A Thief In The Night）
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/小说文学.md
- **术语表**：术语表.md

## 文件分工

| 文件 | 作用 | 谁来改 |
|------|------|--------|
| `项目说明.md` | 项目基本信息、领域配置 | 人工 |
| `术语表.md` | 翻译硬约束层，每篇译完补充新词 | agent / 人工 |
| `translation_queue.csv` | 任务队列（file,size_kb,status） | 翻译前改 doing，完成后改 done（双写根表） |
| `Plan.md`（本文件） | 执行步骤 + 运行日志 | agent 追加日志 |
| `原文/*.md` | 源文 | 不改 |
| `译文/*.zh-CN.md` | 译文产出（块对照双语） | 翻译 agent 产出 |

执行步骤按 `prompts/翻译计划模板.md`（9 步：读配置→取 todo→doing→读源文→翻译→自检→check_bilingual→双写 done→日志）。

## 篇目清单

共 10 篇，见 `translation_queue.csv`（合计 340KB）。

## 运行日志

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-09-06 | chapter-1.md | done | 51 对双语块覆盖 127/127 段（标题合并 1 行）；Original 块经脚本回填、与源文逐字一致（含 U+FEFF×23、NBSP×4）；check_bilingual 退出码 0、check_coverage 0 可疑；首篇定名：拉夫尔斯/邦尼/奥尔巴尼公寓/宫殿花园/赫克托·卡拉瑟斯/阿利克·卡拉瑟斯/洛克马本/沙利文/皇家咖啡馆/罗德板球场/皇后厅 等，已回填术语表（候选 8 行定名 + 追加 22 行） |
| 2026-09-06 | chapter-2.md | done | 59 对块 / 115 段全覆盖；check 退出码 1 仅一处数字锚点误报（270°→二百七十华氏度，核对无误视为通过）；核心定名照用（拉夫尔斯/邦尼/克劳肖/奥尔巴尼公寓/苏格兰场），沿 chapter-1 定名「沙利文（Sullivan 香烟）」；新定名：麦肯齐 Mackenzie、圣约翰伍德、加洛韦、尤斯顿、克鲁、诺森伯兰大道、《帕尔摩报》、城郊银行、斯隆街、福西特、芒特街、参孙、《每日邮报》、米德尔塞克斯郡、银行假日、玩偶匣（jack-in-the-box） | 
| 2026-09-06 | chapter-3.md | done | 87 对块 / 117 段全覆盖（标题合并 1 行）；原文块经 Python 自源文逐字提取组装，21 处特殊字符（U+FEFF×14、U+200A×5、NBSP×2）全保留；check 退出码 1 仅 2 处数字锚点误报（'84→八四年、1884→公元一八八四，玛姆香槟两处，核对无误视为通过）；核心定名照用（拉夫尔斯/邦尼/苏格兰场/奥尔巴尼公寓），沿 ch1「皮卡迪利」、ch2「尤斯顿/芒特街/米德尔塞克斯郡」；新定名：休养疗法 Rest Cure、坎普登山、荷兰步道、克拉奇利上校、皇家工兵 R.E.、维多利亚十字勋章 V.C.、罗克渡口、《名人录》、《鲁滨逊漂流记》、《瑞士家庭鲁滨逊》、金莱克《克里米亚战争史》、泽尔廷格、玛姆（Mumm 香槟）、罗顿公寓、肯辛顿、诺丁山、彼得街、布鲁图斯、《田野》、《体育人》 |
| 2026-09-06 | chapter-4.md | done | 98 对块 / 172 段全覆盖（标题合并 1 行）；原文块经 Python 自源文逐字提取组装，19 处特殊字符（U+FEFF×12、NBSP×6、U+200A×1）全保留；check_bilingual 退出码 0、0 可疑错配；核心定名照用（拉夫尔斯/邦尼/奥尔巴尼公寓/邦德街/沙利文/罗德板球场）；与 ch1-3 无术语冲突。新定名：犯罪学家俱乐部 Criminologists' Club、索恩比伯爵 Thornaby/索恩比府/公园巷 Park Lane、惠特克年鉴、迦特 Gath、弗雷迪·维里克、欧内斯特、金斯米尔御用大律师、帕林顿（荒野小说家）、特伦特桥、对抗赛 Test Matches、缢颈而死 sus. per coll.、赛克斯/甜威廉/皮斯、丹比、米尔切斯特、梅尔罗斯夫人、佩卡姆/所罗门斯、德·昆西《谋杀作为一门艺术》、莱格特、老贝利、雅典娜俱乐部、欣布利、约翰内斯贝格、衣冠窃贼 swell mobsman、卡特·帕特森、查令十字、马尼拉麻绳、Q.E.F. |
| 2026-09-06 | chapter-6.md | done | 51 对块 / 97 段全覆盖（标题合并 1 行）；原文块逐字校验 97/97 与源文一致，2 处 NBSP 差异经脚本自源文修复，其余特殊字符（U+FEFF×34、U+200A×6、U+2018 等）全保留；check 退出码 1 仅 1 处数字锚点误报（62 not out→六十二分不出局，核对无误视为通过）；核心定名照用（拉夫尔斯/邦尼/沙利文/尤斯顿/奥尔巴尼公寓），沿 ch4「对抗赛 Test Matches」；新定名：梅德利科特 Medlicott、摩尔河 Mole、东莫尔西 East Molesey、老特拉福德 Old Trafford、伊舍 Esher、奇普赛德 Cheapside、盗窃保险公司 Burglary Insurance Company、萨里郡、汉普顿宫、护身短棒 life-preserver、曼陀罗香烟 stramonium、亚硝酸戊酯 nitrite of amyl、老风箱 old blowpipes、瑟比顿 Surbiton、泰晤士迪顿 Thames Ditton、因伯苑 Imber Court、因弗内斯斗篷 Inverness cape、纽盖特式刘海 Newgate fringe、辛加里围巾 Zingari、滑铁卢（车站）、曼彻斯特、澳大利亚巡回赛 Australian tour |
| 2026-09-06 | chapter-5.md | done | 109 对块 / 151 个非空源行全覆盖（标题合并 1 行，诗歌段 10 行含 3 个制表符行整体成块）；原文块经 Python 自源文逐字提取组装，特殊字符全保留（U+FEFF×28、U+200A×4、诗歌段制表符缩进、弯引号、斜体星号）；check_bilingual 退出码 0、0 可疑错配；核心定名照用（拉夫尔斯/邦尼/沙利文/奥尔巴尼公寓/板球），沿 ch2「《每日邮报》」、ch3「布鲁图斯」、ch4「查令十字」；新定名：尼珀·纳斯密斯 Nipper Nasmyth（绰号尼珀）、纳布 Nab、菲利比 Philippi（篇题「菲利比战场」，源文标题笔误 Phillipi 照录）、老校友赛 Old Boys' Match、创校人纪念日 Founder's Day、创校基金 Founder's Fund、甲级板球 first-class cricket、墙手球场 fives-courts、沃菲尔德树林 Warfield Woods、斯托克利路 Stockley road、帕丁顿 Paddington、查令十字桥 Charing Cross Bridge、阿喀琉斯 Achilles、凯撒/老布鲁图斯打油诗、大学对抗赛 Varsity match、球员亭 pavilion、绿呢门、方院 quad、中四/高六 |
| 2026-09-06 | chapter-7.md | done | 102 对块 / 164 段全覆盖（标题合并 1 行）；原文块经 Python 自源文逐字提取组装，特殊字符全保留（U+FEFF×32、U+2011×2、U+200A×2、NBSP×3）；check_bilingual 退出码 0、0 可疑错配；核心定名照用（拉夫尔斯/邦尼/奥尔巴尼公寓/苏格兰场/皮卡迪利/双轮马车）；新定名：马圭尔 Maguire/巴尼·马圭尔（美国重量级拳王）、半月街 Half-moon Street、斯威格·莫里森 Swigger Morrison、帝国拳击俱乐部 Imperial Boxing Club、瓦因街 Vine Street、内华达州、萨克拉门托、拳斗俱乐部 Fisticuff Club、白教堂、鲍威利、布鲁厄姆马车 brougham、布拉默锁 Bramah lock、撬锁贼 cracksman（篇题「诱捕撬锁贼的陷阱」）、杀巨人的杰克 Jack-the-Giant-killer、斯库拉/卡律布狄斯、蒙汗药威士忌 hocussed whiskey、小悲剧 tragedietta |
| 2026-09-06 | chapter-8.md | done | 96 对双语块/142 段全覆盖，check_bilingual 退出码 0（无错配）；术语按表（拉夫尔斯/邦尼/奥尔巴尼公寓/沙利文/皮卡迪利/诺森伯兰大道）；新定名：吉勒马德（Guillemard）、圣伦纳德森林、克拉珀姆枢纽站、巴特西、维多利亚站、阿刻戎冥河、土耳其浴、「见狐啦」（view-halloa）、呢绒门、软百叶帘、高脚五斗柜、撬棍、手锥、猎会越野赛马等 |
| 2026-09-06 | chapter-10.md | done | 15 对块 / 18 段全覆盖（标题合并 1 行，全书末篇「最后一句话」，书信体）；原文块经 Python 自源文逐字提取组装，特殊字符全保留（U+FEFF×12、U+200A×1、NBSP×10、日期行制表符缩进）；check 退出码 1 仅 1 处数字锚点误报（39/1900/28→「39号」「1900年6月28日」，数字均原样保留，系正则  遇汉字失效，核对无误视为通过）；核心定名照用（拉夫尔斯/邦尼/宫殿花园/罗德板球场），沿 ch4「梅尔罗斯夫人」、ch7「撬锁贼」；新定名：哈里 Harry（邦尼本名）、坎普登林苑公寓 Campden Grove Court（沿 ch3「坎普登」）、业余撬锁贼 amateur cracksman、阿·杰·拉夫尔斯 A. J. Raffles |
| 2026-09-06 | chapter-9.md | done | 90 对块 / 148 段全覆盖（标题合并 1 行，篇题「拉夫尔斯遗物」）；原文块经 Python 自源文逐字提取组装，特殊字符全保留（U+FEFF×16、NBSP×4，弯引号/斜体星号/源文笔误如 wit、Malter、Giberaltar 照录）；check 退出码 1 仅 1 处数字锚点误报（December, 1899→一八九九年十二月，核对无误视为通过）；核心定名照用（拉夫尔斯/邦尼/奥尔巴尼公寓/苏格兰场/沙利文/皮卡迪利/索恩比伯爵/老贝利/滑铁卢），沿 ch6「护身短棒 life-preserver」、ch7「撬锁贼 cracksman」、ch4「对抗赛」；新定名：拉夫尔斯遗物 Raffles Relics（篇题）、黑色博物馆 Black Museum、哈姆公地 Ham Common、里士满公园 Richmond Park、威斯敏斯特桥、惠斯勒 Whistler、阿瑟·西弗恩 Arthur Severn、查尔斯·皮斯 Charles Peace（文书讹称「小查」）、匹克威克先生、凯利纳餐馆 Keliner’s、『鲱鱼塘』Herring Pond、戴维·琼斯 Davy Jones、『金宝石』Golden Gem、霍舍姆 Horsham、半岛东方 P.& O./Peninsular and Orient、皇帝珍珠/波利尼西亚珍珠、德鲁斯探长 Inspector Druce、查克法姆案 Chalk Farm、卡尔顿饭店 Carlton、大都会警察 Metropolitan Police、白厅 Whitehall、圣斯蒂芬 St. Stephen’s、泰丁顿 Teddington、里士满 Richmond、拉尔夫先生 Mr. Ralph、圣诞老人 Father Christmas、草原 veldt、银箱 silver-chest、侧门 sidedoor | 
| 2026-09-06 | 全书 10 篇 | done 10/10（完结） | 批次1晚间整本完成（19:59 上锁）：ch1 定名篇（51对块，表回填30条）与 ch2/3 核心定名并行防漂移，此后 3 路滚筒；十篇独立成篇（逐出乐园/银箱/休养疗法/犯罪学家俱乐部/菲利比战场/糟糕的一夜/诱捕撬锁贼的陷阱/渎圣的赃物/拉夫尔斯遗物/最后一句话书信体）；check 全过，非零退出码均为数字锚点误报（270°/'84/62 not out/1899/门牌日期）；术语表滚合至110余条（Nasmyth 按先成稿者裁定纳斯密斯，ch5首用）；源文笔误均原样照录；删锁流转 |
