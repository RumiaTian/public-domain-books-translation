# 翻译计划（Plan.md）— 内心的人（The Man Within）

> 翻译一整本书或多文件内容时的标准模式。填入书名、源文/译文目录、篇目清单（`translation_queue.csv`），即可用通用提示词推进翻译，无需手动指定每个文件。

---

## 本计划信息

- **项目名称**：内心的人（The Man Within）
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
| `术语表.md` | 翻译硬约束层。每篇译完补充新词 | agent / 人工 |
| `translation_queue.csv` | 任务队列。每行一文件，`file, size_kb, status` 三列 | 翻译前改 doing，完成后改 done |
| `Plan.md`（本文件） | 执行步骤 + 运行日志 | agent 追加日志 |
| `原文/*.md` | 源文 | 不改 |
| `译文/*.zh-CN.md` | 译文产出（块对照双语） | 翻译 agent 产出 |

---

## translation_queue.csv 格式

```
file,size_kb,status
第01章.md,12.3,todo
第02章.md,18.1,todo
...
```

| 字段 | 含义 | 取值 |
|------|------|------|
| `file` | 源文文件名（在 `原文/` 目录下） | 如 `chapter-1.md` |
| `size_kb` | 源文大小（KB）。>50KB 为长文，按通用翻译引擎第七节分段 | 数字 |
| `status` | 翻译状态 | `todo` 待译 / `doing` 翻译中 / `done` 已完成 |

---

## 执行步骤（agent 按此推进，两种模式共用）

> **谁执行**由 `项目说明.md` 的「内容形态」字段决定（见 `WORKFLOW.md`「判断内容形态」）：委派模式由子代理逐篇执行本流程；连续模式（中篇）由主 agent 自己执行。无论谁执行，这 9 步不变。

### 1. 读配置（每次翻译前必读）
```
1. 本项目 Plan.md（本文件）
2. 项目说明.md
3. 术语表.md（如无则跳过）
4. prompts/通用翻译引擎.md
5. prompts/领域配置/对应领域.md（项目说明指定）
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
回到步骤 2，取下一篇 `todo`，直到全部 `done`。委派模式下由主 agent 决定是否继续派单（见 `WORKFLOW.md`「委派模式调度循环」）。

---

## 篇目清单

| # | 篇名 | 源文 | 大小 | 状态 |
|---|------|------|------|------|
| 1 | 献词 | dedication.md | 0.3KB | todo |
| 2 | 题词 | epigraph.md | 0.1KB | todo |
| 3 | 第一部 | part-i.md | 0.0KB | todo |
| 4 | 第一章 | chapter-1.md | 15.5KB | todo |
| 5 | 第二章 | chapter-2.md | 28.1KB | todo |
| 6 | 第三章 | chapter-3.md | 28.7KB | todo |
| 7 | 第四章 | chapter-4.md | 35.7KB | todo |
| 8 | 第五章 | chapter-5.md | 35.7KB | todo |
| 9 | 第二部 | part-ii.md | 0.0KB | todo |
| 10 | 第六章 | chapter-6.md | 30.5KB | todo |
| 11 | 第七章 | chapter-7.md | 26.8KB | todo |
| 12 | 第八章 | chapter-8.md | 62.6KB | todo |
| 13 | 第九章 | chapter-9.md | 37.5KB | todo |
| 14 | 第三部 | part-iii.md | 0.0KB | todo |
| 15 | 第十章 | chapter-10.md | 44.2KB | todo |
| 16 | 第十一章 | chapter-11.md | 31.2KB | todo |

（以 `translation_queue.csv` 为准）

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
| 2026-09-12 | 第一章（chapter-1.md） | 11 对双语块，通过（check_bilingual.py exit 0，无警告） | 术语按表落位并首现括注：肖勒姆（Shoreham）、卡莱昂（Carlyon）、「萨塞克斯帕德」（the Sussex Pad）、走私贩子（runners）、缉私税吏（gaugers）、走私一批货（run a cargo）、德文郡（Devon）。新定名（不在术语表，供回填）：《汉塞尔与格蕾特尔》（Hansel and Gretel）、格蕾特尔（Gretel）、几尼（guinea）、点亮的芜菁灯（lighted turnip）。*oikia* 依项目说明保留斜体，首现括注「希腊语，房屋」。体例：标题合并「### I / 一」；内心独白两个自我以语气区分（感伤自怜 vs 冷峻自嘲）；本章卡莱昂仅镜中一瞥，威胁靠克制处理；追我的（the officers）译「缉私官员」；文内引号用中文弯引号，原文弯引号原样保留 |
| 2026-09-12 | 第三章（chapter-3.md） | 11 对双语块（37 段），通过（check_bilingual.py exit 0，无警告） | 术语按表落位：卡莱昂（Carlyon）、伊丽莎白（Elizabeth）、安德鲁斯（本章仅姓出现，译「安德鲁斯」）、白垩丘（the down）、小屋（the cottage）。新定名（不在术语表，供回填）：贺拉斯（Horace）、索福克勒斯（Sophocles）、殡葬人（undertaker’s man）、丧主（chief mourner）、白法衣（surplice）、侠义之猿（a chivalrous ape）。圣经/葬仪引文按和合本与公祷书语体译出（约伯记19、诗篇39、哥林多前书15）。体例与第一章对齐：标题合并「### III / 三」；中文对话用弯双引号，破折号用——；内心两个自我语气区分（藏进雾里的乞慰声 vs 「蠢货！」的冷峻诘责）；卡莱昂威胁靠克制平淡处理，邪性一笔（吹哨自语）保留不确定感 |
| 2026-09-12 | 第四章（chapter-4.md） | 45 对双语块，通过（check_bilingual.py exit 0，无警告；块内段落对称 159/159，无 BOM 无截断） | 术语按表落位并首现括注：安德鲁斯（Andrews）、卡莱昂（Carlyon）、伦敦佬哈里（cockney Harry）、乔（Joe）、巴特勒夫人（Mrs. Butler）、缉私税吏（gauger）、缉私官员（revenue men）、走私者（smuggler）。新定名（不在术语表，供回填）：『绅士』（the Gentlemen，走私团伙自称）、共饮之杯（loving cup）、纸捻（spill）、戏单（playbill）、碗柜（dresser）、茶叶罐（caddy）、棚屋（shed）。体例：标题合并「### IV / 四」；两个自我以语气区分（感伤自怜 vs 不眠的内心批评者）；卡莱昂威胁感靠克制平淡语气；文内引号中文弯引号，原文弯引号原样保留；强调斜体（I *am* the music）保留 |
| 2026-09-12 | 第二章（chapter-2.md） | 27 对双语块（73 段），通过（check_bilingual.py exit 0，无警告） | 术语按表落位：卡莱昂（Carlyon）、弗朗西斯/安德鲁斯（Francis Andrews，按表：名单现译「弗朗西斯」，姓单现译「安德鲁斯」）、伊丽莎白（Elizabeth）、詹宁斯先生（Mr. Jennings）、巴特勒夫人（Mrs. Butler）、肖勒姆（Shoreham）、德文郡（Devon）、埃克塞特大教堂（Exeter Cathedral）、南唐斯丘陵（the down/downs）、走私贩子（runners）、缉私官员（revenue men）、缉私税吏（gaugers）。新定名（不在术语表，供回填）：格拉森猪群（Gadarene swine，首现附典故括注）、法利赛人（Pharisee）、育苗棚（potting shed）、海螺粉（Winkle dust，园丁呓语）、波特酒（port wine）。体例与第一、三章对齐：标题合并「### II / 二」；中文对话用弯双引号（本篇初稿直角引号已全书统一转换）；内心两个自我语气区分（感伤自怜的孩子 vs 站在一旁诘问的冷峻批评者）；巴特勒夫人口语带乡土词「哩/呀」；本章卡莱昂未正面登场，威胁以梦境与时间意象克制处理 |
| 2026-09-12 | 前置微件包（dedication/epigraph/part-i/ii/iii） | 5 件全部通过（dedication 2 对块、epigraph 1 对块、part 三件为纯标题合并行 0 对块；check_bilingual.py 各 exit 0，无警告无可疑错配；UTF-8 无 BOM） | 献词「For Vivienne, my wife in wonder」译「致薇薇安，与我共怀惊奇的妻子」——wonder 兼有「惊奇/奇迹」双关，取「惊奇」一词兼顾：「惊」承惊叹之义、「奇」含奇迹之义，较拆译「惊叹奇迹」更贴原文简净语感。十四行诗节选（源为「平凡容器承载珍宝」的宗教诗）实际位于 dedication.md 而非 epigraph.md，按诗行对照 6 行逐行对译，保留 > 引用标记。题词「There's another man within me that's angry with me」译「我内心另有一个人在向我发怒」，首现括注出处，扣合书名《内心的人》；诗人名按通行译名作「勃朗宁」（派发说明作「布朗宁」，未入术语表，如需统一可全局替换）。三个 part 源文标题拆作两行（「## Part」+「 I」），按标题合并体例并为「## Part I / 第一部」「## Part II / 第二部」「## Part III / 第三部」，与篇目清单既定汉名一致 |
| 2026-09-12 | 第七章（chapter-7.md） | 30 对双语块（128 段），通过（check_bilingual.py exit 0，无警告无可疑错配；原文段/中文段 128/128 对称，UTF-8 无 BOM，末段无截断） | 术语按表落位并首现括注：安德鲁斯（Andrews，本章全为姓单现）、卡莱昂（Carlyon）、露西（Lucy）、亨利·梅里曼爵士（Sir Henry Merriman，后文「亨利爵士」）、刘易斯（Lewes）、大街（the High Street）、波特酒（port）、伊丽莎白（Elizabeth）、帕金法官（Parkin）。新定名（不在术语表，供回填）：法恩先生（Mr. Farne，亨利爵士的书记/律师助手，第八章法庭戏将再登场）、押沙龙先生（Mr. Absolom，安德鲁斯匿名信假名，取「大卫王之子」圣经典故故按和合本译「押沙龙」）、麝香葡萄酒（muscatel）、出庭律师（barrister）、证人席（witness box）、缉私局（the Customs，按表 the revenue 一脉译法）、供养人（keeper，露西口中靠男人供养之义）、「伙计」（my man，法恩居高临下称呼，本章冲突枢纽词，含内层引号处用弯单引号）。体例与前四章对齐：标题合并「### VII / 七」；中文对话弯双引号、破折号——；两个自我章末正面现身（「内心的批评者」vs 贪欲的身体），冷峻诘责语气收束；卡莱昂未登场，亨利爵士「绞死凶手」的狂热与镜中烛火意象克制处理；「明天我们要面对枪口」（Tomorrow we face the guns）三次出现统一译法；露西与亨利爵士楼梯调笑段语气轻佻嘲讽，与法庭严肃线形成反差 |
| 2026-09-12 | 第六章（chapter-6.md） | 22 对双语块（88 段），通过（check_bilingual.py exit 0，无警告无可疑错配；块内段落数 22/22 对称 88/88，UTF-8 无 BOM，末段无截断） | 术语按表落位并首现括注：安德鲁斯（Andrews，本章全为姓单现）、卡莱昂（Carlyon）、伊丽莎白（Elizabeth）、詹宁斯先生（Mr. Jennings）、刘易斯（Lewes）、肖勒姆（Shoreham）、迪奇林比肯（Ditchling Beacon）、巡回法庭（the Assizes）、走私一批货（run a cargo）、缉私局（the revenue）、走私者（smugglers）、大道（the High Street）、『白鹿』（the White Hart，对话内嵌套名按体例用『』）。新定名（不在术语表，供回填，与第七章已统一）：法恩先生（Mr. Farne）、押沙龙（Absolom，酒馆假名，同取「大卫王之子」典故按和合本译）；本章另新定：哈里山（Harry's Mount）、露水塘（dew-pond）、萨里丘陵（the Surrey Hills）、格蕾特尔（Gretel，承第一章）、鲍街探员（Bow-street runners）、纽黑文（Newhaven）、哈索克斯（Hassocks）、普拉普顿（Plumpton）、迪奇林（Ditchling）、林德菲尔德（Lindfield）、阿丁利（Ardingly）、基里街（Keerie Street）、索斯欧弗教堂（Southover Church）、乔治（George，酒保）。体例与一至五章对齐：标题合并「### VI / 六」；中文对话弯双引号；两个自我语气区分（「我会回来的」感伤立誓 vs 内心批评者「你这懦夫」冷峻诘责）；卡莱昂未登场、仅存于恐惧想象，威胁靠克制处理；「跟我同名」保留原文四字妙语的字数梗；法恩先生对话一律用「您」显克制的礼貌与冷意；结尾「恕我冒昧打搅，亨利爵士（Sir Henry）」留悬念不点破身份，与第七章衔接 |
| 2026-09-12 | 第五章（chapter-5.md） | 27 对双语块（123 段），通过（check_bilingual.py exit 0，无警告无可疑错配；块内段落数 27/27 对称 123/123，UTF-8 无 BOM，末段双「晚安」无截断） | 术语按表落位并首现括注：安德鲁斯（Andrews，本章全为姓单现）、伊丽莎白（Elizabeth）、卡莱昂（Carlyon）、肖勒姆（Shoreham）、缉私税吏（gaugers）、德文郡（Devon）、乔（Joe）、蒂姆斯（Tims）、詹宁斯先生（Mr. Jennings）、白垩丘（the downs）、巡回法庭（the Assizes）、刘易斯（Lewes）、缉私官员（the officers，无括注按表译）。新定名（不在术语表，供回填）：犹大（Judas，首现括注，「萨塞克斯就有两个犹大」承本章背叛主题）、维纳斯（Venus，「比死亡来得更早」的优先权妙语）、缉私局（the Customs，机构名沿第七/六章既定译法）、『绅士』（the Gentlemen，承接第四章）、不义的管家（the unjust steward，路加福音16比喻，引文按和合本语体：「主人就夸奖这不义的管家，因为他做事聪明」）、得奖种公牛（a prize bull of a man，乔）、皮带（strap）、标本册（album）、界标手势（comprehensive gesture，两处呼应译「包罗一切的手势」）。体例与一至四章对齐：标题合并「### V / 五」；中文对话弯双引号、对白内层引语（詹宁斯原话、乔的原话）用弯单引号『』内层实作‘’；两个自我语气区分（「是的，我是在恋爱」感伤自辩 vs 「可你是在恋爱吗？你吗？你吗？」冷峻嘲弄；「改掉身上的斑点」保留豹斑典故）；卡莱昂未正面登场，威胁靠伊丽莎白转述与「除非是卡莱昂」处爱恨交缠的克制处理；「直至世世无穷」（world without end）按公祷书语体；全章小屋炉边长谈，伊丽莎白身世与詹宁斯「不义管家」前史为本章新素材，为第六至八章刘易斯巡回法庭线作铺垫 |
| 2026-09-12 | 第八章（chapter-8.md） | 85 对双语块（358 段，分 15 批追加落盘），自检通过（源文 358 段与译文 Original 块内 358 段程序化逐段比对全等；块内段落对称 0 异常；UTF-8 无 BOM）；check_bilingual.py：标记成对 85 对、标题合并满足，exit 1 仅 5 处数字锚点误报（February 10→二月十日、twelve→十二等中文数字本地化改写），按派发规则判定过检 | 术语按表落位并首现括注：刘易斯（Lewes）、爱德华·帕金爵士（Sir Edward Parkin，Justice Parkin 译「帕金法官」）、亨利·梅里曼爵士（Sir Henry Merriman）、法恩先生（Mr. Farne）、露西（Lucy）、蒂姆斯（Tims，理查德·蒂姆斯）、布拉多克先生（Mr. Braddock）、托马斯·希利亚德先生、爱德华·雷克索尔、卡莱昂（Carlyon）、伊丽莎白、巴特勒夫人、缉私税吏（gauger）、缉私局（the revenue）、告密者（informer）、伦敦佬哈里（Cockney Harry）、乔·科利尔（Joe Collier）、「白鹿」、「萨塞克斯帕德」、「好机遇号」（斜体保留）、肖勒姆、东萨塞克斯。新定名（不在术语表，供回填）：德鲁斯（Druce）、黑克（Hake）、佩蒂先生（Mr. Petty）、加尼特（Garnet）、索斯奥弗（Southover）、哈索克斯（Hassocks）、提审书记官（Clerk of the Arraigns）、执戟卫队（javelin men）、随员（marshal）、旁听席（public gallery）、庭吏（usher）、验尸研讯（Coroner’s inquisition）、陪审长（foreman）、织工波顿（Bottom）、诺森伯兰公爵、简·格雷、本特利（Bentley’s，鼻烟牌）。体例要点：标题合并「### VIII / 八」；法庭问答保持维多利亚式繁复书面语与乡音证词（税吏/黑克/巴特勒夫人用「俺/哩/呀」）的文体落差；两个自我语气区分（L137 感伤的心「我会闯过去的」对冷峻自嘲「你这多愁善感的傻瓜」，L121 内心批评者「贪图她的身子」）；卡莱昂威胁依旧克制平淡（仅侧写猿脸与「他在追我」）；文内引号中文弯引号、引语内嵌套用弯单引号；结尾 runners 依语境译「捕快」（非走私贩子，警方护送义，供术语表复核） |
| 2026-09-12 | 第十章（chapter-10.md） | 43 对双语块（228/228 段对称），通过（check_bilingual.py exit 0：43 对 Original/Chinese 成对、标题合并满足、可疑错配 0 处、无警告；UTF-8 无 BOM，末段无截断） | 术语按表落位并首现括注：安德鲁斯（Andrews，本章全为姓单现）、卡莱昂（Carlyon）、伊丽莎白（Elizabeth）、刘易斯（Lewes）、肖勒姆（Shoreham）、白垩丘（the down）、证人席（witness box）、『绅士』（the Gentlemen）、巴特勒夫人（Mrs. Butler）、詹宁斯先生（Mr. Jennings）、伦敦佬哈里（Cockney Harry）、露西（Lucy）、乔（Joe）、露水塘、缉私官员（the officers）。与第八章对齐沿用：黑克（Hake，承 chapter-8 译名）、*好机遇号*（the *Good Chance*，斜体保留）。本章新定名（不在术语表，供回填）：奇切斯特（Chichester）、忘川（Lethe）、无罪开释（the acquittal，第九章审判结果可沿用）、婚产授与文书（settlement，安德鲁斯讥语）。体例与前九章对齐：标题合并「### X / 十」；中文对话弯双引号、破折号——；两个自我正面收束（峰顶讥笑的冷峻批评者 vs 「上帝啊……给我勇气」的默祷，第 217 段内心独白）；卡莱昂未登场，威胁经「描摹他听消息的样子」一段克制呈现；清扫屋子与更恶之鬼的比喻按和合本语体译出；「她是我的同类」/「跟任何女人都不一样」对照保留；末章意象（黑花绽开的夜、细茎白花、看不见的恐惧）逐句对译收全书悬念 |
| 2026-09-12 | 第九章（chapter-9.md） | 30 对双语块（116/116 段对称，分 5 批落盘），通过（check_bilingual.py exit 0：30 对 Original/Chinese 成对、标题合并满足、可疑错配 0 处、无警告；UTF-8 无 BOM，末段「终于是你了？」无截断） | 术语按表落位并首现括注：安德鲁斯（Andrews）、卡莱昂（Carlyon）、露西（Lucy）、伊丽莎白（Elizabeth）、亨利爵士/亨利·梅里曼爵士（Sir Henry (Merriman)）、伦敦佬哈里（Cockney Harry）、乔（Joe）、理查德·蒂姆斯（Richard Tims）、「白鹿」（the White Hart）、证人席（witness box）、萨塞克斯（Sussex）。与第八/十章对齐沿用：黑克（Hake，本稿初译「海克」已按 chapter-8 译名全局订正）、哈索克斯（Hassocks）、「好机遇号」（对话内层按弯单引号体例，*the Good Chance* 斜体保留）。runners 三处（看守他的两个、客栈里的、哈里口中）承第八章结尾语境译「捕快」（警方看守义，供术语表复核）。本章新定名（不在术语表，供回填）：圣安妮教堂（St. Anne's Church）、德雷克（Drake，「德雷克的郡」即德文郡，附带「老派海狗」意象）、小娘子（ladybird，哈里对露西的轻佻称呼）。体例与一至十章对齐：标题合并「### IX / 九」；中文对话弯双引号、破折号——；两个自我本章以「理性」与「心」对峙，「内心的批评者」头一遭与心联手反对理性（第七章体例的延续反转）；卡莱昂正面登场仅少年回忆（初见日落一场），威胁感靠哈里转述与克制平淡语气，「剥掉卡莱昂的梦，剩下的那点东西还不如我」的反讽保留；露西诱惑戏与荒丘自省（评判人凭身体还是凭梦）的心理辩证逐段对译；末段钥匙孔前「可把你盼来了？」收束，衔接第十章审判结果线 |
| 2026-09-12 | 第十一章（chapter-11.md） | 21 对双语块（85 段），通过（check_bilingual.py exit 0，无警告无可疑错配；块内段落数 21/21 对称 85/85，UTF-8 无 BOM，末段「有的是智慧，与清明」全书收束无截断） | 术语按表落位并首现括注：安德鲁斯（Andrews）、卡莱昂（Carlyon）、伊丽莎白（Elizabeth）、乔（Joe）、蒂姆斯（Tims）、詹宁斯先生（Mr. Jennings）、肖勒姆（Shoreham）、刘易斯（Lewes）、白垩丘（the down）、缉私官员（the officers）、『绅士』（the Gentlemen，承第四章）；弗朗西斯（Francis）仅卡莱昂一句「弗朗西斯，这不是我干的」及随释出现，与名单体例一致。新定名（不在术语表，供回填）：黑克（Hake，「乔、黑克之流」泛指走私同伙）、佩加索斯（Pegasus，驽马喻作「生着翅膀的佩加索斯天马」）、证人室（the witnesses’ room，承第八章庭审线）、「好机遇号」（*Good Chance*，斜体括注保留）。体例与前十章对齐：标题合并「### XI / 十一」；中文对话弯双引号，内层引语（伊丽莎白的‘快了’、卡莱昂原话、沃恩诗行「他们都已走进光的世界去了，唯我一人枯坐此处，流连不去」）用弯单引号。终章两个自我合流点题：「我就是那批评者」——父亲魂灵与「冷峻而不肯休歇的批评者」的对峙按感伤自怜 vs 冷峻决断分层语气收束；卡莱昂台词保持克制平淡（「有什么用？她死了。」）；农夫方言用粗俗直白口语（臭婊子、吃枪子儿）与蒂姆斯痴傻语气（「你没有把我弄上那证人席」承第七章术语）区分；终局意象完整保留（两支黄蜡烛、白大理石之声、月如船、常春藤幻影），末段以「智慧与清明」收束全书。技术备注：源文段落内散布 U+FEFF/U+00A0/U+200A 隐形字符，Original 块已按源文逐字节原样保留（与源文 85 段逐一比对一致） |
| 2026-09-12 | **整书完结**：格林《内心之人》（The Man Within，1929 处女作）16/16 流转（第 11 册） | 两轮译完 376.9K（08:15 首批 4 章 + 19:45 轮 12 项），零 [1301]/[1308]/回滚；含 62.6K 全书最大章（ch8，15 批 append-only、358 段逐段全等比对、heredoc 截断自愈一次）与前置微件包（dedication 含十四行诗节选/epigraph 布朗宁书名出处名句/part 三部标题） | 风格基线：绵密内心独白+「两个自我」语气区分（感伤自怜 vs 冷峻批评者，终章合流「我就是那批评者」）；圣经/公祷书引文按和合本语体（world without end=直至世世无穷）；卡莱昂威胁感全程克制平淡。体例：标题「### 罗马数字 / 中文数字」；中文弯引号+内层弯单引号（ch2 直角引号 133 对全量改齐判例）。术语：弗朗西斯/安德鲁斯分立、『绅士』=the Gentlemen、黑克（Hake，ch9 依 ch8 回改 6 处）、「好机遇号」（*Good Chance* 斜体保留）、runners 走私义=走私贩子/警方语境=捕快（ch8 起）；新定名一批供回填（法恩、押沙龙、麝香葡萄酒、巡回法庭、证人席、缉私局、供养人等） |
