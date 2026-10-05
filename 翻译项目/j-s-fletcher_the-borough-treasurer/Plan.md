# 翻译计划（j-s-fletcher_the-borough-treasurer）

## 本计划信息

- **项目名称**：j-s-fletcher_the-borough-treasurer（The Borough Treasurer）
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/小说文学.md
- **术语表**：术语表.md

## 文件分工

| 文件 | 作用 | 谁来改 |
|------|------|--------|
| `项目说明.md` | 项目基本信息、领域配置 | 人工 |
| `术语表.md` | 翻译硬约束层，每篇译完补充新词 | agent / 人工 |
| `translation_queue.csv` | 任务队列（file,size_kb,status） | 翻译前改 doing，完成后改 done（双写根表） |
| `Plan.md`（本文件） | 执行步骤 + 运行日志 | agent 追加日志 |
| `原文/*.md` | 源文 | 不改 |
| `译文/*.zh-CN.md` | 译文产出（块对照双语） | 翻译 agent 产出 |

执行步骤按 `prompts/翻译计划模板.md`（9 步：读配置→取 todo→doing→读源文→翻译→自检→check_bilingual→双写 done→日志）。

## 篇目清单

共 31 篇，见 `translation_queue.csv`（合计 441KB）。

## 运行日志

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
| 2026-09-25 | chapter-3.md | done | check_bilingual 通过（10 对 Original/Chinese，退出码 0） |
| 2026-09-25 | chapter-2.md | done | 双语块对照 9 对，check_bilingual 退出码 0 |
| 2026-09-25 | chapter-1.md | done | 首章开译定名（人名/地名/职衔入术语表）；check_bilingual 通过：14 对块、60 段、退出码 0 |
| 2026-09-25 | chapter-4.md | done | check_bilingual 通过（10 对 Original/Chinese，退出码 0） |
| 2026-09-25 | chapter-5.md | done | check_bilingual 通过（16 对 Original/Chinese，退出码 0） |
| 2026-09-25 | chapter-6.md | done | check_bilingual 通过（14 对 Original/Chinese，退出码 0）；新定名哈伯勒/艾维丝/绅士杰克/诺思罗普已回写术语表 |
| 2026-09-25 | chapter-7.md | done | check_bilingual 通过（16 对 Original/Chinese，退出码 0）；新定名：哈伯勒、诺卡斯特、海吉尔枢纽站、警司、警佐入术语表 |
| 2026-09-25 | chapter-8.md | done | check_bilingual 通过（18 对 Original/Chinese，退出码 0）；新定名治安法官/出庭律师/事务律师等已回写术语表；superintendent/your Worship 依 chapter-7 定名（警司/阁下）统一 |
| 2026-09-25 | chapter-9.md | done | check_bilingual 通过（15 对 Original/Chinese，退出码 0）；新定名诺卡斯特/克里斯托弗·佩特/斯蒂尔曼少校等 16 条已回写术语表 |
| 2026-09-25 | chapter-11.md | done | check_bilingual 通过（14 对 Original/Chinese，退出码 0）；新定名克里斯托弗·佩特/波帕姆与皮尔布迪/卡西特街/雷利特/手电筒/遗嘱附录等已回写术语表 |
| 2026-09-25 | chapter-10.md | done | check_bilingual 通过（7 对 Original/Chinese，退出码 0）；新定名治安法庭/布莱顿/草顶上的洞等已回写术语表；superintendent 依 chapter-7/8 定名译「警司」 |
| 2026-09-25 | chapter-12.md | done | check_bilingual 通过（12 对 Original/Chinese，退出码 0）；新定名父亲的焦虑（章名）/死因审讯/道森与福格/小暖阁/特许结婚证已回写术语表 |
| 2026-09-25 | chapter-13.md | done | check_bilingual 通过（12 对 Original/Chinese，退出码 0）；新定名吉福德·布里尔顿/赫伯特·斯通纳/《泰晤士报》/验尸官/“海马基特财库待补”等已回写术语表；inquest 依 chapter-12 定名（死因审讯）对齐 |
| 2026-09-25 | chapter-14.md | done | check_bilingual 通过（8 对 Original/Chinese，退出码 0）；新定名塔林顿/灰母马旅馆/波斯蒂克/波普西/戴维·迈勒/达灵顿/一纸数字（章名）等已回写术语表 |
| 2026-09-25 | chapter-15.md | done | check_bilingual 通过（10 对 Original/Chinese，退出码 0）；新定名一环扣一环/珀西/马洛斯与奇德福思案/雄鹿与猎犬/半张大裁纸等 13 条已回写术语表；Tallington 依 chapter-14 定名（塔林顿）对齐 |
| 2026-09-25 | chapter-16.md | done | check_bilingual 通过（11 对 Original/Chinese，退出码 0）；新定名孤寂的荒原（章名）/荒原/菲瑟比小姐/杓鹬/废弃采石场/事后从犯等已回写术语表；马洛斯/奇德福思/戴夫/封口费依 chapter-15、迈勒/塔林顿/达灵顿依 chapter-14 定名对齐 |
| 2026-09-25 | chapter-18.md | done | check_bilingual 通过（9 对 Original/Chinese，退出码 0）；新定名剪贴簿（章名）/约翰·马洛斯/马克·奇德福思/《威尔切斯特卫哨报》/哈姆韦特太太/霍布威克采石场等已回写术语表；Mallows/Chidforth/Wilchester Assizes 依 chapter-15/1 定名（马洛斯/奇德福思/威尔切斯特巡回法庭）对齐 |
| 2026-09-25 | chapter-17.md | done | check_bilingual 通过（13 对 Original/Chinese，退出码 0）；新定名医学见解（章名）/巴特利太太/总务委员会/停尸房/海马基特纹章旅馆/查票员/查特班克/防身短棒等已回写术语表；荒原/霍布威克采石场依 chapter-16/18 定名对齐 |
| 2026-09-25 | chapter-19.md | done | check_bilingual 通过（15 对 Original/Chinese，退出码 0）；新定名穿灰衣的高个男人（章名）/哈姆韦特太太/善灵冈/赫克森代尔/海马基特肖山林等已回写术语表；crowner 依 chapter-13 定名（验尸官）、偷猎依 chapter-10 定名对齐 |
| 2026-09-25 | chapter-21.md | done | check_bilingual 通过（6 对 Original/Chinese，退出码 0）；新定名中断的逃亡（章名）/布拉德肖/金边证券/逮捕令/验尸官属员等已回写术语表；Hobwick Quarry/海马基特纹章旅馆/警司/阁下 依 chapter-18/17/7 定名对齐 |
| 2026-09-25 | chapter-22.md | done | check_bilingual 通过（7 对 Original/Chinese，退出码 0）；新定名黑暗中的手（章名）/治安法官（justice of the peace）/保释/重罪与轻罪/诺卡斯特监狱/半克朗银币/矮林/下城等已回写术语表；警司/被告席/证人席/霍布威克采石场/肖山/海马基特纹章旅馆/蹲过大牢等依前章定名对齐 |
| 2026-09-25 | chapter-23.md | done | check 通过（12 对块）；译后代理[1308]中断，事后验收收编补账 |
| 2026-09-26 | chapter-25.md | done | check_bilingual 通过（9 对 Original/Chinese，退出码 0）；新定名再无新证（章名）/拘押牢房/控方律师/撤回指控/蓄意谋杀/治安法庭书记官等已回写术语表；诺卡斯特监狱/矮林（spinney）/橡木手杖/各位阁下依 chapter-22/16/7 定名对齐 |
| 2026-09-26 | chapter-20.md | done | check_bilingual 通过（15 对 Original/Chinese，退出码 0）；新定名困兽（章名）/里维埃拉/男傧相/当枪使/吸墨纸板等已回写术语表；spinney 依 chapter-22/25 定名（矮林）对齐；警司/剪贴簿/皮夹/霍布威克采石场/司库/封口费/伯特·斯通纳/威尔切斯特巡回法庭 依前章定名对齐 |
| 2026-09-26 | chapter-24.md | done | check_bilingual 通过（13 对 Original/Chinese，退出码 0）；新定名严格的生意规矩（章名）/罐装肉酱三明治/摩卡/朗姆酒/窝藏/诺卡斯特码头/家具搬运行/干雪利酒/欧洲大陆等已回写术语表；High Gill 依 chapter-7/16 作海吉尔、诺卡斯特监狱/延期再审依 chapter-22、海马基特纹章旅馆/酒吧雅座依 chapter-17/14、热酒/头巾帽依 chapter-23 定名对齐 |
| 2026-09-26 | chapter-28.md | done | check_bilingual 通过（7 对 Original/Chinese，退出码 0）；新定名往昔书页（章名）/雷斯韦特/卡法克斯/斯托布/莱金/苏格兰场/私家侦探/图基党徒/死于意外等已回写术语表；Wraythwaite/Carfax/Stobb/Leykin 为 ch27/28 首现人物新定名；斯蒂尔曼少校/坎大哈村舍/皇家贝尔维迪尔旅馆/库房主管/被服主管依 chapter-9、女管家依 chapter-9、死因审讯依 chapter-12、记事簿依 chapter-10 定名对齐 |
| 2026-09-26 | chapter-27.md | done | check_bilingual 通过（12 对 Original/Chinese，退出码 0）；新定名雷伊的雷思韦特先生（章名）/雷思韦特/雷伊/卡法克斯/公爵头旅馆/威勒比与哈格里夫斯/特威德河/不在场证明/奶兄弟等已回写术语表；证人席/偷猎/赫克森代尔/集市广场/巡回法庭/诺思罗普太太 依前章定名对齐 |
| 2026-09-26 | chapter-26.md | done | check_bilingual 通过（12 对 Original/Chinese，退出码 0）；新定名猜疑的美德（章名）/斯蒂尔比/格拉德斯顿/斯特劳森/篷车/验尸陪审团/高等法院/巡回区/睡前酒/老母夜叉等已回写术语表；大礼帽/小山羊皮手套/诺卡斯特码头/家具搬运行/头巾帽依 chapter-24/23、死因审讯/蓄意谋杀/当庭开释依 chapter-12/25、热酒/左轮手枪依 chapter-23/21 定名对齐 |
| 2026-09-26 | chapter-29.md | done | check_bilingual 通过（4 对 Original/Chinese，退出码 0）；新定名不计后果（章名）/护墙板/走道（entry）/克里斯·佩特（Chris）已回写术语表；头巾帽/村舍/起居室/由起居室改成的卧房/老太太（missis）依 chapter-23/24、马甲/左轮手枪依 chapter-21/22、荒原依 chapter-16 定名对齐 |
| 2026-09-26 | chapter-31.md | done | check_bilingual 通过（3 对 Original/Chinese，退出码 0，全书终章）；新定名出庭律师的酬金（章名）/管家兼经理人（steward and agent）/管家宅子/边境（the Border）已回写术语表；雷思韦特/雷伊/奶兄弟依 chapter-27/28 定名对齐；布里尔顿/艾维丝/本特/莱蒂/马拉柳/肖山/海马基特/诺卡斯特依全书通行定名 |
| 2026-09-26 | chapter-30.md | done | check_bilingual 通过（23 对 Original/Chinese，退出码 0）；新定名科瑟斯通（章名）/国王证人/重犯之友/资深议员（alderman）/牛眼提灯/史密斯已回写术语表；诺卡斯特监狱/集市广场/巡回区/纹章旅馆/司库/荒原/死因审讯/前科犯/皮夹/沃金/小本特/警察局 依前章定名对齐 |
| 2026-09-26 | 整书完结流转 | 31/31 done | 批次1直启：全书 31 章全部 check 通过；两日译毕，历经[1308]中断（ch20/ch23 断点收编重派）；并行撞名 Wraythwaite 已裁定统一雷思韦特；删锁流转 |
