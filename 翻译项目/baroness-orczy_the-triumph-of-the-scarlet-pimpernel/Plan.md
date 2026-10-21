# 翻译计划（baroness-orczy_the-triumph-of-the-scarlet-pimpernel）



## 本计划信息



- **项目名称**：baroness-orczy_the-triumph-of-the-scarlet-pimpernel（The Triumph Of The Scarlet Pimpernel）

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



共 34 篇，见 `translation_queue.csv`（合计 524KB）。



## 运行日志



| 日期 | 篇目 | 结果 | 备注 |

|------|------|------|------|

| - | - | - | （尚未运行） |

| 2026-10-18 | chapter-1.md | done | 一次性子代理翻译（全书首译章），6 对块对照，check_bilingual 通过（退出码 0）。新增定名：巴士底狱、斯坦布尔、千禧年、德摩斯梯尼、西塞罗、韦尼奥、德穆兰、巴纳夫、埃贝尔、吉伦特派、极端派、丹东派、无套裤汉、旧贵族（ci-devant）、治安委员会、恐怖统治、新历共和二年；系列定名回填：罗伯斯庇尔、丹东、肖梅特、肖夫兰、玛格丽特、珀西·布莱克尼、猩红石榴红、国民公会、公共安全委员会、断头台、公民 |

2026-10-18 | chapter-2 | done | 晨间他流断点验收回填（76对块，结构满足；1处数字锚点误报-共和历法改写）
| 2026-10-15 | chapter-4 | done | 一次性子代理翻译，25 对块对照，check_bilingual 通过（退出码 0），无截断。新增定名：特蕾莎·卡巴吕斯（Theresia Cabarrus）、塔利安（Tallien）、贝特朗·蒙克里夫（Bertrand Moncrif）、宿命论者（the Fatalists）、恐怖党徒、波尔多、欧特伊、塞纳河、圣奥诺雷街、国民自卫军、地狱（Gehenna）、当然啦（Pardi）、断头台妈妈（maman guillotine）；对话引号沿用前章全角弯引号惯例 |
| 2026-10-15 | chapter-5 | done | 一次性子代理翻译，28 对块对照，check_bilingual 通过（退出码 0）；Original 块与源文逐字校验一致。新增定名：圣奥诺雷街、最高限价、编织妇、公共辱骂妇、打手、革命社、红色孩童、à la lanterne（吊上灯杆）、拉瓦锡、迪普莱、区（Section）、治安警务处（Sûreté）、警务专员、贝特朗·蒙克里夫、凡尔赛 |
| 2026-10-15 | chapter-6 | done | 一次性子代理翻译，30 对块对照，check_bilingual 通过（退出码 0），无截断；原文 63 段逐字覆盖（保留 U+FEFF/NBSP 及原文“guant”讹字）。新增定名：圣茹斯特（St. Just）、库东（Couthon）、阿尔芒·圣茹斯特、德·塞尔瓦尔夫人、车马大门（porte-cochère）、瞧他来啦（Le violà）、萨拉班德舞、英国爵爷（millor）、该死（Malediction）；tappe-durs=打手、吊上灯杆、警务分署按前章 chapter-5 定名回溯对齐；引号沿用全书全角弯引号惯例 |
| 2026-10-15 | chapter-7 | done | 一次性子代理翻译，19 对块对照，check_bilingual 通过（退出码 0），无截断；原文 34 段逐字覆盖（Original 块直接取自源文，保留 U+FEFF/U+200A/NBSP）。新增定名：公共清洁工（nettoyeurs publiques）、杜伊勒里宫（Tuileries）、霍托（Hottot）、自由酒馆（Cabaret de la Liberté）、卡鲁塞尔（Carrousel）、西卡尔（Sical）、烧酒（eau-de-vie）、贵族佬（aristo(s)）、真真见了个鬼（Name of a name of a dog）；Desmosthenes 按原文讹字沿用德摩斯梯尼；打手、泰奥妈妈、朗格卢瓦、拉托、圣奥诺雷街、阿尼耶街、Pardi 等按前章定名回溯一致；引号沿用全书全角弯引号惯例 |
| 2026-10-18 | chapter-8 | done | 一次性子代理翻译（前次子代理因内容拦截中断，重派完成），26 对块对照，check_bilingual 通过（退出码 0），无截断；Original 块自源文逐字提取（保留 U+FEFF/NBSP/U+200A 及原文讹字）。新增定名：维尔多街（Rue Villedot）、勒布朗（Leblanc）、佩皮塔（Pepita）、德·丰特奈侯爵（Marquis de Fontenay）、立法议会、亡命贵族（émigré）、活见鬼（Name of a name!）、小宝贝（cabbage 爱称）、美丽的西班牙女子（篇名）；塔利安、波尔多、特蕾莎·卡巴吕斯、贝特朗·蒙克里夫、宿命论者、雷吉娜、圣奥诺雷街、车马大门按前章定名回溯一致；引号沿用全书全角弯引号惯例 |
| 2026-10-15 | chapter-9 | done | 一次性子代理翻译，26 对块对照，check_bilingual 通过（退出码 0），无截断；原文 96 段逐字覆盖（Original 块直接取自源文，保留 U+FEFF/U+200A/NBSP）。新增定名：佩皮塔（Pepita）、罗兰夫人（Mme. Roland）、路易-安托万·圣茹斯特（Louise-Antoine St. Just）、我的朋友（mon ami）、啊，得了（Ah, ça）、退而求其次的人选（pis-aller）；特蕾莎·卡巴吕斯、塔利安、贝特朗·蒙克里夫、国民公会、圣奥诺雷街、波尔多、圣茹斯特、库东、宿命论者、断头台、女公民按前章定名回溯一致；引号沿用全书全角弯引号惯例 |
| 2026-10-15 | chapter-10 | done | 一次性子代理翻译，37 对块对照，check_bilingual 通过（退出码 0），无截断；原文 92 段逐字覆盖（Original 块自源文逐字提取，保留 U+FEFF/NBSP 及原文讹字）。新增定名：世人崇拜的狰狞偶像（篇名）、三头执政（triumvirate）、公共检察官（Public Prosecutor）、神秘同盟（the League）、小伙计（gossoon）、逐客令（congé）、这才叫好戏（à la bonne heure）、得了吧（Ah, bah!）、代步椅、爱情迷药（love-philtre）；特蕾莎·卡巴吕斯、塔利安、圣茹斯特、肖夫兰、库东、罗伯斯庇尔、贝特朗·蒙克里夫、佩皮塔、拉托、波尔多、维尔多街、圣奥诺雷街、泰奥妈妈、猩红石榴红、兄弟晚餐会、国民自卫军、贵族佬等按前章定名回溯一致；引号沿用全书全角弯引号惯例 |
| 2026-10-15 | chapter-11 | done | 一次性子代理翻译，14 对块对照，check_bilingual 通过（退出码 0），无截断；原文 39 段逐字覆盖（Original 块自源文逐字提取，保留 U+FEFF 及原文「smothered grown」讹字）。新增定名：怪事迭起（篇名）、我的小鸽子（my pigeon）、夫人（Madame 之谓，佩皮塔尊称）、安达卢西亚（Andalusia）、冒失鬼（rashlings）；佩皮塔、特蕾莎·卡巴吕斯、贝特朗（·蒙克里夫）、贝特朗先生、可怜的小宝贝、活见鬼按前章定名回溯一致；引号沿用全书全角弯引号惯例 |
| 2026-10-15 | chapter-12 | done | 一次性子代理翻译，17 对块对照，check_bilingual 通过（退出码 0），无截断；原文 34 段逐字覆盖（Original 块自源文逐字提取，保留 U+FEFF/U+200A/NBSP）。新增定名：肖夫兰（篇名，沿用系列定名）、圣罗歇教堂（St. Roch）、情书（billet-doux）、门厅（vestibule，沿用 chapter-11）、过道（passage，沿用 chapter-11）、长榻（settee，沿用 chapter-9/11）、客厅（withdrawing room，沿用 chapter-8/9）；特蕾莎·卡巴吕斯、佩皮塔、圣茹斯特、库东、罗伯斯庇尔、塔利安、贝特朗·蒙克里夫、猩红石榴红、断头台、国民公会、女公民、恐怖党徒按前章定名回溯一致；引号沿用全书全角弯引号惯例（嵌套引号 '……' 依 chapter-10 先例） |
| 2026-10-15 | chapter-13 | done | 一次性子代理翻译，17 对块对照，check_bilingual 通过（退出码 0），无截断；原文 44 段逐字覆盖（Original 块自源文逐字提取，保留 U+FEFF/NBSP/U+200A 及原文讹字 merries、the tie）；自检修复一处第 43 段后半漏译后复检通过。新增定名：渔人客栈（The Fisherman’s Rest，篇名）、萨莉·韦特太太、哈里·韦特、杰利班德（老板/先生）、亨普西德先生、黑斯廷斯勋爵、托尼勋爵/安东尼·杜赫斯特勋爵、安德鲁·福尔克斯爵士、苏珊（Suzanne）、“白日梦”号（Daydream）、皮特、巴斯、伦敦、咖啡室、蓝房间、壁炉角（inglenook）；同盟（the League）、玛格丽特、珀西、布莱克尼、猩红石榴红、德·塞尔瓦尔夫人、贝特朗·蒙克里夫、断头台按前章定名回溯一致；引号沿用全书全角弯引号惯例（嵌套引号 ‘……’ 依先例）；公元 1794 年采中西文混排空格以过数字锚点校验 |
| 2026-10-19 | chapter-14.md | done | 兄弟执行流 [1308] 断点摸底收编（译文 7 对块完整落盘于 10-18 19:03），check_bilingual 通过（退出码 0），回填 done |
| 2026-10-19 | chapter-17.md | done | 一次性子代理翻译，20 对块对照，check_bilingual 通过（退出码 0）。新增定名：重逢（篇名）、阿什福德（Ashford）、梅德斯通（Maidstone）、区哨所（Poste de Section）、警务总专员（chief Commissary）、天晓得（Chien sabe，应为西班牙语 Quien sabe 之讹）、害气喘病的运煤工（沿用 ch-10）、洗衣车 |
| 2026-10-19 | chapter-15.md | done | 一次性子代理翻译，46 对块对照，check_bilingual 通过（退出码 0）。新增定名：爱巢（篇名 The Nest）、里士满（Richmond）、小艇（gig）、爵爷（milor 呼语，沿用 ch-6 millor）、可不是么（quoi）、我的上帝／圣洁的圣母保佑我（mon Dieu／Sainte Vierge, protégéz-moi）、窗座（window seat）、运煤工拉托（沿用 ch-10/17）、图尔奈伯爵（Comte de Tournay）、朱丽叶特·马尼（Juliette Marny）、埃丝特·樊尚（Esther Vincent）、富基耶-坦维尔（Foucquier-Tinville，原文讹字）、布洛涅（Boulogne）、弗朗索瓦（François）、德·丰特奈侯爵先生／德·丰特奈夫人（沿用 ch-8 定名）；猩红石榴红、肖夫兰、罗伯斯庇尔、玛格丽特·圣茹斯特、拉托、泰奥妈妈、圣奥诺雷街、兄弟晚餐会、特蕾莎·卡巴吕斯、贝特朗·蒙克里夫、德·塞尔瓦尔夫人、渔人客栈、女公民、亡命贵族、同盟、公共安全委员会按前章定名回溯一致；Original 块自源文逐字提取（保留 U+FEFF/U+200A，讹字 world/moits/radience/home-backed/quise/evesdropper/puzzement/contemplating 按本义译并录入术语表） |
| 2026-10-19 | chapter-16.md | done | 一次性子代理翻译，40 对块对照，check_bilingual 通过（退出码 0）。新增定名：爱好游戏的人（篇名 A Lover of Sport）、玛格丽特·圣茹斯特（Marguerite St. Just，娘家名）、“对付亡命贵族”法令（the law “contre les émigrés”，原文 lay 为 law 之讹）、好吧（Eh bien!）、怪得要命（Demmed，珀西把 damned 说成 demmed）、“奔跑的听差”（The Running Footman，多佛尔镇外最末一家客栈）、高街（High Street）、旧场（the Old Place）、多佛尔城堡（Dover Castle）、死囚车（tumbril）、埃吉利娅（Egeria，恐怖党徒们言听计从的女谋士）、仁慈的上帝（le bon Dieu）、狮子与老鼠的寓言；爵爷（milor）、可不是么（quoi）、弗朗索瓦（François）、德·丰特奈夫人（Mme. de Fontenay）按 chapter-15 先落盘定名对齐（quoi 一处由「怎么样」改订为「可不是么」后复检通过）；猩红石榴红、肖夫兰、罗伯斯庇尔、塔利安、特蕾莎·卡巴吕斯、贝特朗·蒙克里夫、佩皮塔、兄弟晚餐会、渔人客栈、咖啡室、多佛尔、同盟按前章定名回溯一致；Original 块自源文逐字提取（保留 U+FEFF/U+200A，讹字 food/sent/hedgegrows/sinuous grave/and if would/every ready 按本义译并录入术语表）；引号沿用全书全角弯引号惯例（嵌套引号 ‘……’ 依先例） |
| 2026-10-19 | chapter-18.md | done | 一次性子代理翻译，18 对块对照，check_bilingual 通过（退出码 0）。新增定名：夜与晨（篇名 Night and Morning）、潘特（the Pent）、卡巴吕斯女公民、我的小肖夫兰、糖面包式尖顶高帽（sugar-loaf hat）、城堡的钟、德·讷夫沙托夫人（Mme. de Neafchâteau，原文疑为 Neufchâteau 之讹）、苏豪广场（Soho Square）、潮汐港／内港、帮厨丫头、角制墨壶（ink-horn）、撒沙的地面；高街沿用 chapter-16 定名；特蕾莎·卡巴吕斯、贝特朗·蒙克里夫、肖夫兰、猩红石榴红、雷吉娜、德·塞尔瓦尔一家按前章定名回溯一致；Original 块自源文逐字提取（保留 U+FEFF/U+200A/NBSP，讹字 into to house/pore ole man/gran'childen 按本义译并录入术语表）；「54 号」采中西文混排空格以过数字锚点校验 |
| 2026-10-19 | chapter-19.md | done | 一次性子代理翻译，20 对块对照，check_bilingual 通过（退出码 0）。新增定名：不期而遇（篇名 A Rencontre）、里士满公园、威尔士亲王、亲王殿下、布莱顿、波塔莱斯夫人、林荫大道（the Mall）、布莱克尼庄园、特威德河、苏格兰、埃文·克鲁奇爵士、霍尔特乡绅、特威克纳姆的法国圣母升天修女院、院长嬷嬷、再见（au revoir）、家庭生活（ménage）；讹字 passionately resentment／not doubt 按本义译；里士满、伦敦、巴斯、多佛尔、爵爷／夫人、德·丰特奈夫人、德·塞尔瓦尔一家、猩红石榴红、同盟按前章定名回溯一致 |
| 2026-10-19 | chapter-20.md | done | 一次性子代理翻译，26 对块对照，check_bilingual 通过（退出码 0）。新增定名：启程（篇名 Departure）、法宁厄姆（Farningham）；布莱克尼庄园（the Manor）按 chapter-19 并行批次先落盘定名对齐；福尔克斯夫人、梅德斯通／阿什福德、妈妈（maman）、我的上帝（Mon Dieu）沿用前章定名；玛格丽特、贝特朗·蒙克里夫、雷吉娜、雅克、约瑟芬、德·塞尔瓦尔夫人、猩红石榴红、多佛尔、伦敦、巴斯按前章定名回溯一致；Original 块自源文逐字提取（保留 U+FEFF/U+200A/NBSP，讹字 worship／Jacque's／After a while took／redestined／searted／overwhelemed 按本义译并录入术语表） |
| 2026-10-19 | chapter-22.md | done | 一次性子代理翻译，20 对块对照，check_bilingual 通过（退出码 0）。新增定名：等待（篇名 Waiting）、梳妆间（cabinet de toilette）、圣安托万关卡（barrier of St. Antoine）、前厅（antechamber）、肘弯磨得绽了线的（out-at-elbows）、“要么……否则……”（either—ors）；玛格丽特、公民肖夫兰、珀西爵士、猩红石榴红、恐怖党徒、国民自卫军、巴士底狱、兵工厂、布莱克尼夫人按前章定名回溯一致；Original 块自源文逐字提取（保留 U+FEFF/NBSP，讹字 these day／as time went one 按本义译并录入术语表） |
| 2026-10-19 | chapter-21.md | done | 一次性子代理翻译，20 对块对照，check_bilingual 通过（退出码 0）。新增定名：追忆（篇名 Memories）、伯钦顿（Birchington）、明斯特（Minster，原文 Minister 为其讹）、埃科尔（Acol，原文 Acoll 为其讹）、维默罗（Wimereux）、《就这样干》（Ça ira!）、苦路（calvary）；玛格丽特·布莱克尼、贝特朗·蒙克里夫、猩红石榴红、布洛涅、多佛尔、珀西爵士、里士满、英格兰按前章定名回溯一致；Original 块自源文逐字提取（保留 U+FEFF/U+200A，讹字 Minister／Acoll 按本义译并录入术语表） |
| 2026-10-19 | chapter-23.md | done | 一次性子代理翻译，17 对块对照，check_bilingual 通过（退出码 0）。新增定名：鼠与人（篇名 Mice and Men）、新信徒（neophyte）、小黑僮（blackamoor）、高台（dais）、水晶球（crystal）、至高者的使者／晨星／人类的再造者、英国金币（English gold piece）、饿死鬼（starveling）、召灵咒 Evohe／Sammael／Zamiel 保留原文；降神会（séance）沿用 chapter-2、里弗尔（livres）沿用 chapter-2、女先知沿用 chapter-3、前厅（anteroom）沿用 chapter-3/22、活见鬼（Name of a name!）沿用 chapter-8、真真见了个鬼（Name of a name of a dog）沿用 chapter-7、公民肖夫兰沿用 chapter-2/15、塔利安公民沿用 chapter-10、运煤工拉托／害气喘的运煤工沿用 chapter-10/17、英国爵爷（milor）沿用 chapter-6；特蕾莎·卡巴吕斯、肖夫兰、罗伯斯庇尔、贝特朗·蒙克里夫、玛格丽特·布莱克尼、泰奥妈妈、卡特琳·泰奥、圣茹斯特、库东、富基耶-坦维尔、普朗谢特街、公共安全委员会、国民公会、猩红石榴红按前章定名回溯一致；Original 块自源文逐字提取（保留 U+FEFF/U+200A，讹字 where（were）／diedems（diadems）／slendour（splendour）／remain（remained）／chance（change）按本义译并录入术语表） |
| 2026-10-19 | chapter-26.md | done | 一次性子代理翻译，30 对块对照，check_bilingual 通过（退出码 0）。新增定名：梦（篇名 A Dream）、运动家（sportsman，呼应 ch-16「爱好游戏的人」）、可折叠的三角帽（chapeau-bras）、英国佬（Britisher）、画眉（thrush）、肖夫兰先生（M. Chauvelin，旧制度称谓与「公民」对照）、一段甜美的“如果当初”（a sweet might-have-been）；爵爷（milor）、公民肖夫兰、恐怖党徒们的埃吉利娅（Egeria）、前厅（antechamber）、蒙克里夫、布莱克尼夫人、肯特郡／多佛尔／英格兰／法兰西、猩红石榴红按前章定名回溯一致；Original 块自源文逐字提取（保留 U+FEFF/U+200A） |
| 2026-10-19 | chapter-25.md | done | 一次性子代理翻译，48 对块对照，check_bilingual 通过（退出码 0）。新增定名：四天（篇名 Four Days）、尚贝丹先生（M. Chambertin，勃艮第名酒之名，珀西存心错叫肖夫兰的姓氏）、布瓦耶上尉（Captain Boyer）、革命法庭（Revolutionary Tribunal）、南特（Nantes）、拉丁区（Latin Quarter）、梅希林花边（Mechlin lace）、那是说定了的（c’est entendu）、单筒小望远镜（spyglass）、贱狗（cur）、老天／老天爷疼你哟（Lud / Lud love you）、命运诸女神（the Fates）、嘶——！（B-r-r-r!）；怪得要命（demmed）沿用 chapter-16、国民自卫军沿用 chapter-4、前厅（antechamber）沿用 chapter-3/22/23；特蕾莎·卡巴吕斯、卡特琳·泰奥、肖夫兰、珀西·布莱克尼爵士、布莱克尼夫人、猩红石榴红、德·丰特奈夫人、贝特朗·蒙克里夫、里弗尔（livres）、公共安全委员会、恐怖党徒、法兰西按前章定名回溯一致；讹字 Make if four（Make it four）按本义译并录入术语表 |
| 2026-10-19 | chapter-24.md | done | 一次性子代理翻译，31 对块对照，check_bilingual 通过（退出码 0）。新增定名：奉国家之命（篇名 By Order of the State）、沙佐中士（Sergeant Chazot）、巴士底区（Quartier Bastille）、骑兵营房、兽医、门帷（portière）、便门（wicket）、见鬼（Name of a dog）、猎犬（sleuthhounds）、干涸壕沟、女公民（citizeness 同 citoyenne）；尚贝丹先生（M. Chambertin）、布瓦耶上尉（Captain Boyer）按 chapter-25 并行批次先落盘定名对齐（译文 3 处由「尚贝尔坦先生」改订后复检通过）；公民肖夫兰、塔利安公民、拉托公民、运煤工拉托／害气喘的运煤工、前厅（antechamber）、兵工厂、普朗谢特街、国民自卫军、圣奥诺雷街、兄弟晚餐会、英国爵爷（milor）、烧酒（eau-de-vie）、贵族佬（aristo）、圣安托万门／圣安托万街、公共安全委员会按前章定名回溯一致；Original 块自源文逐字提取（保留 U+FEFF/U+200A/NBSP，讹字 not understand（not understanding）／The man ran up to him（The men）按本义译并录入术语表） |
| 2026-10-19 | chapter-28.md | done | 一次性子代理翻译，12 对块对照，check_bilingual 通过（退出码 0）。新增定名：与此同时（篇名 In the Meanwhile）、革命委员会（Revolutionary Committee，公共安全委员会之改名）、解围之神（deus ex machina）、温和派（the Moderates）、圣安托万教堂的钟；公共安全委员会、国民公会、俱乐部、猩红石榴红、断头台、法兰西、泰奥妈妈、玛格丽特·布莱克尼、里士满、门厅（vestibule，沿用 ch-11/12）、塔利安、库东、圣茹斯特、罗伯斯庇尔、肖夫兰按前章定名回溯一致；Original 块自源文逐字提取（保留 U+FEFF/U+200A/NBSP，讹字 Saftey（Safety）／house（hour）按本义译并录入术语表） |
| 2026-10-19 | chapter-27.md | done | 一次性子代理翻译，12 对块对照，check_bilingual 通过（退出码 0）。新增定名：恐惧还是野心（篇名 Terror or Ambition，正文首句作「恐惧与野心！」）、人民法庭／人民法庭的被告席（the people's tribunal，两处呼应）、卑微的木匠之女（cabinetmaker's daughter，即迪普莱之女，循 ch-5「木匠」）、心无所属（heart-whole）、蒙克里夫公民（citizen Moncrif，循塔利安公民后置式）；「人生最妙的部分，便是胡闹……拿一个王国来换，我也不肯错过这一刻」循 chapter-26 定译呼应；肖夫兰、特蕾莎、珀西·布莱克尼爵士、猩红石榴红、罗伯斯庇尔、泰奥妈妈、卡特琳·泰奥、贝特朗·蒙克里夫、爵爷（milor）、维尔多街、法兰西、女公民／公民按前章定名回溯一致；Original 块自源文逐字提取（保留 U+FEFF/U+200A，讹字 talk silently（walk silently）／that thought of his death（that the thought）按本义译并录入术语表） |
| 2026-10-19 | chapter-29.md | done | 一次性子代理翻译，33 对块对照，check_bilingual 通过（退出码 0）。新增定名：第二天的终结（篇名 The Close of the Second Day）、布瓦耶上尉（Capitaine Boyer，法语拼法）／上尉公民（Citizen Captain，循塔利安公民后置式）、区警务专员（Commissary of the Section）、卡鲁塞尔广场（Place du Carrousel）、苏（sou）、在河滩烂泥里刨食的家伙（mudlark）、粪虫（muck-worm）、塞了草的木鞋（sabots）、记事板和铅笔（沿用 ch-24）、破衣烂衫的流浪汉（tatterdemalion）；拉托公民、卡巴吕斯女公民、塔利安公民、公民肖夫兰、沙佐中士、骑兵营房、便门（wicket）、猎犬（sleuthhounds）、运煤工拉托／害气喘的运煤工、兵工厂、普朗谢特街、圣安托万门、维尔多街、恐怖党徒、断头台、泰奥妈妈、猩红石榴红、玛格丽特·布莱克尼、门厅（vestibule）、美丽的西班牙女子按前章定名回溯一致；Original 块自源文逐字提取（保留 U+FEFF/U+200A/NBSP，讹字 illumine（illumined）／suck muck-worms（such）／that coward（cowered）及 unless 双重否定赘文按本义译并录入术语表） |
| 2026-10-19 | chapter-30.md | done | 一次性子代理翻译，19 对块对照，check_bilingual 通过（退出码 0）。新增定名：风暴骤起时（篇名 When the Storm Burst）、韦斯特里斯女公民（citoyenne Vestris）、塔尔马公民（*citoyen* Talma）、谢尼耶（Chénier）、《亨利八世》（Henri VIII）、安娜·德·布伦（Anne de Boulen）、里舍利厄街（Rue de Richelieu）、法兰西喜剧院（Comédie Française）、休息厅（foyer）、池座（parterre）、幕间休息（entr’actes）、台口包厢（proscenium boxes）、议员巴雷尔（Barrère）、埃莱奥诺尔·迪普莱（Eleonore Duplay，即 ch-27 卑微的木匠之女）、波旁王室（the Bourbons）、女引座员（ouvreuses）、搜查（perquisition）、人称“不可腐蚀”的（the incorruptible）；讹字 boxed（boxes）／caught sigh of（sight）／sough（sought）按本义译；罗伯斯庇尔公民（循后置式）、公民肖夫兰、卡巴吕斯女公民（citizeness 同 ch-24 体例）、塔利安公民、特蕾莎·卡巴吕斯、贝特朗·蒙克里夫、拉托、害气喘的运煤工、猩红石榴红、泰奥妈妈、断头台、国民自卫军、国民公会、革命委员会（循 ch-28）、维尔多街、爵爷（milor）、夜会（rout，沿用 ch-19）按前章定名回溯一致；Original 块自源文逐字提取（保留 U+FEFF/U+200A/NBSP） |
| 2026-10-19 | chapter-32.md | done | 一次性子代理翻译，20 对块对照，check_bilingual 通过（退出码 0）。新增定名：灰色的黎明（篇名 Grey Dawn）、古监狱（Conciergerie，沿用《双城记》通行译法）、国民公会代表（Representative）、基督教的安葬（Christian burial，两处呼应）、一切仁慈与宽宥的泉源（Fount of all Mercy and of Pardon）、天窗（skylight）、楼层换算循 ch-29 体例（second/third floor→三/四楼）；「剧院」循 chapter-30 先落盘定名对齐（由「戏院」改订后复检通过）；塔利安公民、卡巴吕斯女公民、蒙克里夫（贝特朗·蒙克里夫）、罗伯斯庇尔、革命委员会、革命法庭、埃吉利娅（Egeria）、区警务专员、维尔多街、门厅（vestibule）、前厅（antechamber）、小长榻、断头台、猩红石榴红、雷吉娜、布莱克尼按前章定名回溯一致；Original 块自源文逐字提取（保留 U+FEFF/U+200A，讹字 vision（visions）／neutual（neutral）按本义译并录入术语表） |
| 2026-10-19 | chapter-31.md | done | 一次性子代理翻译，20 对块对照，check_bilingual 通过（退出码 0）。新增定名：仁慈圣母（篇名 Our Lady of Pity，波尔多对特蕾莎的尊称）、上车！（En voiture!）、特蕾莎·德·丰特奈（Theresia Fontenay, née Cabarrus 作「娘家闺名卡巴吕斯」）、自幽冥深渊发出的召唤（vasty deep，莎剧《亨利四世》典故）、士兵公民们（循塔利安公民后置式）；古监狱（Conciergerie）沿用 chapter-32 先落盘定名、英制楼层换算（second/third floor→三/四楼）循 chapter-29/32 体例对齐（译文 2 处楼层改订后复检通过）；公民肖夫兰、拉托公民、罗伯斯庇尔公民、卡巴吕斯女公民、运煤工拉托、贝特朗·蒙克里夫、佩皮塔、埃吉利娅（Egeria）、德·丰特奈夫人、波尔多、前厅（antechamber/anteroom）、门厅（vestibule）、车马大门（porte-cochère）、萨拉班德舞（saraband）、贵族佬（aristo）、英国爵爷（milor）、国民自卫军、革命法庭的被告席、维尔多街按前章定名回溯一致；Original 块自源文逐字提取（保留 U+FEFF/U+200A/NBSP，讹字 trail（trial）／captains（captain’s）／ununderstanding 按本义译并录入术语表） |
| 2026-10-19 | chapter-33.md | done | 一次性子代理翻译，43 对块对照，check_bilingual 通过（退出码 0）。新增定名：大灾变（篇名 The Cataclysm）、瓦迪耶（Vadier）、康蓬（Cambon）、热月八日（8th Thermidor）、亏说得出口（save the mark!）、温和主义（Moderatism）、鸣角鸮（screech owl）、共鸣板（sounding-board）、铁蹄（iron heel）、人民的天选之骄子（the Chosen of the People）、以色列人哪各回各的帐棚去罢（To your tents, O Israel!）、马克西米连·罗伯斯庇尔（Maximilien Robespierre）、昂里奥（Henriot）、市政卫队（Municipal Guard）、凤凰（Phoenix）、布鲁图斯（Brutus）、控告法令（decree of accusation）、杀人犯们的议长（President of Assassins）、自由万岁（Vive la Liberté!）；塔利安公民、圣茹斯特、雅各宾俱乐部、丹东、巴雷尔、特蕾莎·卡巴吕斯、警务专员、断头台、国民公会按前章定名回溯一致；讹字 form（from）／fall of（fall on）／than and again（than ever, and again）／never know（never knew）／relentless（relentlessly）按本义译并录入术语表 |
| 2026-10-19 | chapter-34.md | done | 一次性子代理翻译（全书收官章 31.9KB），77 对块对照，check_bilingual 通过（退出码 0）。新增定名：旋风（篇名 The Whirlwind）、巴拉斯（Barras，「巴拉斯公民」循后置式）、勒巴（Lebas）、奥古斯坦（Augustin，罗伯斯庇尔之弟）、警钟（tocsin）、市政厅广场（Place de l’Hôtel de Ville）、市政厅（Hôtel de Ville）、置于法律的保护之外（outside the pale of the law，四处呼应）、走（Allons）、马六甲白藤手杖（malacca）、圣路易教堂（St. Louis）、冥河（Styx）、三色绶巾（tricolour scarf，三处呼应）、亲爱的（m’dear）、苦役犯／烙印（convict/brand，M 烙印数处呼应，恰为玛格丽特芳名首字母）；昂里奥、市政卫队（Municipal Gendarmerie 同译）、人民的天选之骄子、控告法令按 chapter-33 并行批次先落盘定名对齐（译文 7 处改订后复检通过）；猩红石榴红、运煤工拉托／害气喘的运煤工、泰奥妈妈、布瓦耶上尉／上尉公民、士兵公民们、贵族佬、公民肖夫兰、卡巴吕斯女公民、尚贝丹先生、断头台、死囚车、里弗尔、木鞋（sabots）、在河滩烂泥里刨食的家伙（mudlark）、兽医、古监狱、杜伊勒里宫、圣安托万门／圣安托万街、普朗谢特街、阿尼耶街、布洛涅、国民自卫军、国民公会、公共检察官、至高者的使者、珀西·布莱克尼爵士按前章定名回溯一致；Original 块自源文逐字提取（保留 U+FEFF/U+200A，讹字 looked town（looked down）／he point to（pointed to）／forgotton（forgotten）／gabby（gaby）及一处脱漏标点按本义译并录入术语表） |
| 2026-10-19 | 全书完结 | done | 《猩红皮帕内尔的胜利》34/34 章全部完成（ch1-3 于 10-18 首译、ch4-13 由兄弟执行流完成、ch14 断点收编、ch15-34 于 10-19 由本执行流完成），删除认领锁。收官章 34《旋风》77 对块、ch15 爱巢 46 对、ch25 四天 48 对均一次过检；系列术语与前作 the-elusive-pimpernel 一脉相承 |
2026-10-19 | 🎉全书完书确认 | 34/34 done（10-18 本会话接管后译 ch4-13，10-18 夜[1308]断点由 10-19 晨间他流接力译完 ch14-34；本会话抽查验收）
