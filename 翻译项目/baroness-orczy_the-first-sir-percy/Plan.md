# 翻译计划

---

## 本计划信息

- **项目名称**：baroness-orczy_the-first-sir-percy（第一代珀西爵士 / The First Sir Percy）
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
01-a-night-on-the-veluwe.md,49.9,todo
02-the-double-wedding.md,54.5,todo
...
```

| 字段 | 含义 | 取值 |
|------|------|------|
| `file` | 源文文件名（在 `原文/` 目录下） | 带两位序号前缀，序号=阅读顺序 |
| `size_kb` | 源文大小（KB）。>50KB 为长文，按通用翻译引擎第七节分段 | 数字 |
| `status` | 翻译状态 | `todo` 待译 / `doing` 翻译中 / `done` 已完成 |

---

## 执行步骤（agent 按此推进，两种模式共用）

> **谁执行**由 `项目说明.md` 的「内容形态」字段决定（见 `WORKFLOW.md`「判断内容形态」）：本项目为长篇 → 委派模式，由子代理逐篇执行本流程。无论谁执行，这 9 步不变。

### 1. 读配置（每次翻译前必读）
```
1. 本项目 Plan.md（本文件）
2. 项目说明.md
3. 术语表.md（如无则跳过）
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
- 长文（源文 >50KB）分段处理见通用翻译引擎第七节。本书 02、14 章超 50KB。
- 章内小节罗马数字（### I / ### II…）照搬不译；章题照术语表译法。

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

| # | 篇名（源文文件） | 大小 | 状态 |
|---|------|------|------|
| 1 | 01-a-night-on-the-veluwe.md | 49.9KB | done |
| 2 | 02-the-double-wedding.md | 54.5KB | todo |
| 3 | 03-the-great-interruption.md | 43.4KB | todo |
| 4 | 04-adder-s-fork.md | 20.4KB | todo |
| 5 | 05-a-race-for-life.md | 10.3KB | todo |
| 6 | 06-a-nest-of-scorpions.md | 40.7KB | todo |
| 7 | 07-a-subtle-traitor.md | 18.7KB | todo |
| 8 | 08-devil-s-writ.md | 29.9KB | todo |
| 9 | 09-mala-fides.md | 34.8KB | todo |
| 10 | 10-a-prince-of-darkness.md | 38.8KB | todo |
| 11 | 11-the-danger-spoke.md | 23.9KB | todo |
| 12 | 12-tears-sighs-hearts.md | 18.4KB | todo |
| 13 | 13-the-stygian-creek.md | 18.6KB | todo |
| 14 | 14-treachery.md | 60.8KB | todo |
| 15 | 15-the-molen-on-the-veluwe.md | 38.3KB | todo |
| 16 | 16-the-final-issue.md | 13.2KB | todo |
| 17 | 17-the-only-world.md | 3.0KB | todo |

（权威队列以 `translation_queue.csv` 为准）

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-10-15 | 01-a-night-on-the-veluwe.md | done（44 对双语块，222 段全覆盖，check_bilingual 退出码 0） | 全书首译章，无黄金样本；新增专名已补入术语表（奥尔登巴内费尔特、格勒内费尔德、瓦尔堡·德·马尔尼克斯、热拉尔、沉默者威廉、弗朗西斯·博尔吉亚、切萨雷、阿珀尔多伦、阿塞尔、朗瑟伦、多斯堡、克莱沃、伊森堡、「鸦巢」客栈）及荷兰咒骂语固定译法（dondersteen=该死、verdommt=见鬼、verfloekte=该死的、plepshurk=蠢货） |
| 2026-10-15 | 02-the-double-wedding.md | done | 54.5KB 分 7 段翻译拼合；60 对块、164 段全量对照，check_bilingual 退出码 0；新词已补入术语表（哈勒姆、科佩尔门、克拉斯等） |
| 2026-10-15 | 04-adder-s-fork.md | done（25 对双语块，88 段全覆盖，check_bilingual 退出码 0） | 新增专名：德·凯泽雷（De Keysere，驻瓦赫宁恩将领）已补入术语表；科佩尔门、科尔特运河街沿用第 2 章译法 |
| 2026-10-15 | 05-a-race-for-life.md | done（6 对双语块，16 段全覆盖，check_bilingual 退出码 0） | 章题译「生死竞逐」，小节标题沿第 2 章格式（### I / 一）；新词已补入术语表（迪伦、布吕门、亨格尔斯）；Hengles 拼写已对照 EPUB 原书核实；De Keysere 沿第 4 章定名「德·凯泽雷」 |
| 2026-10-15 | 03-the-great-interruption.md | done（32 对双语块，163 段全覆盖，check_bilingual 退出码 0） | 章题译「盛大的中断」；43.4KB 分段翻译后拼合为完整单文件；小节标题沿第 2 章格式（### I / 一）；新词已补入术语表（赖斯韦克、布龙克霍斯特、斯皮诺拉、弗雷德里克、德伦特、维金纳琴、行营总管、海市蜃楼等）；De Keysere 沿第 4 章「德·凯泽雷」、St. Bavon 沿第 2 章「圣巴沃」、Lang Soeren 沿第 1 章「朗瑟伦」、Doesburg 沿第 1 章「多斯堡」、plepshurk 沿第 1 章「蠢货」 |
| 2026-10-15 | 06-a-nest-of-scorpions.md | done（35 对双语块，127 段全覆盖，check_bilingual 退出码 0） | 章题译「蝎巢」；40.7KB 按自然场景分 7 节、35 块拼合为完整单文件；小节标题沿（### I / 一）格式；新词已补入术语表（范·艾特泽马、德·福赫特、《国家事务》、蒂伦豪特、奥斯坦德、阿姆斯特丹、圣约里斯门、新门、安东、mejuffrouw=小姐、burgomaster=市长、my lord=大人/我大人、市镇传令官、tête baissée）；Messire 沿第 5 章「马凯老爷」、Isembourg/Kleve 沿第 1 章「伊森堡/克莱沃」、Spinola 沿第 3 章「斯皮诺拉」、里格沿第 5 章；执政 27 处、阿默斯福特 11 处等术语全文一致 |
| 2026-10-15 | 07-a-subtle-traitor.md | done（26 对双语块，81 段全覆盖，check_bilingual 退出码 0） | 章题译「阴险的叛徒」；吉尔达/贝雷斯坦老爷称夫君为「大人/我大人」（沿第 4、6 章定名，第 3 章婚前「夫君」不复用）；新词已补入术语表（奥兰治亲王、阿尔瓦、贝亨奥普佐姆、代尔夫特、《书简》）；De Voocht、mejuffrouw、burgomaster 与第 6 章新增条目一致 |
| 2026-10-15 | 08-devil-s-writ.md | done（27 对双语块，119 段全覆盖，check_bilingual 退出码 0） | 章题沿术语表「魔鬼手书（Devil's-Writ）」；29.9KB 分 3 片翻译后拼合为完整单文件；小节标题沿（### I / 一）格式；新词已补入术语表（弗里塞街、大市场、约里斯大道、旧街、poort/markt 括注、该隐、殿下、哨探、麦酒）；执政/殿下、码头、哲人、麦酒、哨探沿前章定名；March 21 数字锚点保留（3 月 21 日） |
| 2026-10-15 | 10-a-prince-of-darkness.md | done（32 对双语块，144 段全覆盖，check_bilingual 退出码 0） | 章题译「黑暗亲王」；38.8KB 分 3 片翻译后拼合为完整单文件；小节标题沿（### I / 一）格式；新词已补入术语表（马利讷、根特、阿维尔努斯、首席大议长、荷兰语昵称 myn engel/myn schat/myn Geliefde、fair one=美人儿、吉尔达称斯托滕贝格 my lord=勋爵大人）；吉尔达称夫君 my lord 沿第 4、6 章「大人」；执政 7 处、斯托滕贝格 22 处、阿默斯福特 6 处等术语全文一致；原文 144 段逐段经程序校验与译文块一一对应 |
| 2026-10-15 | 09-mala-fides.md | done（48 对双语块，127 段全覆盖，check_bilingual 退出码 0） | 章题沿术语表「背信（Mala Fides）」作「IX 背信」；34.9KB 按 7 节分 3 片翻译后拼合为完整单文件；小节标题沿（### I / 一）格式；原文段（含章内 --- 分隔线）经程序逐段校验与源文完全一致（FEFF/NBSP 等不可见字符保留）；新词已补入术语表（别西卜、马尔尼克斯·德·圣阿尔德贡德、his/your Magnificence=大人阁下、Sovereign Liege Lady=宗主女主、equerry=侍从武官补录）；奥尔登巴内费尔特沿第 1 章定名（弃第 2 章变体）、博尔吉亚沿第 1 章、「笑面骑士」沿第 2 章人名用法、jongejuffrouw=小姐沿第 4 章、尼古拉斯为吉尔达之兄沿第 2/6 章 |
| 2026-10-15 | 11-the-danger-spoke.md | done（29 对双语块，112 段全覆盖，check_bilingual 退出码 0） | 章题译「祸辐」（The Danger-Spoke）；小节标题沿（### I / 一）格式；Magnificence 沿第 9 章「大人阁下」、my lord/your lordship（第欧根尼称斯托滕贝格）沿第 10 章「勋爵大人」、Liege Lady 沿第 9 章「宗主女主」；新词已补入术语表（驯悍记、威廉·莎士比亚、彼特鲁乔、smeerlap=龌龊货、Peter/Willem、Franz Hals 拼写注；别西卜沿第 9 章）；执政、斯托滕贝格勋爵、克拉斯、jongejuffrouw=小姐 沿前章定名 |
| 2026-10-15 | 13-the-stygian-creek.md | done（15 对双语块，50 段全覆盖，check_bilingual 退出码 0） | 章题沿术语表「冥河之溪（The Stygian Creek）」；18.6KB 单次直出完整单文件；小节标题沿（### I / 一）格式；原文 50 段经程序逐段校验与源文完全一致（FEFF 噪声字符按前章惯例剔除）；smeerlap 沿第 11 章定名「龌龊货」（首现章定名，弃本稿初译「油滑无赖」）、Petruchio 沿第 11 章「彼特鲁乔」、Magnificence 沿第 9 章「大人阁下」、my lord（吉尔达/市长称斯托滕贝格）沿第 10 章「勋爵大人」、mynheer=老爷沿第 2 章、Koppel-poort 沿第 2 章「科佩尔门」、麦酒沿第 8 章；新词已补入术语表（myn geloof=我的信仰、The Oille=奥伊大炖羹、Gehenna=地狱、Cornucopia of Fate=命运的丰饶角、腓力四世国王、Sblood=见鬼、au revoir 括注） |
| 2026-10-15 | 12-tears-sighs-hearts.md | done（15 对双语块，61 段全覆盖，check_bilingual 退出码 0） | 章题译「眼泪、叹息与心」；小节标题沿（### I / 一）格式；吉尔达/市长称斯托滕贝格 my lord=勋爵大人 沿第 4/10 章定名；mynheer=老爷 沿第 2/11 章；mejuffrouw/jongejuffrouw=小姐、Magnificence=大人阁下、myn engel=我的天使、plepshurk=蠢货、fair one=美人儿、varlet=恶棍、rogue/knave=无赖 均沿前章定名；新词已补入术语表（*myn chat*=我的宝贝（myn schat 变体拼写）、Heer Burgomaster=市长大人、笑面骑士指人不用书名号沿第 9 章）；原文 61 段经程序逐段校验与源文完全一致（含 FEFF 不可见字符保留） |
| 2026-10-15 | 16-the-final-issue.md | done（12 对双语块，33 段全覆盖，check_bilingual 退出码 0） | 章题译「最终结局」；13.2KB 单次直出完整单文件；小节标题沿（### I / 一）格式；斯托滕贝格勋爵/勋爵大人沿第 10-13 章定名、执政/殿下/哨探/里格/雇佣冒险家/《国家事务》/范·艾特泽马/德·凯泽雷/伊森堡/克莱沃沿前章定名；molen=磨坊沿第 15 章；「Beresteyn's encampment」经 EPUB 原书核实非讹误（第 15 章明载峡谷大营由尼古拉斯·贝雷斯坦统率），照实译「贝雷斯坦营地」；新词已补入术语表（库尔讷、雷嫩、多伦/莱茵河/阿珀尔多伦补录、justiciary=执法者） |
| 2026-10-15 | 15-the-molen-on-the-veluwe.md | done（35 对双语块，125 段全覆盖，check_bilingual 退出码 0） | 章题译「费吕韦的磨坊」（molen 沿术语表）；38.3KB 按 7 自然节、35 块（3-6 段一组）拼合为完整单文件；小节标题沿（### I / 一）格式；原文 125 段程序化自源文逐字提取（FEFF 噪声按前章惯例剔除）并程序校验与源文完全一致；德·福赫特《书简》沿第 6/7 章、myn engel/myn schat/myn geliefde 沿第 10 章（斜体复现首现括注）、《驯悍记》沿第 11 章、plepshurk=蠢货沿第 1 章、smeerlap=龌龊货沿第 11 章、Koppel-poort=科佩尔门沿第 13 章、哨探沿第 5/8 章、Magnificence=大人阁下沿第 9 章、my lord=勋爵大人（吉尔达称斯托滕贝格）沿第 10 章、mejuffrouw/jongejuffrouw=小姐沿第 4/6 章、Heer Burgomaster=市长大人沿第 12 章新增条目（本稿一处已回改）、德·贝格、赖斯韦克、须德海、巴讷费尔德沿前章定名；新词已补入术语表（A moi=来人啊、By my halidame=我的圣徒在上、runnion=胖无赖、Nemesis=复仇女神涅墨西斯、termagant=小泼妇、game of hazard=掷骰子赌戏） |
| 2026-10-15 | 17-the-only-world.md | done（4 对双语块，10 段全覆盖，check_bilingual 退出码 0） | 章题译「唯一的世界」（全书终章，与末句「除了爱的世界，这世上还有别的世界」收束呼应）；3.0KB 终章短章单次直出完整单文件；小节标题沿（### I / 一）格式；原文 10 段程序化自源文逐字提取（FEFF 不可见字符按第 16 章惯例原样保留）并程序校验 byte-exact；磨坊（molen）沿第 15 章、费吕韦/吉尔达/玛丽亚/第欧根尼沿前章定名（本章程内首现附原文括注沿黄金样本惯例）；his lordship（玛丽亚口中斯托滕贝格，咒曰「愿上帝惩罚他」）沿第 10 章「勋爵大人」；无新词，术语表无需增补 |
| 2026-10-15 | 14-treachery.md | done（55 对双语块，268 段全覆盖，check_bilingual 退出码 0） | 章题译「变节」（Treachery）；60.8KB 全书最大章，按 8 自然节分 8 片翻译、55 块（1-8 段一组）拼合为完整单文件；小节标题沿（### I / 一）格式；原文 268 段程序化自源文逐字提取（含 FEFF 不可见字符原样保留）并程序校验逐行连续无缺漏；varlet=恶棍沿第 12/13/15 章多数派定名（本稿初译「无赖坯子」已全部回改并补录术语表）、Heer Burgomaster=市长大人沿第 12 章（初译「市长老爷」已回改）、justiciary=执法者沿第 16 章、Laughing Cavalier 指人不用书名号沿第 9/12 章、Magnificence=大人阁下沿第 9 章、my lord=勋爵大人沿第 10 章、his lordship 叙述=他大人沿第 13 章、Koppel-poort=科佩尔门沿第 13 章、哨探/行营总管/殿下/里格沿前章定名；新词已补入术语表（皮特·瓦勒伦、波尔图酒、Odd's fish=嗬见鬼、English milor=英国爵爷、David's sow=大卫的母猪、muckworm=蛆虫、varlet 补录；molen 条目说明更新为首现第 1 章） |
2026-10-15 | 🎉全书完书 | 17/17 done（本日批次1开册并全部译完，含 60.8KB 最大章14与 54.5KB 章节02）；术语表由各章随译随补累计成型
