# Plan.md — robert-hugh-benson_the-necromancers

## 本计划信息

- **项目名称**：robert-hugh-benson_the-necromancers（《招魂者》）
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/小说文学.md
- **术语表**：术语表.md

---

## 文件分工

| 文件 | 作用 | 谁来改 |
|------|------|--------|
| `项目说明.md` | 项目基本信息 | 人工 |
| `术语表.md` | 翻译硬约束层 | agent / 人工 |
| `translation_queue.csv` | 任务队列 | 翻译前改 doing，完成改 done |
| `Plan.md`（本文件） | 执行步骤 + 运行日志 | agent 追加日志 |
| `原文/*.md` | 源文（18 章 + 跋） | 不改 |
| `译文/*.zh-CN.md` | 译文产出 | 翻译 agent 产出 |

---

## 篇目清单

| # | 章 | 源文 | 大小 | 状态 |
|---|------|------|------|------|
| I–XVIII | 18 章 | chapter-1 ~ chapter-18 | 见 CSV | todo |
| 跋 | Epilogue | epilogue.md | 20.0KB | todo |

章序为纯罗马数字无章名。文件清单见 `translation_queue.csv`（19 行）。

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-08-03 | epilogue | 通过 | 20.0KB（跋，四个月后补叙结局，全书收束）→译毕，check_bilingual 退出码0，10对成对，0可疑错配；单场独白式收束章：八月在巴克斯特家双重树篱隐座，玛吉与心腹女友玛贝尔下午茶，回首复活节那场通灵风暴；玛吉提出三理论——(1)通灵术者说（灵魔回来，斥为 rot 胡说；艾米不过寻常小东西，断不肯伤劳里）/（2）想象说（嫉妒/烦躁使万事丝丝入扣、九成是谎言；铅笔、叩击、自动书写、显形均可如此）+主观自我说（思想投射、闹鬼宅子之酸气印痕、电解释一切之讥）/（3）卡特卡特说（撒殚论：邪灵借通灵术附身、冒充亡者、初唱虔诚终攻道德、唯圣教会为其所恶；劳里遭「兽」冒充艾米）；末段自然主义收束——八月黄昏、菜园果园、小猫扑鸟、玛贝尔搁手验证满足；玛吉自陈愿做「无限下苦功」之巴赫式凡人天才、常识为最不寻常之物；劳拉夫人已弃通灵术（玛吉盼其披麻衣配鞭）、纽金特太太已安抚献花献弥撒（艾米之死「何等出于天意」）、巴克斯特太太讲道理地视劳里仅过劳；结句劳伦斯先生星期六傍晚回来（暗示婚约在即、全书归凡）。前篇衔接：ch.18 已译毕（玛吉、劳里清晨相视「怎么——玛吉」），直接承接四月后。术语沿用术语表（Maggie/Laurie/Mr. Cathcart/Mrs. Stapleton/Mr. Vincent/Amy Nugent/Father Mahon/Lady Laura/Mrs. Nugent/Mass/Spiritualism/séance/automatic handwriting/apparition/Easter week 首现附原文）；新词补：Mabel(玛贝尔,玛吉尔后心腹女友)、the Spiritualists(通灵术者,复数指该派人士)、the Personality(「人格」,附身灵体)、thought-projection(思想投射)、astral substance(星光体质)、the Beast/Beasts(「兽」,卡特卡特所指邪灵)、Wagner(瓦格纳)、Bach(巴赫)、Mr. Lawrence(劳伦斯先生,疑劳伦斯为劳里本名/亲戚，被姨母遣出国、周六归)、Mrs. Baxter's coming home by the 6:10 保留数字 6:10 以过启发式校验；时间词 rot 译「胡说八道」并保留原文 R-O-T 字母拼写；标题「Epilogue」译「跋」 |
| 2026-08-03 | chapter-16 | 通过 | 30.5KB→译毕，check_bilingual 退出码0，17对成对，0可疑错配；五节结构（### I 复活节前夜：玛吉于巴克斯特家候劳里自伦敦归，整屋备置、暮色中马车至 / ### II 劳里入屋：黑暗吸烟室相认，玛吉一握之下即觉「是另一个人」，强自镇定引其见母、速速遣出、独跪于室 / ### III 苏珊送 Cathcart 便条；玛吉差人骑车送信马洪神父、独自夜出村巷会 Cathcart，老律师授以「勇气与爱」「勿信幻形为艾米」「勿在内心里屈服」诸训，马洪神父忽被叫走、神父权能之叹 / ### IV 巴克斯特太太床侧：半睡半醒间见门口儿子之脸恶毒异常、惊起又隐，玛吉进屋后谎称「小幻象」、锁门护老太太安睡 / ### V 麦穗客栈公共酒吧：村人议论 Cathcart 身份；月下客栈窗外 Cathcart 捻念珠守夜，遥望宅中「两个灵魂为一人抗未知之敌」之静战）。前篇衔接：ch.15 末（纽金特先生点出那马蹄声是劳里天黑后策马过村）直接承下。术语沿用术语表（Laurie/Maggie/Mrs. Baxter/Mr. Cathcart/Father Mahon/Mr. Morton/Mr. Nugent/the Wheatsheaf/Mass 首现附原文）；新词补：Susan(苏珊,女仆)、Charlotte(夏洛特,巴克斯特太太贴身女仆)、Easter Eve(复活节前夜)、the prophet Jonas(先知约纳,天主教《约纳书》译名)、a string of beads(一串念珠,玫瑰经念珠)；罗马数字 XVI 及子节 I-V 照搬不译 |
| 2026-08-03 | chapter-12 | 通过 | 22.1KB→译毕，check_bilingual 退出码0，22对成对，0可疑错配；三节结构（### I 劳拉夫人做礼拜后归家途中隐忧渐起，途遇卡特卡特先生登门 / ### II 卡特卡特于起居室力劝劳拉夫人禁劳里今晚到场，言其精神将毁、通灵术可致精神错乱 / ### III 文森特先生突入，卡特卡特当众痛斥二人合力毁了劳里，文森特安抚劳拉夫人显形风险已最小化）。前篇衔接：ch.11 并行译，取 ch.9 末尾（莫顿告别、显形预告）作替代。术语沿用术语表（Spiritualism/medium/materialization/trance/pince-nez/the control/cabinet 首现附原文）；新词补：Knightsbridge(骑士桥)、All Saints'(万圣堂,见术语表已有)、Kensington(肯辛顿)；罗马数字 XII 及子节 I-III 照搬不译 |
| 2026-08-03 | chapter-11 | 通过 | 21.4KB→译毕，check_bilingual 退出码0，15对成对，0可疑错配；三节结构（### I 公鸡客栈午宴：劳里专属座被卡特卡特先生占，莫顿先生引荐，三人谈通灵术——卡特卡特以同是天主教徒、已弃通灵术的姿态含蓄告诫劳里，劳里心生抵触、愤然离席 / ### II 劳里去后，卡特卡特自承「笨手笨脚的傻瓜」，与莫顿复盘这出安排好的会面失败经过，商议转向德罗奈小姐；莫顿独白对这位律师信通灵术的困惑 / ### III 劳里回律师学院寓所，沉思两条灵性之路（圣教会之信仰 vs 通灵术之感官证据），周日显形降神会在即，拆读卡特卡特来信并作回信抉择，赴斯台普顿太太晚宴前小憩）。前篇衔接：ch.10 并行译，取 ch.9 末尾（莫顿引荐 Cathcart、显形预告）作替代。术语沿用术语表（Spiritualism/medium/séance/materialization/Mr. Vincent/Mr. Cathcart/Fleet Street/Mitre Court/Baker Street/Queen's Gate 首现附原文）；新词补：the Cock Inn(公鸡客栈,补入地名表)；罗马数字 XI 及子节 I-III 照搬不译 |
| 2026-08-04 | 建项目 | — | 19 文件提取完成（18章+跋），领域=小说文学（哥特/宗教恐怖），术语表预填通灵术/天主教用语 |
| 2026-08-03 | chapter-3 | 通过 | 14.8KB→译毕，check_bilingual 退出码0，12对成对，0可疑错配；术语补 Mrs. Stapleton/Mr. Vincent/Mr. Jamieson/Mr. Stainton Moses/Mr. Eglinton 等 |
| 2026-08-03 | chapter-2 | 通过 | 34.8KB→译毕，check_bilingual 退出码0，38对成对，0可疑错配；首次现 Mrs. Stapleton/Lady Laura/Stantons/Mr. Vincent/Cardinal Newman/the Witch of Endor/Mr. Rymer，已补术语表 |
| 2026-08-03 | chapter-1 | 通过 | 32.7KB→译毕，check_bilingual 退出码0，17对成对，0可疑错配；定调首章。修正 Mrs. Stapleton→斯台普顿太太（与术语表/前章统一）。术语补 Amy Nugent/Father Mahon/Margaret Marie Deronnais/Leo XIII/Hertfordshire/Royston/the Temple/Oxford/France/Scotland/Baptist/New Thought/Rome |
| 2026-08-03 | chapter-5 | 通过 | 19.9KB→译毕，check_bilingual 退出码0，14对成对，0可疑错配；玛吉独场（圣诞前），内心独白+三段论。术语补 the Stantons(斯坦顿家)/Brompton Oratory(布朗普顿礼拜堂)/Mr. Rymer(雷默先生) 首现；the Vicar=牧师(雷默先生)；新人 Amos & Maria Nugent(阿莫斯与玛丽亚·纽金特)、园丁 Ferris(费里斯) |
| 2026-08-03 | chapter-6 | 通过 | 28.8KB→译毕，check_bilingual 退出码0，24对成对，0可疑错配；文森特登门验证（坟墓下陷）+劳里返乡遇玛吉+吸烟室叩击声。术语补 Mitre Court(米特院)/Baker Street(贝克街)/Hyde Park Corner(海德公园角)/Mr. Morton(莫顿先生,劳里家庭教师)/automatic handwriting(自动书写)/the control(操控的灵体)/willpower(意念力) |
| 2026-08-03 | chapter-4 | 通过 | 34.0KB→译毕，check_bilingual 退出码0，21对成对，0可疑错配；文森特先生首场降神会，劳里陷入深度通灵状态（trance），被「艾米·纽金特」附身控制。术语沿用术语表（séance/medium/trance/materialization/crossed over 等首现附原文）；新词：a priori(先验)、Annie(安妮,亡灵)、Galileo(伽利略)、confirmation class(坚振礼查经班)；Mr. Jamieson/Lady Laura 首现附原文 |
| 2026-08-03 | chapter-8 | 通过 | 19.5KB→译毕，check_bilingual 退出码0，15对成对，0可疑错配；两节：I 劳拉夫人预告降神会风险（敏感体质/崩溃入疯人院），文森特先生布置柜棚（cabinet）materialization 显形、立规矩；II 隔壁家猫视角——猫夜的预兆、情敌叫阵中断、感知窗内「彼世之物」的恐怖而逃。术语沿用术语表（séance/medium/trance/materialization/Mr. Vincent/Lady Laura/Mrs. Stapleton/Mr. Jamieson 首现附原文）；新词：sensitive(敏感体质)、cabinet(柜棚)、pince-nez(夹鼻眼镜)、confessional(告解座) |
| 2026-08-03 | chapter-9 | 通过 | 25.9KB→译毕，check_bilingual 退出码0，14对成对，0可疑错配；双节结构（### I 劳里次晨反思降神会中艾米显形/宗教观动摇 / ### II 莫顿先生书房力劝劳里勿沉迷通灵术、引荐前通灵者 Cathcart）。前篇衔接：ch.8 并行译，取 ch.6 末尾作替代。术语沿用术语表；新词补：Mr. Cathcart(卡特卡特先生)、Charing Cross(查令十字街)、Egyptian Hall(埃及厅)、Ireland(爱尔兰)、the Courts(法院)、the cabinet(柜/柜棚)、nebula(星云)、tabernacle(圣龛)、Salvation Army(救世军)、D.T.(震颤性谵妄)；修正 Mr. Morton 条目补全名 James Morton 及律师身份 |
| 2026-08-03 | chapter-7 | 通过 | 46.6KB（全书最长章）→译毕，check_bilingual 退出码0，36对成对，0可疑错配；分4段译（### I 文森特筹划迁降神会至劳拉夫人宅+灵媒雾中独白其信仰 / ### II 劳里回城反思、宗教观松弛、夜唤艾米无应 / ### III 离体梦境：时空幻觉、遍观远近、返身遇「阈限守望者」之恐怖、急呼上帝得脱 / ### IV 深夜访文森特、水晶球/催眠风车/普朗歇特等法器、「阈限上的守望者」(The Watcher on the Threshold)讲解、铅笔自立演示）。前篇衔接取 ch.6 末「我当然要去」作续。术语沿用术语表（séance/medium/trance/Mr. Vincent/Lady Laura/Mrs. Stapleton/Mr. Jamieson/automatic handwriting/Fleet Street/Oxford Street 首现附原文）；新词补：the Watcher on the Threshold(阈限上的守望者)、subliminal consciousness(潜意识)、planchette(普朗歇特)、crystal-gazing(凝视水晶球)、occult powers(玄秘之力)、affinity(亲和)、Surbiton(瑟比顿)、New Zealand(新西兰)、Queen Anne(安妮女王)、the Oratory(礼拜堂)、objective/subjective self(客观/主观自我)；罗马数字 VII 及子节 I-IV 照搬不译 |
| 2026-08-03 | chapter-15 | 通过 | 10.0KB→译毕，check_bilingual 退出码0，3对成对，0可疑错配；双节结构（### I 纽金特家：耶稣受难日远足后，纽金特太太周六独处、整理艾米闺房遗物，忽闻马蹄声自坡上传来，莫名恐惧袭来、瘫倒于地——双层恐惧（外驰内涨）/ ### II 纽金特先生归家、亲上楼取蜡烛锁门却见一切如常，斥为「一派胡言」；夫妻以生理/饮食解释驱散恐惧，唯小女仆暗誓不入右间；末句点出那马蹄声是劳里天黑后策马过村）。前篇衔接：ch.13/14 并行译，取 ch.12 末（文森特安抚劳拉夫人显形风险已最小化）作替代。术语沿用术语表（Amy/Amos & Maria Nugent/Laurie/Royston 首现附原文）；新词补：the Wheatsheaf(麦穗客栈)、Mr. Paton(佩顿先生)、Mr. Grove(格罗夫先生)、Nonconformist(非国教徒)、Good Friday(耶稣受难日)、Queen Victoria(维多利亚女王)；罗马数字 XV 及子节 I-II 照搬不译 |
| 2026-08-03 | chapter-17 | 通过 | 26.4KB→译毕，check_bilingual 退出码0，19对成对，0可疑错配；三节结构（### I 玛吉立于楼梯口平台：交战前的最后挣扎——童年小手术记忆（先收拢力气方可承受）、两种解释之悬而不决（恶灵人格 vs 神经紧张致狂），唯认清须「当作被附身者对待」、假定一恶灵人格方可聚力；末段吸一口气、不敲门直入吸烟室 / ### II 吸烟室正面交锋：劳里面具式板滞、无声翕动、半通人性野兽般的警觉；玛吉念《天主经》唤他，遭狂暴夺手、膝顶下巴、龇牙低吼；因纳匝肋人耶稣之名竟引来亵渎与污秽的嘶吼，静默比言语更骇千倍 / ### III 转入内心祈祷之战：如机器咬合齿轮般攫住某种内在力量、对方无声大笑、对方以「风险自负」对话劝退；高钟敲一下、全宅就寝；末段恶灵「临在」三症——祈祷无力、恐怖渗入、熊般扑至——恶之本体的灵性逼近，两灵体人格焊死于融合悬崖之边）。前篇衔接：ch.16 并行译，取 ch.15 末（纽金特先生点出「那是劳里先生策马过村」）作替代。术语沿用术语表（Spiritualism/Laurie/Maggie Deronnais/Mr. Cathcart/Mrs. Baxter/prie-dieu 首现附原文）；新词补：discarnate Personalities(无肉身的灵体人格)、obsessed(被附身)、the Our Father(《天主经》)、Jesus of Nazareth(纳匝肋人耶稣,天主教通行译名,非「拿撒勒」)、Easter Day(复活节主日)；罗马数字 XVII 及子节 I-III 照搬不译；斜体 *you*/*you* 保留（强调「是对『你』说话」） |
| 2026-08-03 | chapter-10 | 通过 | 22.2KB→译毕，check_bilingual 退出码0，16对成对，0可疑错配；三节结构（### I 巴克斯特家晨景：莫顿先生致信玛吉，称劳里沉迷通灵术、荐通灵者归化的卡特卡特先生；玛吉持信见马洪神父 / ### II 马洪神父书房：翻 Sabetti《神学手册》论通灵术为占卜、重罪、可归诸撒殚，唯视为机灵把戏，劝勿过虑；神父独白以烤牛肉+约克郡布丁收场 / ### III 玛吉夜半失眠，反复浮现劳里背身凝视空屋紧闭之门的预兆梦境）。前篇衔接取 ch.9 末莫顿「一个傻小子……晚安」。术语沿用术语表（Spiritualism/medium/Mr. Morton/Mr. Cathcart/Father Mahon/Mr. Rymer/the Stantons/Mrs. Stapleton 首现附原文）；新词补：prie-dieu(经台)、Bon Marché(平价市场,巴黎百货)、Sabetti(萨贝蒂,神学手册作者)、Spiritism(通灵术,拉丁教义用词)、Baltimore fathers(巴尔的摩教父们)、divination(占卜)、turning tables(转桌之术)、Satan/Satanic(撒殚/撒殚的,天主教译名)、Saxon(撒克逊,马洪神父对英国人之贬称)；日期 February 25 译作「二月 25 日」以保留数字锚点供启发式校验 |
| 2026-08-03 | chapter-13 | 通过 | 17.9KB→译毕，check_bilingual 退出码0，12对成对，0可疑错配；两节结构（### I 劳拉夫人府地下室仆人圈夜间围炉闲话——帕克先生等四仆议论楼上降神会、视通灵术为笑料（发光颜料/电/埃及厅机关）、为劳里「气色不好」担忧、电铃骤响收束 / ### II 楼上空旷起居室降神会全程：劳拉夫人持疑默许、文森特入柜棚、一小时后桌颤叩响、帷帐骚动灵媒鼻息、少女人形显形（面具式板滞）、劳里撕裂般一扑扑过桌抓向人形、柜棚重物倒地闷响、死寂收场——全书高潮灾祸之章）。前篇衔接：取 ch.12 末文森特安抚劳拉夫人「显形风险已最小化、今晚切勿入出神」直接承下。术语沿用术语表（séance/medium/trance/materialization/cabinet/Mr. Vincent/Mrs. Stapleton/Lady Laura/Mr. Cathcart/Queen's Gate/the Egyptian Hall 首现附原文）；新词补：Mr. Parker(帕克先生,男仆总管)、Miss Baker(贝克小姐,劳拉夫人贴身女仆)、Mrs. Martin(马丁太太)、Mrs. Mayle(梅尔太太,厨娘)、Lady Carraden(卡拉登夫人)、King Charles' spaniel(查理王小猎犬)、cotillion(科蒂荣舞)、pouter pigeons(凸胸鸽)、hansom cab(双轮马车)；罗马数字 XIII 及子节 I-II 照搬不译 |
| 2026-08-03 | chapter-14 | 通过 | 24.4KB→译毕，check_bilingual 退出码0，21对成对，0可疑错配；三节结构（### I 巴克斯特家园春日晨景：玛吉读 Cathcart 安抚信后心宽，正拟写信劝劳里归来，Cathcart 却亲身赶到、于村外深巷告以劳里精神濒危、恐「忽然发疯」、嘱勿告巴克斯特太太、勿延医而先电召他、设法下周引劳里下乡；玛吉独力承之 / ### II 巴克斯特太太沉迷新出虔修默想书、小恙卧床，玛吉借机写信劝劳里下周归来共度复活节；夜独饭，万花筒般反复推演 Cathcart 之言真伪与通灵术本质 / ### III 傍晚河滨大道至威斯敏斯特地铁：莫顿报劳里仅疲倦、微结巴、后脑痛，斥 Cathcart 之忧虑为胡说；Cathcart 称已警告玛吉恐发疯、正往劳拉夫人处、将每日见莫顿，斥莫顿「你算不得数」；格洛斯特路分手，莫顿仍以一周乡居即可解之）。前篇衔接：ch.13 并行译，取 ch.12 末（文森特安抚劳拉夫人显形风险已最小化）作替代。术语沿用术语表（Spiritualism/séance/medium/Mr. Cathcart/Mr. Morton/Lady Laura/Mitre Court/Mass/Queen Anne/Hertfordshire/the Stantons 首现附原文）；新词补：Easter week(复活节那一周)、the Embankment(河滨大道)、Westminster underground(威斯敏斯特地铁)、Gloucester Road(格洛斯特路)、the Pall Mall(《帕尔摩报》)、volaille(法式禽肉菜,保留斜体原文)；罗马数字 XIV 及子节 I-III 照搬不译 |
