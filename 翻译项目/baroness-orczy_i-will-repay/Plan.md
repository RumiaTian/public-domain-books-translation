# 翻译计划（Plan.md）

> 依据 `prompts/翻译计划模板.md` 建立。执行步骤（读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志）见模板，此处不重复。

---

## 本计划信息

- **项目名称**：baroness-orczy_i-will-repay（《我必报应》I Will Repay，Baroness Orczy，1906）
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/小说文学.md（块对照）
- **内容形态 / 执行模式**：长篇 / 委派（序曲 + 30 章 + 献词，共 32 篇，约 362.0KB）
- **术语表**：术语表.md

---

## 篇目清单

| # | 篇名（章题） | 源文 | 大小 | 状态 |
|---|------|------|------|------|
| 1 | À Ma Mère（献词） | 01-dedication.md | 0.0KB | todo |
| 2 | Prologue（序曲） | 02-prologue.md | 34.3KB | todo |
| 3 | I Paris: 1793 | 03-the-outrage.md | 15.7KB | todo |
| 4 | II Citizen-Deputy | 04-citizen-deputy.md | 11.2KB | todo |
| 5 | III Hospitality | 05-hospitality.md | 9.1KB | todo |
| 6 | IV The Faithful House-Dog | 06-the-faithful-house-dog.md | 4.2KB | todo |
| 7 | V A Day in the Woods | 07-a-day-in-the-woods.md | 14.6KB | todo |
| 8 | VI The Scarlet Pimpernel | 08-the-scarlet-pimpernel.md | 11.6KB | todo |
| 9 | VII A Warning | 09-a-warning.md | 5.7KB | todo |
| 10 | VIII Anne Mie | 10-anne-mie.md | 11.3KB | todo |
| 11 | IX Jealousy | 11-jealousy.md | 4.0KB | todo |
| 12 | X Denunciation | 12-denunciation.md | 11.7KB | todo |
| 13 | XI "Vengeance Is Mine" | 13-vengeance-is-mine.md | 16.7KB | todo |
| 14 | XII The Sword of Damocles | 14-the-sword-of-damocles.md | 22.9KB | todo |
| 15 | XIII Tangled Meshes | 15-tangled-meshes.md | 7.8KB | todo |
| 16 | XIV A Happy Moment | 16-a-happy-moment.md | 7.7KB | todo |
| 17 | XV Detected | 17-detected.md | 14.3KB | todo |
| 18 | XVI Under Arrest | 18-under-arrest.md | 9.5KB | todo |
| 19 | XVII Atonement | 19-atonement.md | 7.7KB | todo |
| 20 | XVIII In the Luxembourg Prison | 20-in-the-luxembourg-prison.md | 6.8KB | todo |
| 21 | XIX Complexities | 21-complexities.md | 9.3KB | todo |
| 22 | XX The Cheval Borgne | 22-the-cheval-borgne.md | 13.7KB | todo |
| 23 | XXI A Jacobin Orator | 23-a-jacobin-orator.md | 13.6KB | todo |
| 24 | XXII The Close of Day | 24-the-close-of-day.md | 12.4KB | todo |
| 25 | XXIII Justice | 25-justice.md | 8.6KB | todo |
| 26 | XXIV The Trial of Juliette | 26-the-trial-of-juliette.md | 11.0KB | todo |
| 27 | XXV The Defence | 27-the-defence.md | 17.8KB | todo |
| 28 | XXVI Sentence of Death | 28-sentence-of-death.md | 4.8KB | todo |
| 29 | XXVII The Fructidor Riots | 29-the-fructidor-riots.md | 10.1KB | todo |
| 30 | XXVIII The Unexpected | 30-the-unexpected.md | 13.1KB | todo |
| 31 | XXIX Père Lachaise | 31-p-re-lachaise.md | 14.6KB | todo |
| 32 | XXX Conclusion | 32-conclusion.md | 6.2KB | todo |

（权威队列以 `translation_queue.csv` 为准；状态回填双写——项目 CSV + 根 `translation_queue.csv`）

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-09-10 | 01-dedication.md | done | 献词单行（À Ma Mère / 献给我的母亲，源文非空仅一行）；check_bilingual 0 对误报之外全过（exit 0）、check_coverage exit 0 |
| 2026-09-10 | 02-prologue.md | done | 序曲块对照 36 对（183 段全覆盖）；check_bilingual exit 0（0 错配）、check_coverage exit 0；沿用定名（德鲁莱德/朱丽叶特/马尔尼子爵/马尔尼公爵/阿黛尔·德·蒙谢里/维尔弗兰什侯爵/德·克塔尔/佩特罗内勒/马蒂厄/桑松公民）；新名首现附原文（肖托丹公爵/米尔普瓦子爵/德·米朗热/菲利普/皮埃尔/朗巴勒）；法语词保留附译（en garde、blason、habit de cérémonie、le Roi Soleil、point d'Angleterre、grand siècle、Fête-Dieu、louis、piquet、Mechlin lace、Grand Monarque、Hotel de Marny） |
| 2026-09-10 | 03-the-outrage.md | done | 块对照18对；check_bilingual exit 0、check_coverage exit 0（公历日期1793-08-19以括注形式满足数字锚点）；法语插语（Il n est pas dangereux / voyons l aristo / quelle aristo / À moi）附译，新名首现附原文（Adam Lux / Charlier / Citizeness Margot / jabot） |
| 2026-09-10 | 04-citizen-deputy.md | done | 块对照14对；check_bilingual exit 0（0错配）、check_coverage exit 0；沿用定名（德鲁莱德/朱丽叶特·马尔尼/佩特罗内勒/坦维尔/梅尔兰/桑特尔/夏洛特·科黛/公会议员/死囚车/恐怖统治/吉伦特派/山岳派）；法语插语（cas de conscience/dot）附译；新附原文首现（Ursulines/Star-City/the Great, the Sacred Leveller of Mankind/Mademoiselle de Marny） |
| 2026-09-10 | 05-hospitality.md | done | 块对照10对；check_bilingual exit 1 仅1处数字锚点误报（No. 15 Rue Taitbout 译「泰布街十五号」中文数字改写）、check_coverage exit 0；沿用定名（德鲁莱德/朱丽叶特·马尔尼/安娜·米/佩特罗内勒/公会议员/救国委员会/红花侠）；新名首现附原文（Rue Taitbout/Buhl and Vernis Martin/Committee of National Defence） |
| 2026-09-10 | 06-the-faithful-house-dog.md | done | 块对照6对；check_bilingual exit 0（0错配）、check_coverage exit 0；沿用定名（德鲁莱德/朱丽叶特·马尔尼/安娜·米/佩特罗内勒/马尔尼公爵/马尔尼小姐/夏洛特·科黛）；新名首现附原文（Charlotte Corday/Duc de Marny/Nemesis）；安娜·米独白「the harmless, necessary house-dog」译「无害而少不了的看家狗」，章题「忠心的看家狗」呼应 |
| 2026-09-10 | 07-a-day-in-the-woods.md | done | 块对照18对；check_bilingual exit 0（0错配）、check_coverage exit 0；沿用定名（朱丽叶特·马尔尼/佩特罗内勒/保罗·德鲁莱德/德鲁莱德夫人/马尔尼公爵/夏洛特·科黛/玛丽·安托瓦内特/天罚女神/巴黎古监狱/国民公会/公会议员）；新名首现附原文（Messidor 获月/Thermidor 热月/Fructidor 果月/Suresnes 苏雷讷/Juliette/Pétronelle/Notre Dame/La Sainte Chapelle/St. Gervais）；章题「V 林中一日」 |
| 2026-09-10 | 08-the-scarlet-pimpernel.md | done | 块对照10对；check_bilingual exit 0（0错配）、check_coverage exit 0；沿用定名（德鲁莱德/朱丽叶特·德·马尔尼/德鲁莱德夫人/珀西·布莱克尼爵士/红花侠/红花侠同盟/坦维尔/肖夫兰/罗伯斯庇尔/丹东/梅尔兰/玛丽·安托瓦内特/巴黎古监狱/救国委员会/国民自卫军/公会议员/公诉人/「白日梦号」）；新名首现附原文（Blakeney/Sir Percy Blakeney/Daydream/Chauvelin/Mechlin/Comtesse de Tournai/Juliette de Marny）；法语插语（soupçon/en tête/ma foi）保留原文紧随附译；章题「VI 红花侠」 |
| 2026-09-10 | 09-a-warning.md | done | 块对照9对；check_bilingual exit 0（0错配）、check_coverage exit 0；沿用定名（珀西爵士/布莱克尼/德鲁莱德/朱丽叶特/德鲁莱德夫人/已故马尔尼公爵/马尔尼小姐）；新名首现附原文（Juliette/Déroulède/Blakeney/Duc de Marny/Marny）；布莱克尼论爱长段（feet of clay/sins with us）全译；章题「VII 警告」 |
| 2026-09-10 | 12-denunciation.md | done | 块对照14对；check_bilingual exit 0（0错配）、check_coverage exit 0；沿用定名（朱丽叶特/保罗·德鲁莱德/德鲁莱德夫人/安娜·米/佩特罗内勒/公会议员/珀西·布莱克尼爵士/夏洛特·科黛/玛丽·安托瓦内特/果月）；新名首现附原文（Juliette/Paul Déroulède/Anne Mie/Blakeney/Charlotte Corday/Marat/Joan of Arc/Ursuline Convent/Jansenism/Musée Carnavalet/Place de l'Institut/Louis Capet/ci-devant）；告发信引文按原文blockquote格式全译，共和历日期「果月二十三日」；法语标语（Liberté, Egalité, Fraternité 等）保留原文附译；章题「X 告发」 |
| 2026-09-10 | 11-jealousy.md | done | 块对照6对；check_bilingual exit 0（0错配）、check_coverage exit 0；沿用定名（布莱克尼/安娜·米/保罗·德鲁莱德/德鲁莱德/德·马尔尼小姐/珀西·布莱克尼爵士/德鲁莱德夫人）；新名首现附原文（Blakeney/Anne Mie/Paul Déroulède/Mademoiselle de Marny/Sir Percy Blakeney）；德鲁莱德唤安娜·米 little one 统一译「小家伙」；源文 U+FEFF 不可见字符已清除；章题「IX 嫉妒」 |
| 2026-09-10 | 10-anne-mie.md | done | 块对照21对；check_bilingual exit 0（0错配）、check_coverage exit 0（0漏译）；沿用定名（布莱克尼/安娜·米/保罗·德鲁莱德/德鲁莱德公民/朱丽叶特·马尔尼/德鲁莱德夫人/医学院街/革命广场/红花侠/珀西·布莱克尼爵士）；新名首现附原文（Anne of Austria/La Patrie/Megaera/Place St. Michel/Juliette de Marny/ci-devant）；共和围城锻炉段、梅尔兰《嫌疑犯法令》与爱与怜悯议论三段全译；法语 La Patrie 保留原文附译；章题「VIII 安娜·米」 |
| 2026-09-10 | 13-vengeance-is-mine.md | done | 块对照23对；check_bilingual exit 0（0错配）、check_coverage exit 0（0漏译）；沿用定名（朱丽叶特/安娜·米/德鲁莱德夫人/佩特罗内勒/珀西·布莱克尼爵士/德鲁莱德公民/公会议员/玛丽·安托瓦内特/巴黎古监狱/夏洛特·科黛/布罗加/「破壶」客栈）；新名首现附原文（De Crécy/De Coudremont/Megaera/Vendémiaire）；两段法语歌谣（De ta tige détachée / Je vais où va toute chose）原文照录、译文块内中文对照；章末「Vengeance is mine! I will repay!」用圣经定译「伸冤在我，我必报应」；章题「XI 伸冤在我」 |
| 2026-09-10 | 15-tangled-meshes.md | done | 块对照13对；check_bilingual exit 0（0错配）、check_coverage exit 0（0漏译）；沿用定名（朱丽叶特/德鲁莱德/梅尔兰/佩特罗内勒/公会议员/达摩克利斯之剑/断头台）；新名首现附原文（Aubusson 奥布松地毯/prie-dieu 跪凳）；章题「XIII 缠结的罗网」（源文标题罗马数字为 XIII，与文件序号 15 不一致，照源保留） |
| 2026-09-10 | 14-the-sword-of-damocles.md | done | 块对照22对；check_bilingual exit 0（0错配）、check_coverage exit 0（0漏译）；沿用定名（保罗·德鲁莱德/安娜·米/朱丽叶特/梅尔兰/坦维尔/公会议员/公诉人/救国委员会/国民公会/国民自卫军/巴黎古监狱/断头台/死囚车/信匣/旅行皮箱/《嫌疑犯法令》）；新名首现附原文（Paul Déroulède/Anne Mie/Juliette/Merlin/Tinville/Public Prosecutor/Citizen Juliette Marny/Widow Capet/Musée Carnavalet/the Conciergerie/Notre Dame）；梅尔兰台词 Voyez-moi donc çà 保留原文附译；「year of grace, 1793」译「恩典之年——1793，亦即革命纪元元年」；章题「XII 达摩克利斯之剑」 |
| 2026-09-10 | 16-a-happy-moment.md | done | 块对照11对；check_bilingual exit 0（0错配）、check_coverage exit 0（0漏译）；沿用定名（梅尔兰/德鲁莱德/朱丽叶特/安娜·米/佩特罗内勒/德鲁莱德夫人/珀西·布莱克尼爵士/公会议员/公诉人/救国委员会）；新名首现附原文（Citizen-Deputy/Merlin/Déroulède/Public Prosecutor/Cerberus/Juliette/Anne Mie/Pétronelle/St. Francis/Sir Percy Blakeney/Madame Déroulède）；源文 U+FEFF 不可见字符已清除；madonna 统一译「圣母」呼应圣方济各意象；章题「XIV 幸福的时刻」 |
| 2026-09-10 | 17-detected.md | done | 块对照27对；check_bilingual exit 0（0错配）、check_coverage exit 0（0漏译）；沿用定名（安娜·米/佩特罗内勒/梅尔兰/梅尔兰公民/德鲁莱德/德鲁莱德夫人/朱丽叶特/公会议员/公诉人/信匣）；新名首现附原文（Nemesis 涅墨西斯）；little one 沿用「小家伙」、those devils 沿用「恶鬼」、madonna 沿用「圣母」；源文 U+FEFF 不可见字符已清除；章题「XV 败露」（源文罗马数字为 XV，与文件序号 17 不一致，照源保留） |
| 2026-09-10 | 19-atonement.md | done | 块对照16对（66段全覆盖）；check_bilingual exit 0（0错配）、check_coverage exit 0（0漏译）；沿用定名（梅尔兰/梅尔兰公民/朱丽叶特/安娜·米/德鲁莱德夫人/保罗·德鲁莱德/佩特罗内勒/公会议员/救国委员会/玛丽·安托瓦内特/断头台/医学院街）；新名首现附原文（Merlin/Madame Déroulède/Anne Mie/Juliette/Citizen-Deputy/Marie Antoinette/Paul Déroulède/Pétronelle/Rue Ecole de Médecine）；法语插语（Déroulède! Vive Déroulède!/ma foi）保留原文附译；Atonement/atone 统一译「赎罪」、hunchback 译「驼背」；源文 U+FEFF 不可见字符已按破折号语义清除；章题「XVII 赎罪」（源文罗马数字为 XVII，与文件序号 19 不一致，照源保留） |
| 2026-09-10 | 20-in-the-luxembourg-prison.md | done | 块对照10对（34段全覆盖）；check_bilingual exit 0（0错配）、check_coverage exit 0（0漏译）；沿用定名（朱丽叶特/德鲁莱德/梅尔兰/玛丽·安托瓦内特/救国委员会/国民自卫军/吉伦特派/公诉人/信匣/断头台/断头台夫人/无套裤汉/卢森堡监狱）；新名首现附原文（Madame Guillotine/Place de la Guillotine）；法语插语（*Crache donc sur l'aristo, voyons!*）保留原文附译；「Monsieur」作王弟殿下称号处理、the Great Monarch 沿用「大君主」；Medici 沿用「美第奇」；源文 U+FEFF 不可见字符已清除；章题「XVIII 卢森堡狱中」 |
| 2026-09-10 | 21-complexities.md | done | 块对照16对（62段全覆盖，段级逐一比对一致）；check_bilingual exit 0（0错配）、check_coverage exit 0（0漏译）；沿用定名（德鲁莱德/梅尔兰/朱丽叶特/安娜·米/保罗·德鲁莱德/德鲁莱德夫人/公会议员/救国委员会/共和国/卢森堡监狱/国民公会/断头台/信匣/情夫）；新名首现附原文（Citizen-Deputy Déroulède/Committee of Public Safety/Merlin/Luxembourg Prison/domiciliary visitation/the Republic/Anne Mie/Juliette/Paul/Madame Déroulède/the Convention）；Atonement/atone 沿用「赎罪」、madonna 沿用「圣母」、saint 译「圣女」、little lover→情夫沿用；强调斜体（*her*/*him*/*loved*/*that*）原文照录并以中文星号强调对应；源文 U+FEFF/U+200A 不可见字符已清除（嵌套引语内空格）；章题「XIX 千头万绪」（源文罗马数字为 XIX，与文件序号 21 不一致，照源保留） |
| 2026-09-10 | 18-under-arrest.md | done | 块对照12对（41段全覆盖）；check_bilingual exit 0（0错配）、check_coverage exit 0（0漏译）；沿用定名（德鲁莱德/朱丽叶特/安娜·米/梅尔兰/公会议员/救国委员会/信匣/断头台/恐怖分子/巴黎古监狱不涉本章）；新名首现附原文（Paul Déroulède/Merlin/Juliette/Anne Mie/Juliette Marny/Citizen-Deputy/Committee of Public Safety/Hall of Justice→司法宫/Jacobin→雅各宾党人/Marat/Danton/Robespierre）；法语插语（*À la lanterne, vieux crétin!*/*Nous lui casserons la gueule!*/Adieu!）保留原文附译；madonna 沿用「圣母」；源文 U+FEFF 不可见字符已清除；章题「XVI 被捕」（源文罗马数字为 XVI，与文件序号 18 不一致，照源保留） |
| 2026-09-10 | 24-the-close-of-day.md | done | 块对照20对（80段全覆盖）；check_bilingual exit 0（0错配）、check_coverage exit 0（0漏译）；沿用定名（德鲁莱德/朱丽叶特/朱丽叶特·马尔尼/安娜·米/德鲁莱德夫人/保罗·德鲁莱德/珀西·布莱克尼爵士/佩特罗内勒/梅尔兰/公会议员/救国委员会/共和国/坦普尔监狱/巴黎古监狱/卢森堡监狱/革命广场/医学院街/断头台/红花侠/桑特尔/坦维尔/刽子手桑松/果月）；新名首现附原文（Déroulède/Juliette/Sir Percy Blakeney/Anne Mie/Madame Déroulède/Paul Déroulède/Mirabeau/La Fayette/Desmoulin/Juliette Marny/Rue Ecole de Médecine/Citizen-Deputy/the Republic/Fructidor/Lord Hastings/Lord Anthony Dewhurst/The Scarlet Pimpernel/Pétronelle/Committee of Public Safety/Palais de Justice/Citizen Santerre/the Temple/the Conciergerie/Palais Condé/the Luxembourg/Tinville/Place de la Révolution/Samson/Merlin/Luxembourg Palace→卢森堡宫/Rue des Arts/Marguerite 玛格丽特/The League of The Scarlet Pimpernel 红花侠同盟）；法语插语（*Inconnue*（查无此人）×2/*couvre-feu*（宵禁））保留原文附译；demmed 沿用「该死的」、madonna 沿用「圣母」、those devils 沿用「那些恶鬼」；强调斜体（*he*/*is*）原文照录并以中文星号对应；源文 6 处 U+FEFF 不可见字符（均缀于破折号前）已清除；章题「XXII 一日将尽」（源文罗马数字为 XXII，与文件序号 24 不一致，照源保留） |
| 2026-09-10 | 23-a-jacobin-orator.md | done | 块对照14对（60段全覆盖）；check_bilingual exit 0（0错配）、check_coverage exit 0（0漏译）；沿用定名（勒努瓦/坦维尔/梅尔兰/德鲁莱德/朱丽叶特·马尔尼/公会议员/公诉人/救国委员会/共和国/断头台/《嫌疑犯法令》/独眼马客栈/布罗加/夏洛特·科黛/加来）；新名首现附原文（Lenoir/Tinville/Merlin/Déroulède/Public Prosecutor/Juliette Marny/Foucquier-Tinville/Phrygian cap/Hall of Justice/Charlotte Corday/Calais/Brogard）；法语插语（*Pardi!*（哼！）×2、*Eh bien!*（那好！））保留原文附译；强调斜体（*other* 等）原文照录并以中文星号对应；Minister of Justice 译「司法部长」、coal-heaver 译「运煤工」、watchman 夜呼照史实直译；源文 U+FEFF 不可见字符（均缀于破折号前）已清除；章题「XXI 雅各宾演说家」（源文罗马数字为 XXI，与文件序号 23 不一致，照源保留） |
| 2026-09-10 | 22-the-cheval-borgne.md | done | 块对照19对（65段全覆盖）；check_bilingual exit 0（0错配）、check_coverage exit 0（0漏译）；沿用定名（梅尔兰/富基耶-坦维尔/坦维尔/勒努瓦/德鲁莱德/保罗·德鲁莱德/公会议员/公诉人/断头台夫人/无套裤汉/雅各宾派/恐怖统治/国民公会/革命广场/独眼马客栈/独眼马/信匣/运煤工/共和国）；新名首现附原文（Auberge du Cheval Borgne/Grand Monarque/Vidoq/Marat/Charon/Manuel/Osselin/Rabaut/Custine/Bison/Merlin/Foucquier-Tinville/Déroulède/Marie Antoinette/Louis Capet/Paul Déroulède/Westerman/Brunet/Beauharnais/Widow Capet/ci-devant）；法语插语（*Liberté, Fraternité, Egalité, sinon la Mort.*/*la guillotine va toujours*/*La guillotine va toujours!*/*Vive la Liberté!*/*Pardi!*（哼！沿用 23 章定译））保留原文附译；强调斜体（*know*/*forge*）以中文星号对应；brothel 按时代风貌全译「妓院」；源文 8 处 U+FEFF 不可见字符（均缀于破折号前）在 Original 块按源保留；章题「XX 独眼马客栈」 |
| 2026-09-10 | 26-the-trial-of-juliette.md | done | 块对照14对（51段全覆盖）；check_bilingual exit 0（0错配）、check_coverage exit 0（0漏译）；沿用定名（朱丽叶特·马尔尼/德鲁莱德/富基耶-坦维尔/公诉人/公会议员/梅尔兰/《嫌疑犯法令》定名不涉本章用「梅尔兰那部最不公的法令」/救国委员会/革命法庭/断头台/革命广场/萨尔佩特里埃监狱/果月/国民自卫军/法国国家图书馆/夏洛特·科黛/玛丽·安托瓦内特/共和国）；新名首现附原文（Bulletin du Tribunal Révolutionnaire/Bibliothèque Nationale/Foucquier-Tinville/Public Prosecutor/Juliette Marny/Déroulède/Merlin/Charlotte Corday/Marie Antoinette/Salpêtriere/Hall of Justice/Samson/Committee of Public Safety）；法语插语（*Elle s'essuya le front qui fut perlé de sueur.*）保留原文附译；强调斜体（*她*×3）以中文星号对应；公诉人起诉书长段（鞭笞+萨尔佩特里埃判决）按历史文献风貌全译；源文 U+FEFF 不可见字符（3 处，缀于破折号前）在 Original 块按源保留；Citizeness 译「女公民」；章题「XXIV 朱丽叶特受审」（源文罗马数字 XXIV 与文件序号 26 不一致，照源保留） |
| 2026-09-10 | 25-justice.md | done | 块对照12对（39段全覆盖）；check_bilingual exit 0（0错配）、check_coverage exit 0（0漏译）；沿用定名（富基耶-坦维尔/德鲁莱德/保罗·德鲁莱德/梅尔兰/罗伯斯庇尔/公会议员/公诉人/救国委员会/革命广场/革命法庭/《革命法庭公报》/断头台/果月/共和国）；新名首现附原文（Foucquier-Tinville/Public Prosecutor/Citizen-Deputy/Committee of Public Safety/Styx/Fructidor/Citizen-President/Bulletin du Tribunal Révolutionnaire/Notre Dame/St. Eustache/St. Germain l'Auxerrois/Tribunal Révolutionnaire/Merlin/Lebrun 勒布伦/Robespierre/Déroulède/Paul Déroulède）；法语插语（*La République: une et indivisible*/*Liberté, Egalité, Fraternité!*/*fille de joie*（烟花女子）/*abat-jour*（灯罩）/*Tiens*（瞧））保留原文附译；the sea-green incorruptible 译「海绿色的不可腐蚀者」、save the mark 译「恕我出此一言」；本章无 demmed；断头台不问出身段（公爵/烟花女子/波旁后裔/浪荡儿）按历史风貌全译；源文 8 处 U+FEFF 不可见字符（缀于破折号前）已按破折号语义清除；章题「XXIII 正义」（源文罗马数字为 XXIII，与文件序号 25 不一致，照源保留） |
| 2026-09-10 | 28-sentence-of-death.md | done | 块对照5对（21段全覆盖）；check_bilingual exit 0（0错配）、check_coverage exit 0（0漏译）；沿用定名（德鲁莱德/朱丽叶特/朱丽叶特·马尔尼/保罗·德鲁莱德/富基耶-坦维尔/梅尔兰/罗伯斯庇尔/公会议员/公诉人/国民公会/国民自卫军/革命法庭/共和国/断头台/死囚车/恐怖统治/萨尔佩特里埃监狱不涉本章/《革命法庭公报》/玛丽·安托瓦内特）；新名首现附原文（Bulletin du Tribunal Révolutionnaire/Hall of Justice/Déroulède/National Convention/Foucquier-Tinville/Merlin/Robespierre/Juliette Marny/Paul Déroulède/Marie Antoinette/Public Prosecutor）；法语书名（*Bulletin du Tribunal Révolutionnaire*）保留原文附译；「叛国通信/司法丑剧/自我控告」等按历史风貌全译；源文 3 处 U+FEFF 不可见字符（缀于破折号前）在 Original 块按源保留；章题「XXVI 死刑判决」（源文罗马数字 XXVI 与文件序号 28 不一致，照源保留） |
| 2026-09-10 | 27-the-defence.md | done | 块对照18对（89段全覆盖，逐块段落数1:1自检一致）；check_bilingual exit 0（0错配、标题合并满足）、check_coverage exit 0（0漏译）；沿用定名（德鲁莱德/朱丽叶特/朱丽叶特·马尔尼女公民/勒努瓦/梅尔兰/富基耶-坦维尔/坦维尔/公会议员/公诉人/司法部长/雅各宾俱乐部/巴黎古监狱/国民自卫军/断头台/刑台/信匣/旅行皮箱/司法宫/小家伙们/运煤工）；新名首现附原文（Lebrun 勒布伦/Tigre Jaune『黄虎』/lieutenant-governor 副总督）；法语插语（*Ça ira! ça ira! vas-y Déroulède!*（会好的！会好的！上啊，德鲁莱德！）/*À la lanterne les traîtres! Mort à Déroulède. À la lanterne! l'aristo!*（整串附译）/*Tiens! c'est bête!*（瞧！真蠢！）/*Ma foi!*（说实在的！）/*lanterne*（路灯））保留原文紧随附译；强调斜体（*you*/*their*/*that*/*his*/*he*/*my*）以中文星号对应；the accused 统一译「被告」、self-accused 译「自己招认的叛徒」、pillory of infamy 译「耻辱的示众台」；源文 U+FEFF 不可见字符（缀于破折号前）未录入 Original（手抄原文），校验不受影响；章题「XXV 辩护」（源文罗马数字为 XXV，与文件序号 27 不一致，照源保留） |
| 2026-09-10 | 29-the-fructidor-riots.md | done | 块对照12对（48段全覆盖，逐块段落数1:1自检一致）；check_bilingual exit 0（0错配、标题合并满足）、check_coverage exit 0（0漏译）；沿用定名（德鲁莱德/朱丽叶特·马尔尼/朱丽叶特/珀西·布莱克尼爵士/红花侠/勒努瓦/勒努瓦公民/梅尔兰/梅尔兰公民/桑特尔/桑特尔公民/公会议员/司法部长/司法宫/司法宫大殿/卢森堡宫/卢森堡监狱/国民自卫军/革命广场/死囚车/果月/果月骚乱/运煤工/汽油灯/女公民不涉本章）；新名首现附原文（the Prince of Wales 威尔士亲王/Pont au Change 兑换桥/Rue du Palais 宫殿街/Akous 阿库（布列塔尼呼唤将死者的幽灵）/Maegaeras 梅盖拉（希腊神话复仇女妖）/the Temple 坦普尔监狱）；法语插语（*À la lanterne! À la lanterne! le traître!*/*À la lanterne! À la lanterne!*/*A mort! A mort! À la lanterne les traîtres!*）保留原文紧随附译，lanterne 沿用 27 章「吊路灯去/路灯」；原文 Santerre/Santerne 两拼写均按术语表统一译「桑特尔」；year I of the Revolution 译「革命元年」、Maegaeras 按神话典故意译加注；源文 3 处 U+FEFF 不可见字符（缀于破折号前）未录入 Original（按破折号语义清除），校验不受影响；章题「XXVII 果月骚乱」（源文罗马数字 XXVII 与文件序号 29 不一致，照源保留） |
| 2026-09-10 | 32-conclusion.md | done | 块对照7对（30段全覆盖，逐块段落数1:1自检一致，原文行逐字过检）；check_bilingual exit 0（0错配、标题合并满足）、check_coverage exit 0（0漏译）；沿用定名（珀西·布莱克尼爵士/德鲁莱德/朱丽叶特/朱丽叶特小姐/佩特罗内勒/德鲁莱德夫人/红花侠同盟/拉雪兹神父公墓/勒阿弗尔/果月/阿尔比恩沿用术语表定译不涉本章新注/旅行马车/通行证）；新名首现附原文（Sir Percy Blakeney/Père Lachaise/Pétronelle/Déroulède/Lord Anthony Dewhurst/Sir Andrew Ffoulkes/Lord Hastings/The League of The Scarlet Pimpernel/Le Havre/the Daydream「白日梦号」/Anne Mie/Albion）；法语插语（Madonna!）照录紧随附译（我的圣母！）；船名斜体（*Daydream*）以「白日梦号」加引号对应首现附原文；begad 译「老天在上！」定 Percy 口癖；本章含源文唯一场景分隔线 ---（位于两位女士团聚与海上黎明两场之间），在译文对应位置保留为游离分隔线；章题「XXX 结语」（源文罗马数字 XXX 与文件序号 32 一致） |
| 2026-09-10 | 30-the-unexpected.md | done | 块对照19对（70段全覆盖，逐块段落数1:1脚本核验一致）；check_bilingual exit 0（0错配、标题合并满足）、check_coverage exit 0（0漏译）；沿用定名（德鲁莱德/朱丽叶特/朱丽叶特·马尔尼/珀西·布莱克尼爵士/红花侠/勒努瓦/布罗加/桑特尔/坦维尔/公会议员/国民自卫军/坦普尔监狱/司法大厅/断头台/无套裤汉/「破壶」客栈/艺术街/运煤工/共和国）；新名首现附原文（National Guard/Santerre/Citizen-Deputies/Juliette/Déroulède/Rue des Arts/La Cruche Cassée/Sir Percy Blakeney/Scarlet Pimpernel/Tony/Ffoulkes/Lenoir/League/Tinville/Brogard/Hall of Justice/Lord Anthony Dewhurst/Lord Hastings/sansculottes/tricotteuse）；法语插语（*À moi*×2（到我这儿来）/en route（上路））保留原文紧随附译；Percy 口癖 La!/demmed/Gadzooks/Faith! 译「哎呀/该死的/老天/说真的」；tricotteuse 加注「断头台旁织线的贫妇」；集合暗号 sea-mew/seagull 统一译「海鸥」， rallying cry 译「集合暗号，海鸥的锐鸣连啼三遍」；Santerre/Santerne 两拼写按术语表统一译「桑特尔」；源文 9 处 U+FEFF 不可见字符（缀于破折号前）未录入 Original（按破折号语义清除），校验不受影响；章题「XXVIII 意外之变」（源文罗马数字 XXVIII 与文件序号 30 不一致，照源保留） |
| 2026-09-10 | 31-p-re-lachaise.md | done | 块对照19对（90段全覆盖，逐块段落数1:1自检一致）；check_bilingual exit 0（0错配、标题合并满足）、check_coverage exit 0（0漏译）；沿用定名（桑特尔/德鲁莱德/朱丽叶特/朱丽叶特·马尔尼/珀西·布莱克尼爵士/安德鲁·福尔克斯爵士/安东尼·杜赫斯特勋爵/黑斯廷斯勋爵/红花侠/坦普尔监狱/司法宫/国民自卫军/无套裤汉/运煤工/女公民/死囚车/果月/拉雪兹神父公墓/共和国）；新名首现附原文（Santerre/Déroulède/Juliette/Sir Percy Blakeney/Sir Andrew Ffoulkes/Lord Anthony Dewhurst/Lord Hastings/the Scarlet Pimpernel/Hall of Justice/the Bastille/Père Lachaise/National Guard/Fructidor/Virgin Mary/Abélard/Helöise/Barrière Ménilmontant/Ménilmontant）；街道桥名首现附原文（Pont St. Michel/the Cité/Pont au Change/Pont Neuf/Rue du Temple/Rue des Archives/Rue Turbigo/Belleville gate/Rue des Filles/Rue du Chemin Vert/Popincourt/Rue de la République）；法语插语（*Ça ira*（会好的）/*À la lanterne!*（吊路灯去！）整串附译/*les traîtres!*（那些叛徒）/Ma foi!（说实在的）/*Pardi!*（哼！）/*Quatorze Juillet!*（七月十四日）/*terrains vagues*（荒地）/bousculades（乱冲乱撞））保留原文紧随附译；强调斜体（*would*）以中文星号对应（*定要*）；barriers 统一译「关卡」、gutter song 译「下流歌谣」、sea-mew/seagull 统一「海鸥」；the 14th of July 译「七月十四日」；源文 U+FEFF 不可见字符（缀于破折号/省略号前）未录入 Original（手抄原文），校验不受影响；章题「XXIX 拉雪兹神父公墓」 |
2026-09-10｜批次2｜整书完结：32/32 全部 done，删认领锁。
