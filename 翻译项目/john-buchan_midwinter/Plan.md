# 翻译计划：仲冬

## 本计划信息

- **项目名称**：john-buchan_midwinter
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/小说文学.md
- **术语表**：术语表.md
- **执行模式**：委派（长篇；见 WORKFLOW.md「单篇翻译流程」）

## 执行步骤

单篇 9 步（读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志）以 `prompts/翻译计划模板.md`「执行步骤」为准，本文件不重复。委派模式下由主 agent 派单，子代理简报含黄金样本与前篇末尾。

## 篇目清单

由 `translation_queue.csv` 管理（23 篇，约 481KB）。

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
| 2026-09-30 | in-which-a-nobleman-is-perplexed.md | done | 全书最长章（39.0KB）；35 对块；check_bilingual 退出码 0；原文逐字节校验一致；新增术语 33 条入表 |
| 2026-09-30 | in-which-a-highland-gentleman-misses-his-way.md（第 I 章） | done | 26 对块，check 退出码 0；首章定名，新增术语约 60 条 |
| 2026-09-30 | in-which-private-matters-cut-across-affairs-of-state.md（第 III 章） | done | 16 对块；check_bilingual 退出码 0；88 段原文逐字节程序化保全（FEFF/细空格/NBSP/弯引号全数保留）；新术语 20 条入表 |
| 2026-09-30 | mr-kyd-of-greyhouses.md（第 IV 章） | done | 23 对块；check_bilingual 退出码 0；82 段原文逐字节程序化保全（FEFF 29/细空格 5/NBSP 18/弯引号全数保留）；Edom 依第 III 章既定译名「以东」统一；新术语 41 条入表 |
| 2026-09-30 | john-buchan_midwinter/chance-medley.md（第 V 章 Chance-Medley） | done | 19 对块/87 段，check 退出码 0；新增术语 14 条并对齐 III/IV 章既定名（弗兰伯里/莫尔文/查斯特科特/狗与枪客栈/斯塔福德郡）；章题译作「五、不期而战」 |
| 2026-09-30 | introduces-the-runaway-lady.md（第 VI 章） | done | 12 对块；check_bilingual 退出码 0；72 段原文逐字节程序化保全（FEFF×16／细空格 U+200A×5 全数保留）；撞车归并 2 条（温斯泰、狗与枪客栈），新增术语 26 条入表 |
| 2026-09-30 | john-buchan_midwinter/broom-at-the-crossroads.md（第 VIII 章 Broom at the Crossroads） | done | 18 对块/81 段，check 退出码 0；原文逐字节程序化保全（FEFF×12／细空格 U+200A×4／NBSP×6／弯引号全数保留）；章题译作「八、十字路口的金雀花」；对齐 VI 章既定名（西克尼斯乡绅/吉利兄弟），新术语 21 条入表（月华/布莱特韦尔/快活女人客栈等） |
| 2026-09-30 | how-a-man-may-hunt-with-the-hounds-and-yet-run-with-the-hare.md（第 VII 章） | done | 16 对块/63 段，check 退出码 0；原文逐字节程序化保全（FEFF×35／细空格 U+200A×9／NBSP×3／弯引号全数保留）；章题谚语式译作「七、何以既随猎犬出猎，又与野兔同奔」；按 V/VI/VIII 章既定名统一（月华/黑本杰明/吉普赛本/好叔叔/舅舅/老风箱/审理室），新术语 17 条入表（紫杉大道/韦克赫斯特荒原/马夫比尔/李氏团等） |
| 2026-09-30 | john-buchan_midwinter/old-england.md（第 IX 章 Old England） | done | 18 对块/68 段，check 退出码 0；原文逐字节程序化保全（FEFF×19／细空格 U+200A×2／NBSP×2 全数保留），黛安娜歌诗八行镜像原排版；章题译作「九、古老英格兰」（正文仍用第 I 章既定「老英格兰」）；按 VIII 章既定名归并 4 条（布莱特韦尔×6／烧炭人／以东·洛里／德比郡／阿喀琉斯），新术语 24 条入表（洛希尔/琼内特妈妈/乔布·李/精灵乡的王后等） |
| 2026-09-30 | snowbound-at-the-sleeping-deer.md（第 X 章 Snowbound at the Sleeping Deer） | done | 25 对块/全章 106 行，check 退出码 0；原文逐字节程序化保全（FEFF×30／细空格 U+200A×6／NBSP×20／弯引号全数保留，德莱顿引诗排版镜像）；章题译作「十、雪困睡鹿客栈」；按 VII/IX 章既定名统一（诺里斯夫人／补锅匠／狄安娜／格伦塔尼特／诺丁汉），新术语 30 条入表（睡鹿客栈／塔佩特／佩克欧弗太太／主教酒／教皇琼／迪尔迈德氏族／贝内特／卡罗琳等） |
| 2026-09-30 | john-buchan_midwinter/night-at-the-same-two-visitors.md（第 XI 章 Night at the Same: Two Visitors） | done | 12 对块/51 段，check 退出码 0；原文逐字节程序化保全（FEFF×28／细空格 U+200A×6／NBSP×10／弯引号全数保留）；章题译作「十一、同处夜宿：两位来客」（承第 X 章睡鹿客栈）；按 V/VI/VIII 章既定名统一（奥格尔索普/布莱特韦尔/以东·洛里/佐治亚/狄安娜），新术语 22 条入表（睡鹿客栈/棕室/马洛克/赫尔/骑士/佩勒姆/白厅等） |
| 2026-09-30 | the-hut-in-the-oak-shaw.md（第 XII 章 The Hut in the Oak Shaw） | done | 断点续作：前代理 [1308] 中断时已落盘 4 对块，本次自源文第 14 行后追加译毕余下 52 段，全章共 14 对块/65 段，check 退出码 0；追加模式写入，既有 4 对块零改动；原文逐字节程序化保全（新增段 FEFF×19／细空格 U+200A×6／弯引号全数保留）；65 段双向覆盖校验通过（英段与源文逐字按序一致）；新术语 9 条入表（埃利安·阿弗雷希/圣安德鲁节/橡树丛小屋等）；备注：既有块 Dovedale 译「达夫代尔」与 XI 章术语表「达夫谷」不一致，本章后文无再现，未回改 |
| 2026-09-30 | john-buchan_midwinter/duchess-kitty-on-the-road.md（第 XIV 章 Duchess Kitty on the Road） | done | 17 对块/78 段，check 退出码 0；原文逐字节程序化保全（FEFF×26／细空格 U+200A×5／NBSP×12／弯引号全数保留），流式落盘每 2 块组写盘一次；章题译作「十四、基蒂公爵夫人在途中」；承 II 章定名（基蒂/科恩伯里）与 X/XI 章场景（睡鹿客栈/棕室/小内间），新术语 25 条入表（帮工约翰/会主/塔丘/布莱德韦尔/杜里斯迪尔等）；备注：棕室沿用 XI 章译名（X 章表内「棕屋」为既存不一致，未回改）；XIII 章并行翻译中，「帮工约翰/会主」如与彼章异译，按先入表者统一 |
| 2026-09-30 | journeyman-john.md（第 XIII 章 Journeyman John） | done | 21 对块/69 段，check 退出码 0；原文逐字节程序化保全（FEFF×21／细空格 U+200A×5／弯引号全数保留），英段与源文按序逐字一致校验通过；章题译作「十三、帮工约翰」；按 V/X/XI/XIV 章既定名统一（帮工约翰/吉普赛本/弗兰伯里猎队/布莱特韦尔/狄安娜/赤身人/桑迪爵士/西班牙人），新术语 19 条入表（彭尼克罗斯/埃尔丁吉尔/灰母鸦/善灵/绞架吉格舞等；帮工约翰已由 XIV 章先入表，译名一致） |
| 2026-09-30 | john-buchan_midwinter/bids-farewell-to-an-english-lady.md（第 XVI 章 Bids Farewell to an English Lady） | done | 23 对块/80 段＋歌诗两节，check 退出码 0；原文逐字程序化保全（FEFF×20／细空格 U+200A×6／NBSP×1／弯引号全数保留；源文 CRLF 行尾按 XIV 章惯例规范化为 LF、块内段落空行分隔）；「啊，爱情」两节歌诗镜像原排版；流式落盘三段追加＋规范化一次；章题译作「十六、别英格兰女士」（承 XV 章对句）；克劳迪娅口吃（t-troubles 等）以顿号重字法再现；新术语 7 条入表（陀螺客栈／恩肖班克／里士满／米尔福德等） |
| 2026-09-30 | john-buchan_midwinter/bids-farewell-to-a-scots-laird.md（第 XV 章 Bids Farewell to a Scots Laird） | done | 35 对块/136 段（含边谣引诗一段），check 退出码 0；原文逐字程序化保全（FEFF×38／细空格 U+200A×10／NBSP×27／弯引号全数保留，CRLF 行尾规范化为 LF），英段与源文按序逐字一致校验通过；流式落盘每 2 块组写盘一次；章题译作「十五、别苏格兰领主」（与 XVI 章既出「十六、别英格兰女士」成对句）；按先入表既定名统一（王子殿下/大业/西班牙人/桑迪爵士/卡罗琳/老英格兰/别西卜等），新术语 32 条入表（查尔斯·海/蒂尼斯/埃尔乔/钱珀顿/赫里奥特赛德/托滕树丛/戴伊河/无名氏族等） |
| 2026-09-30 | john-buchan_midwinter/ordeal-of-honour.md（第 XVII 章 Ordeal of Honour） | done | 29 对块/109 段，check 退出码 0；原文逐字节程序化保全（FEFF×39／细空格 U+200A×13／NBSP×7／弯引号全数保留），29 块英段与源文按序逐字一致校验通过；流式落盘每 2 块写盘一次；章题译作「十七、荣誉的裁决」；按既定名统一并回改撞车 2 处（恩肖班克／沼地马匪，从 XV/XVI 章先入表者），新术语 15 条入表（索普克劳德／达夫河／热拉尔／多比尼／急事缓办等） |
| 2026-09-30 | john-buchan_midwinter/in-which-three-gentlemen-confess-their-nakedness.md（第 XVIII 章 In Which Three Gentlemen Confess Their Nakedness） | done | 16 对块/73 个源文段落行（含歌诗三处镜像排版），check 退出码 0；原文逐字节程序化保全（FEFF×23／细空格 U+200A×7／弯引号全数保留，CRLF 规范化为 LF），源文行序覆盖校验通过；流式落盘每 2 块组追加一次；章题译作「十八、三位绅士自陈其窘」；黑刺李歌辞沿用第 I 章原词（我等正是赤身人／光脱脱卧在黑刺李树下），埃尔乔从 XV 章先入表者，皮茨利戈承 II 章正文既出今补录；新术语 21 条入表（基列的拉末／《莉莉布勒罗》／桑尼／凯特兰匪徒／该亚等） |
| 2026-09-30 | john-buchan_midwinter/dedication.md（题献 Dedication） | done | 1 对块/16 诗行，check 退出码 0；原文逐字程序化保全（FEFF×1／弯引号×1／重音字母 ó 全数保留，CRLF 规范化为 LF）；受献人 Vernon Watney 定名弗农·沃特尼，新术语 5 条入表（法尼奇／斯古尔·莫尔／特威德河等） |
| 2026-09-30 | john-buchan_midwinter/ramoth-gilead.md（第 XIX 章 Ramoth-Gilead） | done | 22 对块（含蒲柏诗联镜像一段、--- 场景分隔一处），check 退出码 0；原文逐字节程序化保全（FEFF×16／细空格 U+200A×4／NBSP×9／弯引号全数保留，源文 CRLF 规范化为 LF、块内段落空行分隔），英段与源文逐字一致校验通过；流式落盘每 2 块组追加一次；章题译作「十九、基列的拉末（Ramoth-Gilead）」，正文首现括注《列王纪上》避难之城；阿什本大道按 XVIII 章既定名回改 3 处，基列的拉末/乔治宽宏大量从 XVIII 章先入表者；新术语 29 行入表（丰特努瓦/兰开斯特/游骑队/麦克伊恩/泰蒂/波吕斐摩斯/《捆好行装走》等） |

| 2026-09-30 | john-buchan_midwinter/preface.md（序言 Preface） | done | 8 对块/16 段（编者署名 1＋正文 4＋鲍斯韦尔引文 10＋编者后记 1），check 退出码 0；原文逐字节程序化保全（FEFF×5／NBSP×16／弯引号×43 全数保留，CRLF 规范化为 LF、块内段落空行分隔）；年份数字锚点空格法（1763 年／1745 和 1746）；Sufflamina 括注拉丁原词、脚注号 1 保留；说明文语体与正文罗曼史相区分；新术语 26 条入表（德温特／鲍斯韦尔／埃尔斯菲尔德／怀斯／布伦海姆宫等） |
| 2026-09-30 | john-buchan_midwinter/endnotes.md（尾注 Endnotes） | done | 1 对块，check_bilingual 退出码 0；原文逐字节程序化保全（弯引号 U+2019／回符箭头 U+21A9＋U+FE0E 全数保留，CRLF 规范化为 LF）；「1754 年」数字后留半角空格系校验器  锚点所需（「年」计为词字符）；全书末件译竣；新术语 2 条入表（鲍斯韦尔／《约翰逊传》） |

| 2026-09-30 | john-buchan_midwinter/postscript.md（跋 Postscript） | done | 2 对块/5 段（编者补记 2＋约翰逊残信引文 3），check 退出码 0；原文逐字程序化保全（FEFF×8／细空格 U+200A×3／NBSP×4／弯引号与 N—— 全数保留）；「1748 年」数字锚点空格法；全书末件（I-XIX 章＋序言/题献/尾注俱毕）译竣；新术语 8 条入表（卡洛登/哈里比/高夫广场/阿兰·麦克莱恩/人类愿望之虚妄/维吉尔/奥德赛/斯多噶哲人） |
