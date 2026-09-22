# Plan.md — edgar-saltus_the-perfume-of-eros

## 本计划信息

- **项目名称**：edgar-saltus_the-perfume-of-eros（《爱神之香》）
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
| `原文/*.md` | 源文（20 章 + 2 卷名页） | 不改 |
| `译文/*.zh-CN.md` | 译文产出（块对照双语） | 翻译 agent 产出 |

---

## 篇目清单

**Part I — The Facts in the Case**

| # | 章名 | 源文 | 大小 | 状态 |
|---|------|------|------|------|
| - | [卷名] The Facts in the Case | the-facts-in-the-case.md | 0.0KB | todo |
| 1 | A Man of Fashion | a-man-of-fashion.md | 11.0KB | todo |
| 2 | The Pocket Venus | the-pocket-venus.md | 13.5KB | todo |
| 3 | The Ex-First Lady | the-ex-first-lady.md | 13.2KB | todo |
| 4 | Enchantment | enchantment.md | 7.7KB | todo |
| 5 | Marie Changes Her Name | marie-changes-her-name.md | 13.0KB | todo |
| 6 | The Yellow Fay | the-yellow-fay.md | 8.0KB | todo |
| 7 | Sweet and Twenty | sweet-and-twenty.md | 9.0KB | todo |
| 8 | Two in a Turret | two-in-a-turret.md | 8.8KB | todo |
| 9 | Fanny Changes Her Clothes | fanny-changes-her-clothes.md | 13.1KB | todo |
| 10 | A Victim | a-victim.md | 7.1KB | todo |

**Part II — The General Sessions**

| # | 章名 | 源文 | 大小 | 状态 |
|---|------|------|------|------|
| - | [卷名] The General Sessions | the-general-sessions.md | 0.0KB | todo |
| 11 | Disenchantment | disenchantment.md | 11.4KB | todo |
| 12 | The Mote in the Eye | the-mote-in-the-eye.md | 13.6KB | todo |
| 13 | The Gates of Life | the-gates-of-life.md | 12.2KB | todo |
| 14 | The Return of the Yellow Fay | the-return-of-the-yellow-fay.md | 12.7KB | todo |
| 15 | Exit Fanny | exit-fanny.md | 9.7KB | todo |
| 16 | What the Papers Said | what-the-papers-said.md | 11.4KB | todo |
| 17 | Held Without Bail | held-without-bail.md | 15.4KB | todo |
| 18 | The Defendant to the Bar | the-defendant-to-the-bar.md | 12.3KB | todo |
| 19 | The Twelfth Juror | the-twelfth-juror.md | 19.4KB | todo |
| 20 | The Verdict | the-verdict.md | 5.3KB | todo |

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-08-03 | 建项目 | — | 20 章 + 2 卷名页提取完成，领域=小说文学，术语表 30+ 词条 |
| 2026-08-03 | 卷名页 ×2（Facts/General Sessions） | 通过 | 仅分卷标题行，0块，结构满足 |
| 2026-08-03 | I A Man of Fashion | 通过 | 14对块，结构契约满足；check退出码1为£5,000「000」数字锚点误报（在另一块），人工核对块对应无误；首章：洛夫特斯家晚宴，引出罗伊尔/范妮/西尔维娅/安南代尔/奥尔/玛丽·杜朗及通灵师米兰达预言，伏笔「这一带有死亡」 |
| 2026-08-03 | II The Pocket Venus | 通过 | 18对块，check退出码0，可疑错配0；范妮访西尔维娅于欧文广场旧宅、议阿瑟婚期、众人赴谢里餐厅午餐、奥尔论无政府主义、安南代尔定左轮、范妮与洛夫特斯斗嘴；术语表补Irving Place/Sherry's/Narragansett/Ferdinand/Mrs.Waldron 5词条；修2处uptown残留后通过 |
| 2026-08-03 | III The Ex-First Lady | 通过 | 14对块，check退出码0，可疑错配0；洛夫特斯误送花给科恩家、尾随玛丽至盖伊街、贿马尚夫人得引见、后客厅突袭表白；术语表补Morris Park/Gay Street/Jefferson Market/Washington Square/Mme.Machin/Cohen/bel canto等词条；修2处conscious/subconscious残留后通过 |
| 2026-08-03 | IV Enchantment | 通过 | 12对块，check退出码0，可疑错配0；洛夫特斯贿马尚夫人得与玛丽独处、强吻后许婚「在神与人面前发誓娶你」、诱其私奔未遂（玛丽挂念父亲）；术语表补Faust词条 |
| 2026-08-03 | V Marie Changes Her Name | 通过 | 14对块，结构契约满足；check退出码1为「32口径」数字锚点误报（在同块内），人工核对无误；洛夫特斯置玛丽于阿伦德尔公寓改名勒鲁瓦、安南代尔赴鸟舍晚宴、奥尔论股市与「爱神之香」原动力、夜遇醉酒的安南代尔；术语表补Arundel/Lexington Ave/Paquin/Tambourini/Mesnilmontant/Harris等词条 |
| 2026-08-03 | VI The Yellow Fay | 通过 | 10对块，check退出码0，可疑错配0；安南代尔宿醉失忆、西尔维娅经奥尔传话解除婚约、奥尔劝其戒酒、提及新仆哈里斯来历存疑（伏笔）；术语表补Newport/Catty/Kincardine/Littré词条；修1处punctuate残留后通过 |
| 2026-08-03 | VII Sweet-and-Twenty | 通过 | 11对块，check退出码0，可疑错配0；安南代尔写信无果赴纳拉甘西特避暑、赌场舞会遇范妮、范妮劝其接受与西尔维娅已了、相约多留数日；译中曾误用减号块标记（===Chinese---/===Original---共14处），sed批量修正为标准等号后通过 |
| 2026-08-04 | VIII Two in a Turret | 通过 | 17对块，check退出码0，可疑错配0；社交季尾声安南代尔携范妮登卡西诺塔楼、借景求婚遭婉拒（「我们一直是朋友」）、范妮点破他移情只是造化填空、提及洛夫特斯已携玛丽·勒鲁瓦出国一年令范妮暗自心伤；下楼遇普莱斯太太盘问收入（安南代尔年入两万五千）、责范妮错失洛夫特斯；术语表补 Mrs.Price/Marie Leroy/Casino/Christian Endeavorers |
| 2026-08-04 | IX Fanny Changes Her Clothes | 通过 | 18对块，check退出码0，可疑错配0；罗金厄姆旅店大火延及卡西诺、安南代尔冲入火场救出范妮衣裳首饰却忘了抢救普莱斯太太衣物、范妮感其勇相许订婚（「永久投降？」）、母斥其接洛夫特斯「挑剩的」并痛贬安南代尔为「金发碧眼的穷光蛋」、范妮心知所爱已远只能自欺「他算条好汉」；术语表补 Rockingham/Lowell/Ruinart/lemon squash/Hobson/Fred |
| 2026-08-04 | X A Victim | 通过 | 8对块，check退出码0，可疑错配0；视角转西尔维娅于莱诺克斯——时间软化旧创、经奥尔作证安南代尔醉酒失忆属实而悔己当初之决绝、读报见其纳拉甘西特火场英勇、旧情复燃正欲修书却接范妮订婚信、痛悔「我的错、我的十字架」、强持骄傲回信祝贺「他娶了我最亲爱的朋友我们必是挚友」、伏案恸哭；术语表补 Lenox/Narragansett Pier/Leonidas at Thermopylae/Roosevelt at San Juan/Arthur |
| 2026-08-04 | I Disenchantment（Part II 首章）| 通过 | 15对块，check退出码0，可疑错配0；视角转玛丽于阿伦德尔——一年后嗓艺精进而幸福更渺远、披露洛夫特斯种种谎言（母病/去庄园/赴欧皆为捏造）、中央公园撞见洛夫特斯与安南代尔太太同车、玛丽辞仆只留黑人女佣布兰奇以存自尊、洛夫特斯以「等你做了安南代尔太太」之口风打发；块11保留洛夫特斯纠正玛丽用词的英文原词（young lady/girl/young woman/gentlewoman）为情节必需，非残留；术语表补 Il segreto/Elysian Fields/Havre/Hudson/Central Park/Blanche/Mrs.Annandale/Miss Waldron |
| 2026-08-04 | II The Mote in the Eye | 通过 | 19对块，结构契约满足；check退出码1为「1000股艾奇逊/钢铁」数字锚点误报（译文「一千股」在同块内），人工核对无误；安南代尔年入实为五万、婚后居格拉默西公园、做股票自诩金融家、夫妻貌合神离（「他唯一的毛病：他不是另一个人」）、范妮与洛夫特斯旧情复燃、夜宴独处摊牌要洛夫特斯打发玛丽并许诺向阿瑟提离婚（去西部办）、洛夫特斯借「做空亏损」试探、安南代尔归报大单买进、临行向洛夫特斯耳语「替我向勒鲁瓦小姐致意」；术语表补 Mr.Skitt/ticker/drag/Annette,Juliette/opal/Atchison,Steel/congé/dot/faute de mieux/objet de luxe |
| 2026-08-04 | III The Gates of Life | 通过 | 12对块，check退出码0，可疑错配0；玛丽于阿伦德尔独候洛夫特斯、痛陈一年谎言、决意摊牌求一夜成婚否则便走、洛夫特斯以「陪母去哈德逊/玛丽宜出国」施缓兵之计、被玛丽识破安南代尔太太将赴达科他离婚、玛丽痛斥「骗子」要今夜成婚、洛夫特斯递名片夹（一万二千）作分手费被玛丽掷出窗外、玛丽绝望哭喊惊动女佣布兰奇、布兰奇义愤护主痛骂洛夫特斯「绞死都便宜」、洛夫特斯骂「见鬼」拂袖而去；术语表补 Tambourini/Pasta,Alboni,Malibran/Dakota/Canary/sapphire |
| 2026-08-04 | IV The Return of the Yellow Fay | 通过 | 14对块，结构契约满足；check退出码1为「$50,000,000」数字锚点跨块误报（译文「五千万」在邻块），人工核对无误；5月9日股市大崩盘夜、洛夫特斯赴宴报告已依范妮之命打发玛丽、席间与范妮暗里牵手被西尔维娅撞见、安南代尔灌酒填窟窿、席散范妮当面提离婚、安南代尔醉中翻出旧忆怒吼「要毙了洛夫特斯这条狗」、携西尔维娅遗落之珍珠送还欧文广场、醉告西尔维娅「范妮洛夫特斯要私奔我要毙了他」、西尔维娅劝其回家、安南代尔「我没有家」踉跄离去；术语表补 Melanchthon Orr/Harris/the Yellow Fay/sherry and bitters/étagère/Atch.U.P.St.Paul Steel/Irving Place |
| 2026-08-04 | V Exit Fanny | 通过 | 13对块，check退出码0，可疑错配0；洛夫特斯清晨被发现死于格拉默西公园长椅旁中弹、奥尔受西尔维娅之托访安南代尔、安南代尔醉中失记昨晚行踪、奥尔晓以「动机+威胁=表面证据」之利害、范妮一身黑衣登场以「当时怎么不把我也毙了」开场、扬言「愿发誓作证你说过的话」「再不愿见你除非法庭、必去法庭亲眼看你被判刑」、安南代尔瘫椅「不知女人能恨成这样」范妮答「那是因为你不知女人能爱成什么样」、范妮含笑退场；修1处 surely 残留；术语表补 Hugo/prima facie case |
| 2026-08-04 | VI What the Papers Said | 通过 | 15对块，check退出码0，可疑错配0；舆论狂欢——洛夫特斯之死登号外、玛丽照片（实为美编伪造）成「逃跑女凶手」、皮科克检察官盘问布兰奇（玛丽爱吃甜面包/三等舱/sewerage误读/挥小手送别痛哭）、玛丽开船时在海上排除嫌疑、洛夫特斯家族接受「拦路强人」说以遮家丑、拒绝悬赏、《纪事报》维多克式记者查洛夫特斯恐慌赔五百万先抛自杀说因凶器未找到而弃、悬赏五千征集线索、哈里斯献线索：亲耳听见安南代尔对太太说「我要宰了洛夫特斯」、太太提离婚、安南代尔上楼取32口径手枪出门；术语表补 Peacock/ Chronicle/Vidocq/Digby/sewerage steerage |
| 2026-08-04 | VII Held Without Bail | 通过 | 17对块，check退出码0，可疑错配0；西尔维娅寄望自杀说被奥尔以「精神癫痫/无意识行为」反驳、安南代尔被捕不准保释、舆论初判有罪、范妮伤寒病故（七月）、西尔维娅自责「都是我的错」、决意尽本分、九月返城探监安南代尔、谎称不知威胁以护他、订婚宣告、奥尔暗示将「给哈里斯吃药」；术语表补 Vox populi vox stulti/crime passionnel/cendrier/the Tombs/psychical epilepsy |
| 2026-08-04 | VIII The Defendant to the Bar | 通过 | 13对块，check退出码0，可疑错配0；法庭大戏开审——皮科克控方陈词、奥尔沙袋般击溃哈里斯（揭其盗窃伪造收钱作证前科）、辩方专家证「精神癫痫可致无意识」、安南代尔日场戏般从容；曾误写 ===Chinese++ 两处已sed修正；修3处英文残留(ladies/himself/prejudicing)；术语表补 the Recorder/Solon/Senegambian/Falstaff Mercutio/Tatterdemalia |
| 2026-08-04 | IX The Twelfth Juror | 通过 | 21对块，check退出码0，可疑错配0；全书高潮——安南代尔上证人席自承醉酒失忆、西尔维娅出庭为爱发伪证、双方结案陈词（皮科克骑兵冲锋式/奥尔拆哈里斯之「岩石」）、陪审团评议三小时判无罪、第十二位陪审员迪朗（玛丽之父）心脏病发临终自白「我才是凶手」当场死去、奥尔与皮科克如战后将帅相拥、正义「很少属人、有时属神」；修1处 lugubrious 残留 |
| 2026-08-04 | X The Verdict（全书完）| 通过 | 9对块，check退出码0，可疑错配0；尾声——两年后大都会歌剧院新排《阿依达》、女低音新秀黛拉兰迪即玛丽·勒鲁瓦（嫁坦布里尼、成名在望）、西尔维娅与安南代尔已婚一年、西尔维娅闻之动容「她受过苦我们当宽恕她」、全书以「这是我的裁决——也是你的，亲爱的，是不是？」收束；修2处残留(romanza/blissfully)。**全书22篇全部译完（100%）** |
