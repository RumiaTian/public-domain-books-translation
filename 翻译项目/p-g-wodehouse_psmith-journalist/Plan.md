# 翻译计划：普史密斯记者

## 本计划信息

- **项目名称**：p-g-wodehouse_psmith-journalist
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/小说文学.md
- **术语表**：术语表.md
- **执行模式**：委派（长篇；见 WORKFLOW.md「单篇翻译流程」）

## 执行步骤

单篇 9 步（读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志）以 `prompts/翻译计划模板.md`「执行步骤」为准，本文件不重复。委派模式下由主 agent 派单，子代理简报含黄金样本与前篇末尾。

## 篇目清单

由 `translation_queue.csv` 管理（31 篇，约 322KB）。

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-09-05 | preface.md | done | 段A；序言，check 退出码 0，回填术语 5 条 |
| 2026-09-05 | [1308]额度中断收尾（批次2第17本进行中） | 2/31 done | 三段错峰开跑约3分钟即全线阵亡（限额05:44重置）；摸底回填：preface已done、a-friend-in-need过检回填done、the-honeyed-word无译文重置todo；【定名勘误】主代理误预置皮史密斯，段B临终裁定+主代理亲证in-the-city勘误记（501:0）后定稿普史密斯，a-friend-in-need机械回改21处，术语表锚点已勘误定稿；锁保留，下次启动优先断点续作本书 |
| 2026-09-05 | a-red-taximeter.md | done | 段A·夜2续作；check 仅数字锚点误报（84→八十四），回填术语 10 条 |
| 2026-09-05 | billy-windsor.md | done | 段A；check 退出码 0，回填术语 6 条（普格西/舒适时光/巴特·贾维斯等） |
| 2026-09-05 | an-addition-to-the-staff.md | done | 段A；check 退出码 0，回填术语 10 条（小子布雷迪/战斗编辑/铅头短棍等） |
| 2026-09-05 | cosy-moments.md | done | 段A；check 退出码 0，回填术语 8 条（威尔伯弗洛斯/阿舍/Moments栏目「××时光」系列定名） |
| 2026-09-05 | the-man-at-the-astor.md | done | 段C·夜2续作；check 退出码 0，回填术语 4 条（汤米/贺雷修斯/布拉-巴-纳-戈什/威利）；tenement 按 A 段回填定名「廉租公寓」改 3 处 |
| 2026-09-05 | the-honeyed-word.md | done | 段B·夜2续作；check 退出码 0，回填术语 4 条（沃特曼/斯皮勒/基德船长/尼克博克）；对齐段A定名威尔伯弗洛斯/《冥想时光》《欢笑时光》/B·亨德森·阿舍等 4 处 |
| 2026-09-05 | at-the-gardenia.md | done | 段A；check 退出码 0，回填术语 6 条（栀子花餐厅/M.C.C./弗雷迪同志等） |
| 2026-09-05 | the-highfield.md | done | 段C；check 退出码 0，回填术语 9 条（海菲尔德/哈莱姆河/旋风阿尔·沃尔曼/地铁/三报馆名等） |
| 2026-09-05 | bat-jarvis.md | done | 段A；check 退出码 0，回填术语 12 条（格鲁姆街帮/三叶草舞厅/坦慕尼厅/帮众四人组等） |
| 2026-09-05 | planning-improvements.md | done | 段B·夜2续作；check 退出码 0，回填术语 3 条（费城/萨斯喀彻温/一马镇＋司各特诗句注） |
| 2026-09-05 | an-episode-by-the-way.md | done | 段A；check 退出码 0，回填术语 9 条（三点帮/桌山帮/纨绔子道森/蜘蛛莱利/科斯顿等）；敏感绰号按公版文学规范处理 |
| 2026-09-05 | going-some.md | done | 段C；check 退出码 0，回填术语 8 条（弗朗西斯·帕克/普莱森特街/神枪手卡斯伯特/奥布里·博德金等） |
| 2026-09-05 | in-pleasant-street.md | done | 段B·夜2续作；check 退出码 0，回填术语 7 条（奥洛尼/意面同志/wop·Dago 规范等）；对齐段A定名桌山帮/蜘蛛莱利 2 处 |
| 2026-09-05 | a-gathering-of-cat-specialists.md | done | 段A；check 退出码 0，回填术语 10 条（怀特普莱恩斯/安哥拉猫/猫薄荷/skiddoo 等）；写盘时一处草稿误植已修复重验 |
| 2026-09-05 | the-knockout-for-mr-waring.md | done | 段C；check 退出码 0，回填术语 4 条（斯图尔特·沃林/布伦金索普香膏/自由大厅/国际银行）；1 处英文块笔误自纠 |
| 2026-09-05 | the-tenements.md | done | 段C；check 退出码 0，回填术语 3 条（新亚银行系列定名/里斯本苹果/用武之地） |
| 2026-09-05 | full-steam-ahead.md | done | 段B·夜2续作；check 退出码 0，回填术语 6 条（人人杂志/疯狂金融/珍珠街/二房东等） |
| 2026-09-05 | concerning-mr-waring.md | done | 段A；check 退出码 0，回填术语 7 条（古奇/市议员/建筑局长/埃迪·伍德/高筒帽等）；沃林条目与段C合并去重 |
| 2026-09-05 | reviewing-the-situation.md | done | 段C；check 退出码 0，回填术语 2 条（无双小子/埃德格伦与泰德） |
| 2026-09-05 | guerilla-warfare.md | done | 段B·夜2续作；check 退出码 0，回填术语 5 条（蒙克·伊斯曼/小子特威斯特/惠勒/哈里根/辛格大厦） |
| 2026-09-05 | cornered.md | done | 段A；check 退出码 0，回填术语 7 条（新新监狱/妮莉/琼斯先生/珀西/小黑洞等）；段A·夜2续作 10 篇全部完成 |
| 2026-09-05 | trapped.md | done | 段C；check 退出码 0，回填术语 7 条（比夫维尔/冯·毛奇/阿尔忒缪斯·沃德/布伦海姆橙等）；the Island 对齐既有定名布莱克韦尔岛 |
| 2026-09-05 | visitors-at-the-office.md | done | 段C；check 退出码 0，回填术语 2 条（麦迪逊大道/第三十街＋外交微笑与甜言蜜语对齐 VIII 章题） |
| 2026-09-05 | conclusion.md | done | 段C；终篇译毕；check 退出码 0，回填术语 3 条（埃迪·伍德/伊顿六月四日/学监与两块大洋） |
| 2026-09-05 | psmith-concludes-his-ride.md | done | 段B·夜2续作；check 退出码 0，回填术语 6 条（科利尔/墨西哥来客/布莱克韦尔岛/纳索街等） |
| 2026-09-05 | the-first-battle.md | done | 段B·夜2续作；check 退出码 0，回填术语 4 条（马丁·凯利/威利·哈维/乔·彼得森/警棍）；一处英文残留自纠重验 |
| 2026-09-05 | the-battle-of-pleasant-street.md | done | 段B·夜2续作；check 退出码 0，回填术语 7 条（山姆/库克医生北极/罗斯福大棒/拉丁法语引用等） |
| 2026-09-05 | reductions-in-the-staff.md | done | 段B·夜2续作；check 退出码 0，回填术语 9 条（杰斐逊市场/华盛顿广场/杰夫里斯/凯特尔/坐牢主编等） |
| 2026-09-05 | standing-room-only.md | done | 段B·夜2续作；check 退出码 0，回填术语 4 条（墨西哥人乔/昆斯伯里规则/赞姆巴克/P不发音例证词）；段B·夜2续作 10 篇全部完成 |
| 2026-09-05 | 整书完结（批次2第17本） | 31/31 done | 夜1开译2篇遭[1308]，夜2三段错峰续作29篇一次跑通（10/10/9）；系列定名普史密斯全书485处零皮史密斯泄漏；【事故】三段并发写CSV互相覆写9行done，段B三重验证（译文存在+check过检+Plan日志）后set_status修复；主代理全量复验31件（30件exit 0，1件数字锚点误报），术语回填190+条 |
