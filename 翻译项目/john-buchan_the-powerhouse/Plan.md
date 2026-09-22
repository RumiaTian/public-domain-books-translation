# 翻译计划（动力室）

## 本计划信息

- **项目名称**：动力室（约翰·巴肯，The Power-House）
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

## translation_queue.csv 格式

```
file,size_kb,status
chapter-1.md,14.7,todo
chapter-2.md,18.5,todo
...
```

| 字段 | 含义 | 取值 |
|------|------|------|
| `file` | 源文文件名（在 `原文/` 目录下） | 如 `chapter-1.md` |
| `size_kb` | 源文大小（KB）。>50KB 为长文，按通用翻译引擎第七节分段 | 数字 |
| `status` | 翻译状态 | `todo` 待译 / `doing` 翻译中 / `done` 已完成 |

## 执行步骤

按 `prompts/翻译计划模板.md`「执行步骤」9 步推进（读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志）。本项目为中篇，执行模式为连续，由主 agent 在自身上下文内逐篇执行。

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
| 2026-08-13 | chapter-1 | 14.7KB / 退出码 1 | 数字锚点误报（"at 11"→"十一点"），结构契约全满足；术语依表，黄金样本缺（prologue 未落盘）据术语表+配置确立风格 |
| 2026-08-13 | prologue | 2.2KB / 退出码 0 | 编者序框架故事，全书首篇；确立爱德华绅士口吻与术语基线，作为后续黄金样本；新增 Monte Carlo=蒙特卡洛 |
| 2026-08-13 | chapter-2 | 18.5KB / 退出码 1 | 数字锚点误报（"11 a.m."→"上午十一点"，同 chapter-1），结构契约全满足（29 对块）；术语依表，衔接 chapter-1 末尾（汤米赴莫斯科）；新词附原文：Julius Pavia=朱利厄斯·帕维亚、Tuke=图克、White Lodge=白屋、the Albany=奥尔巴尼、Athenaeum=雅典娜神庙俱乐部、Old Wedgwood=老韦奇伍德瓷器、Jenkinson=詹金森、Bokhara=布哈拉 等 |
| 2026-08-13 | chapter-4 | 23.1KB / 退出码 0 | 结构契约全满足（54 对块，0 处可疑错配）；术语依表并衔接前篇（Tuke=图克、White Lodge=白屋、the Albany=奥尔巴尼、Bokhara=布哈拉、Pavia=帕维亚）；日期序数词（27th/15th/2nd/10th 等）与 9:30 已妥善处理、未触发数字锚点误报；新词附原文：Felix=费利克斯、Macgillivray=麦克吉利夫雷、Routh=劳思、Saronov=萨罗诺夫、Twilight of Civilisation=《文明的暮色》、the Powerhouse=动力室、Old Bailey=老贝利、the Northeastern circuit=东北巡回法庭、bucket-shop=投机经纪行、bearer-bonds case=不记名债券案、Pamirski Post=帕米尔斯基哨所、Hissar range=希萨尔山脉、Oxus=阿姆河、Turkestan=突厥斯坦 等 |
| 2026-08-13 | chapter-3 | 30.1KB / 退出码 1 | 结构契约全满足（64 对块，标题合并满足）；退出码 1 仅数字锚点误报（"'95 Perrier-Jouet"→"九五年的佩里耶-茹埃"，中文数字），核验后可接受；分 2 段写入同一文件（Write+追加合并，UTF-8 无 BOM）；衔接前篇并揭示核心意象——本章为反派安德鲁·拉姆利（Andrew Lumley）首度正面上场、"powerhouse/动力室"概念首次得名；术语依表并衔接 chapter-2/4（Lumley=拉姆利、Pavia=帕维亚、Bokhara=布哈拉、Scotland Yard=苏格兰场、the Bar=律师界）；新词附原文：Stagg=斯塔格、High Ashes=海艾什斯、Knowles=诺尔斯、Elliman=埃利曼（药油）、Raeburn=雷伯恩、Perrier-Jouet=佩里耶-茹埃、Madeira=马德拉酒、Hapsburg=哈布斯堡、Saturn=萨图恩、Tyrol=蒂罗尔、Nietzschean=尼采派、the Romanovs=罗曼诺夫王朝、Whitsuntide=圣灵降临节 等 |
| 2026-08-13 | chapter-7 | 22.3KB / 退出码 1 | 结构契约全满足（47 对块，标题合并满足）；退出码 1 仅数字锚点误报（"9:30"→"九点半"，中文时间表达，2 处），核验后可接受；chapter-6 尚未落盘，以 chapter-1 黄金样本确立风格；本章为利思滕携证据在伦敦街头遭"动力室"全程追杀、最终遁入俄罗斯大使馆寻得避难所的高潮逃亡段；术语依表并衔接前篇（Lumley=拉姆利、Pavia=帕维亚、Saronov=萨罗诺夫、Tuke=图克、Felix=费利克斯、Macgillivray=麦克吉利夫雷、Chapman=查普曼、Pitt-Heron=皮特-赫伦、the Powerhouse=动力室、Scotland Yard=苏格兰场、the Temple=律师学院区、Down Street=唐街）；新词附原文：Waters=沃特斯、Stagg=斯塔格、Levison=莱维森、Hewins=休因斯、Alphonse=阿尔丰斯（主厨）、Antioch Street=安提阿街、St. Thomas's Hospital=圣托马斯医院、Whitehall=白厅、Piccadilly=皮卡迪利、Belgrave Square=贝尔格雷夫广场、Bayswater=贝斯沃特、Hyde Park Corner=海德公园角、Green Park=绿园、Grosvenor Gate/Place=格罗夫纳门/坊、Hamilton Place=汉密尔顿坊、Park Lane=公园巷、the Edgeware Road=埃奇韦尔路、Marylebone Road=马里波恩路、Harrow=哈罗、Brentford=布伦特福德、Kensington=肯辛顿、Edgeley Street=埃奇利街、Connaught Mews=康诺特马厩巷、the Albany=奥尔巴尼公寓、the Bachelors' Club=单身汉俱乐部、Modder River=莫德尔河、Exmoor=埃克斯穆尔、the Metropolitan force=伦敦警察厅；法语对白（含 *Messieurs les assassins*）依叙事提示译为中文、斜体法语保留原文并括注 |
| 2026-08-13 | chapter-5 | 19.0KB / 退出码 0 | 结构契约全满足（37 对块，0 处可疑错配）；术语依表并衔接前篇（Lumley=拉姆利、Chapman=查普曼、Tuke=图克、Saronov=萨罗诺夫、Felix=费利克斯、Macgillivray=麦克吉利夫雷、Routh=劳思、the Powerhouse=动力室、Bokhara=布哈拉、Oxus=阿姆河、the Albany=奥尔巴尼、Down Street=唐街、the Temple=律师学院区、Scotland Yard=苏格兰场）；本章为利思滕招揽查普曼同住、并通过麦克吉利夫雷揭示德文 *Krafthaus*（=动力室）之欧洲渊源，结尾在政治宴会上再遇拉姆利、隔桌对峙；查普曼的约克郡劳工口吻与俚语（topper/give it them hot and strong/stir its stumps 等）已口语化处理；新词附原文：Josiah Routh=约西亚·劳思（全名）、Waters=沃特斯、Hilderstein=希尔德斯坦、East Claygate=东克莱盖特、Higgins=希金斯、Wattles=沃特尔斯、Parnell=帕内尔、Sheffield=谢菲尔德、Hyde Park=海德公园、Bloomsbury=布卢姆斯伯里、Piccadilly=皮卡迪利、Regent Street=摄政街、Jermyn Street=杰明街、Samarkand=撒马尔罕、the Strand=河滨大道、House of Lords=上议院、Court of Appeal=上诉法院、Legion of Honour=荣誉军团勋章、Lord Morecambe=莫克姆勋爵、Undersecretary=副国务大臣、Professor M——=M——教授、Jena=耶拿、Antwerp=安特卫普、loess=黄土、nullahs=干沟 等 |
| 2026-08-13 | chapter-8 | 16.0KB / 退出码 0 | 结构契约全满足（22 对块，0 处可疑错配）；全书高潮对峙章——利思滕赴奥尔巴尼公寓与拉姆利正面交锋、拉姆利哲学式反派独白；术语依表并衔接 chapter-7（Lumley=拉姆利、Pavia=帕维亚、Saronov=萨罗诺夫、Tuke=图克、Felix=费利克斯、Macgillivray=麦克吉利夫雷、Chapman=查普曼、Pitt-Heron=皮特-赫伦、Tommy=汤米、the Powerhouse=动力室、Scotland Yard=苏格兰场、the English Bar=英国律师界、Labour Member=工党议员、House of Commons=下议院、the Albany=奥尔巴尼公寓、Antioch Street=安提阿街、Belgrave Square=贝尔格雷夫广场、Green Park=绿园、Piccadilly=皮卡迪利）；新词附原文：Constitution Hill=宪法山、Devonshire House=德文郡大厦、rococo=洛可可式、late Georgian=乔治时代晚期、bibliophile=藏书家、vellum=犊皮纸、morocco=摩洛哥皮、Viceroys=总督们、Cabinet Ministers=内阁大臣、the Machine=机器、métier=本行、the Zeus of Pheidias=菲狄亚斯的宙斯神像、Aldines=阿尔丁版本书、James=詹姆斯（仆名）、Westminster Bridge=威斯敏斯特桥、Capitalism=资本主义 |
| 2026-08-13 | chapter-9 | 5.7KB / 退出码 0 | 结构契约全满足（8 对块，0 处可疑错配）；终章——拉姆利"心脏病猝逝"神话落幕、葬礼盛况、皮特-赫伦归家、智利仲裁案后与汤米重逢并完成全书反转收尾；与 chapter-1「野鹅追踪之始」首尾呼应（标题"野鹅归来"）；术语依表并衔接前篇（Lumley=拉姆利、Pitt-Heron/Ethel=皮特-赫伦/埃塞尔、Macgillivray=麦克吉利夫雷、Chapman=查普曼、Felix=费利克斯、Tommy=汤米、Scotland Yard=苏格兰场、the Powerhouse=动力室、Portman Square=波特曼广场、the Temple=律师学院区、West Ham=西汉姆、the Chilean Arbitration=智利仲裁案、De mortuis=De mortuis（死者为大））；新词附原文：The Times=《泰晤士报》、Beckford=贝克福德、Atticus=阿提库斯、Maecenas=梅塞纳斯、Lord Houghton=霍顿勋爵、Morning Post=《晨邮报》、Arabian Nights=《天方夜谭》、Fenimore Cooper=芬尼莫尔·库珀、moss-troopers=边境马贼、Eternity=永恒。全书 10 篇全部译完（连续模式主 agent 直译） |
