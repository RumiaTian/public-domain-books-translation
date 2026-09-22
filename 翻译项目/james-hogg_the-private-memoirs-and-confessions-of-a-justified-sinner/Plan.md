# Plan

> 本文件为《称义罪人的私人回忆录与忏悔》翻译计划。建项目阶段已生成 `translation_queue.csv` 与 `原文/*.md`；翻译推进时按 `prompts/翻译计划模板.md` 的 9 步执行。

## 本计划信息

- **项目名称**：称义罪人的私人回忆录与忏悔（James Hogg, *The Private Memoirs and Confessions of a Justified Sinner*）
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/小说文学.md
- **术语表**：术语表.md
- **内容形态 / 执行模式**：长篇 / 委派（子代理逐文件译）

## 篇目清单

| # | 篇名 | 源文 | 大小 | 状态 |
|---|------|------|------|------|
| 1 | 编者的叙述（开篇） | 01-editors-narrative.md | 165.5KB | todo |
| 2 | 罪人的回忆录 | 02-the-sinners-memoir.md | 260.3KB | todo |
| 3 | 编者的叙述（尾声） | 03-editors-conclusion.md | 26.7KB | todo |

（权威队列以 `translation_queue.csv` 为准，合计约 452.5KB。）

## 文件分工

| 文件 | 作用 | 谁来改 |
|------|------|--------|
| `项目说明.md` | 项目基本信息、领域配置、形态 | 人工 |
| `术语表.md` | 翻译硬约束层；每篇译完补充新词 | agent / 人工 |
| `translation_queue.csv` | 任务队列，三列 `file,size_kb,status` | doing→done |
| `Plan.md`（本文件） | 执行步骤 + 运行日志 | agent 追加日志 |
| `原文/*.md` | 源文 | 不改 |
| `译文/*.zh-CN.md` | 译文产出（块对照双语） | 翻译 agent 产出 |

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-08-14 | 03-editors-conclusion | exit 1（仅数字锚点误报：100/200/201 转中文数字，可接受） | 26.7KB；编者尾声+掘墓场景；23 对块对照；霍格「牧羊人」、老牧羊人 B——e、L——w 苏格兰方言口语化；残缺人名破折号照搬；术语补：wool-stapler 羊毛商、paulies 保利羊、Highland stotts 高地壮牛、spleuchan 烟草袋、frock coat 长尾礼服大衣、serge 哔叽、phrenologist 颅相学者、Robert Laidlaw 罗伯特·莱德劳、Mr. Watson 华生先生 |
| 2026-08-14 | 01-editors-narrative | exit 0 | 165.5KB 超长篇，分 8 段译；62 对块对照；编者第三人称平实现代汉语；贝尔·奥德、老巴尼特式仆人苏格兰方言对话口语化（哩/俺/这搭/嗐）；加尔文派术语统一（称义/预定论/蒙拣选者/被弃绝者/反律法主义）；残缺人名 L——t 保留破折号；诅咒诗篇全译；术语补：Arabella Logan/Mrs.Logan 阿拉贝拉·洛根/洛根夫人、Arabella/Bell Calvert 贝尔·卡尔弗特、Thomas Drummond 托马斯·德拉蒙德、Bessy Gillies 贝西·吉利斯、Adam Gordon 亚当·戈登、Lord Craigie/Sir Thomas Wallace 克雷基勋爵、Ridsley 里兹利、Bogle-heuch 博格尔-赫克、the Ringans 林甘们 |
| 2026-08-14 | 02-the-sinners-memoir | exit 1（仅数字锚点误报：1704/1712/27/24/30/18 等日期转中文数字，6 处均核对为正确对应，可接受） | 260.3KB 全书最长篇，分 12 段译；98 对块对照；罪人罗伯特·林金第一人称用稍古、神经质、引经据典语体（与编者平实汉语拉开反差）；吉尔-马丁=神秘变形同伴；苏格兰方言对话（老巴尼特、狱卒、塞缪尔·斯克雷普/彭彭特、塔姆·道格拉斯、织工多兹、拉琪·肖等）用北方乡土口语（哩/俺/这搭/嗐/哩）；加尔文派/反律法主义术语统一并首次附原文；残缺神名「主——啊——」破折号照搬；含奥赫特蒙蒂魔鬼讲道嵌入民间故事全译；术语补：Czar Peter 彼得沙皇、Mr. Blanchard 布朗查德、M'Gill 麦吉尔、Mr. Wilson 威尔逊、Mr. Millar 米勒、Andrew Handyside 安德鲁·汉迪赛德、Samuel Scrape/Penpunt 塞缪尔·斯克雷普/彭彭特、Mrs. Keeler 基勒夫人、Lawyer Linkum 林克姆律师、Linton 林顿、Elliot 埃利奥特（化名）、Cowan 考恩（化名）、Mr. James Watson 詹姆斯·沃森、Lucky Shaw 拉琪·肖、Robin Ruthven 罗宾·鲁思文、Auchtermuchty 奥赫特蒙蒂、Cameronian 卡梅隆派、Cloud of Witnesses《殉道者云证录》、Lord Justice Clerk 高等司法书记官、Queensberry 昆斯伯里公爵、Finnieston 芬尼斯顿、Paisley 佩斯利、Pearman Sike 皮尔曼溪、St. Anthony's well 圣安东尼井、North Loch 北湖、Hewie's Lane 休伊巷、Ellanshaws 埃伦肖斯、Ancrum 安克鲁姆、Dalkeith 达尔基斯、Portsburgh 波茨堡、West Port 西港、Ellan 埃伦、Tweed 特威德、Hawick 霍伊克、Roberton 罗伯顿、Redesdale 雷兹代尔、Ault-Righ 奥尔特-赖（王之溪）、Dorington Moor 多灵顿荒原、Boddel Brigg 博德尔桥、Jehu 耶户、Cyrus 居鲁士、Nebuchadnezzar 尼布甲尼撒、Ahab 亚哈、Melchizedek 麦基洗德、Daniel 但以理、Jonah 约拿、Ninevites 尼尼微人、Ezekiel 以西结、Gilgal 吉甲、Tophet 陀斐特、Antichrist 敌基督、West Lowmond 西洛蒙德、Sidlaw hills 锡德劳丘陵、Macbeth 麦克白、Cupar/Newburgh/Strathmiglo 库帕/纽堡/斯特拉斯米格洛、Perth 珀斯、Dundee 邓迪、Fife 法夫、Grampian hills 格兰扁丘陵、St. Johnston 圣约翰斯顿、Lowmonds 洛蒙德山 |
