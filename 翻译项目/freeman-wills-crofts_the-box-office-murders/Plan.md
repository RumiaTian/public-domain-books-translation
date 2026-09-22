# 翻译计划（Plan.md）

---

## 本计划信息

- **项目名称**：freeman-wills-crofts_the-box-office-murders（《售票处谋杀案》The Box Office Murders）
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/小说文学.md
- **术语表**：术语表.md
- **内容形态 / 执行模式**：长篇 / 委派（子代理逐篇执行下述 9 步）

---

## 文件分工

| 文件 | 作用 | 谁来改 |
|------|------|--------|
| `项目说明.md` | 项目基本信息、领域配置、篇目清单 | 人工 |
| `术语表.md` | 翻译硬约束层。每篇译完补充新词 | agent / 人工 |
| `translation_queue.csv` | 任务队列。每行一文件，`file, size_kb, status` 三列 | 翻译前改 doing，完成后改 done |
| `Plan.md`（本文件） | 执行步骤 + 运行日志 | agent 追加日志 |
| `原文/*.md` | 源文 | 不改 |
| `译文/*.zh-CN.md` | 译文产出（块对照双语） | 翻译 agent 产出 |

---

## translation_queue.csv 格式

```
file,size_kb,status
01-the-purple-sickle.md,31.2,todo
02-french-makes-an-assignation.md,22.3,todo
...
```

| 字段 | 含义 | 取值 |
|------|------|------|
| `file` | 源文文件名（在 `原文/` 目录下） | 如 `01-the-purple-sickle.md` |
| `size_kb` | 源文大小（KB）。>50KB 为长文，按通用翻译引擎第七节分段 | 数字 |
| `status` | 翻译状态 | `todo` 待译 / `doing` 翻译中 / `done` 已完成 |

---

## 执行步骤（agent 按此推进，两种模式共用）

> 本项目为**委派模式**：主 agent 只当调度员，每篇的 9 步下沉到一次性子代理执行（简报见 `WORKFLOW.md`「子代理简报」）。

### 1. 读配置（每次翻译前必读）
```
1. 本项目 Plan.md（本文件）
2. 项目说明.md
3. 术语表.md
4. prompts/通用翻译引擎.md
5. prompts/领域配置/小说文学.md
6. 译文/ 下任意一篇已完成的 .zh-CN.md（作为风格黄金样本，照此风格译；无则跳过）
```

### 2. 取任务
读 `translation_queue.csv`，取第一个 `status=todo` 的行。先 `ls 译文/` 检查该篇译文是否已存在：
- 已存在 → 直接改 `done`，跳到步骤 8。
- 不存在 → 把该行 `status` 改为 `doing` 并保存 CSV，继续。

### 3. 读源文
读 `原文/对应文件名`。

### 4. 翻译
产出到 `译文/对应文件名去.md加.zh-CN.md`。

**双语对照格式、标记规则、完整性禁令**：见 `prompts/通用翻译引擎.md` 第五、六节（标记成对、标题合并「英文 / 中文」、不跳过不缩写、UTF-8 无 BOM）。此处不重复。

**本流程专有提醒**：
- 逐块对照原文，绝不漏译、不合并段落、不缩写、不总结，尤其结尾别截断。
- 严守术语表：遇表内源词必译为指定译法。新词自行确定统一译法，首次附原文「中文（English）」。
- 人物/语气/风格全文一致（文学类尤其重要），照黄金样本风格译。
- 长文（源文 >50KB）分段处理见通用翻译引擎第七节。

### 5. 自检
- 完整性：源文每一段都在译文 Original 块中出现，末尾无截断。
- 块对称：Original/Chinese 数量相等，每块内段数对应。
- 标题格式：全部「英文 / 中文」合并。
- 术语一致：抽查 5 个术语词，全文译法统一。
- 不满足则改到满足。

### 6. 自动检查
```
python scripts/check_bilingual.py 译文/对应篇名.zh-CN.md
```
结构契约满足（标记成对、标题合并格式、可疑错配少）则继续；有违规回步骤 4 修订。

### 7. 回填状态（双写）
检查通过后，`status` 从 `doing` 改 `done`，改两处：
- ① 项目 `translation_queue.csv` 该行；
- ② 根 `translation_queue.csv` 中 `<本项目名>,<本篇名>` 那一行（`WORKFLOW.md`「双写状态」）。

### 8. 追加日志
在本文件「运行日志」追加一行。

### 9. 循环
回到步骤 2，取下一篇 `todo`，直到全部 `done`。委派模式下由主 agent 决定是否继续派单（见 `WORKFLOW.md`「委派模式调度循环」，并发上限 3）。

---

## 篇目清单

| # | 篇名 | 源文 | 状态 |
|---|------|------|------|
| 1 | 一 紫色镰刀 | 01-the-purple-sickle.md | todo |
| 2 | 二 弗伦奇定下约会 | 02-french-makes-an-assignation.md | todo |
| 3 | 三 验尸讯问 | 03-the-inquest.md | todo |
| 4 | 四 弗伦奇开局 | 04-french-makes-a-start.md | todo |
| 5 | 五 李-昂-索伦特 | 05-lee-on-the-solent.md | todo |
| 6 | 六 最高上诉法院 | 06-the-supreme-appeal-court.md | todo |
| 7 | 七 公道的乘客们 | 07-fair-passengers.md | todo |
| 8 | 八 灰色汽车的路线 | 08-the-grey-car-s-round.md | todo |
| 9 | 九 弗伦奇再定约会 | 09-french-makes-a-second-assignation.md | todo |
| 10 | 十 窃贼弗伦奇先生 | 10-mr-cracksman-french.md | todo |
| 11 | 十一 满足的父亲 | 11-the-happy-paterfamilias.md | todo |
| 12 | 十二 汽车的货物 | 12-the-car-s-freight.md | todo |
| 13 | 十三 补给的运输 | 13-the-transport-of-supplies.md | todo |
| 14 | 十四 毗邻的产业 | 14-the-property-adjoining.md | todo |
| 15 | 十五 卡利莫尔先生详加阐释 | 15-mr-cullimore-expounds.md | todo |
| 16 | 十六 落网 | 16-in-the-net.md | todo |
| 17 | 十七 阴影渐逼 | 17-the-shadows-loom-nearer.md | todo |
| 18 | 十八 棋逢对手 | 18-when-greek-meets-greek.md | todo |
| 19 | 十九 结局 | 19-conclusion.md | todo |
| 20 | 尾注 | 20-endnotes.md | todo |
| 21 | 插图说明 | 21-list-of-illustrations.md | todo |

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-09-10 | 二 弗伦奇定下约会 | done | 114 段、30 组块对照；check_bilingual 与 check_coverage 均 0 违规；新定名待回填术语表：彼得斯太太（Mrs. Peters）、希尔斯医生（Dr. Hills）、亨特警司（Superintendent Hunt）、斯基普顿（Skipton）、克拉彭（Clapham）、奥兰多街（Orlando Street）、曼彻斯特（Manchester）、伯明翰（Birmingham）、斯塔弗尔（Starvel）、达特穆尔（Dartmoor）、档案记录部（Record Department）、《战斗的忒弥莱尔号》（*Fighting Temeraire*） |
| 2026-09-10 | 01-the-purple-sickle.md（一 紫色镰刀） | done | 双语对照 35 对块；check_bilingual 与 check_coverage 均 exit 0（0 可疑错配、0 漏译）；新定名待回填术语表：刑事调查部（Criminal Investigation Department）、彼得斯太太（Mrs. Peters）、克拉彭（Clapham）、奥兰多街（Orlando Street）、伯肯黑德（Birkenhead）、《中部乡区公报》（Mid-Country Gazette）、J. S. 乔丹医生（Dr. J. S. Jordan）、皇冠旅店（Crown Inn）、雷德希尔（Redhill）、托马斯·宾克斯（Thomas Binks）、亚当·穆迪医生（Dr. Adam Moody）、约翰·韦尔斯（John Wells）、贝克卢线（Bakerloo）、大象城堡（the Elephant）、牛津圆环（Oxford Circus）、福勒餐馆（Fuller’s）、莱昂斯街角屋（Lyons’ Corner House）、圣潘克拉斯（St. Pancras）、卢顿（Luton）、财团（syndicate）、寄宿公寓（boarding house） |
| 2026-09-10 | 04-french-makes-a-start.md（四 弗伦奇开局） | done | 双语对照 21 对块（75 段）；check_bilingual 结构 0 违规、仅 1 处数字锚点误报（3:00/5:00 a.m. 改写为「3 点至 5 点」，块内已人工核对无错配）；check_coverage exit 0（0 漏译）；新定名待回填术语表：南海城（Southsea）、斯普兰迪德旅馆（the Splendid）、伊斯特本（Eastbourne）、奇切斯特（Chichester）、阿伦河（the Arun）、沃金厄姆（Wokingham）、奥尔德肖特（Aldershot）、戈德尔明（Godalming）、霍舍姆（Horsham）、阿什当森林（Ashdown Forest）、索伦特海峡（the Solent）、内政部（Home Office）、滑铁卢（Waterloo）、警察局长（chief constable）、歇洛克·福尔摩斯（Sherlock Holmes） |
| 2026-09-10 | 三 验尸讯问 | done | 83 段、17 组块对照；check_bilingual 与 check_coverage 均 exit 0（0 可疑错配、0 漏译）；沿用术语表及第 1、2 章既定译名（弗伦奇、瑟扎·达克、希尔斯医生、戈利特利警士、彼得斯太太、米兰电影院、提斯比号、刑事调查部等）；新定名待回填术语表：刘易斯·珀肖（Lewis Pershaw）、卡斯韦尔医生（Dr. Carswell）、验尸官（coroner） |
| 2026-09-10 | 05-lee-on-the-solent.md（五 李-昂-索伦特） | done | 104 段、27 对块对照；check_bilingual 与 check_coverage 均 exit 0（0 可疑错配、0 漏译）；沿用术语表及既定译名（弗伦奇、奥斯汀·芒恩、达克小姐、拉平医生、斯泰尔、韦斯汀豪斯、格温·莱斯特兰奇、苏格兰场、斯托克斯湾、山岬、伯里湾口、南安普敦湾、索伦特海峡、李-昂-索伦特、协查通报等）；新定名待回填术语表：尼斯（Nice）、派克表兄弟（the Pyke cousins）、戈斯波特（Gosport）、吉尔基克角（Gilkicker Point）、南安普敦（Southampton）、汤姆·曼纳斯（Tom Manners）、伯里港（Burry Port）、拉内利（Llanelly）、考斯（Cowes）、奥斯本树林（Osborne Woods）、法勒（Farrar）、芬德利（Findlay）、戴姆勒（Daimler）、汉普郡（Hampshire）、萨里郡（Surrey）、双套结（clove hitch）、绳梯锁结（ratline lock）、滑道（slip）、系艇索（painter）、循环绳（endless rope）、无线电台（wireless station）、轿车型（saloon） |
| 2026-09-10 | 06-the-supreme-appeal-court.md（六 最高上诉法院） | done | 79 段、21 对块对照（每块 3-5 段）；check_bilingual 与 check_coverage 均 exit 0（0 可疑错配、0 漏译、无数字锚点误报）；沿用术语表及既定译名（弗伦奇、弗伦奇太太、肥皂乔、米切尔探长、拉平医生、阿罗史密斯先生、瑟扎·达克、艾琳·塔克、阿加莎·弗林顿、苏格兰场、朴茨茅斯、阿伦德尔、卡特汉姆、莱斯特广场、干草市场、斯特兰德大街、世界电影院、万花筒电影院、威尼斯电影院、星号电影院、售票姑娘、寄宿公寓）；新定名待回填术语表：蒂奇菲尔德（Titchfield）、法勒姆（Fareham）、比晓普斯沃尔瑟姆（Bishop's Waltham）、帕拉迪姆剧院（the Palladium）、哈顿花园（Hatton Garden）、盖辛（Gething）、X 太太（Mrs. X）、埃米莉（Emily）、埃姆（Em）、采石坑（quarry hole）、通令（circular） |
| 2026-09-10 | 07-fair-passengers.md（七 秀丽的乘客） | done | 76 段、22 对块对照（每块 3-4 段）；check_bilingual 与 check_coverage 均 exit 0（0 可疑错配、0 漏译、无数字锚点误报）；沿用术语表及既定译名（弗伦奇、卡特警士、哈维警士、莉莲·伯吉斯、莫莉·莫兰、埃丝特·艾萨克斯、瑟扎·达克、韦斯汀豪斯、柯蒂斯·韦兰、苏格兰场、干草市场、莱斯特广场、斯特兰德大街、查令十字、纳尔逊街、约克路、滑铁卢路、韦伯街、塔奇布鲁克街、沃克斯豪尔桥路、贝斯沃特路、牛津街、皮卡迪利、格罗夫纳广场、贝克卢线、大象城堡、售票姑娘、寄宿公寓）；新定名待回填术语表：莫宁顿月牙街（Mornington Crescent；术语表并存「晨顿月牙街」，本篇取前者）、科克斯珀街（Cockspur Street）、克雷文街（Craven Street）、威斯敏斯特桥路（Westminster Bridge Road）、大乔治街（Great George Street）、圣詹姆斯公园（St. James's Park）、格林公园（Green Park）、海德公园（Hyde Park）、蛇形湖（the Serpentine）、海德公园角（Hyde Park Corner）、林荫路（the Mall）、皮卡迪利广场（Piccadilly Circus）、阿灵顿路（Arlington Road）、新肯特路（New Kent Road）、西奥博尔德街（Theobald Street）、钱多斯街（Chandos Street）、贝德福德街（Bedford Street）、加里克街（Garrick Street）、克兰伯恩街（Cranbourne Street）、查令十字路（Charing Cross Road）、环线（Circle）、圣殿（the Temple）、诺福克街（Norfolk Street）、奥尔德威奇（Aldwych）、金斯威路（Kingsway）、怀尔德街（Wild Street）、德鲁里巷（Drury Lane）、布罗德街（Broad Street）、北奥德利街（North Audley Street）、南奥德利街（South Audley Street）、南街（South Street）、韦弗顿街（Waverton Street）、查尔斯街（Charles Street）、伯克利街（Berkeley Street）、格罗夫纳道（Grosvenor Place）、格罗夫纳路（Grosvenor Road）、贝斯伯勒街（Bessborough Street）、佩奇街（Page Street）、达尔文街（Darwin Street）、老肯特路（Old Kent Road）、伯蒙德赛（Bermondsey）、朗巷（Long Lane）、纽因顿堤道（Newington Causeway）、泰特巷（Tate's Lane）、托马斯·卡兰（Thos. Cullan）、老维克剧院（the Old Vic）、波因特先生（Mr. Pointer）、恩特威斯尔太太（Mrs. Entwhistle）、汉普斯特德—高门线（Hampstead and Highgate）、佣金经纪人（commission agent） |
| 2026-09-10 | 09-french-makes-a-second-assignation.md（九 弗伦奇再定约会） | done | 双语对照 22 对块（44 块）；check_bilingual 与 check_coverage 均 exit 0（0 可疑错配、0 漏译）；沿用术语表及既定译名（弗伦奇、莫莉·莫兰、瑟扎·达克、柯蒂斯·韦兰、韦斯汀豪斯、苏格兰场、纳尔逊街、查令十字、老康普顿街、希腊街、查令十字路、万花筒电影院、蒙特卡洛、卡特警士、售票处、寄宿公寓）；新定名待回填术语表：维利尔斯街（Villiers Street）、格林街（Green Street）、杰勒德局（Gerrard，电话局名）、维多利亚局（Victoria，电话局名）、老贝利（the Old Bailey）、刑事共谋（criminal conspiracy）、赌注登记人（bookmaker）、唇读（lipread）、潜望镜（periscope）、爱尔兰土腔（brogue）、严父的架势（heavy father） |
| 10-mr-cracksman-french.md | done | 单次直译完成；check_bilingual 21 对块全过、coverage 0 漏译；新定名：查布锁（Chubb lock）、默丘里（Mercury，15/20 型轿车）、桑代克医生（Dr. Thorndyke）、西姆金斯（Simkins，弗伦奇化名）、约克街（York Street） |
| 2026-09-10 | 11-the-happy-paterfamilias.md（十一 幸福的家长） | done | 单次直译完成；双语对照 18 对块（36 块，每块 3-5 段）；check_bilingual 与 check_coverage 均 exit 0（0 可疑错配、0 漏译、无数字锚点误报）；沿用术语表及既定译名（弗伦奇、奥姆斯比警士、卡特警士、哈维警士、肥皂乔、柯蒂斯·韦兰、莫莉·莫兰、苏格兰场、阿卡西亚街、万花筒电影院、售票处、售票姑娘、验尸讯问）；新定名待回填术语表：哈罗（Harrow，站名）、弗雷迪·奥姆斯比（Freddie Ormsby，奥姆斯比之子）、塞西尔（Cecil，弗伦奇为男孩临时起的化名）、汤姆·米克斯（Tom Mix，片中被模仿的影星）、《好莱坞的胡克小姐》（Miss Hook of Hollywood，儿童剧）、克里平医生（Dr. Crippen，历史案件人名）、鞍囊式扶手椅（saddlebag armchair）、带锁酒瓶架（tantalus）、卷盖式书桌（roll-top desk）、白雪（snow，毒品黑话）、入场金属牌（metal disc of entrance）、帆布围棚（canvas structure） |
| 2026-09-10 | 08-the-grey-car-s-round.md（八 灰色轿车的巡回） | done | 45 段、17 对块对照（每块 2-6 段）；check_bilingual 与 check_coverage 均 exit 0（0 可疑错配、0 漏译、无数字锚点误报）；沿用术语表及既定译名（弗伦奇、莫莉·莫兰、柯蒂斯·韦兰、卡特警士、哈维警士、皮克福德警士、苏格兰场、朴茨茅斯、韦伯街、约克路、泰特巷、塔奇布鲁克街、沃克斯豪尔桥路、格罗夫纳广场、贝克卢线、老肯特路、灰色轿车、佣金经纪人、售票处、寄宿公寓）；新定名待回填术语表：哈罗（Harrow）、科尔盖特（Colgate）、雅克（Jacques，糖果商）、滑铁卢桥（Waterloo Bridge）、威廉王街（King William Street）、奥兰治街（Orange Street）、约克街（York Street）、惠特科姆街（Whitcomb Street）、沃尔多街（Wardour Street）、伯克利广场（Berkeley Square）、格拉夫顿街（Grafton Street）、罗切斯特街（Rochester Row）、摄政街（Regency Street）、上格兰奇路（Upper Grange Road）、砖匠臂车站（Bricklayers’ Arms station）、埃奇韦尔路（Edgware Road）、皇家电影院（the Royal Cinema）、托泽（Harold Tozer，工程师兼建筑师）、费尔柴尔德（Fairchild，虚构寻访对象） |
| 2026-09-10 | 13-the-transport-of-supplies.md（十三 补给品的运送） | done | 单次直译完成；双语对照 23 对块（46 块，每块 2-6 段）；check_bilingual 与 check_coverage 均 exit 0（0 可疑错配、0 漏译、无数字锚点误报）；沿用术语表及既定译名（弗伦奇探长、奥姆斯比警士、莫莉·莫兰、柯蒂斯·韦兰、斯泰尔、格温·莱斯特兰奇、苏格兰场、皇家造币厂、万花筒电影院、化妆包、入场金属牌、售票处、验尸讯问口径、白雪、阿卡西亚街、约克路、泰特巷、汽车房、暗板、检修井、集水坑、隔断存水弯、清淤口、通气管、三通、赌注登记人）；新定名待回填术语表：半克朗（half crown，银币面额）、伦敦郡银行（London and County Bank）、骑士桥分行（Knightsbridge Branch）、埃尔伍德（Elwood，该行经理）、惠特利（Whitley，该行职员）、排出管（outfall）、弯头（bend，管件）、通函（circular，致各银行的查询函） |
| 2026-09-10 | 12-the-car-s-freight.md（十二 汽车里的货物） | done | 94 段、20 对块对照（每块 3-5 段）；check_bilingual 与 check_coverage 均 exit 0（0 可疑错配、0 漏译、无数字锚点误报）；沿用术语表及既定译名（弗伦奇、莫莉·莫兰、瑟扎·达克、格温·莱斯特兰奇、柯蒂斯·韦兰、赫维·韦斯汀豪斯、斯泰尔、苏格兰场、查令十字花园、纳尔逊街、牛津街、米兰电影院、万花筒电影院、蒙特卡洛、朴茨茅斯、皇家造币厂、化妆包、售票处、刑事共谋、赌注登记人、爱尔兰土腔、暗板夹袋）；新定名待回填术语表：售票窗（pay-box）、售票钱箱（till，九/十章已用但表缺）、借据（I.O.U.）、王室证人（King’s evidence）、皇家造币厂剔除戳记（Mint rejection mark）、佣金（percentage）、半克朗（half crown，与第十三章日志所报一致） |
| 2026-09-10 | 14-the-property-adjoining.md（十四 毗邻的产业） | done | 单次直译完成；双语对照 32 对块（64 块，每块 2-4 段）；check_bilingual 与 check_coverage 均 exit 0（0 可疑错配、0 漏译、无数字锚点误报）；沿用术语表及既定译名（弗伦奇、奥姆斯比警士、卡特警士、哈维警士、皮克福德警士、米切尔探长、柯蒂斯·韦兰、斯泰尔、格温·莱斯特兰奇、莫莉·莫兰、瑟扎·达克、克鲁斯太太、苏格兰场、皇家造币厂、万花筒电影院、西奥博尔德-格鲁金公司、银器作坊、化妆包、半克朗、查布锁、泰特巷、纳尔逊街、莱斯特广场、朴茨茅斯、车身行、集水坑、检查井盖、通气管）；新定名待回填术语表：金雀花街（Killowen Street，泰特巷平行街，术语表已列但音译待统一核对）、克鲁斯太太（Mrs. Creuse，莫兰包饭公寓老板娘）、蛇杆（serpent，下水道疏通通条）、鲍登钢丝（bowden wire）、阿姆斯特朗-西德利（Armstrong Siddeley，斯泰尔的墨绿轿车）、人梯（back，翻墙搭手）、银瓦刀（silver trowel，奠基礼器）、传话管（speaking tube）、银锭（ingots）、邮政汇票（postal order） |
| 2026-09-10 | 15-mr-cullimore-expounds.md（十五 卡利莫尔先生高谈阔论） | done | 单次直译完成；双语对照 20 对块（40 块，每块 3-6 段），110 个原文段落逐一核入 Original 块（0 漏译、块内段数全对称）；check_bilingual 与 check_coverage 均 exit 0（0 可疑错配、无数字锚点误报）；沿用术语表及既定译名（弗伦奇、莫莉·莫兰、莫兰小姐、柯蒂斯·韦兰、斯泰尔、格温·莱斯特兰奇口径未出场未用、莫蒂默·埃利森爵士、助理总监、坦纳探长、卡特警士、哈维警士、米切尔探长、苏格兰场、皇家造币厂、万花筒电影院、纳尔逊街、化妆包、售票姑娘、半克朗、伪币、淘汰币口径、白雪未出场、验尸讯问未涉及）；新定名待回填术语表：达夫先生（Mr. Dove，造币厂官员，表内已有）、克罗伊登（Croydon，米切尔被耽搁地）、吉姆·西布利（Jim Sibley，造币厂前工程师，表内已有）、土耳其纸烟（Turkish cigarettes）、银币炸弹（silver bombshell，莫蒂默戏语） |
| 2026-09-10 | 17-the-shadows-loom-nearer.md（十七 阴影渐逼） | done | 单次直译完成；双语对照 21 对块（42 块，每块 2-4 段）；check_bilingual 过检（仅 1 处数字锚点误报：Victoria 7000 电话号码照搬原文）、check_coverage exit 0（0 漏译）；沿用术语表及既定译名（莫莉·莫兰、瑟扎·达克、弗伦奇、斯泰尔、格温·莱斯特兰奇、苏格兰场、万花筒电影院、售票处、莫宁顿月牙街口径未涉及）；新定名待回填术语表：克里斯蒂娜·怀亚特（Christina Wyatt，旧手稿簿原主）、维多利亚7000（Victoria 7000，苏格兰场电话局交换台号码）、纸镖（dart，折页纸飞机式求救信）、带轮矮床（truckle bed）、炉石（hearthstone）；书目：《点灯人》《奎奇》《费尔柴尔德一家》《红字》《天路历程》照原名意译/通行译名 |
| 2026-09-10 | 19-conclusion.md（十九 结局） | done | 单次直译完成；双语对照 11 对块（22 块，每块 2-3 段）；check_bilingual exit 0（0 可疑错配、无数字锚点误报）、check_coverage exit 0（0 漏译）；沿用术语表及既定译名（弗伦奇、吉姆·西布利、格温·莱斯特兰奇、柯蒂斯·韦兰、赫维·韦斯汀豪斯、韦伯斯特/斯泰尔、瑟扎·达克、莫莉·莫兰、苏格兰场、皇家造币厂、银器作坊、西奥博尔德-格鲁金公司、吉尔福德、赖德、南安普敦湾、山岬、李-昂-索伦特、拉平医生、米兰电影院、采石坑、浴缸新娘杀手、查令十字花园、灰色轿车、通令、售票姑娘）；新定名待回填术语表：「西布利、西布利与韦兰」商号（the firm of Sibley, Sibley & Welland，戏拟合伙商号名）、拘留室（the cells，警局关押间） |
| 2026-09-10 | 20-endnotes.md（尾注） | done | 单次直译完成；双语对照 1 对块（2 条尾注）；check_bilingual 与 check_coverage 均 exit 0（0 可疑错配、0 漏译）；沿用术语表既定书名《斯塔弗尔谷惨案》（The Starvel Hollow Tragedy）与《海上疑云》（The Sea Mystery），弗伦奇探长口径一致；无新定名 |
| 2026-09-10 | 21-list-of-illustrations.md（插图清单） | done | 单次直译完成；双语对照 1 对块（2 条图注）；check_bilingual 与 check_coverage 均 exit 0（0 可疑错配、0 漏译）；沿用既定术语：汽油箱剖面、检修井、通气管（第十二章/十三章口径）、汽车房；新定名待回填术语表：暗袋（pocket，油箱前端三角形空当内的藏币容器） |
| 2026-09-10 | 16-in-the-net.md（十六 落入网中） | done | 单次直译完成；双语对照 24 对块（48 块，每块 2-3 段），71 个原文段落逐行核入 Original 块（0 漏译、无数字锚点误报）；check_bilingual 与 check_coverage 均 exit 0（0 可疑错配、0 漏译）；沿用术语表及既定译名（弗伦奇、莫莉·莫兰、瑟扎·达克、艾琳·塔克、阿加莎·弗林顿、韦斯汀豪斯、斯泰尔、格温·莱斯特兰奇、苏格兰场、探长职级、万花筒电影院、售票处、化妆包、半克朗、查令十字花园、蒙特卡洛、泰特巷、约克路、滑铁卢、哈罗、金雀花街、银器作坊、格林公园、威斯敏斯特桥、传话管、卷盖书桌、寄宿公寓、采石坑、浴缸新娘口径）；新定名待回填术语表：詹金斯（Jenkins，作坊伙计，十四/十六章已用）、哈格雷夫斯先生（Mr. Hargreaves，奖盾客户）、奥特韦（Otway，购盾商号）、史密斯（Smith，浴缸新娘案凶手，表内已有词条）、后部车厢（tonneau，轿车后舱）、金属圆片票（disc tickets，与第七章口径一致）、奖盾（presentation shield）、题字（inscription）、过道（entry，与十四章口径一致）、职员（clerk，银器作坊伙计） |
| 2026-09-10 | 18-when-greek-meets-greek.md（十八 棋逢对手） | done | 单次直译完成；双语对照 21 对块（42 块，每块 3-6 段），102 个原文段落逐一核入 Original 块（逐段 verbatim 核对 0 错配、0 漏译）；check_bilingual 与 check_coverage 均 exit 0（0 可疑错配、无数字锚点误报）；沿用术语表及既定译名（弗伦奇探长、莫兰小姐、莫莉·莫兰、比格尔警士、卡特警士、哈维警士、斯泰尔、柯蒂斯·韦兰、格温·莱斯特兰奇、特雷维连、吉姆·西布利、卡利莫尔先生、达夫先生、苏格兰场、皇家造币厂、刑事调查部、维多利亚局（Victoria 7000）、吉尔福德、法勒姆、南安普敦、南安普敦湾、阿姆斯特朗-西德利、轿车型、通气管、汽艇、售票姑娘、怀特岛、逮捕状口径）；新定名待回填术语表：爱德华·博兰德（Edward Boland）、德拉敦（Dehra Dun，博兰德宅名）、埃尔姆福德（Elmford）、迪恩（Deane，苏格兰场人员）、埃尔默·马伍德（Elmer Marwood，自报姓氏照译）、金斯顿（Kingston）、里普利（Ripley）、索尔兹伯里（Salisbury）、温彻斯特（Winchester）、奥尔顿（Alton）、内特利（Netley）、老内特利（Old Netley）、海奇恩德（Hedge End）、博特利（Botley）、汉布尔（Hamble）、豪恩德（Hound）、伍尔斯顿（Woolston）、海斯（Hythe）、希尔顿（Hilton）、纸飞镖（paper dart）、折叠式平底小船（collapsible punt）、压印机（press）、锚泊灯（riding lights）、普遍呼叫（general call）、戴维·琼斯的箱子（Davy Jones's locker） |
2026-09-11｜批次2｜整书完结：21/21 全部 done，删认领锁。
