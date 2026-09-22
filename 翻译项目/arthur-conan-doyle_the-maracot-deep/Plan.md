# 翻译计划（马拉科特深渊）

## 本计划信息

- **项目名称**：马拉科特深渊
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

按 `prompts/翻译计划模板.md`「执行步骤」9 步推进（读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志）。本项目中篇/连续模式，主 agent 自身逐篇执行。

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-08-13 | - | 建项目 | 从 待翻译/ epub 提取 7 章正文（chapter-1～7），建术语表初版，生成队列。判定：中篇/连续 |
| 2026-08-14 | chapter-1 | 退出码 0 | 37.8KB，38 对块，check_bilingual 通过（结构满足、0 可疑错配）。委派模式逐篇首译，本篇作黄金样本。术语备注：本篇人名译法（马若科/海德利/斯坎兰/马若科深渊）按委派任务指令执行，与术语表.md/项目说明.md 现存写法（马拉科特/黑德利/斯坎伦）不一致，待人工统一——见返回报告。 |
| 2026-08-14 | chapter-2 | 退出码 1 | 38.0KB，50 对块，check_bilingual 结构契约满足（标记成对、标题合并格式满足）。1 处可疑错配为数字锚点误报：原文 "32° Fahrenheit" 译为 "华氏三十二度"（中文数字），属正常意译。术语沿用黄金样本（马拉科特/黑德利/斯坎伦），新词：曼达（Manda）、琉璃钟罩（bells of vitrine）、荧光照明系统（fluor system）、沃尔斯特德（Volstead，禁酒法案）。 |
| 2026-08-14 | chapter-3 | 22.1KB / 退出码 0 | 30 对块，check_bilingual 通过（结构满足、0 可疑错配）。本篇三人坠入海底亚特兰蒂斯「庇护所」苏醒、思想投影屏、千人讲堂、误闯摩洛/巴力神庙、雅典娜神龛与希腊老祭司。术语沿用黄金样本（马拉科特/黑德利/斯坎伦/曼达/莫娜），新词已补入术语表：马拉克斯（Marax，深渊怪兽/魔王）、摩洛/巴力（Moloch/Baal，腓尼基古神）、雅典娜（Athena）、塞亚（Thea，希腊语「女神」）、梭伦（Solon）、赛斯（Sais）、硅石工坊（silica works）。注：原文含 Scanlan 两处旧时种族蔑称（comic Chinaman / cheese-faced Chink / coon songs），按黄金样本先例（chapter-1 已将 Chink 译作「病秧子」）做去蔑称归化处理（滑稽丑角/塌鼻扁脸的滑稽佬/黑人小调），保留 Scanlan 粗莽口吻不保留蔑称。 |
| 2026-08-14 | chapter-4 | 27.6KB / 退出码 0 | 25 对块，check_bilingual 通过（标记成对、标题合并格式满足、0 可疑错配）。本篇海床远足（出舱室、琉璃潜水罩/肩挂式呼吸器/荧光管）、探访旧潜水钟、猎比目鱼、深海煤矿与两族劳工、玄武岩断崖虎斑蟹惊魂、沉没之城卫城王宫（黑鱿鱼占寝宫）、坠落的抹香鲸、族中"电影"放映亚特兰蒂斯兴亡史（巴力祭司/方舟/法罗斯灯塔倾覆/卫城沉没）、木乃伊推算八千年。术语沿用黄金样本（马拉科特/黑德利/斯坎伦/曼达/庇护所/亚特兰蒂斯），新词首次附原文：深海平原（bathybian plain）、抱球虫软泥（globigerina ooze）、海百合珊瑚（crinoid coral）、虎斑蟹（tiger crab）、银鲛（Chimoera）、抹香鲸（sperm whale）、赫库兰尼姆（Herculaneum）/庞贝（Pompeii）、卢克索的卡纳克神庙（Temple of Karnak at Luxor）、尤卡坦（Yucatan）、柏拉图（Plato）、法罗斯灯塔（Pharus）、米切尔·赫奇斯（Mitchell Hedges）；"Manda, the chief"译"首领曼达"。 |
| 2026-08-14 | chapter-6 | 31.5KB / 退出码 1 | 39 对块，check_bilingual 结构契约满足（标记成对、标题合并格式满足）。1 处可疑错配为数字锚点误报：原文 "200 miles southwest of the Canaries" 译为 "加那利群岛西南二百英里处"（中文数字），属正常意译（同 chapter-2 先例）。本篇为衔接高潮的回忆篇：深海凶险奇观（普拉克萨 Praxa 绿雾生物/克里克斯乔克 Krixchok 电海虫/Hydrops ferox 食血小鱼/巨型比目鱼/海底龙卷风）、黑德利与莫娜定情并遭旋风濒死获救、曼达以思想投影屏揭示前世今生（黑德利前世为古希腊劫亲者被曼达前世以斧劈杀，亚特兰蒂斯末日避难所即今之庇护所）、伯布里克斯混血婴孩事件引爆与社群唯一冲突、祭司欲献祭婴孩（承上启下引出"暗面之主 the Lord of the Dark Face"）。术语沿用黄金样本（马拉科特/黑德利/斯坎伦/曼达/莫娜/伯布里克斯/庇护所），新词首次附原文：众暗面之主/暗面之主（the Lords/Lord of the Dark Face）、普拉克萨（Praxa）、克里克斯乔克（Krixchok）、片螺（lamellaria）、盘管虫（serpularia）、深海石斑鱼（deep-sea groper）、鲽鱼（dab）、囊鳃鳗（gastrostomus）、帆水母（Valella）/紫螺（Ianthina）/僧帽水母（Physalia）、思想影戏（thought cinemas）。去蔑称归化（沿用 chapter-1/3 先例）：nigger down South→最受欺负的有色人；bindlestiff→混账神棍；breed of that sort→混血的后代。 |
| 2026-08-14 | chapter-7 | 34.2KB / 退出码 0 | 35 对块，check_bilingual 通过（结构满足、0 可疑错配）。全书终章/高潮篇：黑德利与斯坎伦违逆曼达劝阻擅探黑大理石宫（黑魔法殿堂，美杜莎蛇发门楣、黄真菌帷幔、紫色海蛞蝓/黄色瓣鳃贝/黑比目鱼），唤醒远古邪灵巴力-西帕（Baal-seepa，暗面之君 the Lord of the Dark Face）——其自述为以太为生、超越死亡之永生者，历数其勾连人间诸恶（匈奴/撒拉森/圣巴托洛缪之夜/奴隶贸易/烧女巫/巴黎血流/俄国）；曼达读祸信后聚众于中央大厅，邪灵降临宣判灭族。高潮：马拉科特经书房祈祷得沃达（Warda，古亚特兰蒂斯智者灵体）显灵灌力，跃上台座以灵性层面之力斥退邪灵，邪灵化为黑腐肉溃灭；尾声唯物论者马拉科特自述灵界经历、唯灵论（白魔法克黑魔法/善强于恶/精神层面 plane of spirit）主题点题；斯坎伦升梅里班克厂长、黑德利得莫娜（深海明珠）。术语沿用黄金样本（马拉科特/黑德利/斯坎伦/曼达/巴力/庇护所/亚特兰蒂斯/灵体），新词首次附原文：巴力-西帕（Baal-seepa）/暗面之君（Lord of the Dark Face）、黑大理石宫（Palace of Black Marble）、美杜莎（Medusa）、所多玛与蛾摩拉（Sodom and Gomorrah）、圣巴托洛缪之夜（Bartholomew's night）、瓣鳃贝（lamellibranch）、神秘术（occult arts）、鱼类学（Ichthyology）、唯物论者（materialist，术语表已有）、六发左轮（six-shooter）。沃达（Warda）术语表已有，本篇首次正文登场。 |
| 2026-08-14 | chapter-5 (30.5KB 重试) | done | exit 0 | **全书 7/7 译完** |
