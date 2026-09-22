# 翻译计划：能干的麦克劳克林家

## 本计划信息

- **项目名称**：margaret-wilson_the-able-mclaughlins
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/小说文学.md
- **术语表**：术语表.md
- **执行模式**：委派（长篇；见 WORKFLOW.md「单篇翻译流程」）

## 执行步骤

单篇 9 步（读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志）以 `prompts/翻译计划模板.md`「执行步骤」为准，本文件不重复。委派模式下由主 agent 派单，子代理简报含黄金样本与前篇末尾。

## 篇目清单

由 `translation_queue.csv` 管理（22 篇，约 348KB）。

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
| 2026-09-14 | iv.md | 完成 | 4对块13段全译，check_bilingual exit 0；定名Allen/Dod/Sarah/Andy/Harvey Stowe/Gib McWhee/Waupsipinnikon已回填术语表 |
| 2026-09-14 | iii.md | done | 16对块52段全覆盖，check_bilingual exit0；弯引号校验通过；术语表回填13行 |
| 2026-09-14 | ii（第二章） | done | 19 对块、check_bilingual exit 0；术语音译 Allen艾伦/Stowe斯托/McNair麦克奈尔/Jeannie珍妮/Alex亚历克斯/Ayrshire艾尔郡/Waupsipinnikon沃普西平尼科尔等，详见术语表批次1补充 |
| 2026-09-14 | i（第一章） | done | 18对块66段全覆盖，check_bilingual exit 0；首译样板：叙述质朴坚实、苏格兰口语有力度； Hughie 从众改「休伊」、Iowa 从众改「艾奥瓦」，新增定名19条（戴维/玛丽/杰西/弗洛拉/詹姆斯/安德鲁/奈特先生/泰勒/多纳尔森堡/格兰特/林肯/谢尔曼/纽约论坛报/北方佬/愿你的烟囱长冒烟/bairns娃娃/sweeties糖果等）回填术语表 |
| 2026-09-14 | vi（第六章） | done | 9对块34段全覆盖，check_bilingual exit 0；中文弯引号19对校验通过；源文零宽字符(U+FEFF)已清理、Mrs.后不换行空格按源文保留；定名Squire乡绅、伍利之弟John约翰已回填术语表 |
| 2026-09-14 | v（第五章） | done | 18对块68段全覆盖，check_bilingual exit 0、语义错配0处；英文块与源文逐段字节一致、中文弯引号100对校验通过、无BOM；定名Peter Keith彼得·基思（区别家主之子彼得）、Tam McWhee塔姆·麦克威、Havers胡扯已回填术语表 |
| 2026-09-14 | vii（第七章） | done | 21对块63段全覆盖，check_bilingual exit 0，弯引号118对平衡无直引号；新定名西庇太/彭斯/南丁格尔/醉汉小径/独立日/新英格兰人/哭哭啼啼的娃娃已回填术语表；备考：vii源文两处实证伍利之父为John McLaughlin，与初版「Peter McLaughlin 家主」条冲突，供主agent复核 |
| 2026-09-14 | viii（第八章） | done | 12对块39段全覆盖，check_bilingual exit 0；弯引号44对校验通过、无直引号；新定名Barbara芭芭拉/Squire乡绅/Weir韦尔/Bob McNorkel鲍勃·麦克诺克尔/kist大木箱/laird大老爷已回填术语表；CSV doing→done 已双读确认 |
| 2026-09-14 | xi（第十一章） | done | 7对块25段全覆盖，check_bilingual exit 0；英文块与源文逐段字节一致（清理U+FEFF 6处、保留Mrs.后NBSP 8处），中文弯引号19对平衡无直引号、写盘管线直引号38处已程序化转回；新定名Janet珍妮特/Maggie Stewart玛吉·斯图尔特/Johnnie小约翰尼/Glasgow格拉斯哥/Quaker贵格派/crack闲扯/Hogmanay霍格马奈/curling冰上掷石戏/Metternich jacket梅特涅式短外套已回填术语表 |
| 2026-09-14 | xii（第十二章） | done | 20对块65段全覆盖，check_bilingual exit 0、错配0处；英文块与源文逐段字节一致，中文弯引号24对+单引号3对全平衡、无直引号、无BOM；新定名Glasgow格拉斯哥/McCreath麦克雷思/Geordie Sproul乔迪·斯普劳尔/lintie小雀儿/Johnnie约翰尼等已回填术语表；CSV doing→done 双读确认 |
| 2026-09-14 | x（第十章） | done | 16对块50段全覆盖，check_bilingual exit 0、可疑错配0处；英文块与清理FEFF后源文逐段字节一致；中文弯引号69对平衡、无直引号；新定名安迪·麦克菲/老约翰·麦克奈特/玛吉·斯图尔特/皮尔斯-箭/一月化冻/小珍妮已回填术语表；sty猪圈沿用viii/xii定名；CSV doing→done 双读确认 |
| 2026-09-14 | ix（第九章） | done | 30对块94段全覆盖，check_bilingual exit仅‘49→一八四九年’数字锚点误报；英文块与源文逐段一致（含U+200A发丝空格保留、零宽字符清理）、中文弯引号79对平衡无直引号、无BOM；新定名Iowa City艾奥瓦城/livery stable车马行/James McWhee詹姆斯·麦克威/gomeral傻小子已回填术语表 |
| 2026-09-14 | xiii（第十三章） | done | 8对块17段全覆盖，check_bilingual exit 0、可疑错配0处；英文块与源文逐段一致（St.后NBSP保留2处、U+FEFF零宽字符按惯例清理2处），中文弯引号12对平衡无直引号、无BOM；新定名Fisher's Grove费舍尔格罗夫/Professor Jamison詹米森教授/Isaiah《以赛亚书》/Scott司各特·Dickens狄更斯·Macaulay麦考利已回填术语表；CSV doing→done 双读确认 |
| 2026-09-14 | xv（第十五章） | done | 17对块72段全覆盖，check_bilingual exit 0、可疑错配0处；英文块与清理FEFF（20处）后源文逐段字节一致（保留U+200A发丝空格6处、Mrs.后NBSP 4处），中文弯引号96对平衡无直引号、无BOM；新定名Lammie小羊儿/Gib吉布/Jimmy McTaggert吉米·麦克塔格特/Aggie阿吉/O'Brien奥布赖恩/bach it已回填术语表；CSV doing→done 双读确认 |
| 2026-09-14 | xvi（第十六章） | done | 9对块20段全覆盖，check_bilingual exit 0、错配0处；英文块与清理FEFF(13处)后源文逐段字节一致，中文弯引号30对平衡无直引号、无BOM；沿用xv章定名Lammie小羊儿/麦克塔格特家的路口/吉米·麦克塔格特/奥布赖恩并修正初译「兰米」；新定名Young Sproul小斯普劳尔/Bob McWhee鲍勃·麦克威/Jennie Price小珍妮·普莱斯/John McCreath约翰·麦克雷思/Gib McTaggert吉布·麦克塔格特已回填术语表 |
| 2026-09-14 | xiv（第十四章） | done | 14对块43段全覆盖，check_bilingual exit 0；英文块与源文逐段字节一致（保留FEFF23处/NBSP1处/发丝空格2处），中文弯双引号52对平衡、无直引号、无BOM；新定名伍尔西/白尾鹞/奥布赖恩酒馆/约翰逊/麦克塔格特家路口/草皮玉米/迪豆/噗/安恩等已回填术语表；CSV doing→done 双读确认 |
| 2026-09-14 | xviii（第十八章） | done | 8对块29段全覆盖，check_bilingual exit 0、可疑错配0处；英文块与源文逐段字节一致（清理FEFF 13处、保留发丝空格1处），中文弯引号20对平衡无直引号、无BOM；新定名Aunt Flora弗洛拉姑姑/cradle摇架钐刀/Uncle Keith基思叔叔/goldenrod一枝黄花/A wee'an's bones小不点儿的一把骨头已回填术语表；CSV doing→done 双读确认 |
| 2026-09-14 | xx（第二十章） | done | 12对块51段全覆盖，check_bilingual exit 0、错配0处；英文块与源文逐段字节一致（FEFF13处、St./Mr./Mrs.后NBSP9处按源文保留），中文弯双引号50对+弯单引号3对平衡无直引号、无BOM；新定名Harmony哈莫尼/Jimmy Sproul吉米·斯普劳尔/Lyons County莱昂县/Great West大西部旅店/Pierson皮尔逊/tintype锡版照相/half section半区土地/elevator粮栈升运机房已回填术语表；CSV doing→done 双读确认 |
| 2026-09-14 | xvii（第十七章） | done | 16对块56段全覆盖，check_bilingual exit 0、可疑错配0处；英文块与清理FEFF（19处）后源文逐段字节一致（保留U+200A发丝空格5处），中文弯引号53对平衡无直引号、无BOM；新定名Davie McDowell戴维·麦克道威尔/Marget McDowell玛格特·麦克道威尔已回填术语表，沿用乔迪·斯普劳尔/莉比姑姑/奥布赖恩酒馆/胡扯等既定名；CSV todo→done 双读确认 |
| 2026-09-14 | xix（第十九章） | done | 9对块35段全覆盖，check_bilingual exit 0、可疑错配0处；英文块与清理FEFF（6处）后源文逐段字节一致（保留发丝空格1处），中文弯引号21对+单引号3对平衡、无直引号、无BOM；新定名Houghton霍顿/铁马/绿背纸币/修女纱/安息日客厅/提篮花样的拼布被/认捐单/普儿儿已回填术语表；沿用漂亮的小约翰尼（从xiii/xviii，与xvii「小宝贝约翰尼」并存备考）/莉比姑姑/乡绅之子约翰；CSV doing→done 双读确认 |
| 2026-09-14 | xxii（第二十二章·末章） | done | 5对块17段全覆盖，check_bilingual exit 0、可疑错配0处；英文块与源文逐段字节一致（FEFF 8处、发丝空格1处按源文保留），中文弯引号9对平衡无直引号、无BOM；新定名Nellie内莉已回填术语表；Lammie小羊儿系克丽丝蒂对幼子爱称（详见术语表备考）；CSV doing→done 双读确认 |
| 2026-09-14 | xxi（第二十一章） | done | 18对块86段全覆盖，check_bilingual exit 0、可疑错配0处；英文块与清理FEFF（9处，均在破折号前）后源文逐段字节一致，中文弯双引号68对平衡、无直引号、无BOM；本章无新专名，沿用伍利/克丽丝蒂/伊莎贝尔·麦克劳克林/莉比姑姑/莉比·基思/彼得·基思/车马行/独立日既定名，苏格兰语用法（I doubt只怕/Giddup驾/do evil作恶等）回填术语表；CSV doing→done 双读确认 |
| 2026-09-14 | 整书完结（22/22 章） | 全书 22 章批量复检通过（ix 数字锚点为 '49→一八四九年既定放行类） | 体例：「## 罗马数字 / 第N章」；首章代理回填 19 行硬约束+苏格兰语汇锁词（bairns=娃娃/Havers=胡扯/Lang may your lum reek=愿你的烟囱长冒烟）；主 agent 修正预设备注 3 处（Isobel=伍利之母/约翰之妻、Peter McLaughlin 非家主、Chirstie=伍利恋人——源文实证）；父名张力（ch2/7 约翰 vs ch15 暗示彼得）判原作歧异各随源文留审核；跨章自对齐：休伊/艾奥瓦/小羊儿/Lammie 双向统一 |
