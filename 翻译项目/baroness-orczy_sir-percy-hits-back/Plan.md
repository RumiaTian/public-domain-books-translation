# 翻译计划（Plan.md）

---

## 本计划信息

- **项目名称**：baroness-orczy_sir-percy-hits-back（《珀西爵士反击》，Baroness Orczy，1927）
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
01-i.md,13.5,todo
02-ii.md,13.9,todo
...
```

| 字段 | 含义 | 取值 |
|------|------|------|
| `file` | 源文文件名（在 `原文/` 目录下） | 如 `01-i.md` |
| `size_kb` | 源文大小（KB）。>50KB 为长文，按通用翻译引擎第七节分段 | 数字 |
| `status` | 翻译状态 | `todo` 待译 / `doing` 翻译中 / `done` 已完成 |

---

## 执行步骤（agent 按此推进，两种模式共用）

> **谁执行**由 `项目说明.md` 的「内容形态」字段决定（见 `WORKFLOW.md`「判断内容形态」）：本项目为长篇 → **委派模式**，由子代理逐篇执行本流程。

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
- 长文（源文 >50KB）分段处理见通用翻译引擎第七节。

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
- ② 根 `translation_queue.csv` 中 `<本项目名>,<本篇名>` 的那一行（`WORKFLOW.md`「双写状态」）。

### 8. 追加日志
在本文件「运行日志」追加一行。

### 9. 循环
回到步骤 2，取下一篇 `todo`，直到全部 `done`。委派模式下由主 agent 决定是否继续派单（见 `WORKFLOW.md`「委派模式调度循环」）。

---

## 篇目清单

全书 39 章（罗马数字 I–XXXIX），文件名 `NN-roman.md`，队列顺序=阅读顺序。清单以 `translation_queue.csv` 为准，此处不重复。

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
| 2026-10-15 | 03-iii.md | done（check_bilingual 退出码 0，5 对块零错配） | 新词：迪弗洛（Duflos）、帕多瓦圣安东尼、勿忘我；FEFF×10/NBSP×3 原样保留 |
| 2026-10-15 | 02-ii.md | done（check_bilingual 退出码 0，49 对块零错配） | 逐段块对照；标题体例「## II / 第二章」；新词：女公民马尔托（Citizeness Martot）、四橡树（the Four Oaks）、三角帽（tricorne）；FEFF×15 原样保留 |

| 2026-10-15 | 01-i.md | done | 首篇黄金样本。章题样式定为「## I / 第一章」（源文体例罗马数字+中文章号合并单行）；块对照 1-4 段/块（24 对）；U+FEFF×23、U+00A0×1 照录保留；check_bilingual 退出码 0；新词已补术语表 |
| 2026-10-15 | 06-vi.md | done（check_bilingual 退出码 0，3 对块零错配） | 块对照 2/2/1 段；标题「## VI / 第六章」；本章无 FEFF/NBSP；新词：路易·德·弗朗特纳克（Louis de Frontenac）、安娜·德·格兰维尔（Anne de Grandville），已补术语表 |
| 2026-10-15 | 04-iv.md | done（check_bilingual 退出码 0，9 对块零错配） | 块对照 6/4/8/4/5/6/4/8/8 段；标题「## IV / 第四章」；FEFF×5/NBSP×1 原样保留（均在 Original 块）；新词：阿希尔（Achille）、乡警（garde-champêtre）、阿梅莉大娘（M'ame Amèlie）、吉内特（Ginette）、警察专员先生、初领圣体等，已补术语表 || 2026-10-15 | 05-v.md | done（check_bilingual 退出码 0，65 对块零错配） | 逐段块对照；标题「## V / 第五章」；新词：无套裤汉（sansculottes）、旧贵族（ci-devant）首现附注、米松（Mison）、篷车（calèche）、贞德（Jeanne d'Arc）、栋雷米（Domremy）、路易丝大娘（M'ame Louise）、公民中尉（citizen lieutenant）、里格（league，从 04 章体例）；FEFF×18/NBSP×4 原样照录 |
| 2026-10-15 | 09-ix.md | done（check_bilingual 退出码 0，33 对块零错配） | 逐段块对照；标题「## IX / 第九章」；FEFF×7/NBSP×1 原样保留（均在 Original 块）；新词：罗伊（Roy）、特龙谢寡妇/特龙谢大娘、匣子（casket）、钱夹（wallet）、亲爱的比比（Bibi chéri）、公民科隆布，已补术语表 |
| 2026-10-15 | 07-vii.md | done（check_bilingual 退出码 0，78 对块零错配） | 逐段块对照；标题「## VII / 第七章」；FEFF×26 原样照录（均在 Original 块，脚本装配逐字节保真）；新词：马蒂厄（Mathieu）、皮埃尔（Pierre）、安德烈（André）、让（Jean）、亨利（Henri）、巴普蒂斯特（Baptiste，庄园旧仆），已补术语表 |
| 2026-10-15 | 08-viii.md | done（check_bilingual 退出码 0，57 对块零错配） | 逐段块对照；标题「## VIII / 第八章」；FEFF×12/NBSP×3 原样照录（Original 块与源文逐字节比对 0 差异）；匣子/钱夹从 09 章术语表定名对齐；新词：波吉亚家族（Borgias）、斯皮内琴（spinet）、奥布松地毯（Aubusson）、野蔷薇（dog-rose）、芝麻开门等，已补术语表 |
| 2026-10-15 | 11-xi.md | done（check_bilingual 退出码 0，9 对块零错配） | 逐段块对照；标题「## XI / 第十一章」；本章源文含场景分隔符 `---`（段落 6/7 之间），译文原位保留独占一行；FEFF×3/NBSP×1 原样照录（Original 块与源文逐字节比对 0 差异）；新词：互订终身（tokened to one another），已补术语表 |
| 2026-10-15 | 10-x.md | done（check_bilingual 退出码 0，47 对块零错配） | 逐段块对照；标题「## X / 第十章」；FEFF×24 原样照录（Original 块由源文逐字节装配，0 差异）；1794 按引擎「保持原样」留阿拉伯数字；新词：五月王后（Queen of the month of May）、永恒的夏娃、天使长、杂货铺（épicerie）、工具棚、钱袋，已补术语表 |
| 2026-10-15 | 12-xii.md | done（check_bilingual 退出码 0，92 对块零错配） | 逐段块对照；标题「## XII / 第十二章」；FEFF×35/NBSP×2 原样照录（Original 块与源文逐字节比对 0 差异）；匣子/钱夹/格拉姆老爹从术语表定名对齐；新词：安热莉克（Angelique）、宪兵队（poste de gendarmerie）、《卡马尼奥拉》（Carmagnole）、里戈东舞（rigadoon）、瓦朗斯（Valence）、韦松（Vaison）、罪证物件（pièces de conviction）等，已补术语表 |
| 2026-10-15 | 13-xiii.md | done（check_bilingual 退出码 0，29 对块零错配） | 逐段块对照；标题「## XIII / 第十三章」；FEFF×8 原样照录（Original 块与源文逐字节比对 0 差异）；互订终身（tokened）、亲爱的比比、迪弗洛先生、老路易丝等从术语表定名对齐；新词：镶花边的小便帽（mobcap）、义姐妹（foster-sister）、带扣鞋，已补术语表 |
| 2026-10-15 | 14-xiv.md | done（check_bilingual 退出码 0，32 对块零错配） | 逐段块对照；标题「## XIV / 第十四章」；FEFF×8/NBSP×3 原样照录（Original 块与源文逐字节比对 0 差异）；迪弗洛先生/老路易丝/互订终身/值钱物件/我的天主（Mon Dieu）等从术语表与既有章节定名对齐；新词：阿里斯蒂德·西卡尔（Aristide Sicard）、一小杯（petit verre）、一万图尔里弗（livres tournois）、车棚，已补术语表 |
| 2026-10-15 | 15-xv.md | done（check_bilingual 退出码 0，24 对块零错配） | 逐段块对照；标题「## XV / 第十五章」；FEFF×5 原样照录（Original 块与源文逐字节比对 0 差异）；车棚/我的圣母按 13/14 章新定名对齐；科隆布大娘/阿梅代/比比/值钱物件/杂货铺（épicerie）从术语表定名；新词：阿尔芒先生（Monsieur Armand）、天上的声音、大路上耍空中飞人，已补术语表 |
| 2026-10-15 | 18-xviii.md | done（check_bilingual 退出码 0，41 对块零错配） | 逐段块对照；标题「## XVIII / 第十八章」；FEFF×3/U+200A×1 原样照录（Original 块由源文逐字节装配，0 差异）；戈岱中尉/乡村公共马车（coche）/公民阿尔芒/阿尔芒先生/肖维兰/奥朗日/女公民/公民中尉/亲爱的比比从术语表与既有章节定名对齐；新词：共和国街（Rue de la République）、共和国广场（Place de la République）、公民昂里奥（Henriot）、公安委员会第三区（Section III）、善心的撒玛利亚人，已补术语表 |
| 2026-10-15 | 16-xvi.md | done（check_bilingual 退出码 0，18 对块零错配） | 逐段块对照；标题「## XVI / 第十六章」；FEFF×4/NBSP×1 原样照录（Original 块与源文逐字节比对 0 差异）；公安委员会/断头台/三色绶带/贵族佬/旧贵族/乡村公共马车（coche，01 章定名）/杏树园/巴普蒂斯特·波塔尔从术语表与既有章节定名对齐；新词：梅乌热河（Méouge）、下阿尔卑斯群山（Basses Alpes）、土伦（Toulon）、第八十七战列团、警察专员公署、练兵场（Place d'Armes）、佩潘、圣艾蒂安-莱奥尔格、索镇（Sault）、卡庞特拉（Carpentras）、波塔尔大娘，已补术语表 |
| 2026-10-19 | 19-xix.md | done（check_bilingual 退出码 0，76 对块零错配） | 逐段块对照；标题「## XIX / 第十九章」；FEFF×15/U+200A×4 原样照录（Original 块由源文逐字节装配，比对 0 差异）；肖维兰/比比/值钱物件/工具棚/乡村公共马车/篷车（05 章定名）/三色绶带/贵族佬/旧贵族（ci-devant）/特龙谢寡妇/背柴老人从术语表与既有章节定名对齐；新词：穆瓦松上尉（Captain Moisson）、黑猫客栈（Chat Noir）、得啦（Allons, allons）、昭雪一桩大冤屈，已补术语表 |
| 2026-10-19 | 17-xvii.md | done（check_bilingual 退出码 0，102 对块零错配） | 逐段块对照；标题「## XVII / 第十七章」；FEFF×31/U+200A×1 原样照录（Original 块由源文逐字节装配，0 差异）；续接中断草稿（tmp_zh17_p1.txt 覆盖段 1-34）补译段 35-102；1794 按引擎与 10 章体例留阿拉伯数字；戈岱中尉/公民肖维兰/猩红繁笺花同盟/嫌疑犯法令/断头台/公安委员会/贵族佬/吉伦特派从术语表与既有章节定名对齐；新词：市政厅（Hôtel de Ville）、公共工程（Travaux Publics）、精锐连（compagnies d'élite）、宪兵队总监、国民公会特派代表、尼翁斯（Nyons）、瓦尔雷亚（Walreas）、德拉克河（Drac）、波夏尔（Pochart）、达努（Danou）、极乐世界（Elysian fields）、见鬼（Nom d'un nom/nom de nom），已补术语表 |
| 2026-10-19 | 20-xx.md | done（check_bilingual 退出码 0，87 对块零错配） | 逐段块对照；标题「## XX / 第二十章」；FEFF×30 原样照录（Original 块由源文逐字节装配，0 差异）；公安委员会/嫌疑犯法令/三色绶带/贵族佬/值钱物件/篷车（calèche）/乡村公共马车（coche）/黑猫客栈（19 章定名）从术语表与既有章节定名对齐；新词：市政厅（Hôtel de Ville）、公民波夏尔（Pochart）、公民达努（Danou）、特派代表/公民代表、梅兰和杜埃（Merlin/Douai）、复仇女神（Nemesis）、可疑之可疑，已补术语表 |
| 2026-10-19 | 22-xxii.md | done（check_bilingual 退出码 0，24 对块零错配） | 逐段块对照；标题「## XXII / 第二十二章」；FEFF×6 原样照录（Original 块由源文逐字节装配，0 差异，本章无 NBSP）；肖维兰/国民公会特派代表/篷车/断头台/贵族佬/猩红繁笺花/市政厅/黑猫客栈从术语表与既有章节定名对齐；新词：革命法庭（Revolutionary Tribunal）、公诉人伊斯纳尔（Isnard）、勒格朗热庭长（Legrange）、卡里埃（Carrier）、南特（Nantes）、虔诚信徒（calotins）、蒙泰利马尔（Montélimar），已补术语表 |
| 2026-10-19 | 23-xxiii.md | done（check_bilingual 退出码 0，31 对块零错配） | 逐段块对照；标题「## XXIII / 第二十三章」；FEFF×7/NBSP×1 原样照录（Original 块由源文逐字节装配，0 差异）；1794 按引擎与 10/17 章体例留阿拉伯数字（两侧空格）；肖维兰/弗勒蕾特/篷车/三色绶带/瓦朗斯/里昂/奥朗日/宪兵队/看热闹的老汉/走在队首（en tête）/见鬼（Nom de nom）/勒格朗热庭长/公诉人伊斯纳尔（22 章定名对齐）从术语表与既有章节定名对齐；新词：人头馆（Maison des Têtes）、大街（Grand' Rue）、德龙区（Drôme）、门房、驿童、罗讷河谷（Rhône）、圣阿波利奈尔（St. Apollinaire）、拉图尔街（rue Latour）、拦路贼、公共马车、轻便马车（chaise）、天晓得（pardieu），已补术语表 |

| 2026-10-19 | 21-xxi.md | done（check_bilingual 退出码 0，59 对块零错配） | 逐段块对照；标题「## XXI / 第二十一章」；FEFF×18 原样照录（Original 块由源文逐字节装配，0 差异）；革命法庭/拘押所/勿忘我/互订终身/工具棚/黑猫客栈前情衔接；新词：革命法庭（Revolutionary Tribunal）、弗勒尔·肖维兰（Fleur Chauvelin）、卡里斯蒂（Caristie）、阿维尼翁（Avignon）、菲利普·德·奥尔良（Philippe d'Orléans）、海市蜃楼（Fata Morgana）、Sainte Nitouche，已补术语表 |
| 2026-10-19 | 26-xxvi.md | done（check_bilingual 退出码 0，23 对块零错配） | 逐段块对照；标题「## XXVI / 第二十六章」；FEFF×7 原样照录（Original 块由源文逐字节装配，0 差异，本章无 NBSP）；137 留阿拉伯数字（10/17 章 1794 体例）；波夏尔/达努/特派代表/勒格朗热庭长/公诉人伊斯纳尔/戈岱中尉/贵族佬/热忱有亏/见鬼（nom de nom）从术语表与既有章节定名对齐；新词：中央公安委员会（Central Committee of Public Safety）、指券（assignat）、空中电报（aerial telegraph）、「让恐怖成为当日的议程」（Que la Terreur soit à l'ordre du jour）、「先下手为强，莫等自己先挨打」，已补术语表 |
| 2026-10-19 | 24-xxiv.md | done（check_bilingual 退出码 0，72 对块零错配） | 逐段块对照；标题「## XXIV / 第二十四章」；FEFF×16/NBSP×5/U+200A×1 原样照录（Original 块由源文逐字节装配，0 差异）；篷车/国民公会特派代表/猩红繁笺花同盟/值钱物件/断头台/贵族佬/庐庄/蒙泰利马尔/见鬼（Nom de nom）/我的天主（Mon Dieu）从术语表与既有章节定名对齐；新词：利夫龙（Livron）、塞斯特（Cest）、德龙河（Drôme）、拉朗斯峰（La Lance）、爵爷（milor’）、碗柜（armoire）、我的朋友（mon ami）、泥猴儿（mudlarks），已补术语表 |
| 2026-10-19 | 25-xxv.md | done（check_bilingual 退出码 0，37 对块零错配） | 逐段块对照；标题「## XXV / 第二十五章」；FEFF×19/NBSP×4 原样照录（Original 块由源文逐字节装配，0 差异）；弗勒蕾特/比比/老路易丝/阿梅代/庐庄/贵族佬/断头台/市政厅/革命法庭/卡里斯蒂（21 章定名）/《卡马尼奥拉》（12 章定名）/黑人（叙述语境规范译法）从术语表与既有章节定名对齐；新词：莫尔纳伯爵夫人（Comtesse de Mornas）、埃莱娜·德·莫尔纳（Hélène de Mornas）、欧仁妮·布朗（Eugénie Blanc）、克莱尔·德·沙特拉尔（Claire de Châtelard）、德·圣吕克先生（M. de St. Luce）、德·博莱讷先生（M. de Bollène）、点名（Roll-call）、断头夫人（Madame la Guillotine）、《导报》（Moniteur）、好天主（le bon Dieu）、草垫、气窗，已补术语表 |
| 2026-10-19 | 27-xxvii.md | done（check_bilingual 退出码 0，30 对块零错配） | 逐段块对照；标题「## XXVII / 第二十七章」；FEFF×7 原样照录（Original 块由源文逐字节装配，0 差异，本章无 NBSP；本章源文段落间为单换行，仅引用块前后有空行）；引用块（法令条文）保留 > 前缀；137 留阿拉伯数字（26 章体例）；波夏尔/达努/勒格朗热庭长/公诉人/特派代表/嫌疑犯法令/断头台/死囚车/报应（20 章定名）/中央公安委员会（26 章定名）/爱国志士（26 章定名）从术语表与既有章节定名对齐；新词：卡博公民（Citizen Cabot）、雾月（Brumaire）、比约（Billaud）、库东（Couthon）、圣茹斯特（Saint Just）、我的魔星，已补术语表 |
| 2026-10-19 | 29-xxix.md | done（check_bilingual 退出码 0，48 对块零错配） | 逐段块对照；标题「## XXIX / 第二十九章」；FEFF×18 原样照录（Original 块由源文逐字节装配，0 差异，本章无 NBSP）；`>` 引语信件（肖维兰致弗勒蕾特）原位保留；142/12 留阿拉伯数字（23/26 章两侧空格体例）；卡里斯蒂/克莱尔·德·沙特拉尔/泥猴儿/值钱物件/图尔里弗/卫兵上尉/点名从术语表与既有章节定名对齐；新词：富基耶-坦维尔（Foucquier-Tinville）、九月大屠杀、科尔马尔寡妇（Colmars）、波利厄将军（Paulieu）、月亮咖啡馆（café de la Lune）、雷米（Rémi）、长街（Rue Longue），已补术语表 |
| 2026-10-19 | 28-xxviii.md | done（check_bilingual 退出码 0，10 对块零错配） | 逐段块对照；标题「## XXVIII / 第二十八章」；FEFF×1 原样照录（Original 块由源文逐字节装配，0 差异，本章无 NBSP）；本章无阿拉伯数字锚点；断头夫人/卡里斯蒂/共和国街/南特/波夏尔/达努/贵族佬/旧贵族（ci-devant）/拘押所/庐庄/老路易丝从术语表与既有章节定名对齐；新词：布洛涅（Boulogne）、朱丽叶特·马尼（Juliette Marny）、伊冯娜·德·克尔诺甘（Yvonne de Kernogan）、富凯神父（Abbé Foucquet）、玛德琳·拉努瓦（Madeleine Lanoy）、玛格丽特·布莱克尼全名形式、区委员、屈辱的面包，已补术语表 |
| 2026-10-19 | 31-xxxi.md | done（check_bilingual 退出码 0，4 对块零错配） | 逐段块对照；标题「## XXXI / 第三十一章」；FEFF×2 原样照录（Original 块由源文逐字节装配，0 差异，本章无 NBSP）；本章无阿拉伯数字锚点；亲爱的比比/假面闹戏/演断头台戏/假撒旦/庭长/公诉人/头巾（25 章定名）/克莱尔·德·沙特拉尔（首现附原文）从术语表与既有章节定名对齐；新词：针线篮（workbasket）、好耶稣（le bon Jésus）、看守（warder，统一 25 章「狱卒」用法并固化）、消遣的钟点（recreation，25 章消遣体例），已补术语表 |
| 2026-10-19 | 30-xxx.md | done（check_bilingual 退出码 0，45 对块零错配） | 逐段块对照；标题「## XXX / 第三十章」；本章源文无 FEFF/NBSP/U+200A（仅 é 与弯引号，Original 块由源文逐字节装配，0 差异）；142/12 留阿拉伯数字（29 章两侧空格体例）；月亮咖啡馆/长街/卡里斯蒂/雷米/共和国广场/拘押所/打扫夫/流氓/信物从术语表与既有章节定名对齐；新词：萨博公民（Citizen Sabot）、武弗雷（Vouvray）、博若莱（Beaujolais）、苦艾酒（absinthe）、修路工、阿穆雷公民（Citizen Amouret）、蜡烛匠（chandler）、石板灰（slate-grey），已补术语表 |
| 2026-10-19 | 32-xxxii.md | done（check_bilingual 退出码 0，77 对块零错配） | 逐段块对照；标题「## XXXII / 第三十二章」；FEFF×8/NBSP×8/U+200A×1 原样照录（Original 块由源文逐字节装配，0 差异，CRLF→LF 从 29 章体例）；本章无阿拉伯数字锚点；肖维兰/弗勒蕾特/公民阿尔芒/猩红繁笺花同盟/贵族佬/泥猴儿/打扫夫/卡里斯蒂/科尔马尔寡妇/波利厄将军/雷米/长街/共和国街/共和国广场从术语表与既有章节定名对齐；新词：桥街（Rue du Pont）、吕西安·阿穆雷（Lucien Amouret）、粮商、集市大车、沙盒、铃绳、记录天使、瓦罐不离井上破，已补术语表 |
| 2026-10-19 | 33-xxxiii.md | done（check_bilingual 退出码 0，9 对块零错配） | 逐段块对照；标题「## XXXIII / 第三十三章」；FEFF×4/NBSP×1 原样照录（Original 块由源文逐字节装配，0 差异，CRLF→LF 从 29 章体例）；本章无阿拉伯数字锚点（六月十五日/二十天按源文拼写形式以中文数字出之）；戈岱/波夏尔/达努/卡里埃/菲利普·德·奥尔良/丹东/勒格朗热庭长/公诉人伊斯纳尔/空中电报/弗勒尔·肖维兰/克莱尔·德·沙特拉尔/莫尔纳夫人/欧仁妮·布朗/德·博莱讷先生/点名/看守/帮手/打扫夫/把戏/假面闹戏/公共大厅/值钱物件/好天主（le bon Dieu）/庐庄/老路易丝从术语表与既有章节定名对齐；新词：布里索（Brissot）、nommée（又名）、磨难与波折（trials and tabulations 源文误拼照文意译），已补术语表 |
| 2026-10-19 | 34-xxxiv.md | done（check_bilingual 退出码 0，19 对块零错配） | 逐段块对照；标题「## XXXIV / 第三十四章」；FEFF×1/NBSP×2 原样照录（Original 块由源文逐字节装配，0 差异，CRLF→LF 从 29 章体例）；本章无阿拉伯数字锚点（fifteen/eighteen 等按源文拼写形式以中文数字出之）；亲爱的比比/革命法庭/贵族佬/断头台/三色帽徽/本堂神父/阿梅代先生/初领圣体/卡里斯蒂/公共大厅/克莱尔·德·沙特拉尔/莫尔纳夫人从术语表与既有章节定名对齐；「Fleur Chauvelin, nommée Armand」传唤套语与「得啦（Allons, allons）」从 33/19 章体例沿用；新词：鞭笞柱（whipping-post）、公民庭长（Citizen President）、自由出身的法国女人、阴惨闹戏，已补术语表 |
| 2026-10-19 | 35-xxxv.md | done（check_bilingual 退出码 0，83 对块零错配） | 逐段块对照；标题「## XXXV / 第三十五章」；FEFF×12/U+200A×1 原样照录（Original 块由源文逐字节装配，0 差异，CRLF→LF 从 29 章体例）；「穗月二十二日」留阿拉伯数字锚点；肖维兰/弗勒蕾特/波夏尔/达努/戈岱中尉/阿黛尔/特龙谢寡妇/阿梅代·科隆布/匣子与钱夹/庐庄/拉拉涅/上街/旧贵族（ci-devant）/爱国志士/国务枢机/《导报》/恶名昭彰的法庭/断头台/罗伯斯庇尔/丹东/富基耶-坦维尔/值钱物件从术语表与既有章节定名对齐；新词：穗月（Messidor）、让-保罗·马拉全名形式、吊上路灯去（A la lanterne）、Vas-y、Cet imbécile、Hein、女权主义者（féministes）、木鞋（sabots）、国民自卫军、鞭笞柱，已补术语表 |
| 2026-10-19 | 38-xxxviii.md | done（check_bilingual 退出码 0，29 对块零错配） | 逐段块对照；标题「## XXXVIII / 第三十八章」；FEFF×4 原样照录（Original 块由源文逐字节装配，0 差异，CRLF→LF 从 29 章体例，本章无 NBSP/U+200A）；本章无阿拉伯数字锚点；亲爱的比比/好天主（le bon Dieu）/女公民/弗勒蕾特小姐/阿梅代先生/猩红繁笺花/驿车从术语表与既有章节定名对齐；拉拉涅/德龙河/拉朗斯峰/尼姆本章首现附原文；新词：圣塞泽尔（Ste. Césaire）、克雷斯特（Crest）、公民马科尔（Citizen Marcor）蹄铁匠、下街（Rue Basse）、le mouron rouge、la sainte Vierge、Tu m'aimes、假扮的士兵，已补术语表 |
| 2026-10-19 | 37-xxxvii.md | done（check_bilingual 退出码 0，27 对块零错配） | 逐段块对照；标题「## XXXVII / 第三十七章」；FEFF×6 原样照录（Original 块由源文逐字节装配，0 差异，CRLF→LF 从 29 章体例）；本章无阿拉伯数字锚点（ten/twenty/fifteen 等按源文拼写形式以中文数字出之）；市政厅/《导报》/断头夫人/好天主（le bon Dieu）/猩红繁笺花同盟/打扫夫/雷米/卡里斯蒂拘押所/阿梅代·科隆布/三色绶带/爱国志士/勒格朗热庭长/公诉人伊斯纳尔/吊上路灯去从术语表与既有章节定名对齐；nommée 体例从 33/35 章沿用；新词：塔尔蒂纳公民（Citizen Tartine）、莫蒂斯（Motus）、看守长、警察总监（Chief Commissary of Police）、最高主宰（Etre Suprême）、冥府、泰坦，已补术语表 |
| 2026-10-19 | 36-xxxvi.md | done（check_bilingual 退出码 0，39 对块零错配） | 逐段块对照；标题「## XXXVI / 第三十六章」；FEFF×4/NBSP×1 原样照录（Original 块由源文逐字节装配，0 差异，CRLF→LF 从 29 章体例；源文段落间单换行无空行，39 段逐段成对）；「XXV 卷 516–17 页」「1794 年 6 月 16 日」留阿拉伯数字锚点（10/17 章体例）；肖维兰/弗勒蕾特/珀西爵士/波夏尔/达努/阿黛尔/戈岱中尉/罗伯斯庇尔/被告栏/木鞋（sabots）/吊上路灯去（A la lanterne）/共和国广场/市政厅/长街/雷米/卡里斯蒂/打扫夫/爱国志士/《导报》/贵族佬/旧日（ci-devant）从术语表与既有章节定名对齐；新词：《报告选辑》（Choix des Rapports）、归我（A moi）、「三蜜蜂」客栈（Les Trois Abeilles）、塔尔蒂纳公民（Citizen Tartine）、泰坦（Titan）、军容（tenue）、针线杂货铺、滴水石兽、小混混、统一不可分割的共和国，已补术语表 |
| 2026-10-19 | 39-xxxix.md | done（check_bilingual 退出码 0，23 对块零错配） | 逐段块对照；标题「## XXXIX / 第三十九章」（全书末章，39 章全部译毕）；FEFF×4/NBSP×1 原样照录（Original 块由源文逐字节装配，0 差异，CRLF→LF 从 29 章体例；源文段落间单换行无空行，23 段逐段成对）；本章无阿拉伯数字锚点；肖维兰/弗勒蕾特/珀西爵士/布莱克尼/布莱克尼夫人/尚贝尔坦先生/驿车/奥朗日/英国从术语表与既有章节定名对齐；尼姆本章首现附原文；「嗐，伙计（La, man）」「天哪（Egad）」从术语表口头语体例；「反击（hitting back）」从 36 章定名沿用并点题收束；本章无新词入表 |
