# 翻译计划：牧师与医生一家

## 本计划信息

- **项目名称**：margaret-oliphant_the-rector-and-the-doctors-family
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/小说文学.md
- **术语表**：术语表.md
- **执行模式**：委派（短篇集；见 WORKFLOW.md「单篇翻译流程」）

## 执行步骤

单篇 9 步（读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志）以 `prompts/翻译计划模板.md`「执行步骤」为准，本文件不重复。委派模式下由主 agent 派单，子代理简报含黄金样本与前篇末尾。

## 篇目清单

由 `translation_queue.csv` 管理（24 篇，约 370KB）。

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
| 2026-09-10 | ii-2.md（医生的家人 II） | done | check_bilingual/check_coverage 均 0；11 对块；新定名：莱德/弗雷德/弗雷德里克/妮蒂/苏珊/贝西·克里斯琴/玛丽 |
| 2026-09-10 | iv-2.md（IV） | done | check_bilingual/check_coverage 均 0；8 对块；沿用已定名；新定名待回填：露西·伍德豪斯（Lucy Wodehouse）/安德伍德小姐（Miss Underwood）/泰坦妮亚（Titania）/史密斯太太（Mrs. Smith）/圣罗克小屋（St. Roque's Cottage） |
| 2026-09-10 | i-2.md（医生的家人 I） | done | check_bilingual/check_coverage 均 0；5 对块（每 3 段一组）；Rider 依 ii-2 定名莱德；新定名待回填：马杰里班克斯（Marjoribanks）/爱德华·莱德（Edward Rider）/内德（Ned）/弗雷德（Fred）/贝西·克里斯琴（Bessie Christian）/格兰奇巷（Grange Lane）/格罗夫街（Grove Street） |
| 2026-09-10 | iii-2.md（III） | done | check_bilingual/check_coverage 均 0；8 对块；沿用既定名（莱德/爱德华·莱德/弗雷德/妮蒂/苏珊/贝西·克里斯琴/安德伍德小姐/泰坦妮亚/圣罗克/史密斯/伍德豪斯/马杰里班克斯/格兰奇巷/卡林福德）；新定名待回填：弗雷迪（Freddy，家中男孩）/蓝猪旅馆（the Blue Boar）/圣罗克教堂（St. Roque's）/弗雷德太太（Mrs. Fred，叙述中对苏珊的称呼） |
| 2026-09-10 | i.md（牧师 I） | done | check_bilingual/check_coverage 均 0；10 对块；沿用已定名：卡林福德/莱德/圣罗克/露西·伍德豪斯/副牧师；新定名待回填：普罗克特牧师（Mr. Proctor，表内已有）/伯里先生（Mr. Bury）/伍德豪斯先生（Mr. Wodehouse）/伍德豪斯小姐（Miss Wodehouse）/玛丽（Mary，昵称莫莉 Molly）/弗兰克·温特沃斯牧师（Rev. Frank Wentworth）/撒冷礼拜堂（Salem Chapel）/万灵学院（All Souls）/牧师（Rector）/常驻副牧师（perpetual curate） |
| 2026-09-10 | ii.md（牧师 II） | done | check_bilingual/check_coverage 均 0；13 对块（每 3 段一组，末块 4 段）；沿用已定名：普罗克特牧师/露西·伍德豪斯/圣罗克教堂系；新定名待回填：教区长（Rector）/莫利（Morley）/老普罗克特太太（old Mrs. Proctor）/伍德豪斯先生（Mr. Wodehouse）/伍德豪斯小姐（Miss Wodehouse 长姐）/伯里先生（Mr. Bury）/温特沃斯先生（Mr. Wentworth）/圣罗克教堂（St. Roque's）/万灵学院（All Souls）/研究员（Fellow of All Souls）/德文郡（Devonshire）/牧师宅（rectory）/教堂执事（churchwarden）/非国教（Dissent） |
| 2026-09-10 | iii.md（III） | done | check_bilingual/check_coverage 均 0；8 对块；沿用既定名（普罗克特牧师/牧师/伍德豪斯小姐/露西·伍德豪斯/弗兰克·温特沃斯/撒冷礼拜堂/万灵学院/常驻副牧师/格罗夫街/卡林福德）；新定名待回填：索福克勒斯（Sophocles）/摩根（Morgan）/德文郡（Devonshire）/普罗克特太太（Mrs. Proctor） |
| 2026-09-10 | iv.md（牧师 IV） | done | check_bilingual/check_coverage 均 0；12 对块（块内 1-2 段）；沿用既定名：普罗克特牧师/莫利/普罗克特太太/摩根/德文郡/露西·伍德豪斯/伍德豪斯小姐/伯里先生/温特沃斯先生/圣罗克教堂/万灵学院/常驻副牧师/研究员/不奉国教者；新定名待回填：利先生（Mr. Leigh，副牧师）/圣贾尔斯街（St. Giles's，牛津）/极乐世界（Elysium） |
| 2026-09-10 | v.md（V） | done | check_bilingual/check_coverage 均 0；6 对块（块对照 1+4+4+4+4+2 段）；沿用既定名（卡林福德/妮蒂/弗雷德/弗雷迪/苏珊/伍德豪斯小姐/露西/温特沃斯先生/常驻副牧师/莱德太太/爱德华·莱德/贝西·克里斯琴/布朗太太/圣罗克小屋/圣罗克教堂/史密斯太太/格兰奇巷/撒克逊/小女杰）；新定名待回填：吉尔伯特·斯科特（Gilbert Scott，建筑师）/约翰尼（Johnnie，家中男孩）/米迦勒节雏菊（Michaelmas daisies） |
| vii.md | 2026-09-10 | done | 块对照 7 对；过检通过；新定名：爱德华·莱德、妮蒂、小弗雷迪、圣罗克小屋、安德伍德小姐、史密斯先生/太太、弗雷德太太、爱德华医生（妮蒂对 Edward Rider 的称呼） |
| x.md | done | 译文/x.zh-CN.md | 16 对块 | check_bilingual/check_coverage 通过（退出码 0），无错配；术语沿用既有定名，无新定名 |
| 2026-09-10 | 子代理单章翻译 | +1 | 12700 | 0 | viii.md 单章直译完成（9 对块），check_bilingual/check_coverage 退出码 0，状态 done |
| vi.md | 2026-09-10 | done | 译文/vi.zh-CN.md | 21 对块（每块 1 段，长段独立成块） | check_bilingual/check_coverage 退出码 0、无错配；沿用既定名：妮蒂/弗雷德（爱德华之兄）/弗雷德太太/弗雷迪/苏珊/史密斯太太/爱德华·莱德/安德伍德小姐/马杰里班克斯医生/格兰奇巷/圣罗克小屋/圣罗克教堂/伍德豪斯小姐/温特沃斯先生/弗兰克·温特沃斯牧师/卡林福德/莱德太太；无新定名，人名首现括注按全书惯例标注 |
| xi.md | 2026-09-10 | done | 译文/xi.zh-CN.md | 2 对块（每块 1 段，两个长段各自成块） | check_bilingual/check_coverage 退出码 0、无错配；沿用既定名：妮蒂/苏珊/弗雷德/爱德华·莱德/史密斯太太/史密斯/卡林福德/租屋/小鬼/莱德太太；无新定名 |
| 2026-09-10 | xii.md（XII） | done | check_bilingual/check_coverage 均 0（24 对块，块内 1-3 段，无可疑错配/漏译）；沿用既定名：妮蒂/弗雷德/苏珊/弗雷德太太/小弗雷迪/爱德华·莱德/莱德医生/爱德华医生/温特沃斯先生/伍德豪斯小姐/露西/马杰里班克斯小姐/贝西·克里斯琴/史密斯太太/圣罗克小屋/格兰奇巷/殖民地/马车/泰坦妮亚/莱德太太；新定名待回填：理查德·查塔姆（Richard Chatham）/墨尔本（Melbourne）/约翰·布朗太太（Mrs. John Brown）/回马箭（Parthian shot） |
| xv.md（XV） | 2026-09-10 | done | check_bilingual/check_coverage 均 0（6 对块，首块为超长整段独立成块，与 vi/xi 章块法一致，无可疑错配/漏译）；沿用既定名：爱德华·莱德/莱德医生/妮蒂/弗雷德/苏珊（史密斯太太转述中）/史密斯太太/史密斯/玛丽/卡林福德/格兰奇巷/圣罗克小屋/伍德豪斯先生/温特沃斯先生/副牧师；新定名待回填：澳洲丛林人（Bushman，首现「高大的澳洲丛林人（Bushman）」） |
| 2026-09-10 | xiii.md（XIII，查塔姆来访） | done | 译文/xiii.zh-CN.md | 7 对块（超长段独立成块，对话每 3 段一组） | check_bilingual/check_coverage 退出码 0、0 处可疑；沿用既定名：卡林福德/妮蒂/弗雷德/弗雷迪/小弗雷迪/苏珊（姐姐）/弗雷德太太/爱德华·莱德/爱德华医生/莱德太太/利先生/伍德豪斯小姐/露西·伍德豪斯/常驻副牧师/圣罗克小屋/圣罗克教堂/蓝猪旅馆/乔治街/格兰奇巷；新定名待回填术语表：理查德·查塔姆（Richard Chatham）/查塔姆先生/澳洲丛林人（Bushman，与xv章定名一致）/丛林莽汉（Bushranger）/仁慈姊妹会（sisterhood of mercy）/滴漏不止（the continual dropping，圣经典故） |
| xvi.md（XVI，妮蒂定策装箱、查塔姆苏珊宣布婚约） | 2026-09-10 | done | 译文/xvi.zh-CN.md | 19 对块（超长段独立成块，对话每 3 段一组） | check_bilingual/check_coverage 退出码 0、0 处可疑；沿用既定名：妮蒂/苏珊（姐姐）/弗雷德太太/弗雷德/查塔姆先生/澳洲丛林人/史密斯太太/史密斯/爱德华·莱德/莱德医生/爱德华医生/卡林福德/格兰奇巷/玛丽/泰坦妮亚；无新定名 |
| xiv.md | 2026-09-10 | done | 译文/xiv.zh-CN.md | 9 对块（两个超长叙述段各自成块，短段 3-5 段一组） | check_bilingual/check_coverage 退出码 0、无错配；沿用既定名：伍德豪斯先生/伍德豪斯小姐/露西·伍德豪斯/温特沃斯先生/常驻副牧师/妮蒂/弗雷迪/苏珊/史密斯太太/爱德华·莱德/爱德华医生/莱德医生/圣罗克教堂/圣罗克小屋/卡林福德/马杰里班克斯小姐/马杰里班克斯医生/莫莉/贝西；新定名待回填：查塔姆先生（Mr. Chatham，澳大利亚来客）/丛林客（Bushman，叙述中对查塔姆的绰称）/玛土撒拉（Methuselah，圣经人名） |
| 2026-09-10 | xvii.md（XVII，终章定情） | done | 译文/xvii.zh-CN.md | 9 对块（超长段独立成块，对话每 2-5 段一组） | check_bilingual/check_coverage 退出码 0、0 处可疑；沿用既定名：卡林福德/妮蒂/弗雷迪/小弗雷迪/苏珊/弗雷德太太/爱德华·莱德/莱德医生/爱德华医生/理查德·查塔姆/圣罗克/圣罗克小屋/格兰奇巷/蓝猪旅馆/露西·伍德豪斯/殖民地/马车/极乐世界；新定名待回填术语表：丘比特（Cupid） |
| xviii.md（XVIII，全书终章） | 2026-09-10 | done | 译文/xviii.zh-CN.md | 4 对块（对话 3+3 段一组，两个叙事长段各自成块） | check_bilingual/check_coverage 退出码 0、0 处可疑；沿用既定名：伍德豪斯小姐/露西/温特沃斯先生/常驻副牧师/妮蒂/弗雷迪/小弗雷迪/弗雷德/弗雷德太太/苏珊/查塔姆先生/莱德医生/马杰里班克斯医生/马杰里班克斯小姐/玛丽/卡林福德/格罗夫街/格兰奇巷/圣罗克教堂/圣罗克小屋/小鬼/女杰；新定名：皇家外科医师学会会员（M.R.C.S.） |
| the-doctor-s-family.md（《医生的家人》扉页） | 2026-09-10 | done | 译文/the-doctor-s-family.zh-CN.md | 纯标题件（原文 25 字节，仅一行章名，无正文块） | check_bilingual/check_coverage 退出码 0；标题单行合并为 The Doctor’s Family / 医生的家人，与全书既有定名（医生的家人）一致 |
| the-rector.md（《牧师》扉页） | 2026-09-10 | done | 译文/the-rector.zh-CN.md | 纯标题件（原文 14 字节，仅一行章名，无正文块） | check_bilingual/check_coverage 退出码 0；标题单行合并为 The Rector / 牧师，与全书项目名《牧师与医生一家》定名一致（教区长为职衔译名，书名沿用牧师） |
2026-09-11｜批次2｜整书完结：24/24 全部 done，删认领锁。
2026-09-11｜批次2｜勘误：完结日志误发——ix.md（21.2KB）此前因队列视图竞态漏派，仍为 todo，锁已恢复，ix 落地后重新走完结流转。
2026-09-11｜补派单篇｜ix.md（IX，幻灭初临·弗雷德夜出未归至运河寻尸）｜done｜译文/ix.zh-CN.md｜18 对块（超长叙事段各自成块，对话段逐段成块，与 x 章块法一致）｜check_bilingual/check_coverage 退出码 0、0 处可疑；沿用既定名：妮蒂/弗雷德/苏珊/爱德华·莱德/莱德医生/爱德华医生/史密斯太太/马杰里班克斯医生/马杰里班克斯小姐/伍德豪斯先生/贝西·克里斯琴/卡林福德/圣罗克小屋；新定名：提泰妮娅（Titania）
2026-09-11｜批次2｜整书完结确认：24/24 全部 done（含 ix.md 补派），删认领锁。
