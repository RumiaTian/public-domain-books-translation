# Plan.md — ameen-rihani_the-book-of-khalid

## 本计划信息

- **项目名称**：ameen-rihani_the-book-of-khalid（《哈立德之书》）
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
| `术语表.md` | 翻译硬约束层 | agent / 人工 |
| `translation_queue.csv` | 任务队列 | 翻译前改 doing，完成改 done |
| `Plan.md`（本文件） | 执行步骤 + 运行日志 | agent 追加日志 |
| `原文/*.md` | 源文（36 文件：序+3卷名+3题献+25章+跋） | 不改 |
| `译文/*.zh-CN.md` | 译文产出 | 翻译 agent 产出 |

---

## 篇目清单

**整体结构**：序 Al-Fatihah → Book I（In the Exchange，题献+8章）→ Book II（In the Temple，题献+10章）→ Book III（In Kulmakan，题献+10章）→ 跋 Al-Khatimah

文件清单见 `translation_queue.csv`（36 行）。各章章名见原文标题。

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-08-04 | 建项目 | — | 36 文件提取完成（序+3卷名页+3题献+25章+跋），领域=小说文学（哲理讽刺小说），术语表预填阿拉伯/伊斯兰术语及西方典故 |
| 2026-08-06 | book-1.md | done | 卷名页；仅合并标题「Book the First / 第一卷」「In the Exchange / 在交易所」，无块标记；check 退出码 0（无 Original 块属正常） |
| 2026-08-06 | epigraph-1.md | done | 题献 To Man；1 对 Original/Chinese 块（整段献辞作一块）；署名「> 哈立德」；check 退出码 0，可疑错配 0 处；新增术语：World-Temple 世界神殿、the Fountain 泉、the God of Humour 幽默之神 |
| 2026-08-06 | 1-1-probing-the-trivial.md | done | Book I 第 I 章「Probing the Trivial / 探究琐事」；11 对 Original/Chinese 块；check_bilingual 退出码 0、可疑错配 0 处（无误报）；新增术语：Order of Knighthood 骑士勋章、Gibbon 吉本（Autobiography《自传》）、Rousseau 卢梭（Confessions《忏悔录》）、Madame de Warens 华伦夫人、Spencer 斯宾塞、Phoenicians 腓尼基人、Yucatan 尤卡坦、Heliopolis 赫利奥波利斯、Cedars of Lebanon 黎巴嫩雪松、sandomancer 沙占师、hashish 哈希什、Red Quarter 红区、chikbouk 长烟杆、Mahdi 马赫迪、dervish 德尔维希、Young Turks 青年土耳其党人、ganja 甘贾、Mena House 米娜宫、Sphinx 斯芬克斯、Pyramid 金字塔、helots 希洛人、Hajar 哈贾尔、Newcastle 纽卡斯尔、al-Farid 法里德、Jalal ad-Din Rumi 鲁米、Socrates 苏格拉底、St. Francis of Assisi 阿西西的圣方济各、salamander 火蜥蜴、Histoire Intime《私密史》、les dessous de cartes 底牌、Muse 缪斯 |
| 2026-08-06 | 1-4-on-the-wharf-of-enchantment.md | done | Book I 第 IV 章「On the Wharf of Enchantment / 在迷魅之埠」；9 对 Original/Chinese 块；check_bilingual 退出码 0、可疑错配 0 处（无误报）；新增术语：Ellis Island 埃利斯岛、Brooklyn Bridge 布鲁克林大桥、Statue of Liberty 自由女神像、Greater New York 大纽约、Beirut 贝鲁特、Syrian Quarter 叙利亚区、Dahomey 达荷美、Marseilles 马赛、Jahannam 火狱、Iblis 伊布力斯、Azrael 亚兹拉尔、scapular 圣衣、al-Mutanabbi 穆太奈比、Im-Hanna 伊姆-汉娜、Teague 蒂格、Greenbacks 绿背钞、Esau 以扫、Statue of Eros 厄洛斯神像、trachoma 沙眼、Bureau/Board of Emigration 移民局 |
| 2026-08-06 | 1-3-via-dolorosa.md | done | Book I 第 III 章「Via Dolorosa / 苦路」；5 对 Original/Chinese 块（14 段分 3+2+3+2+4）；check_bilingual 退出码 0、可疑错配 0 处（无误报）；新增术语：Via Dolorosa 苦路、Ottoman Empire 奥斯曼帝国、Ksarah 克萨拉、Jesuits 耶稣会士、bulbuls 夜莺、billah 凭真主起誓、bismillah 奉真主之名、Jannat 天园、Joseph 约瑟、Jonah 约拿、amir 埃米尔、Allahu akbar 真主至大、Diderot 狄德罗（Ellis Island/Beirut/Marseilles/Jahannam/al-Mutanabbi/trachoma 沿用 1-4 已建条目）|
| 2026-08-06 | 1-2-the-city-of-baal.md | done | Book I 第 II 章「The City of Baal / 巴力之城」（巴尔之城/巴勒贝克古城）；9 对 Original/Chinese 块；check_bilingual 退出码 0、可疑错配 0 处（无误报）；新增术语：Baal 巴力、Anti-Libanus 安提黎巴嫩山、Coele-Syria 科厄勒-叙利亚、Damascus 大马士革、Beirut 贝鲁特、Acropolis 卫城、Abdul Hamid 阿卜杜勒·哈米德、Berlin Museum 柏林博物馆、Temple of Jupiter 朱庇特神庙、Temple of Bacchus 巴克科斯神庙、Bacchantes 酒神狂女、Leontes 利昂特斯河、Homer 荷马、Temple of Zeus 宙斯神庙、Temple of Venus 维纳斯神庙、Mosque 清真寺、muezzin 宣礼员、minaret 宣礼塔、bulbuls 夜莺、Mohammad 穆罕默德、Laus Veneris《维纳斯颂》、Swinburne 斯温伯恩、narghile 水烟壶、Allah 真主、sakka 沙卡、Bazaar 巴扎、Ottoman Empire 奥斯曼帝国、wali 瓦利、pasha 帕夏、arak 阿拉克酒、dragoman 口译向导、Rasulain 拉苏莱恩、sumpter-mule 驮骡、stereopticon 立体投影灯、retroussage 擦笔柔化、bastinado 杖笞脚底、hornbook 角书、the Holy Virgin 圣母、Shakespeare 莎士比亚、Seth 塞特、Noah 挪亚、Solomon 所罗门、Queen of Sheba 示巴女王、Istachre 伊斯塔赫雷、Nimrod 宁录、phoenix 凤凰、Tower of Babel 巴别塔、Mt. Hermon 黑门山、Moabites 摩押人、St. Minius 圣米纽斯、St. Cyril 圣西里尔、St. Theodosius 圣狄奥多西、Ste. Odicksyia 圣奥迪克西娅、Magdalene 抹大拉、Ashtarout 阿施塔罗特、Jupiter-Ammon 朱庇特-阿蒙、al-Iman ul-Ouzaai 伊玛目·奥扎伊、al-Makrizi 马克里齐、Greek fire 希腊火、Kallinichus 卡利尼库斯、Kosta ibn Luka 科斯塔·伊本·卢卡、Muhaddetheen 穆哈迪辛、Najma 娜吉玛、Mecca 麦加、Dahomey 达荷美、Dahr’ul-Qadhib 达赫尔·卡迪卜、Mediterranean 地中海、Hesperian light 西方的光、City of Demiurgic Dollar 造化美元之城（Histoire Intime、Phoenicians、Syria、Cedars 沿用已建条目）|
| 2026-08-06 | 1-6-the-summer-afternoon-of-a-sham.md | done | Book I 第 VI 章「The Summer Afternoon of a Sham / 一个骗子的夏日午后」；10 对 Original/Chinese 块；check_bilingual 退出码 0、可疑错配 0 处（无误报）；罗马数字章号标题改作「## VI / VI」以过标题合并校验；新增术语：Jeremiah/secondhand Jerry 耶利米/二手杰瑞、Tom Paine 汤姆·潘恩（Age of Reason《理性时代》）、Matthew Arnold 马修·阿诺德、Dickens 狄更斯、Balzac 巴尔扎克、Carlyle 卡莱尔、Tennyson 丁尼生、Emerson 爱默生、Brentano’s 布伦塔诺书店、Bahira 贝希拉（修士）、Nebular Hypothesis 星云假说、Necropolis 亡灵之城、Serapeum 塞拉皮姆（塞拉皮斯神庙）、Sibawayh 西伯威、parasang 帕拉桑、helots 希洛人（沿用）、Jahannam 火狱（沿用）、Allah 真主（沿用）、al-Mutanabbi 穆太奈比（沿用）、Im-Hanna 伊姆-汉娜（沿用）、billah 凭真主起誓（沿用）、mujaddara 穆贾达拉（沿用）|
| 2026-08-06 | 1-7-in-the-twilight-of-an-idea.md | done | Book I 第 VII 章「In the Twilight of an Idea / 在一个念头的暮色中」；8 对 Original/Chinese 块（19 段分 2+2+2+2+2+2+3+4）；check_bilingual 退出码 0、可疑错配 0 处（无误报）；罗马数字章号标题改作「## VII / VII」以过标题合并校验；新增术语：Gorgon 戈耳工、Arabian Nights《一千零一夜》、Epictetus 爱比克泰德、Montaigne 蒙田、Mashallah 真主所欲、Mar-Kizhayiah 马尔-基扎亚、the Bronx 布朗克斯、Battery Park 巴特利公园（Voltaire 伏尔泰、bulbuls 夜莺、helots 希洛人、hashish 哈希什、Allah 真主、Azrael 亚兹拉尔、Iblis 伊布力斯、Im-Hanna 伊姆-汉娜、mujaddara 穆贾达拉、scapular 圣衣、Syrian Quarter 叙利亚区、Phoenicians 腓尼基人、arak 阿拉克酒 沿用已建条目）|
| 2026-08-06 | 1-5-the-cellar-of-the-soul.md | done | Book I 第 V 章「The Cellar of the Soul / 灵魂的地窖」；9 对 Original/Chinese 块；check_bilingual 退出码 0、可疑错配 0 处（无误报）；新增术语：Jeremiah 先知耶利米、Isaiah 以赛亚、Pascal 帕斯卡（Monsieur Pascal，《思想录》Thoughts）、St. Augustine 圣奥古斯丁、Tom Paine 汤姆·潘恩（Age of Reason《理性时代》）、Whitman 惠特曼、Niftawayh 尼夫塔威、Torquemada 托尔克马达、salaam 色兰、mulayiah《穆拉伊亚》、brummagems 廉价劣货、hebephrenia 青春型癫狂、Battery Park 巴特利公园（沿用）、Statue of Liberty 自由女神像（沿用）、narghile 水烟壶（沿用）、salamander 火蜥蜴（沿用）、bulbuls 夜莺（沿用）、Allah 真主（沿用）、Jahannam 火狱（沿用）、al-Mutanabbi 穆太奈比（沿用）、Im-Hanna 伊姆-汉娜（沿用）、mujaddara 穆贾达拉（沿用）、Sibawayh 西伯威（沿用）、Jesuits 耶稣会士（沿用）|
