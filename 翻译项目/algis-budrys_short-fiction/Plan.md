# 翻译计划（Plan.md）

---

## 本计划信息

- **项目名称**：algis-budrys_short-fiction（阿尔吉斯·巴德里斯短篇科幻小说集）
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
01-riya-s-foundling.md,16.1,todo
02-blood-on-my-jets.md,93.1,todo
...
```

| 字段 | 含义 | 取值 |
|------|------|------|
| `file` | 源文文件名（在 `原文/` 目录下） | 如 `01-riya-s-foundling.md` |
| `size_kb` | 源文大小（KB）。>50KB 为长文，按通用翻译引擎第七节分段 | 数字 |
| `status` | 翻译状态 | `todo` 待译 / `doing` 翻译中 / `done` 已完成 |

---

## 执行步骤（agent 按此推进，两种模式共用）

> 本项目**内容形态=短篇集**，**执行模式=委派**：主 agent 只当调度员，每篇的 9 步下沉到一次性子代理执行（子代理简报见 `WORKFLOW.md`）。9 步本身不变：

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

**双语对照格式、标记规则、完整性禁令**：见 `prompts/通用翻译引擎.md` 第五、六节。此处不重复。

**本流程专有提醒**：
- 逐块对照原文，绝不漏译、不合并段落、不缩写、不总结，尤其结尾别截断。
- 严守术语表：遇表内源词必译为指定译法。新词自行确定统一译法，首次附原文「中文（English）」。
- 人物/语气/风格全篇一致（文学类尤其重要），照黄金样本风格译。
- 长文（源文 >50KB，本项目中 02/05/06/08 四篇）分段处理见通用翻译引擎第七节。

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
结构契约满足则继续；有违规回步骤 4 修订。

### 7. 回填状态（双写）
检查通过后，`status` 从 `doing` 改 `done`，改两处：
- ① 项目 `translation_queue.csv` 该行；
- ② 根 `translation_queue.csv` 中 `<本项目名>,<本篇名>` 那一行。

### 8. 追加日志
在本文件「运行日志」追加一行。

### 9. 循环
回到步骤 2，取下一篇 `todo`，直到全部 `done`。委派模式下由主 agent 按调度循环派单。

---

## 篇目清单

| # | 篇名 | 源文 | 大小 | 状态 |
|---|------|------|------|------|
| 1 | Riya's Foundling（里娅的养子） | 01-riya-s-foundling.md | 16.1KB | todo |
| 2 | Blood on My Jets（我喷流上的血） | 02-blood-on-my-jets.md | 93.1KB | todo |
| 3 | Firegod（火神） | 03-firegod.md | 10.3KB | todo |
| 4 | Desire No More（欲求无多） | 04-desire-no-more.md | 28.8KB | todo |
| 5 | Citadel（堡垒） | 05-citadel.md | 52.0KB | todo |
| 6 | The Barbarians（蛮族） | 06-the-barbarians.md | 53.6KB | todo |
| 7 | The Stoker and the Stars（司炉与群星） | 07-the-stoker-and-the-stars.md | 22.9KB | todo |
| 8 | Wall of Crystal, Eye of Night（水晶之墙，夜之眼） | 08-wall-of-crystal-eye-of-night.md | 44.2KB | todo |
| 9 | The Rag and Bone Men（收破烂的人） | 09-the-rag-and-bone-men.md | 15.6KB | todo |
| 10 | Die, Shadow!（死吧，影子！） | 10-die-shadow.md | 36.2KB | todo |

（篇名中文为参考译名，最终以各篇译文标题为准。）

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-08-19 | 建项目 | - | 从待翻译/algis-budrys_short-fiction.epub 提取 10 篇短篇，领域=小说文学，形态=短篇集，模式=委派，粒度=块对照；术语表初版建立；原 epub 归档至 原书/ |
| 2026-09-16 | 03-firegod.md | done | Firegod/火神；14 对块覆盖 54+54 段，场景分隔符 3 处保留；check_bilingual 退出码 0；术语按表：德海·梅苏、托尔斯、火神梅苏、边陲（the Rim）、伪帝、银河护国公 |
| 2026-09-16 | 01-riya-s-foundling.md（里娅的养子） | done | 16.1KB，32 对块；check_bilingual 退出码 0；术语按表（菲尔迪/里娅·赛尔/考恩小姐/黎曼折叠/人族/战争孤儿安置农场），U.E.S./TT-34/B-72 照搬；字母口诀仿「X 者，……也」，词典条目/竖排词块照源文排版镜像 |
| 2026-09-16 | 02-blood-on-my-jets.md（我喷流上的血） | done | 93.1KB 超大篇，7 批分段（1-119/120-212/213-338/339-446/447-549/550-611/612-617）append-only 拼合；127 对块 580+580 段，原文块字节级一致（U+FEFF/U+200A/弯引号程序化保留）；信件 blockquote 行 > 前缀镜像；check_bilingual 仅 9 个罗马数字小节标题（### I~IX 照搬体例）警告，0 错配；术语按表（帕特/索斯滕/霍尔科姆/莫特·魏德曼/明/火箭街/法拉盛太空港/新上海/特兰索拉/火星佬/海峡），新增建议：Pat McKay 帕特·麦凯、Ash 阿什、D.O. 特派行动员、S.B.I./T.S.N./K class/T Class 照搬、Lou Foster 卢·福斯特、Kull 库尔、Seetee 西提、contraterrene 反物质 |
| 2026-09-16 | 04-desire-no-more.md（欲求无多） | done | 28.8KB，44 对块 196+196 段（题词块、诗歌 10 行骨架镜像原文排版），场景分隔符 --- 15 处双侧保留；原文块字节级一致（U+FEFF×56/U+200A×7 程序化提取自源文）；check_bilingual 退出码 0，0 错配 0 警告；术语按表（伊什（Isherwood）/马蒂/南/纳维恩/空间站），篇内专名首现附原文：霍华德·伊舍伍德、玛格丽特·伊舍伍德、戴夫、麦肯齐、大沼泽地（Everglades）；建议增补术语表：the Foo 福号、Vandenberg Cup 范登堡杯、Mark VII 马克七号、MacKenzie 麦肯齐 |
2026-09-16  05-citadel.md（Citadel/堡垒，52.0KB）翻译完成：3 批拼合 76 对块，check_bilingual 标记成对满足、数字锚点 0 误报，仅 9 个罗马数字章号（### I~IX）照搬触发标题警告（合法例外，见 prompts/质量校验与EPUB打包.md 判读表；与 02 体例一致）。
| 2026-09-16 | 07-the-stoker-and-the-stars.md（司炉与群星） | done | 22.9KB，23 对块（98 段正文+题诗 12 行，诗歌行骨架镜像原文排版），场景分隔符 --- 9 处双侧保留；原文块字节级一致（U+FEFF/U+200A/弯引号程序化提取自源文）；check_bilingual 退出码 0，0 错配 0 警告；术语按表（司炉/杰克人/拉德人/诺苏维人/丹尼尔斯/科普/「塞雷努斯号」/大战），篇内专名首现附原文：麦克雷迪（MacReidie）/麦克/贝克/半人马座/天狼星/半人马座阿尔法星/地球人；已增补术语表：MacReidie、Baker、Alpha Centaurus、Venus（金星号）、Marines、Merchant Marine |
| 2026-09-16 | 06-the-barbarians.md（蛮族） | done | 53.6KB 长篇，3 批（L1-60/L62-133/L135-212）append-only 拼合；46 对块 203+203 段，8 处场景分隔符照源文保留；原文块字节级一致（U+FEFF×79/U+200A×4 程序化提取自源文行）；check_bilingual 退出码 0（0 警告 0 错配，本篇无罗马小节题）；术语按表（朱利恩·杰弗里/杜格尔德/米卡/韦瑟比/蛮族将军/海滨联盟/小型坦克），首现附原文：霍德·萨维奇、哈罗德·杜格尔德、杰弗里翁、西姆·韦瑟比、主堡（Keep）；建议增补术语表：Hodd Savage 霍德·萨维奇、Harolde Dugald 哈罗德·杜格尔德、Geoffrion 杰弗里翁、Sime Weatherby 西姆·韦瑟比、Keep 主堡、trial by combat 决斗裁判、test of fitness 适者考验、mark 印记、intransigent tribesmen 不服王化的部落人 |
| 2026-09-16 | 09-the-rag-and-bone-men.md（收破烂的人） | done | 15.6KB，16 对块 60+60 段，4 处场景分隔符 --- 双侧保留；原文块字节级一致（U+FEFF×33/U+200A×2 程序化提取自源文行）；check_bilingual 退出码 0，0 错配 0 警告（本篇无罗马小节题）；术语按表（夏尔庞捷/毛雷尔/维尔德/基金会/沃尔多机械手/地球有机玻璃），首现附原文：罗切斯特明尼苏达生物物理设备公司、「伟大社会主义俄罗斯」凝聚器、布朗·博韦里、贝克顿-迪金森耶鲁；General Electric/I.B.M. 704 照搬；建议修订术语表：Veldish 形容词用法应译「维尔德式」（表中「维尔德语」仅适用语言语境，本篇 5 处均为形容词），建议增补：transporter 传送器 |
| 2026-09-16 | 10-die-shadow.md（死吧，影子！） | done | 36.2KB，33 对块 150+150 段，9 处场景分隔符 --- 双侧保留；原文块字节级一致（U+FEFF×110/U+200A×15 程序化提取自源文行）；check_bilingual 标记成对满足、数字锚点 0 错配，仅 4 个罗马数字小节题（### I~IV 照搬体例）警告（合法例外，与 02/05 体例一致）；术语按表（大卫·格里夫斯/「不屈号」/梅隆/阿黛莉/维吉尔/影族/埃克斯特罗姆博士/第一城/大殿/金星），首现附原文：坠毁救生舱（Crash Capsule）、连续统（continuum）、影族大殿（Shadow chamber）、影族神庙（Temple of Shadows）；本篇为全书末篇，10/10 完成 |
| 2026-09-16 | 08-wall-of-crystal-eye-of-night.md（水晶之墙，夜之眼） | done | 44.2KB，3 批（L1-56/L57-152/L153-272）append-only 拼合；66 对块 252+252 段，14 处场景分隔符 --- 照源文双侧保留；原文块字节级一致（U+FEFF×39/NBSP×55/U+200A×2 程序化提取自源文行）；check_bilingual 标记成对满足，仅 5 个罗马数字小节题（### I~V 照搬体例）警告（合法例外，与 02/05/10 体例一致）+1 处数字锚点误报（'98 Dinner→九八年宴会，中文数字改写属豁免类）；术语按表（鲁弗斯·索莱纳/厄明先生/科特赖特·伯尔/尤提利杰姆附简注/长岛设施/曼哈顿岛/特别公共关系办公室），首现附原文：贝丝·阿拉代斯（Bess Allardyce）、马尔科姆·勒维耶（Malcolm Levier）、阿伯纳西场（Abernathy Field）、阿雷西亚（Aresia）、环球电视网（Transworld TV Network）、国际广播业者协会、自由放任（laissez faire）；照搬不译：EmpaVid/E.V./I.A.B./S.P.R.O./TTV/火星不死术语境 Martian engineers→火星工程师；斜体 5 处逐处镜像（*不可能*/*自由放任*/*他们*/*究竟*/*这会儿*）；建议增补术语表：Bess Allardyce、Malcolm Levier、Abernathy Field、Aresia、Transworld TV Network、EmpaVid/E.V. 照搬、I.A.B./S.P.R.O. 照搬、Cort 科特（伯尔昵称） |

## 2026-09-16 完书收尾（主 Agent）

- **全书 10/10 done**（批次1直启·default-translator·c3，21:32–22:48 约 76 分钟，373KB 含两超大篇）。
- 93.1KB 超大篇 02-blood-on-my-jets 七批 append-only（127对块、580+580段字节全等、U+FEFF×175）；52KB 级 05/06、44KB 级 08 均分批攻坚成功。
- **罗马数字小节题照搬体例豁免裁定**（项目说明明文）：02/05/08/10 四篇退出码1均仅此豁免项，验收全过。
- Original 块字节保真硬约束全程生效（U+FEFF/U+200A/NBSP/U+2012/¼ 全等）；术语表 162→~180 行并发回填（代理自补 15 行+主 Agent 十八轮合并；Mac/Veldish 预置备注两处实证修正）。
- 认领锁已删除，流转完成。当晚批次1直启三连册收官。
