# 翻译计划：不安之财

## 本计划信息

- **项目名称**：p-g-wodehouse_uneasy-money
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/小说文学.md
- **术语表**：术语表.md
- **执行模式**：委派（长篇；见 WORKFLOW.md「单篇翻译流程」）

## 执行步骤

单篇 9 步（读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志）以 `prompts/翻译计划模板.md`「执行步骤」为准，本文件不重复。委派模式下由主 agent 派单，子代理简报含黄金样本与前篇末尾。

## 篇目清单

由 `translation_queue.csv` 管理（26 篇，约 385KB）。

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
| 2026-09-13 | dedication（献词页） | done | 1 对块，check_bilingual exit 0；无专名，术语表无需回填 |
| 2026-09-13 | iii（第三章） | done | 14 对块（逐块段数奇偶校验通过），check_bilingual exit 0；弯引号校验合规；术语表回填 15 行 |
| 2026-09-13 | ii（第二章） | done | 13 对块 63 段，check_bilingual exit 0；写盘直引号已程序化转回弯引号；Dawlish 从Ⅲ定名「达利什」；术语表回填 7 行 |
| 2026-09-13 | i（第一章） | done | 28 对块 123 段，check_bilingual exit 0；原文块逐行取自源文零走样，中文块弯引号校验合规；首章定名勋爵全名、Ira Nutcombe=艾拉·纳特科姆等 21 行回填术语表；Brown's 已对齐Ⅱ定名「布朗氏俱乐部」 |
| 2026-09-13 | v（第五章） | done | 18 对块 82 段，check_bilingual exit 0；原文块由脚本按源文件行合并（零走样，含 U+FEFF 等不可见字符），中文块弯引号校验合规（0 直引号）；Elizabeth Boyd=伊丽莎白·博伊德、Brookport=布鲁克波特等 13 行回填术语表 |
| 2026-09-13 | vii（第七章） | done | 27 对块 109 段，check_bilingual exit 0；原文块脚本按行合并零走样，中文块弯引号校验合规；Ⅶ章纳蒂=纳蒂·博伊德（与比尔同席，非比尔本人），译文保持中性归属；the Good Sport=「爽快姑娘」、《普绪克之梦》等 17 行回填术语表 |
| 2026-09-13 | iv（第四章） | done | 25 对块 105 段（英文块按行号取自源文零走样），check_bilingual exit 0；中文块弯引号校验合规，括注英文撇号统一 U+2019；跨段台词按中文体例逐段起引号、末段收引号；术语表补 9 行（珀金斯、林肯律师学院广场、沃尔顿希思等；律所全名与Ⅴ章定名一致不重复）；CSV doing→done 双重读确认 |
| 2026-09-13 | vi（第六章） | done | 29 对块 114 段（三行诗引与两处 --- 场景分隔照源保留，英文块程序化逐行取自源文零走样），check_bilingual exit 0；中文块弯双引号/内嵌弯单引号校验合规；the Good Sport 对齐Ⅶ定名「爽快姑娘」16 处；术语表回填黛西·伦纳德、海因里希·约尔格等 12 行；CSV doing→done 双重读确认 |
| 2026-09-13 | xi（第十一章） | done | 5 对块 14 段（英文块按行号程序化取自源文零走样，含 7 处 U+FEFF），check_bilingual exit 0；中文块弯双引号校验合规（0 直引号），括注英文撇号统一 U+2019；全章无新专名，术语表无需回填；CSV doing→done 双重读确认（间隔 6 秒×2） |
| 2026-09-13 | viii（第八章） | done | 9 对块 32 段（英文块逐行取自源文零走样，含 U+FEFF 隐藏字符），check_bilingual exit 0；中文块弯双引号/内嵌弯单引号校验合规（0 直引号），补译漏句 1 处后复核通过；术语表回填“空中嬉戏”、皮尔餐厅、伦纳德小姐、舅舅艾拉 4 行；CSV doing→done 双重读确认 |
| 2026-09-13 | xiv（第十四章） | done | 25 对块 106 段（英文块按行号程序化取自源文零走样，含 15 处 U+FEFF、2 处 U+00A0），check_bilingual exit 0；中文块弯双引号校验合规（0 直引号）；拉丁文 suggestio falsi 保留原词括注意；术语表回填印度棒、白色大道、suggestio falsi 3 行；CSV doing→done 双重读确认（间隔 6 秒×2） |
| 2026-09-13 | xvi（第十六章） | done | 26 对块 106 段（英文块按行号程序化取自源文零走样，20 处 U+FEFF、64 处 U+2019 原样保留），check_bilingual exit 0；中文块弯双引号校验合规（0 直引号）；比尔句尾 what? 统一「是不是？」；新专名 Morrisville=莫里斯维尔、King George=乔治国王、Duke of Norfolk=诺福克公爵、State Road=州道 4 行回填术语表（Indian clubs 从ⅩⅣ定名「印度棒」）；CSV doing→done 双重读确认（间隔 6 秒×2） |
| 2026-09-13 | xii（第十二章） | done | 13 对块 41 段（英文块按行号程序化取自源文零走样，含 5 处 U+FEFF、6 处 U+00A0；源文排印瑕疵 looked a at him 照源保留按原意译出），check_bilingual exit 0；中文块弯双引号校验合规（0 直引号）；本章无对话内嵌引号；新专名 Luella Delia Philpotts=露埃拉·迪莉娅·菲尔波茨、Tennyson=丁尼生、Maud=《莫德》3 行回填术语表；CSV doing→done 双重读确认（间隔 6 秒×2） |
| 2026-09-13 | x（第十章） | done | 21 对块 62 段（英文块按行号程序化取自源文零走样，16 处 U+FEFF、17 处 U+00A0 原样保留，四处歌行/诗引块结构照源镜像），check_bilingual exit 0；中文块弯双引号校验合规（0 直引号），逐块段数奇偶校验通过；比尔句尾 what? 本章未出现；新专名 The Voice that Breathed O’er Eden=《伊甸园上飘过的声音》、Little Lord Fauntleroy=小勋爵方特罗伊、Ruth=路得、Old Faithful=“老忠实泉”、Detroit=底特律、The Wedding Glide=《婚礼滑步曲》6 行回填术语表；CSV todo→doing→done 三重读确认（间隔 6 秒） |
| 2026-09-13 | xiii（第十三章） | done | 21 对块 92 段（英文块按行号程序化取自源文零走样，15 处 U+FEFF、5 处 U+00A0、4 处 U+200A 原样保留），check_bilingual exit 0；中文块弯双引号/内嵌弯单引号校验合规（0 直引号）；the hape 定名「哈猴」、coon 按对话语境出版惯例定名、bona fides 保留拉丁原词；新专名 13 行回填术语表；CSV doing→done 双重读确认（6 秒+3 秒） |
| 2026-09-13 | ix（第九章） | done | 35 对块 133 段（英文块按行号程序化取自源文零走样，32 处 U+FEFF 原样保留），check_bilingual exit 0；中文块弯双引号/内嵌弯单引号校验合规（0 直引号）；比尔句尾 what? 两处统一「是不是？」；Rogues’ Gallery=惯犯照片馆、Jack the Blood=嗜血杰克、East Side=东区 3 行回填术语表；CSV doing→done 三重读确认（间隔 7 秒+6 秒） |
| 2026-09-13 | xvii（第十七章） | done | 9 对块 32 段（英文块按行号程序化取自源文零走样，11 处 U+FEFF、23 处 U+00A0 原样保留），check_bilingual exit 0；中文块弯双引号校验合规（0 直引号）；新专名 Raffles=拉弗尔斯、The Man=那个人 2 行回填术语表；CSV doing→done 双重读确认（间隔 6 秒×2，期间 CSV 被并行代理规范化为 CRLF，按当前字节格式原位改写） |
| 2026-09-14 | xv（第十五章） | done | 30 对块 140 段（英文块按行号程序化取自源文零走样，25 处 U+FEFF、13 处 U+00A0 原样保留；源文排印瑕疵 Lady, Weatherby、one of whose 照源保留按原意译出），check_bilingual exit 0（可疑错配 0 处）；中文块弯双引号/内嵌弯单引号校验合规（0 直引号，252 对双引号平衡）；比尔句尾 what? 本章未出现；新专名 the Savoy=萨伏伊大饭店、Lincoln=林肯赛马场、Atlantic=“大西洋号”、the Tenderloin=嫩腰区、Nut Comedian=“怪人谐星”、rubber=“橡皮脖子” 6 行回填术语表；CSV doing→done 双重读确认（间隔 6 秒） |
| 2026-09-14 | xviii（第十八章） | done | 39 对块 204 段（英文块按行号程序化取自源文零走样，40 处 U+FEFF、41 处 U+00A0 原样保留），check_bilingual exit 0（可疑错配 0 处）；中文块弯双引号/内嵌弯单引号校验合规（0 直引号，155 对双引号与源文 155 对奇偶相合）；比尔句尾 what? 三处统一「是不是？」；outhouse 沿ⅩⅥ定名「棚屋」、林中 shack studio 另译「窝棚画室」以别二屋、The Man 沿ⅩⅦ定名「那个人」；新专名 Fenimore Cooper=费尼莫尔·库珀、Chingachgook=金加古、Jess Willard=杰斯·威拉德、Romney=罗姆尼、Gainsborough=庚斯博罗、Spanish Armada=西班牙无敌舰队、the swag=贼赃、the submerged tenth=沉沦的十分之一 8 行回填术语表；CSV doing→done 双重读确认 |
| 2026-09-14 | xxi（第二十一章） | done | 6 对块 21 段（英文块按行号程序化取自源文零走样，4 处 U+FEFF、英文撇号 U+2019 原样保留），check_bilingual exit 0（可疑错配 0 处）；中文块弯双引号校验合规（0 直引号，9 对双引号平衡）；比尔句尾 what? 本章未出现；全章无新专名，克莱尔、比尔、伊丽莎白·博伊德、纳蒂·博伊德均沿既有定名首现括注原文，术语表无需回填；CSV doing→done 双重读确认（间隔 7 秒） |
| 2026-09-14 | xxii（第二十二章） | done | 31 对块 112 段（英文块按行号程序化取自源文零走样，18 处 U+FEFF 原样保留），check_bilingual exit 0（可疑错配 0 处）；中文块弯双引号校验合规（0 直引号，82 对双引号平衡）；比尔句尾 what? 本章未出现；全章无新专名，比尔/伊丽莎白/纳蒂/达利什勋爵/舅舅艾拉均沿既定定名，术语表无需回填；CSV doing→done 双重读确认（间隔 6 秒） |
| 2026-09-14 | xx（第二十章） | done | 15 对块 71 段（英文块按行号程序化取自源文零走样，10 处 U+FEFF、28 处 U+00A0、57 处 U+2019 原样保留），check_bilingual exit 0（可疑错配 0 处）；中文块弯双引号/内嵌弯单引号校验合规（0 直引号，49 对双引号、5 对单引号平衡）；本章无比尔台词，句尾 what? 未出现；新专名 Subconscious Self=潜意识、Eddie Foy=埃迪·福伊、Bildad the Shuhite=书亚人比勒达、Lucifer=路西法、gargoyle=石像鬼、foxtrot=狐步舞、Gloomy Gus=丧气鬼、trailing arbutus=匍匐熊果（双关括注）、Ford=福特 9 行回填术语表；CSV doing→done 双重读确认（间隔 6 秒×2） |
| 2026-09-14 | xix（第十九章） | done | 24 对块 103 段（英文块按行号程序化取自源文零走样，21 处 U+FEFF、6 处 U+00A0、73 处 U+2019 原样保留），check_bilingual exit 0（可疑错配 0 处）；中文块弯双引号校验合规（0 直引号，148 对双引号平衡）；比尔句尾 what? 一处统一「是不是？」；文件首行按本次派单要求加公版免责 HTML 注释行；新专名 Polly Wetherby=波莉·韦瑟比、Lady Wetherby=韦瑟比夫人 2 行回填术语表；CSV doing→done 双重读确认（间隔 6 秒，仅 xix 行变更） |
| 2026-09-14 | xxiii（第二十三章） | done | 10 对块 43 段（英文块按行号程序化取自源文零走样，7 处 U+FEFF、32 处 U+2019 原样保留），check_bilingual exit 0（可疑错配 0 处）；中文块弯双引号校验合规（0 直引号，33 对双引号平衡）；比尔句尾 what? 本章未出现；全章无新专名，伊丽莎白/纳蒂/比尔/达利什勋爵/弗拉克家均沿既定定名，术语表无需回填；CSV doing→done 双重读确认（间隔 6 秒） |
| 2026-09-14 | xxv（第二十五章，末章） | done | 19 对块 75 段（英文块按行号程序化取自源文零走样，13 处 U+FEFF 原样保留），check_bilingual exit 0（可疑错配 0 处）；中文块弯双引号/内嵌弯单引号校验合规（0 直引号，全部成对平衡）；比尔句尾 what? 本章未出现（What?/Eh? What? 均系疑问词非句尾助词）；新专名 Long Island=长岛、East Moriches=东莫里奇斯、Mary Pickford=玛丽·碧克馥、Gingery Stories=《姜味故事集》、Harold=哈罗德、Brooklyn Bridge=布鲁克林大桥、City Hall=纽约市政厅、Twenty-ninth Street=二十九街、Fifth Avenue=第五大道、Jamaica=牙买加（皇后区）、Islip=艾斯利普 11 行回填术语表；CSV todo→doing→done 双重读确认（间隔 7 秒） |
| 2026-09-14 | xxiv（第二十四章） | done | 19 对块 72 段（英文块按行号程序化取自源文零走样，14 处 U+FEFF、8 处 U+00A0、66 处 U+2019 原样保留），check_bilingual exit 1，唯一可疑为数字锚点误报（原文 87 cake，译文按中文数字作「八七年的老蛋糕」），按派单规则判定通过；中文块弯双引号/内嵌弯单引号校验合规（0 直引号，60 对双引号、3 对单引号平衡），括注英文撇号统一 U+2019；比尔句尾 what? 本章未出现，杰里的英式语气尾 what/did I 同样统一作「是不是？」；新专名 the governor=老爷子、without prejudice=无损权益、bloomer=昏招、stymie=障碍球、Gerry Society=杰里协会、Bloomingdale=布鲁明代尔、Marcus Aurelius=马可·奥勒留、Fletcherizing=弗莱彻式细嚼慢咽、on the wagon=在戒酒、old 87 cake=八七年的老蛋糕 10 行回填术语表；CSV doing→done 三重读确认（间隔 6 秒×2） |
| 2026-09-14 | 整书完结（26/26 篇：献词+25 章） | 全书 26 篇批量复检通过（check_bilingual 全过；xxiv 数字锚点为 '87 cake→八七年中文数字改写既定放行类） | 体例：「## 罗马数字照搬 / 第N章」；首章代理定基调并回填术语表 21 行硬约束；主 agent 裁定统一：章题中文侧「第N章」（ii 补正）、Noblesse oblige 保留法语原词（iii 两处回改）；比尔句尾 what?=「是不是？」全书一致；[1301] xix 免责重派一次成功并覆盖半程残留；跨午夜双日期日志各随实际（09-13/09-14） |
