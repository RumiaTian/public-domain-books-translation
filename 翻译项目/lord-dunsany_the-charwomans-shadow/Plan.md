# 翻译计划：打杂女工的影子

## 本计划信息

- **项目名称**：lord-dunsany_the-charwomans-shadow
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/小说文学.md
- **术语表**：术语表.md
- **执行模式**：委派（长篇；见 WORKFLOW.md「单篇翻译流程」）

## 执行步骤

单篇 9 步（读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志）以 `prompts/翻译计划模板.md`「执行步骤」为准，本文件不重复。委派模式下由主 agent 派单，子代理简报含黄金样本与前篇末尾。

## 篇目清单

由 `translation_queue.csv` 管理（30 篇，约 383KB）。

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
| 2026-09-14 | III The Charwoman Tells of Her Loss（打杂女工自述所失） | done | 13 对块 28 段；check_bilingual exit 0；新定名：术艺大师、术士、打杂女工、阿拉贡、提托诺斯、老妪、银莲花、仙灵 |
| 2026-09-14 | the-lord-of-the-tower-finds-a-career-for-his-son.md（I 塔楼之主为儿子谋前程） | done | 15 块对／38 段，check_bilingual exit 0 无错配；回填术语表硬约束 9 行（塔楼与岩林之主、约瑟夫神父、林中之屋、黄金时代、伊曼纽尔、马克、彼得、高岗上的学校、尘世），并按表对齐 magician→术士、philosopher's stone→哲人石。阅读顺序：各源文首行自带罗马数字章号即全书顺序，按号衔接 I→XXX：I the-lord-of-the-tower…、II ramon-alonzo-comes-to-the-house-in-the-wood、III the-charwoman-tells-of-her-loss、IV ramon-alonzo-learns-a-mystery-known-to-the-reader、V ramon-alonzo-learns-of-the-box、VI there-is-talk-of-gulvarez、VII ramon-alonzo-follows-the-art、VIII ramon-alonzo-shares-the-idleness-of-the-maidens-of-aragona、IX the-technique-of-alchemy、X the-exposure-of-the-false-shadows、XI the-chill-of-space、XII mirandola-demands-a-love-potion、XIII ramon-alonzo-compounds-the-potion、XIV the-folk-of-aragona-strike-for-the-faith、XV ramon-alonzo-talks-of-technique-and-muddles-his-father、XVI the-work-of-father-joseph、XVII the-three-fair-fields、XVIII the-love-potion、XIX father-joseph-explains-how-the-laity-have-no-need-of-the-pen、XX the-magician-imitates-a-way-of-the-gods、XXI white-magic-comes-to-the-wood、XXII ramon-alonzo-crosses-a-sword-with-magic、XXIII the-plan-of-ramon-alonzo、XXIV ramon-alonzo-dances-with-his-shadow、XXV the-release-of-the-shadow、XXVI the-wonderful-casting、XXVII they-dread-that-a-witch-has-ridden-from-the-country-towards-moon-s-rising、XXVIII gonsalvo-sings-what-had-been-the-latest-air-from-provence、XXIX the-casket-of-silver-and-oak-is-given-to-se-or-gulvarez、XXX the-end-of-the-golden-age |
| 2026-09-14 | II Ramon Alonzo Comes to the House in the Wood（中文题名自拟：拉蒙·阿隆索来到林中之屋） | 完成 | 12 对块 38 段；check_bilingual exit 0；术语随表（法术/大师/术士/林中之屋/高岗上的学校），新增术语 10 条 |
| 2026-09-14 | IV 拉蒙·阿隆索得知一桩读者早已知晓的奥秘 | 完成 | 10 对块；check_bilingual exit 0；Master 对齐 II 章（术艺大师／大师）；回填术语：法术、奥秘大人、束脩、转生、哲人石、震旦等 |
| 2026-09-14 | VIII Ramon Alonzo Shares the Idleness of the Maidens of Aragona（中文题名自拟：拉蒙·阿隆索与阿拉贡少女们共享闲散） | done | 11 对块 38 段；check_bilingual exit 0 无错配；术语随表（拉蒙·阿隆索/术士/术艺大师/阿拉贡/林中之屋/约瑟夫神父/黄金时代/奥秘大人/打杂女工/塔楼与岩林之主）；新定名 3 条：堂（Don）、小姐（señorita）、黑法术（the Black Art），均回填术语表 |
| 2026-09-14 | VI There Is Talk of Gulvarez（中文题名自拟：众人谈起古尔瓦雷斯） | done | 13 对块 48 段；check_bilingual exit 0 无错配；对齐 VIII 章新硬约束 the Black Art→黑法术；回填术语 8 行：古尔瓦雷斯、影谷公爵、尊显大人（Magnifico）、《罗德里格斯编年史》、塔楼夫人、武装侍卫、钱柜、黑暗诸权势 |
| 2026-09-14 | VII Ramon Alonzo Follows the Art（中文题名自拟：拉蒙·阿隆索研习法术） | done | 11 对块 29 段；check_bilingual exit 0、可疑错配 0；弯引号写盘校验无损；术语随表（法术/术士/大师/束脩/哲人石/震旦/阿拉贡/彼得/阿非利加/西班牙）；回填新词 4 条：影匣（shadow-box）、嬗变（transmutation）、萨拉曼卡主教、十字圣号 |
| 2026-09-14 | V Ramon Alonzo Learns of the Box（中文题名自拟：拉蒙·阿隆索得知那只匣子） | done | 15 对块 65 段；check_bilingual exit 0；术语随表（术士/大师/法术/束脩/银莲花/彼得/塔楼与岩林/黄金时代/老妪/打杂女工）；新定名：小魔怪（imp）、匣子（box）、酸模草（Dockweed） |
| 2026-09-14 | X The Exposure of the False Shadows（中文题名自拟：假影子的败露） | done | 7 对块 22 段；check_bilingual exit 0、可疑错配 0；弯引号写盘校验无损（首段跨三段连续引语，续段开引号体例与源文一致）；术语随表（哲人石/术士/大师/嬗变/束脩/林中之屋/阿拉贡/西班牙/十字圣号/仙灵）；回填新词 3 条：阿里奥娜（Ariona）、洛伦（Lolun）、无敌舰队（the Armada） |
| 2026-09-14 | XII Mirandola Demands a Love-Potion（中文题名自拟：米兰多拉索要爱情魔药） | done | 12 对块 52 段；check_bilingual exit 0、可疑错配 0；弯引号写盘校验无损；术语随表（拉蒙·阿隆索/术士/大师/束脩/影匣/哲人石/嬗变/震旦/打杂女工/林中之屋/小少爷/旧绿门/猎猪犬；「奉祀法术的屋子」与「中文」对齐 IV 章）；回填新词 12 条：堂娜（Donna）、爱情魔药（love-potion）、祈祷书（prayerbook）、猎猪犬（boarhound）、毗湿奴（Vishnu）、海伦（Helen）、奥兹曼迪亚斯（Ozymandias）、拉美西斯（Rameses）、玫瑰精油（attar of roses）、萤火虫（glowworm）、中文（Chinese） |
| 2026-09-14 | XI The Chill of Space（中文题名自拟：太空之寒） | done | 19 对块 68 段；check_bilingual exit 0、可疑错配 0；术语随表（拉蒙·阿隆索/术士/术艺大师/黑法术/影匣/打杂女工/银莲花/尘世/阿拉贡/挂锁），洛伦/阿里奥娜对齐 X 章定名并移除冗余标注；回填新词 4 条：太空（Space）、木星、灵／恶灵、幽影 |
| 2026-09-14 | IX The Technique of Alchemy（中文题名自拟：点金术的法门） | done | 10 对块 47 段；check_bilingual exit 0、可疑错配 0；弯引号写盘校验无损；术语随表（拉蒙·阿隆索/银莲花/阿拉贡/打杂女工/术士/大师/术艺大师/法术/猎野猪/束脩/匣子/哲人石/嬗变/尘世）；「sacred to magic」取「奉予魔法的屋子」（对齐 XI；与 XII「奉祀法术的屋子」尚存分歧，请主 agent 裁量统一）；回填新词 2 条：咒语学（dictology）、黄铁矿（iron pyrites） |
| 2026-09-14 | XIII Ramon Alonzo Compounds the Potion（中文题名自拟：拉蒙·阿隆索配制魔药） | done | 9 对块 33 段；check_bilingual exit 0、可疑错配 0；弯引号写盘校验无损（第 21 段外双内单嵌套引语栈校验通过）；术语随表（拉蒙·阿隆索/米兰多拉/术士/大师/打杂女工/林中之屋/奉祀法术的屋子/影匣/爱情魔药/阿拉贡/银莲花/小魔怪/萤火虫/玫瑰精油/海伦/奥兹曼迪亚斯/尘世/中文/假影子），XII 已注专名（Helen/Ozymandias）不再重复标注；elixir vitae 按表保留拉丁斜体；回填新词 1 条：执笔之术（the art of the pen） |
| 2026-09-14 | XVI The Work of Father Joseph（中文题名自拟：约瑟夫神父的活计） | done | 9 对块 43 段；check_bilingual exit 0、可疑错配 0；弯引号写盘校验无损；术语随表（米兰多拉/约瑟夫神父/塔楼之主/影谷公爵/古尔瓦雷斯/武装侍卫/塔楼夫人/彼得/大师/束脩/拉蒙·阿隆索）；回填新词 3 条：希达戈（hidalgo）、加尔达宪警（la Garda）、家宅诸神（Penates） |
| 2026-09-14 | XV Ramon Alonzo Talks of Technique and Muddles His Father（中文题名自拟：拉蒙·阿隆索大谈法门，绕晕了他父亲） | done | 9 对块 28 段；check_bilingual exit 0、可疑错配 0；弯引号写盘校验无损；术语随表（拉蒙·阿隆索/米兰多拉/塔楼与岩林之主/打杂女工/爱情魔药/嬗变/古尔瓦雷斯/先生/阿拉贡/猎猪矛/宽边帽）；回填新词 4 行：宁芙（nymph）、招股说明书（prospectus）、阿诺德·威尔金顿／默里·詹金斯爵士、罗弗／菲多／陶泽 |
| 2026-09-14 | XIV The Folk of Aragona Strike for the Faith（中文题名自拟：阿拉贡乡民为信仰而战） | done | 13 对块 31 段；check_bilingual exit 0、可疑错配 0；弯引号写盘校验无损（弯双引号 14 对、直引号 0）；英文块由 Python 自源文逐字节拼装保真；术语随表（拉蒙·阿隆索/打杂女工/术士/法术/阿拉贡/西班牙/塔楼）；回填新词 11 行：信仰（the Faith）、圣米迦勒、圣约瑟、圣犹大（非加略人犹大）、圣安妮、影潮（shadow-tide）、歇晌（siesta）、杜鹃花（azalea）、银河（the Milky Way）、大地（Earth 人格化，别于尘世）、是啊（Aye） |
| 2026-09-14 | XVII The Three Fair Fields（中文题名自拟：三块秀美田园） | done | 11 对块 50 段；check_bilingual exit 0、可疑错配 0；弯引号写盘校验无损（弯双引号 42 对、直引号 0）；英文块由 Python 自源文逐行拼装保真；术语随表（米兰多拉/古尔瓦雷斯/塔楼夫人/塔楼之主/约瑟夫神父/影谷公爵/贡萨尔沃/拉蒙·阿隆索/钱柜/武装侍卫/希达戈/黄金时代/先生/猎猪矛）；回填新词 6 行：三块秀美田园（the three fair fields）、小瓶（vial）、弓手（bowmen）、半人马（centaur）、金克朗（crowns of the Golden Age）、猎猪矛（boar-spears） |
| 2026-09-14 | XVIII The Love-Potion（中文题名自拟：爱情魔药） | done | 10 对块 43 段；check_bilingual exit 0、可疑错配 0；弯引号写盘校验无损（中文块弯双引号 25 对、直引号 0、无 BOM）；术语随表（影谷公爵/塔楼之主/塔楼夫人/约瑟夫神父/米兰多拉/古尔瓦雷斯/贡萨尔沃/希达戈/尊显大人/法术/爱情魔药/拉蒙·阿隆索/阿非利加/西班牙/弓手，bowmen 对齐 XVII 同刻补录行）；回填新词 6 条：斯芬克斯、吉卜赛人、神圣教会、堂区、高脚杯（chalice，XVII 章已现且译文并行，请主 agent 与 XVII 裁量对齐）、酒壶（flagon） |
| 2026-09-14 | XIX Father Joseph Explains How the Laity Have No Need of the Pen（中文题名自拟：约瑟夫神父解说平信徒无需执笔） | done | 11 对块 39 段；check_bilingual exit 0、可疑错配 0；弯引号写盘校验无损（弯双引号 37 对、直引号 0）；英文块由 Python 自源文逐字节拼装保真；术语随表（约瑟夫神父/拉蒙·阿隆索/贡萨尔沃/古尔瓦雷斯/塔楼夫人/塔楼之主/米兰多拉/影谷公爵/大师/术士/林中之屋/影匣/爱情魔药/奉祀法术的屋子/黑法术/震旦/希达戈/阿拉贡/猎猪矛/先生/修士）；回填新词 4 行：平信徒（laity）、阿洛伊修斯弟兄（Aloysius / Brother Aloysius）、旌旗（gonfalon）、羊皮纸（parchment） |
| 2026-09-14 | XX The Magician Imitates a Way of the Gods（中文题名自拟：术士效法诸神之道） | done | 11 对块 32 段；check_bilingual exit 0、可疑错配 0；弯引号写盘校验无损（弯双引号 27 对、直引号 0、无 BOM、英文块逐字节自源文拼装）；术语随表（拉蒙·阿隆索/术士/大师/法术/影匣/打杂女工/林中之屋/震旦/阿拉贡/彼得/米兰多拉/奉祀法术的屋子/灵/太空/尘世）；回填新词 5 行：萨拉戈萨（Saragossa）、魔法讲席（the Chair of Magic）、叮（Ting）、潘（Pan）、海王星（Neptune） |
| 2026-09-14 | XXII Ramon Alonzo Crosses a Sword with Magic（中文题名自拟：拉蒙·阿隆索以剑斗法术） | done | 10 对块 50 段；check_bilingual exit 0、可疑错配 0；弯引号写盘校验无损（中文块直引号 0、无 BOM、英文块由 Python 自源文逐字节拼装保真）；术语随表（拉蒙·阿隆索/术士/大师/束脩/打杂女工/影匣/爱情魔药/奉祀法术的屋子/银莲花/叮/尘世/读经台/点金之术）；回填新词 3 行：咚／当（Tong/Tang）、物质归一（the oneness of matter）、细剑（rapier） |
| 2026-09-14 | XXI White Magic Comes to the Wood（中文题名自拟：白魔法来到林间） | done | 16 对块 49 段；check_bilingual exit 0、可疑错配 0；弯引号写盘校验无损（中文块弯双引号 41 对、直引号 0、无 BOM、英文块逐字节自源文拼装）；术语随表（拉蒙·阿隆索/打杂女工/老妪/术士/约瑟夫神父/黑法术/十字圣号/圣水/影匣/匣子/林中之屋/震旦/小魔怪/假影子/真影子/羊皮纸/天国/是啊(Aye)/尘世）；回填新词 6 行：白魔法（white magic）、阿拉拉巴（Alaraba）、地精（gnome）、精灵（elf，别于仙灵 fairy）、圣水（holy water）、影子王国（the Kingdom of Shadows） |
| 2026-09-14 | XXIII The Plan of Ramon Alonzo（中文题名自拟：拉蒙·阿隆索的计划） | done | 16 对块 23 段；check_bilingual exit 0、可疑错配 0；弯引号写盘校验无损（中文块弯双引号 13 对、直引号 0、无 BOM、英文块由 Python 自源文逐字节拼装保真）；术语随表（拉蒙·阿隆索/打杂女工/术士/大师/影匣/挂锁/奉祀法术的屋子/法术/黑法术/束脩/叮/咚／当（沿用 XXII 定名）/细剑/斯芬克斯/萨拉戈萨/魔法讲席/尘世）；Earth 分义：the folk of Earth、the narrower views of Earth 译「尘世」，the past of the Earth（地质）译「地球」；回填新词 9 行：鲁伊·洛佩斯（Ruy Lopez）、印度群岛（the Indies）、可畏大师（the Dread Masters）、巫道（Wizardry）、穆护（Magi）、西顿（Sidon）、波斯咒语（Persian spells）、雍（Yung）、阿布（Ab） |
| 2026-09-14 | XXIV Ramon Alonzo Dances with His Shadow（中文题名自拟：拉蒙·阿隆索与他的影子共舞） | done | 7 对块 17 段；check_bilingual exit 0、可疑错配 0；弯引号写盘校验无损（中文块弯双引号 12 对、直引号 0、无 BOM、英文块由 Python 自源文逐字节拼装）；术语随表（拉蒙·阿隆索/大师/术士/法术/奉祀法术的屋子/影匣/挂锁/打杂女工/银莲花/米兰多拉/萨拉戈萨/魔法讲席/束脩/叮/雍/阿布/波斯咒语/西班牙/尘世），对齐 XXIII：the Dread Masters→可畏大师；新定名 4 条：山中伯爵（the Count of the Mountain）、罕（Han，叮雍罕全咒）、救赎（salvation）、Aye 大师庄语→诚然（别于 XIV 村民「是啊」） |
| 2026-09-14 | XXVIII Gonsalvo Sings What Had Been the Latest Air from Provence（中文题名自拟：贡萨尔沃唱起那支昔日普罗旺斯的最新曲调） | done | 7 对块 25 段；check_bilingual exit 0、可疑错配 0；弯引号写盘校验无损（中文块弯双引号 15 对、直引号 0、无 BOM，英文块由 Python 自源文逐字节拼装保真）；术语随表（塔楼之主/约瑟夫神父/彼得/拉蒙·阿隆索/米兰多拉/古尔瓦雷斯/贡萨尔沃/公爵（影谷公爵）/塔楼夫人/猎猪矛/弓手/术士/林中之屋）；回填新词 5 行：普罗旺斯（Provence）、比利牛斯山（the Pyrenees）、游吟诗人（troubadours）、普罗旺斯语（Provençal）、安达卢西亚（Andalusia） |
| 2026-09-14 | XXVI The Wonderful Casting（中文题名自拟：奇妙的投影） | done | 11 对块 32 段；check_bilingual exit 0、可疑错配 0；弯引号写盘校验无损（中文块弯双引号 22 对、直引号 0、无 BOM、英文块由 Python 自源文逐字节拼装保真）；术语随表（拉蒙·阿隆索/老妪/阿拉贡/打杂女工/术士/银莲花（Anemone）附注/悉听尊便对齐 XX/bargain 取「买卖」对齐 VII 与 XII）；回填新词 1 行：阿尔卑斯（Alpine） |
| 2026-09-14 | XXV The Release of the Shadow（中文题名自拟：影子的释放） | done | 9 对块 37 段；check_bilingual exit 0、可疑错配 0；弯引号写盘校验无损（中文块直引号 0、无 BOM、英文块由 Python 自源文逐字节拼装、逐段弯引号开合差与源文完全一致）；术语随表（打杂女工/阿拉贡/大师/术士/先生/法术/奉祀法术的屋子/影匣/挂锁/西班牙/救赎/尘世/来世/咒法/巫道/林中之屋）；charwoman 自述之 Aye 对齐 XIV 取「是啊」（别于 XXIV 大师庄语「诚然」，请主 agent 裁量）；回填新词 2 行：精灵之乡（elfland）、距离的平方（the square of the distance） |
| 2026-09-14 | XXVII They Dread That a Witch Has Ridden from the Country Towards Moon’s Rising（中文题名自拟：他们惧怕有女巫自月升之国驰来） | done | 21 对块 68 段；check_bilingual exit 0、可疑错配 0；弯引号写盘校验无损（中文块弯双引号 101 对、直引号 0、无 BOM、英文块由 Python 自源文逐行拼装保真）；术语随表（拉蒙·阿隆索/银莲花/米兰多拉/古尔瓦雷斯/先生/约瑟夫神父/彼得/大师/黑法术/信仰/是啊/救赎/大地/林中之屋/塔楼/塔楼之主/阿非利加/小少爷/羊皮纸）；回填新词 8 行：月升之国、女巫、扫帚、石榴、椴树、紫杉、五月游春、里格 |
| 2026-09-14 | XXX The End of the Golden Age（中文题名自拟：黄金时代之终） | done | 10 对块 33 段；check_bilingual exit 0、可疑错配 0；弯引号写盘校验无损（中文块弯双引号 40 对、直引号 0、无 BOM，英文块由 Python 自源文逐字节拼装保真，L2 源文 U+FEFF 原样保留）；术语随表（拉蒙·阿隆索/银莲花/彼得/米兰多拉/影谷公爵/塔楼/约瑟夫神父/术士/大师/弓手/小少爷/月升之国/黄金时代/打杂女工/奉祀法术的屋子/羊皮纸/比利牛斯山/普罗旺斯/潘/小魔怪/仙灵/尘世/长老橡树旁暗号手帕）；elixir vitae 按表保留拉丁斜体；末章收束：君王赦令抹平低微出身、charwoman 一词因避讳而废用、黄金时代随术士携魔法诸物入月升之国而终；回填新词 27 行（摩尔人/公正的君主/公正而荣耀的君主/得胜的君王·得胜的君主/命运女神/赦令/石楠/助理司铎/大主教/大教堂/钟乐/半羊人/fays 仙灵/精灵丘/仙环/永罚/查令十字街/老泽姆布拉街/古物馆/伦敦/马德里/欧罗巴/四部金色古书/避讳戏称五连） |
| 2026-09-14 | XXIX The Casket of Silver and Oak Is Given to Señor Gulvarez（中文题名自拟：银橡木匣赠予古尔瓦雷斯先生） | done | 25 对块 88 段；check_bilingual exit 0、可疑错配 0；弯引号写盘校验无损（中文块弯双引号 64 对、直引号 0、无 BOM，英文块由 Python 自源文逐字节拼装保真，逐字节比对与源文一致）；术语随表（贡萨尔沃/古尔瓦雷斯/米兰多拉/影谷公爵/约瑟夫神父/塔楼夫人/塔楼之主/彼得/弓手头领/武装侍卫/三块秀美田园/银橡木匣/小姐/尊显大人/黄金时代/猎猪矛/石楠）；the Moors 对齐 XXX 已定行摩尔人；回填新词 3 行：踏梯（stile）、曼陀林（mandolin）、喜鹊（magpie） |
| 2026-09-14 | 整书完结（30/30 章） | 全书 30 章批量复检通过（零非零 exit） | 体例：「## 罗马数字 英文章名 / 中文题名」+章题译名报备制（30 题全自拟报备）；阅读顺序依源文首行罗马数字排出（文件名与章号无序）；邓萨尼典雅古风轻讽腔+咒语音节锁词（叮/雍/阿布/咚/当/罕）；主 agent sed 统一「奉祀法术的屋子」（3:2 多数方，IX/XI 回改 4 处）；跨章自对齐密集：黑法术/影匣/可畏大师/弓手/摩尔人等双向报备互改；术语表并发回填经代理自查去重+主 agent 复扫无乱码无真重复 |
