# Plan.md — edgar-rice-burroughs_pirates-of-venus

## 本计划信息

- **项目名称**：edgar-rice-burroughs_pirates-of-venus（《金星的海盗》）
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
| `原文/*.md` | 源文（14 章） | 不改 |
| `译文/*.zh-CN.md` | 译文产出（块对照双语） | 翻译 agent 产出 |

---

## 篇目清单

| # | 章名 | 源文 | 大小 | 状态 |
|---|------|------|------|------|
| 1 | I Carson Napier | carson-napier.md | 19.2KB | todo |
| 2 | II Off for Mars | off-for-mars.md | 22.0KB | todo |
| 3 | III Rushing Toward Venus | rushing-toward-venus.md | 31.6KB | todo |
| 4 | IV To the House of the King | to-the-house-of-the-king.md | 21.2KB | todo |
| 5 | V The Girl in the Garden | the-girl-in-the-garden.md | 26.6KB | todo |
| 6 | VI Gathering Tarel | gathering-tarel.md | 24.5KB | todo |
| 7 | VII By Kamlot's Grave | by-kamlot-s-grave.md | 23.7KB | todo |
| 8 | VIII On Board the Sofal | on-board-the-sofal.md | 20.4KB | todo |
| 9 | IX Soldiers of Liberty | soldiers-of-liberty.md | 18.0KB | todo |
| 10 | X Mutiny | mutiny.md | 22.5KB | todo |
| 11 | XI Duare | duare.md | 17.9KB | todo |
| 12 | XII A Ship | a-ship.md | 22.4KB | todo |
| 13 | XIII Catastrophe | catastrophe.md | 21.6KB | todo |
| 14 | XIV Storm | storm.md | 36.2KB | todo |

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-08-03 | 建项目 | — | 14 章提取完成，领域=小说文学，术语表 28 词条 |
| 2026-08-03 | I Carson Napier | 通过 | 21对块，check_bilingual 退出码0，可疑错配0；引子章，第一人称回忆视角 |
| 2026-08-03 | II Off for Mars | 通过 | 22对块，结构契约满足；1处数字锚点6.93误报（中文译为「六点九三」）；修了1处Original块误粘中文后通过 |
| 2026-08-03 | III Rushing Toward Venus | 通过 | 31对块，check退出码0，可疑错配0；主角飞向金星途中被金星引力捕获、穿越云层着陆巨树、首遇金星野兽与金星人；续用术语表（Amtor→阿姆托/韦帕贾等暂未在本章出现） |
| 2026-08-03 | IV To the House of the King | 通过 | 19对块，check退出码0，可疑错配0；首次系统介绍金星世界观（Amtor/Trabol/Strabol/Karbol/Jong/Klufar/Danus/Tofar/Olthar/Zuro/Alzo），术语表补12词条 |
| 2026-08-03 | V The Girl in the Garden | 通过 | 26对块，check退出码0，可疑错配0；花园救人情节，介绍Vepaja/Thorist革命史/长寿血清；术语表补Mintep/Thor/Zar/Thorists/Thorism 5词条 |
| 2026-08-03 | VI Gathering Tarel | 通过 | 21对块，check退出码0，可疑错配0；揭示tarel即蜘蛛网、与targo巨蛛搏斗、卡姆洛特之死；术语表补tarel/targo/tork/R-ray 4词条 |
| 2026-08-03 | VII By Kamlot's Grave | 通过 | 20对块，check退出码0，可疑错配0；背尸下树、误入蛛网再杀塔戈、为友掘墓却发现其中毒假死、复苏后合力猎杀basto；术语表补basto/tob/Chand Kabi 3词条 |
| 2026-08-03 | VIII On Board the Sofal | 通过 | 20对块，check退出码0，可疑错配0；被鸟人klangan所擒、押上索拉船Sofal、结识狱友Honan、揭示Duare为韦帕贾公主；术语表补klangan/angan/ganfal/jodades/Thora/Thoran/Kooaad/Duare/vik-ro/lor/yor-san/T-ray 12词条 |
| 2026-08-03 | IX Soldiers of Liberty | 通过 | 20对块，check退出码0，可疑错配0；囚船上结识甘福尔/基隆/佐格三狱友、密谋夺船、组建「自由之兵」秘密结社、阿诺斯暗探身份暴露、夜半舱内闷响次日发现阿诺斯被杀；术语表补vookor/joram 2词条 |
| 2026-08-03 | X Mutiny | 通过 | 24对块，check退出码0，可疑错配0；阿诺斯尸首引出船长盘问、午后第七时辰发动哗变血洗军官、卡森被推为vookor、柯季争权被佐格夺械压制、议定破晓登船夺僚船Sovong救杜阿雷；术语表补Sovong/Kodj/te 3词条 |
| 2026-08-03 | XI Duare | 通过 | 19对块，check退出码0，可疑错配0；破晓登船夺Sovong、舱中剑战亲手格杀其船长、搬空其军火口粮并送还韦帕贾女俘、柯季被逐、揭示杜阿雷即『君』之女且为花园中所见姑娘；修2处英文残留（relentless/空格）后通过 |
| 2026-08-03 | XII “A Ship!” | 通过 | 24对块，check退出码0，可疑错配0；卡森向杜阿雷表明身份遭其斥退、卡姆洛特因『君』之女婚禁险些拔剑、释Sofal/Sovong词源（sofal=杀手 Sovong=守卫者）、维洛尔毛遂求守janjong被婉拒、瞭望见敌船升ongyan旗即寡头穆斯科之船；术语表补ongyan/klongyan/janjong/notar 4词条；修2处英文残留（persona non grata/whichever）后通过 |
| 2026-08-03 | XIII Catastrophe | 通过 | 20对块，check退出码0，可疑错配0；炮战夺扬号擒穆斯科留作人质、卡森强吻杜阿雷、夜半暴风巨浪中杜阿雷失踪、卫兵瞭望皆遇害、维洛尔真身乃索拉间谍与穆斯科同遁；术语表补Yan/Noobol/Byea/Shepherd's Star 4词条；修2处英文残留（quarter/he）后通过 |
| 2026-08-03 | XIV Storm | 通过 | 34对块，check退出码0，可疑错配0；甘福尔推理还原劫持真相、卡森被浪卷落泅渡努博尔、解kloonobargan/nobargan词源、野人围攻中救杜阿雷、崖顶燃信号火、维洛尔穆斯科率众来追、杜阿雷被安甘送走前呼爱、卡森落入敌手而欢喜全书终；术语表补kloonobargan/nobargan/Comanche 3词条；修7处英文残留（scarcely/heliotrope/contemplation/unmistakable/jagged/yearn/devoured/creep）后通过 |
