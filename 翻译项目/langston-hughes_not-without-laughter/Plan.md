# 翻译计划（Plan.md）

> 翻译一整本书或多文件内容时的标准模式。复制本文件到项目文件夹，重命名为 `Plan.md`，填入书名、源文/译文目录、篇目清单（或生成 `translation_queue.csv`），即可用通用提示词推进翻译，无需手动指定每个文件。
>
> 适配任意内容：小说、文集、手册、论文集……只需在「项目说明.md」选好领域配置（技术/历史/学术/小说），Plan.md 的执行流程不变。

---

## 本计划信息

- **项目名称**：不是没有笑（Not Without Laughter）—— langston-hughes_not-without-laughter
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
01-storm.md,12.3,todo
02-conversation.md,18.1,todo
...
```

| 字段 | 含义 | 取值 |
|------|------|------|
| `file` | 源文文件名（在 `原文/` 目录下） | 如 `01-storm.md` |
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
5. prompts/领域配置/小说文学.md（项目说明指定）
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
- 标题格式：全部「英文 / 中文」合并（章节标题保留罗马数字，如 "I Storm / 一 风暴"）。
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

全书 30 章（罗马数字 I–XXX），源文文件已按阅读顺序加数字前缀，清单由 `translation_queue.csv` 管理（运行 `python scripts/gen_project_files.py` 生成）。

| # | 章名 | 源文 |
|---|------|------|
| 1 | I Storm | 01-storm.md |
| 2 | II Conversation | 02-conversation.md |
| 3 | III Jimboy's Letter | 03-jimboy-s-letter.md |
| 4 | IV Thursday Afternoon | 04-thursday-afternoon.md |
| 5 | V Guitar | 05-guitar.md |
| 6 | VI Work | 06-work.md |
| 7 | VII White Folks | 07-white-folks.md |
| 8 | VIII Dance | 08-dance.md |
| 9 | IX Carnival | 09-carnival.md |
| 10 | X Punishment | 10-punishment.md |
| 11 | XI School | 11-school.md |
| 12 | XII Hard Winter | 12-hard-winter.md |
| 13 | XIII Christmas | 13-christmas.md |
| 14 | XIV Return | 14-return.md |
| 15 | XV One by One | 15-one-by-one.md |
| 16 | XVI Nothing but Love | 16-nothing-but-love.md |
| 17 | XVII Barbershop | 17-barbershop.md |
| 18 | XVIII Children's Day | 18-children-s-day.md |
| 19 | XIX Ten Dollars and Costs | 19-ten-dollars-and-costs.md |
| 20 | XX Hey, Boy! | 20-hey-boy.md |
| 21 | XXI Note to Harriett | 21-note-to-harriett.md |
| 22 | XXII Beyond the Jordan | 22-beyond-the-jordan.md |
| 23 | XXIII Tempy's House | 23-tempy-s-house.md |
| 24 | XXIV A Shelf of Books | 24-a-shelf-of-books.md |
| 25 | XXV Pool Hall | 25-pool-hall.md |
| 26 | XXVI The Doors of Life | 26-the-doors-of-life.md |
| 27 | XXVII Beware of Women | 27-beware-of-women.md |
| 28 | XXVIII Chicago | 28-chicago.md |
| 29 | XXIX Elevator | 29-elevator.md |
| 30 | XXX Princess of the Blues | 30-princess-of-the-blues.md |

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
| 2026-09-24 | 03-jimboy-s-letter.md | done | 7 对块，check 通过（exit 0）；新术语 7 组回写术语表 |
| 2026-09-24 | 02-conversation（II Conversation / 二 闲谈） | done | 15 对块，check_bilingual 退出码 0，无错配 |
| 2026-09-24 | 04-thursday-afternoon.md | done | 18 对块，check 通过（exit 0）；新术语 10 组回写术语表 |
| 2026-09-24 | 01-storm.md | done | check 通过（11 对块，退出码 0）；开篇章无黄金样本，依术语表+rudolph-fisher 风格奠基全书文风；新术语 4 组回写术语表 |
| 2026-09-24 | 05-guitar（V Guitar / 五 吉他） | done | 16 对块，check 通过（exit 0），无错配；歌词韵文保留分行，吉姆博伊/黑格/约翰逊老两口乡土腔按术语表分档；新术语 12 组回写术语表 |
| 2026-09-24 | 06-work.md | done | 12 对块，check 通过（exit 0）；新术语 4 组回写术语表 |
| 2026-09-24 | 07-white-folks.md | done | 14 对块，check 通过（exit 0）；新术语 19 组回写术语表 |
| 2026-09-24 | 08-dance（VIII Dance / 八 舞会） | done | 27 对块，check 通过（exit 0），无错配；歌词韵文保留分行与结构，黑格乡土腔、盥洗间众人与乐队叙述按术语表分档，"plug-ugly niggers" 叙述内群语境作「老黑」；新术语 17 组回写术语表 |
| 2026-09-24 | 09-carnival.md | done | 15 对块，check 通过（exit 0），无错配；白人观众/班主口中 nigger、coon 按分档如实译出，黑格乡土腔照旧；本鲍/杰茜/痨病/鹰摇摆等从 07、08 章既定名对齐；新术语 24 条回写术语表 |
| 2026-09-24 | 10-punishment（X Punishment / 十 惩罚） | done | 9 对块，check 通过（exit 0），无错配；黑格/捡废铁男孩乡土腔与吉姆博伊训子标准口语分档，白人孩子口中 Nigger 如实作「黑鬼」，游乐场/肥肉/柳条/五分镍币/痨病等从 08、09 章既定名对齐；新术语 9 组回写术语表 |
| 2026-09-24 | 11-school（XI School / 十一 学校） | done | 10 对块，check 通过（exit 0），无错配；歌词韵文保留分行，课堂白人教师标准语与黑格乡土腔按术语表分档，黑人互称 nigger/coon 作「老黑」、萨迪自称作「黑人」；新术语 14 条回写术语表 |
| 2026-09-24 | 12-hard-winter（XII Hard Winter / 十二 严冬） | done | 14 对块，check 通过（exit 0），无错配；黑格/约翰逊姊妹乡土腔与安吉/桑迪标准口语分档，黑人互称 nigger 作「黑人」，哈丽雅特求救信照标准语译出，末尾信件保留 blockquote 结构；新术语 17 条回写术语表 |
| 2026-09-24 | 14-return（XIV Return / 十四 归来） | done | 11 对块，check 通过（exit 0），无错配；哈丽雅特归家章，黑格/玛丽之母乡土腔与哈丽雅特/安吉较平口语分档，哈丽雅特口中 nigger 作「老黑」、肤色等级语 sulphur-yellow 入表；新术语 11 条回写术语表 |
| 2026-09-24 | 13-christmas（XIII Christmas / 十三 圣诞节） | done | 18 对块，check 通过（exit 0），无错配；黑格/安吉乡土腔与坦皮标准硬腔分档，睡前祷告保留分行，坦皮口中 niggerish 作「老黑气」；金色飞驰/埃德蒙森五金店/斯梅德利先生（原文 Mr. Siles 变体）等新术语 12 条回写术语表 |
| 2026-09-24 | 16-nothing-but-love（XVI Nothing but Love / 十六 唯有爱） | done | 6 对块，check 通过（exit 0），无错配；黑格夏夜长篇独白乡土腔照旧，珍妮小姐等白人引语用标准语对照，黑人自称互称 nigger 作「黑人／老黑」；新术语 11 条回写术语表 |
| 2026-09-24 | 15-one-by-one（XV One by One / 十五 一个接一个） | done | 11 对块，check 通过（exit 0），无错配；亲友离散章（安吉赴底特律），黑格乡土腔与安吉/伊尔维拉母子较平口语分档，白人男孩口中 nigger 如实作「黑鬼」，场景分隔 --- 保留 2 处；新术语 11 组回写术语表 |
| 2026-09-24 | 17-barbershop（XVII Barbershop / 十七 理发店） | done | 10 对块，check 通过（exit 0），无错配；理发店群像章，黑格／洛根老爹乡土腔与店中众人市井口语分档，黑人互称 nigger 作「老黑」、jig show／Jim-Crow 等种族语汇按语境处理并入表；哈丽雅特·威廉斯等从既有定名对齐；新术语 23 条回写术语表 |
| 2026-09-24 | 19-ten-dollars-and-costs（XIX Ten Dollars and Costs / 十九 十美元加诉讼费） | done | 5 对块，check 通过（exit 0），无错配；哈丽雅特与莫德尔被捕判罚章，查理·纳特市井腔与黑格乡土腔按术语表分档，报载 negresses 作「黑人女子」、哈丽雅特·威廉斯循定名，街头拉客罪名与布林顿法官新定名入表；新术语 9 条回写术语表 |
| 2026-09-24 | 18-children-s-day（XVIII Children’s Day / 十八 儿童节） | done | 14 对块，check 通过（exit 0），无错配；白人检票员与模仿其腔调的口中 darkies/nigger 如实作「黑鬼」，黑孩子互称 jigaboos 作「老黑们」，黑格/约翰逊姊妹乡土腔照旧，安吉家书保留 blockquote 落款结构，末尾灵歌《星星之外》保留分行；新术语 16 条回写术语表 |
| 2026-09-24 | 20-hey-boy（XX Hey, Boy! / 二十 嘿，小子！） | done | 7 对块，check 通过（exit 0），无错配；旅馆侍应章，查理·纳特市井腔与南方白人醉汉拖腔标准语分档，白人口中 nigger/darky/coon 如实作「黑鬼／黑崽子」，乔治·克拉克、玛西娅·麦凯等新定名入表；新术语 8 条回写术语表 |
| 2026-09-24 | 21-note-to-harriett（XXI Note to Harriett / 二十一 致哈丽雅特的便条） | done | 15 对块，check 通过（exit 0），无错配；书简传话章（坦皮便条促哈丽雅特归家、黑格病重），洼地区风月场所群像与黑格病榻守望两段；黑格/约翰逊姊妹乡土腔、德·卡特夫人拿腔作调、坦皮与白人医生标准语分档，布鲁斯歌词、坦皮便条与电报保留 blockquote；哈丽雅特·威廉斯循定名、坦皮大姨对齐旧章；新术语 7 条回写术语表 |
| 2026-09-24 | 22-beyond-the-jordan（XXII Beyond the Jordan / 二十二 约旦河彼岸） | done | 12 对块，check 通过（exit 0），无错配；黑格临终与葬礼挽歌章，黑格/约翰逊姊妹乡土腔与坦皮生硬体面腔、医生白人平直语分档，安吉家书与坦皮背面回信 blockquote 保留，坟头灵歌「夜何其黑，地何其冷」保留分行；塔尔萨/托莱多/西普拉街/约旦河彼岸等新术语 8 条回写术语表 |
| 2026-09-24 | 23-tempy-s-house（XXIII Tempy’s House / 二十三 坦皮的家） | done | 8 对块，check 通过（exit 0），无错配；坦皮家体面中产章，坦皮/斯梅德利先生标准硬腔与桑迪乡土腔分档，坦皮内化贬语 nigger/darky 如实作「黑鬼」，don’t/ain’t 语法纠错以「扣不住哩→扣不住」「俺没有→我没有」传神，原文 Mr. Siles/Arkins Siles 循 13 章先例归并斯梅德利；新术语 13 条回写术语表 |
| 2026-09-24 | 24-a-shelf-of-books（XXIV A Shelf of Books / 二十四 一书架的书） | done | 6 对块，check 通过（exit 0），无错配；阅读启蒙章（腮腺炎居家识书、《危机》与杜波依斯社论、普伦蒂斯铺读书、作文得奖），坦皮体面标准腔与桑迪少年口语、巴斯特市井腔分档，坦皮贬语 white folks' nigger 循 16 章作「白人跟前的老黑」，书名（白鲸／威尼斯商人／超越奴役／雪松后面的房子等）按通行译法；潘塞塔·杨循既有定名、巴尔-格兰特太太循 23 章定名；新术语 18 条回写术语表 |
| 2026-09-24 | 26-the-doors-of-life（XXVI The Doors of Life / 二十六 人生之门） | done | 8 对块，check 通过（exit 0），无错配；少年成长抉择章（内省独白与伙伴对白交织），坦皮/斯梅德利标准硬腔与桑迪/巴斯特/吉姆乡土市井腔分档，巴斯特口中考大学的老黑循黑人互称分档，ofay／冒充白人新词入表，《人生之门》书名与章题统一、圣经引文出处数字保留；新术语 10 条回写术语表 |
| 2026-09-24 | 25-pool-hall（XXV Pool Hall / 二十五 台球厅） | done | 12 对块，check 通过（exit 0），无错配；台球厅少年江湖章，丹大叔乡土吹牛长篇、赌客史汀加里市井腔与报载讯息分档，黑人自称互称 nigger 作「黑汉子／老黑」，哈丽雅特循定名哈丽雅特·威廉斯，流浪汉歌与报摘保留 blockquote 分行，「也不是没有笑」点题句呼应书名；侧门普尔曼／咸狗儿／种马老黑等新术语 22 条回写术语表 |
| 2026-09-24 | 27-beware-of-women（XXVII Beware of Women / 二十七 当心女人） | done | 15 对块，check 通过（exit 0），无错配；少年情愫与世故告诫章，坦皮/斯梅德利先生标准硬腔与桑迪少年口语、吉米·莱恩茶房市井腔分档，坦皮口中 nigger 作「老黑」、桑迪负气 darky 作「老黑」，《生命之门》书名与 26 章章题对齐，歌谣「漫不经心的爱情」保留分行，场景分隔 --- 保留 1 处；新术语 12 条回写术语表 |
| 2026-09-24 | 29-elevator（XXIX Elevator / 二十九 电梯） | done | 6 对块，check 通过（exit 0），无错配；电梯男孩打工章（书末倒数第二章），桑迪内省独白与斯梅德利先生体面硬腔分档，斯梅德利内化贬语 nigger 循 23 章坦皮先例作「黑鬼」，黑格忆语乡土腔「俺」照旧，上——下劳作节奏与「一班跳舞的」叠句保留复沓，书末收束笔调；卢普区／黑人地带／L 高架电车／布雷斯特圣纳泽尔／香槟战区等新术语 11 条回写术语表 |
| 2026-09-24 | 28-chicago（XXVIII Chicago / 二十八 芝加哥） | done | 13 对块，check 通过（exit 0），无错配；北上芝加哥章（安吉家书 blockquote 落款保留、夜行列车、州街黑人地带初见），安吉书信平白口语、约翰逊姊妹乡土腔、坦皮标准硬腔、哈里斯先生市井腔、浅肤色怪客柔腻腔分档，桑迪内心照旧「俺」腔，场景分隔 --- 保留；高架电车／高架铁道循 29 章并行定名对齐；新术语 13 条回写术语表 |
| 2026-09-24 | 30-princess-of-the-blues（XXX Princess of the Blues / 三十 布鲁斯公主） | done | 14 对块，check 通过（exit 0），无错配；终章哈丽雅特归乡献唱与桑迪求学抉择收束章，哈丽雅特/比利市井演艺腔、安吉温软口语与桑迪少年腔分档，黑人自称 niggers 作「咱们黑人」、jigaboo 循 18 章作「老黑」，哈丽雅特唱段三支布鲁斯歌词（红太阳／小鸟儿／忧郁的早晨）保留 AAB 分行 blockquote，姊妹档嬷嬷歌与收束灵歌「等呀等呀，等到天亮的时候」保留分行，场景分隔 --- 保留 1 处；新术语 19 条回写术语表 |
| 2026-09-24 | 整书完结流转 | 30/30 done | 批次1直启：全书 30 章全部 check 通过；种族语汇按术语表分档（黑人互称/白人口中贬称/内化贬语三档），乡土腔「俺/娃儿/主啊」贯穿；并行撞名两起已裁定统一（Pletzky=普列茨基、《人生之门》）；删锁流转 |
