# 翻译计划：盲角

## 本计划信息

- **项目名称**：dornford-yates_blind-corner
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/小说文学.md
- **术语表**：术语表.md
- **执行模式**：连续（中篇；见 WORKFLOW.md「单篇翻译流程」）

## 执行步骤

单篇 9 步（读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志）以 `prompts/翻译计划模板.md`「执行步骤」为准，本文件不重复。连续模式下由主 agent 直接执行。

## 篇目清单

由 `translation_queue.csv` 管理（10 篇，约 369KB）。

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-09-10 | dedication.md | 完成 | check_bilingual/check_coverage 均通过；1 对块；新定名：诺曼·肯尼思·斯蒂芬（Norman Kenneth Stephen） |
| 2026-09-10 | out-of-the-eater.md | 完成 | check_bilingual 66 对块、check_coverage 均通过；新定名：罗斯·诺布尔（Rose Noble）、曼塞尔（Mansel）、钱多斯（Chandos）、汉伯里（Hanbury）、罗利（Rowley）、卡森（Carson）、贝尔（Bell）、泰斯特（Tester）、乔布（Job）、潘特（Punter）、红发阿克塞尔（Axel the Red）、瓦根斯堡（Wagensburg）、椽子（Rafter） |
| 2026-09-10 | the-attack-on-the-well.md | 完成 | check_bilingual 34 对块、check_coverage 均通过；沿用既定人名，新增定名：埃利斯（Ellis）、克恩滕（Carinthia）、萨尔茨堡（Salzburg）、小威利/大威利（Little Willie/Big Willie） |
| 2026-09-10 | tester-gives-tongue.md | 完成 | check_bilingual 45 对块、check_coverage 均通过；沿用既定人名（罗斯·诺布尔/曼塞尔/钱多斯/汉伯里/罗利/卡森/贝尔/泰斯特/乔布/潘特/埃利斯/大威利/小威利/瓦根斯堡/萨尔茨堡/菲拉赫/克恩滕），新增定名：圣马丁（St. Martin）、勒拉（Lerai）、邦奇（Bunch）、「神圣」戈登（"Holy" Gordon）、囚井（oubliette）、哨峰（the sentinel peak） |
| 2026-09-10 | rose-noble-moves.md | 完成 | check_bilingual 63 对块、check_coverage 均通过；沿用既定人名与术语（罗斯·诺布尔/曼塞尔/钱多斯/汉伯里/罗利/卡森/贝尔/泰斯特/乔布/埃利斯/潘特/邦奇/瓦根斯堡/萨尔茨堡/菲拉赫/克恩滕/圣马丁/勒拉），新定名：威廉（William）、乔治（George）、窗洞（embrasure）、锤柄（helve）；术语对齐：oubliette=囚井、dungeon=地牢、ramp=坡道、劳斯莱斯（Rolls） |
| 2026-09-10 | the-battle-with-the-springs.md | 完成 | check_bilingual 49 对块、check_coverage 均通过；沿用既定人名与勒拉（Lerai），新增定名：卡尔顿烤肉馆（Carlton Grill）、克罗伊斯（Croesus）、霍尔本（Holborn）、沙特尔（Chartres）、梅普尔公司（Maple's）、珀涅罗珀（Penelope） |
| 2026-09-10 | the-way-to-wagensburg.md | 完成 | check_bilingual 47 对块、check_coverage 均通过；沿用既定人名（曼塞尔/汉伯里/钱多斯/埃利斯/卡森/泰斯特/瓦根斯堡/勒拉/萨尔茨堡/菲拉赫/克恩滕/大井/封闭汽车），新增定名：圣詹姆斯街（St. James's Street）、皮卡迪利（Piccadilly）、克利夫兰罗街（Cleveland Row）、帕尔马尔街（Pall Mall）、库克旅行社（Cook's）、布洛涅（Boulogne）、迪耶普（Dieppe）、斯特拉斯堡（Strasbourg）、沙特尔（Chartres）、黑森林（the Black Forest）、西里汉姆梗（Sealyham）、《连祷文》（the Litany）、瓦根斯堡大井（The Great Well of Wagensburg） |
| 2026-09-10 | the-race-for-the-chamber.md | 完成 | check_bilingual 37 对块、check_coverage 均通过；沿用既定人名与术语（罗斯·诺布尔/曼塞尔/钱多斯/汉伯里/罗利/卡森/贝尔/泰斯特/埃利斯/制革匠/乔治/囚井/地牢/壁垒/坑道/竖井/溜槽/涵洞/探照灯/水槽/谷地/圣马丁/勒拉/萨尔茨堡/菲拉赫），新增定名：活土（live ground）、汇流处（the junction）、坑道头（the nose of the shaft）、电警铃（electric alarm）、盗贼的至爱（The Burglar's Delight）、薄纱衫（zephyr）、巴珊公牛（the bulls of Bashan）、胸墙（breastwork）、攻城槌（battering-ram）、卡芒贝尔奶酪（Camembert cheese） |
| 2026-09-10 | the-well-digger-s-statement.md | 完成 | check_bilingual 36 对块、check_coverage 均通过；沿用既定人名（曼塞尔/汉伯里/罗利/卡森/贝尔/埃利斯/瓦根斯堡/勒拉/菲拉赫/克恩滕/萨尔茨堡/克利夫兰街/红发阿克塞尔），新定名：理查德·威廉·钱多斯（Richard William Chandos）、乔纳森·曼塞尔（Jonathan Mansel）、乔治·汉伯里（George Hanbury）、波默罗伊（Pomeroy）、基督堂学院（Christchurch）、掘井人（well-digger）、盲角（Blind Corner） |
| 2026-09-10 | we-go-to-ground.md | 完成 | check_bilingual 63 对块、check_coverage 均通过；沿用既定人名与术语（罗斯·诺布尔/曼塞尔/汉伯里/乔治/罗利/卡森/贝尔/泰斯特/乔布/潘特/埃利斯/邦奇/瓦根斯堡/萨尔茨堡/菲拉赫/克恩滕/囚井/地牢/坑道/竖井/溜槽/画廊/壁垒/胸墙/窗洞/哨峰/探照灯/大井/封闭汽车/劳斯莱斯/掘井人/小教堂/罗盘/测深绳），新定名：马具房（harness-room）、牛栏（byre）、抬架（hurdle）、小碉堡（sconce）、据点（blockhouse）、康沃尔梯级（Cornish stile）、吊座（the seat） |
2026-09-10｜批次2｜整书完结：10/10 全部 done，删认领锁。
