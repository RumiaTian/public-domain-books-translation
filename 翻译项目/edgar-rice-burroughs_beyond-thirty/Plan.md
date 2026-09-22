# Plan.md — edgar-rice-burroughs_beyond-thirty

## 本计划信息

- **项目名称**：edgar-rice-burroughs_beyond-thirty（《越过三十度》）
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
| `原文/*.md` | 源文（9 章） | 不改 |
| `译文/*.zh-CN.md` | 译文产出（块对照双语） | 翻译 agent 产出 |

---

## 篇目清单

| # | 章名 | 源文 | 大小 | 状态 |
|---|------|------|------|------|
| 1 | I | i.md | 33.5KB | todo |
| 2 | II | ii.md | 11.4KB | todo |
| 3 | III | iii.md | 18.2KB | done |
| 4 | IV | iv.md | 47.1KB | todo |
| 5 | V | v.md | 21.0KB | todo |
| 6 | VI | vi.md | 21.0KB | todo |
| 7 | VII | vii.md | 8.9KB | todo |
| 8 | VIII | viii.md | 24.1KB | todo |
| 9 | IX | ix.md | 20.4KB | todo |

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-08-16 | ii（11.4KB） | 通过（check_bilingual 退出码 0，11 对块，0 错配） | 委派模式首篇。术语表词全数沿用；新词：新英格兰（New England）、加拿大联邦诸州（Federated States of Canada）、德文郡（Devon）、条顿人（Teutons）。原文 para “It is treason, sir,” I replied 为原书笔误，按上下文改判斯奈德台词 |
| 2026-08-16 | iii（18.2KB） | 通过（check_bilingual 退出码 0，19 对块覆盖 78/78 段，0 错配） | 委派模式。Devon 从 ii 章对齐为「德文郡」；本章 East/West Camp 实为怀特岛格拉布列坦人两部落营地（非阿比西尼亚俘虏营），术语表说明已更正；新词已补入术语表：Solent、Bolt Head、Ryde、Newport、Hants、东营人/西营人、Felis tigris、Tigerland、软头弹/钢壳弹 |
| 2026-08-16 | i（33.5KB） | 通过（check_bilingual 退出码 0，35 对块覆盖 116/116 段，0 错配） | 委派模式。术语表词全数沿用（杰斐逊·特克、科尔德沃特号、空潜两用舰、重力屏发生器、死线等）；新词：圣约翰斯（St. Johns）、科伯恩（Coburn）、路劫匪（footpad）、无政府主义（anarchy）、武装商舰（merchantmen-of-war）、浮力发生器（buoyancy generators）、百慕大（Bermudas）。原文为数字形式处（30°/175°/1972/2116/SS-96/Q 138）保留阿拉伯数字并按中英混排加空格；本章无时代种族蔑称，无需归化处理 |
| 2026-08-16 | v（21.0KB） | 通过（check_bilingual 退出码 0，28 对块覆盖 94/94 段，0 错配） | 委派模式。术语表词全数沿用（薇克托莉、白金汉、汽艇、泰晤士河等）；新词已补入术语表：威斯敏斯特教堂（Westminster Abbey）、伦敦塔（the Tower）、伦敦桥（London Bridge）、坦布里奇韦尔斯（Tunbridge Wells）、菲利普爵士（Sir Phillip）、大瘟疫（the Death）；格雷/张伯伦/基奇纳/萧伯纳为对往昔伟人的悬想，首现附原文；残缺日记条目以「……」保真呈现断句；本章无时代种族蔑称 |
| 2026-08-16 | vi（21.0KB） | 通过（check_bilingual 退出码 0，17 对块覆盖 74/74 段，0 错配） | 委派模式。术语表词全数沿用（薇克托莉、德尔卡特、斯奈德、泰勒、三十六、白金汉、格拉布列坦、汽艇、科尔德沃特号等）；北海沿用 iii 章译法不加注；新词已补入术语表：奥斯坦德（Ostend）、科隆（Cologne）、易北河（Elbe）、赤鹿（red deer）、象乡（elephant country）、狮乡（lion country）；莱茵河、柏林为全书首现，附原文；本章无时代种族蔑称 |
| 2026-08-16 | iv（47.1KB） | 通过（check_bilingual 退出码 0，64 对块覆盖 210/210 段＋颂歌诗节，0 错配） | 委派模式，按§7分3段写入。术语表词全数沿用；新词首现附原文：里约（Rio）、圣迭戈（San Diego）、瓦尔帕莱索（Valparaiso）、伊里斯（Erith）、非洲象（*Elephas africanus*）、狮（*Felis leo*）、白金汉（Buckingham）、威廷（Wettin）、狮营（Camp of the Lions）、象乡（Elephant Country）、阿尔比恩（Albion）、玛丽（Mary）、薇克托莉（Victory）；薇克托莉之名于本章经玛丽之口首现。白金汉祷歌系《天佑吾王》之戏仿，译为颂歌体；时代种族用语无需归化处理 |
| 2026-08-16 | vii（8.9KB） | 通过（check_bilingual 退出码 0，8 对块覆盖 33/33 段，0 错配） | 委派模式。术语表词全数沿用（薇克托莉、斯奈德、泰勒、德尔卡特、格拉布列坦、汽艇、莱茵河等）；新词已补入术语表：火石火镰（flint and steel）；开篇死者即上章末遇害之三十六，依上下文译「死去的格拉布列坦人」；结尾黑脸士兵为阿比西尼亚军，faces as black as coal 按字面直译「黑得像煤」（描述性用语，非蔑称） |
| 2026-08-16 | viii（24.1KB） | 通过（check_bilingual 退出码 0，29 对块覆盖 86/86 段，0 错配） | 委派模式。术语表词全数沿用（薇克托莉、德尔卡特、泰勒、斯奈德、汽艇、格拉布列坦、阿比西尼亚、阿布·贝利克、梅内利克十四世、亚的斯亚贝巴、新贡达尔、柏林、黄种人等，专有名词首现附原文）；新词已补入术语表：菩提树下大街（Unter den Linden）、不列颠群岛、斯堪的纳维亚、贴身仆人（body servant）、白奴（white slave）；1916 年时代种族用语（negro 等）去蔑称归化为「黑人」或描述性译法 |
| 2026-08-16 | ix | 20.4KB | 0 | 全书收官。子代理两度触[1301]后第三次于落盘后总结被过滤，译文完整（19对块、0错配、末段齐全），主agent代校验双写done |
