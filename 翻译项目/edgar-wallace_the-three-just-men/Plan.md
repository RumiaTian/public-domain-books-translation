# 翻译计划（Plan.md）

---

## 本计划信息

- **项目名称**：edgar-wallace_the-three-just-men（《三义士》，埃德加·华莱士）
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/小说文学.md
- **术语表**：术语表.md
- **执行模式**：委派（长篇，34 章，约 514KB；子代理逐章译，跨章连贯靠术语表+黄金样本+前章末尾补偿）

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
01-the-firm-of-oberzohn.md,18.3,todo
02-the-three-men-of-curzon-street.md,15.1,todo
...
```

| 字段 | 含义 | 取值 |
|------|------|------|
| `file` | 源文文件名（在 `原文/` 目录下） | 如 `01-the-firm-of-oberzohn.md` |
| `size_kb` | 源文大小（KB）。>50KB 为长文，按通用翻译引擎第七节分段 | 数字 |
| `status` | 翻译状态 | `todo` 待译 / `doing` 翻译中 / `done` 已完成 |

---

## 执行步骤（agent 按此推进，两种模式共用）

> **谁执行**由 `项目说明.md` 的「内容形态」字段决定：本项目为长篇→委派模式，子代理逐章执行本 9 步；主 agent 只当调度员（并发 ≤3）。

### 1. 读配置（每次翻译前必读）
```
1. 本项目 Plan.md（本文件）
2. 项目说明.md
3. 术语表.md
4. prompts/通用翻译引擎.md
5. prompts/领域配置/小说文学.md
6. 译文/ 下任意一篇已完成的 .zh-CN.md（风格黄金样本；无则跳过，
   风格基准可参照 ../edgar-wallace_the-four-just-men/译文/ 同系列已完成译篇）
```

### 2. 取任务
读 `translation_queue.csv`，取第一个 `status=todo` 的行。先 `ls 译文/` 检查该篇译文是否已存在：
- 已存在 → 直接改 `done`，跳到步骤 8。
- 不存在 → 把该行 `status` 改为 `doing` 并保存 CSV，继续。

### 3. 读源文
读 `原文/对应文件名`。

### 4. 翻译
产出到 `译文/对应文件名去.md加.zh-CN.md`。

- 逐块对照原文，绝不漏译、不合并段落、不缩写、不总结，尤其结尾别截断。
- 严守术语表：遇表内源词必译为指定译法。新词自行确定统一译法，首次附原文「中文（English）」。
- 人物/语气/风格全文一致，照黄金样本风格译。
- 长文（源文 >50KB）分段处理见通用翻译引擎第七节。

### 5. 自检
- 完整性：源文每一段都在译文 Original 块中出现，末尾无截断。
- 块对称：Original/Chinese 数量相等，每块内段数对应。
- 标题格式：全部「英文 / 中文」合并（罗马数字照搬，见项目说明备注）。
- 术语一致：抽查 5 个术语词，全文译法统一。

### 6. 自动检查
```
python scripts/check_bilingual.py 译文/对应篇名.zh-CN.md
```

### 7. 回填状态（双写）
`status` 从 `doing` 改 `done`，改两处：① 项目 `translation_queue.csv`；② 根 `translation_queue.csv` 对应行。

### 8. 追加日志
在本文件「运行日志」追加一行。

### 9. 循环
回到步骤 2，直到全部 `done`。

---

## 篇目清单

| # | 篇名 | 源文 | 大小 | 状态 |
|---|------|------|------|------|
| 1 | The Firm of Oberzohn | 01-the-firm-of-oberzohn.md | 18.3KB | todo |
| 2 | The Three Men of Curzon Street | 02-the-three-men-of-curzon-street.md | 15.1KB | todo |
| 3 | The Vendetta | 03-the-vendetta.md | 10.1KB | todo |
| 4 | The Snake Strikes | 04-the-snake-strikes.md | 9.6KB | todo |
| 5 | The Golden Woman | 05-the-golden-woman.md | 14.6KB | todo |
| 6 | In Chester Square | 06-in-chester-square.md | 14.1KB | todo |
| 7 | “Moral Suasion” | 07-moral-suasion.md | 12.6KB | todo |
| 8 | The House of Oberzohn | 08-the-house-of-oberzohn.md | 13.6KB | todo |
| 9 | Before the Lights Went Out | 09-before-the-lights-went-out.md | 5.3KB | todo |
| 10 | When the Lights Went Out | 10-when-the-lights-went-out.md | 12.7KB | todo |
| 11 | Gurther | 11-gurther.md | 9.3KB | todo |
| 12 | Leon Theorizes | 12-leon-theorizes.md | 15.5KB | todo |
| 13 | Mirabelle Goes Home | 13-mirabelle-goes-home.md | 14.1KB | todo |
| 14 | The Pedlar | 14-the-pedlar.md | 18.9KB | todo |
| 15 | Two “Accidents” | 15-two-accidents.md | 19.2KB | todo |
| 16 | Rath Hall | 16-rath-hall.md | 33.2KB | todo |
| 17 | Written in Braille | 17-written-in-braille.md | 14.1KB | todo |
| 18 | The Story of Mont d’Or | 18-the-story-of-mont-d-or.md | 13.0KB | todo |
| 19 | At Heavytree Farm | 19-at-heavytree-farm.md | 20.3KB | todo |
| 20 | Gurther Reports | 20-gurther-reports.md | 9.0KB | todo |
| 21 | The Account Book | 21-the-account-book.md | 18.8KB | todo |
| 22 | In the Store Cellar | 22-in-the-store-cellar.md | 12.0KB | todo |
| 23 | The Courier | 23-the-courier.md | 13.2KB | todo |
| 24 | On the Night Mail | 24-on-the-night-mail.md | 15.0KB | todo |
| 25 | Gurther Returns | 25-gurther-returns.md | 10.4KB | todo |
| 26 | In Captivity | 26-in-captivity.md | 15.8KB | todo |
| 27 | Mr. Newton’s Dilemma | 27-mr-newton-s-dilemma.md | 21.0KB | todo |
| 28 | At Frater’s | 28-at-frater-s.md | 8.6KB | todo |
| 29 | Work for Gurther | 29-work-for-gurther.md | 22.2KB | todo |
| 30 | Joan a Prisoner | 30-joan-a-prisoner.md | 20.7KB | todo |
| 31 | The Things in the Box | 31-the-things-in-the-box.md | 15.6KB | todo |
| 32 | The Search | 32-the-search.md | 17.5KB | todo |
| 33 | The Siege | 33-the-siege.md | 28.0KB | todo |
| 34 | The Death Tube | 34-the-death-tube.md | 3.1KB | todo |

> 注：表中大小为建项时快照，权威以 `translation_queue.csv` 为准。

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
| 2026-10-17 | 01-the-firm-of-oberzohn.md | done | 一次性子代理翻译（全书首译章），37 对块对照，check_bilingual 通过（退出码 0）。新增定名：Mrs. Carter=卡特太太、Orme Place=奥姆广场、Telford Park=特尔福德公园、Alington=阿灵顿、Bank of England=英格兰银行 |
| 2026-10-17 | 02-the-three-men-of-curzon-street.md | done | 一次性子代理翻译，30 对块对照，check_bilingual 通过（退出码 0）。新增定名：Benguella=本格拉号、Woerman=沃曼船、Petworth Hotel/Norfolk Street=佩特沃思旅馆/诺福克街、West Sussex=西萨塞克斯、Chancery judge=大法官法庭法官、Assistant Commissioner of Police=助理警务总监、empire desk=帝政式书桌、bushmen=布须曼人、Hun=德国佬、half a crown=半克朗、firewater=火酒 |
| 2026-10-17 | 03-the-vendetta.md | done | 一次性子代理翻译，23 对块对照，check_bilingual 通过（退出码 0）。新增定名：Adolph Oberzohn=阿道夫·欧伯佐恩、Lisa=丽莎、Puerto Rico=波多黎各、Café of the Seven Virtues=七美德咖啡馆、Prado=普拉多、Ascot=阿斯科特、Venezuela=委内瑞拉、Derby hat=圆顶硬礼帽、Ingenious creature=妙人儿 |
| 2026-10-17 | 04-the-snake-strikes.md | done | 一次性子代理翻译，16 对块对照，check_bilingual 通过（退出码 0）。新增定名：Joan Alice Murphy=琼·艾丽斯·墨菲、the Embankment=滨河大道、Blackfriars Bridge/Waterloo Bridge=黑修士桥/滑铁卢桥、Cleopatra's Needle=克娄巴特拉方尖碑、the Rolls=劳斯莱斯、green board=绿呢赌台、Children of the Law=律法之子们 |
| 2026-10-17 | 07-moral-suasion.md | done | 一次性子代理翻译，34 对块对照，check_bilingual 通过（退出码 0）。新增定名：Lisa Marthon=丽莎·马尔通 |
| 2026-10-17 | 05-the-golden-woman.md | done | 一次性子代理翻译，55 对块对照，check_bilingual 通过（退出码 0）。新增定名：Raymond=雷蒙德、Arbuthnot=阿巴思诺特、Gordon/Williams/Thompson/Elfred=戈登/威廉斯/汤普森/埃尔弗雷德、Johnny=约翰尼、Paddington=帕丁顿、St. Paul de Loanda=圣保罗-德-罗安达、Lobuo=洛布奥、Kalahari Desert=卡拉哈里沙漠、Congo=刚果河、Brightlingsea=布莱特灵西、Home Secretary/Home Office=内政大臣/内政部、bête=兽偶、vespa vulgaris=普通黄蜂、Jekyll and Hyde=吉基尔与海德、nine-thonged whip=九尾鞭、pistol automatic of precision=精密自动手枪 |
| 2026-10-17 | 06-in-chester-square.md | done | 一次性子代理翻译，28 对块对照，check_bilingual 通过（退出码 0）。新增定名：Minnie Gray=明妮·格雷、Benton=本顿、Belgravia=贝尔格莱维亚、Chester Gardens=切斯特花园、pierrette=皮埃罗特（女丑角）、domino=多米诺斗篷、Old Guard=老近卫军、American bar=美式酒吧 |
| 2026-10-17 | 09-before-the-lights-went-out.md | done | 一次性子代理翻译，23 对块对照，check_bilingual 通过（退出码 0）。新增定名：Lord Evington=埃文顿勋爵、Jim=吉姆、Mainz=美因茨、“Kulloo”=《库卢》 |
| 2026-10-17 | 08-the-house-of-oberzohn.md | done | 一次性子代理翻译，31 对块对照，check_bilingual 通过（退出码 0）。新增定名：Iwan Pfeiffer=伊万·法伊弗、Sven Gurther=斯文·格瑟、Frau Siedlitz=西德利茨太太、Grand Surrey Canal=萨里大运河、Altostadt=阿尔托施塔特、Corinthian Hall=科林斯大厅、Smyrna=士麦那、the Bronx=布朗克斯 |
| 2026-10-17 | 10-when-the-lights-went-out.md | done | 一次性子代理翻译，36 对块对照，check_bilingual 通过（退出码 0）。新增定名：Phillips=菲利普斯、Herr Fluen=弗卢恩先生、Seville=塞维利亚、Swindon=斯温登、Treasury(8877)=财政部、Child of the Snake=蛇之子、Herr Doktor=博士先生、Browning=勃朗宁手枪、莱昂西班牙语戏语（senorinetta=塞尼奥丽内塔、Raymondo mio=我的雷蒙多、muchos simpatico=极通人情） |
| 2026-10-17 | 11-gurther.md | done | 一次性子代理翻译，49 对块对照，check_bilingual 通过（退出码 0）。新增定名：Leskina=莱斯基纳、Poste Restante=留局待取、tantalus=带锁酒柜 |
| 2026-10-17 | 13-mirabelle-goes-home.md | done | 一次性子代理翻译，36 对块对照，check_bilingual 通过（退出码 0）。新增定名：Bishaka=比沙卡、Heavytree Lane=赫维特里巷、Professor Leicester=莱斯特教授（Braille 首现章注记补正为 13） |
| 2026-10-17 | 12-leon-theorizes.md | done | 一次性子代理翻译，26 对块对照，check_bilingual 通过（退出码 0）。新增定名：Chelmsford Prison=切姆斯福德监狱、Winchester Street=温彻斯特街、Bayswater Road=贝斯沃特路、Rowton House=罗顿宿舍、Port Nottosh=诺托什港、Natural History Syndicate=自然历史辛迪加、snake-proof=蛇毒不侵、'tigers'/notechis sentatus=虎蛇、viperidae crotalinae=照录不译 |
| 2026-10-17 | 14-the-pedlar.md | done | 一次性子代理翻译，74 对块对照，check_bilingual 通过（退出码 0）。新增定名：Mary=玛丽、Highcombe Road=海科姆路、the Ramon murder=拉蒙谋杀案 |
| 2026-10-17 | 15-two-accidents.md | done | 一次性子代理翻译，68 对块对照，check_bilingual 通过（退出码 0）。新增定名：Newbury=纽伯里、Oxford Street=牛津街、Dean Street=迪安街、Mr. Heinz=海因茨先生 |
| 2026-10-17 | 16-rath-hall.md | done | 一次性子代理翻译（长章 33.2KB），127 对块对照，check_bilingual 通过（退出码 0）。新增定名：Poole=普尔、Lawley=劳利、Beech Hotel=山毛榉旅馆、Cottage Hospital=乡村医院、Dr. Pinto Caillao=平托·卡亚奥、Gian Visconti=吉安·维斯孔蒂、charabanc=大游览车、Christmas cracker/bonbons=圣诞拉炮/拉炮糖、silencer=消音器、third/ninety-ninth degree=三级/九十九级审讯、Bokhara rug=布哈拉真丝地毯、Schweinhund与hein=照录不译、wax matches=蜡梗火柴、Zoological Gardens=动物园；另勘正 Rath Hall 词条说明（宅主为约翰逊·李） |
| 2026-10-17 | 19-at-heavytree-farm.md | done | 一次性子代理翻译，66 对块对照，check_bilingual 通过（退出码 0）。新增定名：Diego=迪亚戈、Gloucestershire=格洛斯特郡、Great West Road=大西路、Thames=泰晤士河、Wellingtons=威灵顿长靴、English Factory Act=英国《工厂法》、the Coast=「海岸」（西非沿岸）、gracious lady/ladies=雍容的小姐（们） |
| 2026-10-17 | 18-the-story-of-mont-d-or.md | done | 一次性子代理翻译，25 对块对照，check_bilingual 通过（退出码 0）。新增定名：Mont d’Or=蒙多尔山、Oxley=奥克斯利、Basutoland=巴苏陀兰、Thaba=塔巴、the Star Chief=「星酋」、Constable Kirk=柯克巡警 |
| 2026-10-17 | 17-written-in-braille.md | done | 一次性子代理翻译，38 对块对照，check_bilingual 通过（退出码 0）。新增定名：Mike Selwyn=迈克·塞尔温、Milan=米兰、Bureau of the Ministry of Colonies=里斯本殖民地部公署、Hue and Cry=《缉凶公报》、milreis=米尔雷斯、dago=拉丁佬、Illustrious Senhor=显赫的先生 |
| 2026-10-17 | 22-in-the-store-cellar.md | done | 一次性子代理翻译，22 对块对照，check_bilingual 通过（退出码 0）。新增定名：Heine=海涅、Bordeaux=波尔多、slush factory=假币作坊、lovely lady=美丽的小姐、the vital elixir=长生灵药 |
| 2026-10-17 | 20-gurther-reports.md | done | 一次性子代理翻译，32 对块对照，check_bilingual 通过（退出码 0）。新增定名：Liverpool=利物浦、Greenwich Registrar’s Office=格林尼治登记处、special licence=特别结婚许可证、box ottoman=箱式软凳、Nietzsche=尼采；Monte Doro 并入蒙多尔山、O. & S. 缩写同译 |
| 2026-10-17 | 21-the-account-book.md | done | 一次性子代理翻译，38 对块对照，check_bilingual 通过（退出码 0）。新增定名：Chiltern Hills=奇尔特恩丘陵、Chief Constable=郡警察总监、Mr. Liggins=里金斯先生、Marie=玛丽（里金斯之妹）、Hymar Pasha=希马尔帕夏、Gringo Club=格林戈俱乐部、East End=伦敦东区、君士坦丁堡/敖德萨、Aylesbury=艾尔斯伯里、Aix-la-Chapelle/Spa=亚琛/斯帕、en voiture=照录斜体首现括注、Unplausible Inventions=《难以置信的虚构集》 |
| 2026-10-17 | 25-gurther-returns.md | done | 一次性子代理翻译，23 对块对照，check_bilingual 通过（退出码 0）。新增定名：Eastbourne=伊斯特本 |
| 2026-10-17 | 24-on-the-night-mail.md | done | 一次性子代理翻译，19 对块对照，check_bilingual 通过（退出码 0）。新增定名：Deptford=德普特福德、St. Paul’s=圣保罗教堂、Newhaven/Dieppe=纽黑文/迪耶普、Croydon=克罗伊登、Redhill=雷德希尔、Horsham Junction=霍舍姆枢纽站 |
| 2026-10-17 | 23-the-courier.md | done | 一次性子代理翻译，22 对块对照，check_bilingual 通过（退出码 0）。新增定名：Clarke=克拉克、Senhor Alvaz Manuel y Cintra=阿尔瓦兹·曼努埃尔·伊·辛特拉先生、Regent Street=摄政街、Peckham=佩卡姆、Portlington Mews=波特林顿马厩巷、Lingfield=林菲尔德、Ituri=伊图里、Dover/Calais=多佛尔/加来、Valladolid=巴利亚多利德、Irun=伊伦、Sud Express=「南方快车」、blah=傻叨叨、rolled housewife=针线包、Portuguese mail=葡萄牙邮政列车（Newhaven/Dieppe 已由 24 章先行落盘，沿用） |
| 2026-10-18 | 28-at-frater-s.md | done | 一次性子代理翻译，24 对块对照，check_bilingual 通过（退出码 0）。新增定名：Shaftesbury Avenue=沙夫茨伯里大道、Cranbourn Street=克兰伯恩街、Charing Cross Road=查令十字路、Rupert Street=鲁珀特街、Fitzreeve Gardens=菲茨里夫花园、crumpet=烤面饼、knockers off=「敲车佬」 |
| 2026-10-18 | 26-in-captivity.md | done | 一次性子代理翻译，30 对块对照，check_bilingual 通过（退出码 0）。新增定名：Miguel Garcia=米格尔·加西亚、Tittlemouse=「小耗子」、Dennis=丹尼斯、Gare St. Lazare=圣拉扎尔车站、Piccadilly Circus=皮卡迪利广场、Cannon Row=坎农街、Victoria Dock Road=维多利亚船坞路、New Scotland Yard=新苏格兰场、Dartmoor=达特穆尔监狱、The Ringer=《敲钟人》、green baize box=绿呢箱子、ticket-of-leave man=领假释证的人、prompt side=提词侧 |
| 2026-10-18 | 27-mr-newton-s-dilemma.md | done | 一次性子代理翻译，60 对块对照，check_bilingual 通过（退出码 0）。新增定名：Baron Eruc Oberzohn=埃鲁克·欧伯佐恩男爵、Bermondsey=伯蒙德赛、the Baltic=波罗的海、chemin de fer/baccarat/banquo=「铁路」牌/巴卡拉/「班科」、mantrap=捕人铁夹、cheval de frise=碎玻璃拒马、tout=揽客的托儿 |
| 2026-10-18 | 31-the-things-in-the-box.md | done | 一次性子代理翻译，49 对块对照，check_bilingual 通过（退出码 0）。新增定名：Gott in himmel!=照录不译首现括注「上帝在天」（另补注 green baize box 词条第 31 章情节） |
| 2026-10-18 | 29-work-for-gurther.md | done | 一次性子代理翻译，71 对块对照，check_bilingual 通过（退出码 0）。新增定名：Regent’s Park/Outer Circle=摄政公园/外环道、Unter den Linden=菩提树下大街、Buenos Aires=布宜诺斯艾利斯、Lisle Street=莱尔街、Old Kent Road=老肯特路、Thames police=泰晤士河警察、the pedlar=货郎、linkman=执灯侍者、commissionaire=门警、joss-sticks=线香、water-gate=水门、gymnasium=文科中学、busy/nose=「大忙人」/「鼻子」、chef d’oeuvre=杰作 |
| 2026-10-18 | 30-joan-a-prisoner.md | done | 一次性子代理翻译，55 对块对照，check_bilingual 通过（退出码 0）。新增定名：Hartford, Connecticut=哈特福德（康涅狄格州）、Venice=威尼斯、busies=条子、Treasury bills=国库券、condemned cell=死囚牢、Junker=容克、Snaking=「放蛇」 |
| 2026-10-18 | 34-the-death-tube.md | done | 一次性子代理翻译（全书收官章），10 对块对照，check_bilingual 通过（退出码 0）。新增定名：无 |
| 2026-10-18 | 33-the-siege.md | done | 一次性子代理翻译（高潮长章 28KB），104 对块对照，check_bilingual 通过（退出码 0）。新增定名：Fleet Street=舰队街、the snake-room=蛇室、the Deputy Commissioner/the police chief=副警务总监/警察总监、Maxim gun=马克沁机枪、Mauser=毛瑟枪、mamba=曼巴（统称条）、fer-de-lance=矛头蛇（统一定名条） |
| 2026-10-18 | 32-the-search.md | done | 一次性子代理翻译，51 对块对照，check_bilingual 通过（退出码 0）。新增定名：the Quiet People=「安静的人们」、puff-adder=鼓腹蝰、Danish maid/Danish servant=丹麦女仆（统条）、letter-slit=投信口；Mauser 依 33 章先落盘定名对齐为「毛瑟枪」，fer-de-lance 条补第 32 章用例 |
| 2026-10-18 | 全书完结 | done | 《三义士》34/34 章全部完成（10-17 直启批次1 开册 01-25 章，10-18 完成 23 收编断点与 26-34 章），删除认领锁。全书高潮章 33 围攻 104 块对、长章 16 拉思府 127 块对均一次过检 |
