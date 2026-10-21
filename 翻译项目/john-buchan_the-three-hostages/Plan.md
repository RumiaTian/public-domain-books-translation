# 翻译计划：三名人质

## 本计划信息

- **项目名称**：john-buchan_the-three-hostages
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/小说文学.md
- **术语表**：术语表.md
- **执行模式**：委派（长篇；见 WORKFLOW.md「单篇翻译流程」）

## 执行步骤

单篇 9 步（读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志）以 `prompts/翻译计划模板.md`「执行步骤」为准，本文件不重复。委派模式下由主 agent 派单，子代理简报含黄金样本与前篇末尾。

## 篇目清单

由 `translation_queue.csv` 管理（23 篇，约 599KB）。

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
| 2026-10-15 | how-a-french-nobleman-discovered-fear.md | done | check_bilingual 通过（36 对块，退出码 0） |
| 2026-10-15 | how-a-german-engineer-found-strange-fishing.md | done | check_bilingual 通过（81 对块，结构满足；仅 1 处数字锚点误报："December '15"→1915年） |
| 2026-10-15 | how-i-stalked-wilder-game-than-deer.md | done | check_bilingual 通过（100 对块，退出码 0）；术语表回填第 XXI 章人名/地名 19 条 |
- 2026-10-12 07:20｜批次3直启主代理｜dedication.md、endnotes.md 完成，check_bilingual 通过（内联翻译）
- 2026-10-13 06:19｜批次3直启子代理｜doctor-greenslade-theorises.md 完成，check_bilingual 通过

2026-10-13 06:32｜批次3直启子代理｜i-hear-of-the-three-hostages.md 完成，check_bilingual 通过
- 2026-10-13 06:43｜批次3直启子代理｜researches-in-the-subconscious.md 完成，check_bilingual 通过
- 2026-10-13 06:52｜批次3直启子代理｜i-make-the-acquaintance-of-a-popular-man.md 完成，check_bilingual 通过
- 2026-10-13 07:01｜批次3直启子代理｜the-thursday-club.md 完成，check_bilingual 通过
| 2026-10-15 | i-return-to-servitude.md | done | check_bilingual 通过（66 对块，退出码 0，无误报） |
| 2026-10-15 | i-am-introduced-to-strong-magic.md | done | check_bilingual 通过（86 对块，结构满足；仅 1 处数字锚点误报："6:30 p.m."→下午6点30分）；术语表回填第 IX 章词条 22 条 |
| 2026-10-15 | i-visit-the-fields-of-eden.md | done | check_bilingual 通过（89 对块，退出码 0，无误报）；圣歌/韵文沿用既有章节译法；术语表回填第 XIII 章地名/人名 19 条 |
| 2026-10-15 | machray.md | done | check_bilingual 通过（61 对块，退出码 0，零误报）；第 XX 章新词已定名待回填：克莱博迪勋爵（Lord Claybody）、格伦芬南勋爵（Lord Glenfinnan，即阿奇伯父亚历山大）、艾伦·麦克尼科尔（Alan Macnicol）、克拉赫格拉斯（Clach Glas）、斯古尔莫尔（Sgurr Mor）、宅畔草甸（Home Meadow）、花园水潭（Garden Pool） |
| 2026-10-15 | our-time-is-narrowed.md | done | check_bilingual 通过（99 对块，退出码 0，零误报）；liquidation 锁定「大清算」沿用既有译法；术语表回填第 XVI 章词条 11 条（克里斯蒂安尼亚、卑尔根、安德森、奥雷尔·斯坦因、巴纳德、多布森-雷、震怒之日、《田野》杂志、白腰草鹬等） |
| 2026-10-15 | sir-archibald-roylance-puts-his-foot-in-it.md | done | check_bilingual 通过（87 对块，退出码 0，零误报）；术语表回填第 XIV 章词条 13 条（托特纳姆宫路、大查尔斯街、托菲特、蒙马特、克莱尔小姐、怀蒙德姆小姐、亚历山大·汤姆森、多丽亚姨妈、南希·特拉弗斯、帕明特家、路西法、夏洛特·科黛、汉普顿宫），巴纳德首现归属修正为第 XIV 章 |
| 2026-10-15 | the-blind-spinner.md | done | check_bilingual 结构满足（25 对块；仅 2 处数字锚点误报："autumn of '17"→1917年、"Royal Academy, 1887"→1887年展，数字均在译文）；术语表回填第 VIII 章词条 13 条（帕尔米拉广场、福音橡、巴斯俱乐部、布莱顿、艾米斯福特夫人、威勒尔斯登、巴肯、卡斯尔-康内尔、德比大赛、厄尔斯语、乔克托语、毕士大池、下议院），Harlows/贾森首现归属修正为第 VIII 章 |
| 2026-10-15 | some-experiences-of-a-disciple.md | done | check_bilingual 通过（67 对块，退出码 0，零误报）；术语表回填第 VII 章词条 11 条（温莎森林、萨宁代尔勋爵、勒瓦瑟尔、凡·戴克、霍克白葡萄酒、利凡特人、摄政街、兰厄姆街、菲茨罗伊广场、麻鹬、麦克），「绿衣姑娘」首现归属修正为第 VII 章；帕尔米拉广场、德比大赛沿用既有定译 |
| 2026-10-15 | the-district-visitor-in-palmyra-square.md | done | check_bilingual 通过（50 对块，退出码 0，零误报）；术语表回填第 XVII 章词条 15 条（圣裘德堂、教区探访员、阿格尼丝·克拉克、埃尔茜·奥思韦特、拉德赫斯特、女王新月街、埃姆普森先生、女友谊会等）；源文隐形字符（U+FEFF/U+00A0/U+200A）在 Original 侧字节级保留 |
| 2026-10-15 | the-house-in-gospel-oak.md | done | check_bilingual 结构满足（38 对块，块内段落逐块对称；仅 1 处数字锚点误报："June day of 1914"→1914年6月，数字已在译文）；术语表回填第 VI 章词条 18 条（牛津街、马里波恩路、皇家美术学院、波特兰街、摄政公园、肯特、黑石、圣潘克拉斯、克勒肯维尔、格尔达、查茨沃斯、基钦纳别墅、西罗斯、北贝里克、慕尼黑、《泰晤士报》、法国国家图书馆、青春之国），帕尔米拉广场/福音橡/布雷达夫人首现归属修正为第 VI 章；源文 38 处 U+FEFF 在 Original 侧原样保留 |
| 2026-10-15 | the-night-of-the-first-of-june.md | done | check_bilingual 结构满足（83 对块；仅 2 处数字锚点误报：两处 "1914" 数字均在译文（「1914年6月」「1914年以来」），\b 于 CJK 边界失配）；术语表回填第 XVIII 章词条 38 条（维克托小姐、特灵、伊文霍、霍伊克、儒勒、阿斯科特、惠廷顿斯、彼得·皮纳尔、朝觐掮客等）；梅迪纳（人名）与麦地那（城名）按语境区分；源文隐形字符（U+FEFF×48/U+200A×7/U+00A0×1）在 Original 侧字节级保留 |
| 2026-10-15 | the-night-of-the-first-of-june-later.md | done | check_bilingual 通过（58 对块，退出码 0，零误报）；第 XIX 章系第十八章同一夜下半场，对齐主章译文与术语表：Miss Victor 依 XVIII 章新定词条译「维克托小姐」，阿德拉·维克多沿用既有定名；术语表回填第 XIX 章词条 12 条（加夫雷尔、辛迪加、詹姆斯党伯爵、眼墨、邓尼金、贞德、古龙水、死亡的灵药、哈弗汉姆、红脚鹬、皮姆利科、小鼠脑袋）；源文隐形字符（U+FEFF×96/U+200A×29/U+00A0×10）在 Original 侧字节级保留 |
- 2026-10-16 | confidences-at-a-wayside-inn | 直启批次3 子代理完成 | check 通过
