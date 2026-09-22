# 翻译计划（爱之血脉）

## 本计划信息

- **项目名称**：爱之血脉（詹姆斯·布兰奇·卡贝尔）
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

## 执行步骤

按 `prompts/翻译计划模板.md`「执行步骤」9 步推进（读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志）。委派模式：主 agent 调度，子代理逐篇执行。

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-08-13 | - | 建项目 | 从 待翻译 epub 提取 10 篇正文、建术语表初版、生成队列；领域 小说文学；形态 短篇集；模式 委派 |
| 2026-08-15 | chapter-2-adhelmar-at-puysange.md | done（退出码 1，仅数字锚点误报，已核验） | 33.6KB；37 对块对照；奥克语/古法语/拉丁引诗照录附意译；新词：Sylvie=希尔薇、Mélite=梅莉特、Reinault=雷诺、Hugues d'Arques=于格·达尔克、Nointel=努安泰尔、d'Andreghen=安德雷根、White Turret=白塔楼 |
| 2026-08-15 | chapter-1-the-wedding-jest.md | done（退出码 1，仅日期数字锚点误报，已核验） | 31.2KB；30 对块对照；1293 年普瓦泰斯姆开篇；奥克语卷首引诗照录附意译；新词补入术语表：Ralph de Nointel=拉尔夫·德·努安泰勒、Perion=林间的佩里翁、Demetrios=德米特里奥斯、Lilith=莉莉丝、Raimbaut de Vaqueiras=兰博·德·瓦凯拉斯、Miramon Lluagor=米拉蒙·柳阿戈尔、Marchfeld=马希费尔德；Sylvie 从并行第2篇译法统一为希尔薇 |
| 2026-08-15 | chapter-3-love-letters-of-falstaff.md | done（退出码 1，仅年份数字锚点误报，已核验） | 28.8KB；124 对块对照；莎剧引文及福斯塔夫对白循朱生豪腔调；两首诗体情书照录并译为分行诗；术语补入：Sylvia=西尔维娅、Bardolph=巴道夫、Mistress Quickly=快嘴桂嫂、Doll Tearsheet=桃儿·贴席、Poins=波因斯、Hotspur/潘西、sack=白葡萄酒、Yaxham=亚克斯姆、Winstead=温斯特德、Eastcheap=东市、Boar's Head=野猪头酒店等 |
| 2026-08-15 | chapter-4-sweet-adelais.md | 33.1KB / 退出码1（仅数字锚点误报，核验通过） | 第4篇「甜蜜的阿德莱丝」译毕；新增人物术语已补入术语表 |
| 2026-08-15 | chapter-6-the-conspiracy-of-arnaye.md | 36.6KB / 退出码1（仅数字锚点误报，人工核验通过） | 政略联姻反转型短篇；新增人名地名见术语表补充 |
| 2026-08-15 | chapter-5-in-necessitys-mortar.md | 41.1KB / 退出码1（仅年份数字锚点误报，核验通过） | 第5篇「必要之臼」（维永题材）译毕；54 对块对照；古法语卷首引诗及谣曲体情歌照录附意译；Catherine de Vaucelles 依并行第6篇术语统一为卡特琳·德·沃塞勒；新词补入术语表：François de Montcorbier=弗朗索瓦·德·蒙科尔比耶、François Villon=弗朗索瓦·维永、Sermaise=塞尔莫瓦斯、Ysabeau/René de Montigny=伊莎博/勒内·德·蒙蒂尼、Guillaume de Villon=纪尧姆·德·维永、Rue Saint Jacques=圣雅克街、Montfaucon=蒙福孔、Châtelet=夏特莱法院、Crowned Ox=加冕牛酒店、Companions of the Cockleshell=贝壳帮、Battle of the Herrings=鲱鱼之战等 |
| 2026-08-15 | chapter-7-the-castle-of-content.md | 38.5KB / 退出码1（仅日期数字锚点误报：1519、1485，译文中均在，核验通过） | 第7篇「所谓知足城堡」译毕；21 对块对照；中古英语卷首题词及「知足城堡」三首谣曲照录附意译；威尔·萨默斯自述体（弄臣第一人称冷嘲）；新词补入术语表：Lady Adeliza=阿德莉扎小姐、Stephen Allonby=斯蒂芬·阿隆比、Tom Allonby=汤姆·阿隆比、Elinor Sommers=埃莉诺·萨默斯、Anne de Beaujeu=安妮·德·博热、Blaise=布莱兹、Beatris=贝亚特丽丝、Tiverton=蒂弗顿、Devon=德文郡、Havre=勒阿弗尔、Bosworth=博斯沃思、Teignmouth=廷茅斯、Exe=埃克斯河、Castle of Content=知足城堡等 |
| 2026-08-15 | chapter-8-in-ursulas-garden.md | 31.5KB / 退出码1（仅卷首日期数字锚点误报，核验通过） | 第8篇「厄休拉的花园」译毕；33 对块对照；边区古谣卷首引诗及剧中歌谣照录附意译；第3篇旧线收束（威尔·萨默斯与法尔茅斯侯爵夫人）；新词补入术语表：Lady Ursula Heleigh=厄休拉·希利、Richard Mervale=理查德·默维尔、Katherine Beaufort=凯瑟琳·博福特、Stephen Allonby=斯蒂芬·阿隆比、Pevensey（伯爵）=佩文西、Longaville Court=朗加维尔府、Lucius Rossmore=卢修斯·罗斯莫尔、Rochford=罗奇福德、Norreys=诺里斯、Wyatt's Rebellion=怀亚特叛乱
| 2026-08-15 | chapter-9-porcelain-cups.md | 36.1KB / 退出码0（结构契约与语义锚点全部通过） | 第9篇「所谓瓷杯」译毕；37 对块对照；1593 年德特福德，辛西娅·阿隆比三求婚者；马洛《热情的牧人致情人诗》两节引诗分行照录并译；Marlowe/Marler 双关照译（马洛/马勒）；新词补入术语表：George Bulmer=乔治·布尔默、Kit Marlowe=基特·马洛、Ned=内德、Gloriana=格罗丽亚娜、celadon=青瓷、Hero and Leander=《赫洛与利安德》、Tamburlaine=帖木儿、the Golden Hind=金鹿酒店、Deptford=德特福德、Arcadia=阿卡狄亚、carpet earl=地毯伯爵等 |
| 2026-08-15 | chapter-10-semper-idem.md | 6.6KB / 退出码0（结构契约与语义锚点全部通过） | 第10篇「所谓终曲 Semper Idem（始终如一）」译毕，全书收官；7 对块对照；1905–1919 近代收束；《威尼斯商人》卷首引诗照录附意译；法语收场白与 Explicit linea amoris 照搬附注；新词补入术语表：The Musgraves of Matocton=《马托克顿的马斯格雷夫家族》、Roi Atnaury=《阿特瑙里王》、Dizain des Reines=《王后十篇》、Roman de Lusignan=《吕西尼昂传奇》、Schahriah=山鲁亚尔、dark lady=「黑夫人」 |
