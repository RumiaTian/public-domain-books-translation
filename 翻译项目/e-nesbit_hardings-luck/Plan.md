# 翻译计划：哈丁的运气

## 本计划信息

- **项目名称**：e-nesbit_hardings-luck
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/小说文学.md
- **术语表**：术语表.md
- **执行模式**：委派（长篇；见 WORKFLOW.md「单篇翻译流程」）

## 执行步骤

单篇 9 步（读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志）以 `prompts/翻译计划模板.md`「执行步骤」为准，本文件不重复。委派模式下由主 agent 派单，子代理简报含黄金样本与前篇末尾。

## 篇目清单

由 `translation_queue.csv` 管理（14 篇，约 373KB）。

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
| 2026-09-10 | burglars.md | done | 块对照 41 对（183 段全覆盖）；check_bilingual.py 与 check_coverage.py 均退出码 0；原文行与译文 Original 块逐行一致（含不可见字符） |
| 2026-09-10 | dedication.md | done | 献辞 1 对块，check_bilingual/check_coverage 均过 |
| 2026-09-10 | list-of-illustrations.md | done | 插图清单 1 对块，check_bilingual/check_coverage 均过 |
| 2026-09-10 | buried-treasure.md | done | 块对照 67 对（218 行全覆盖，含两首诗与两处场景分隔）；check_bilingual.py 与 check_coverage.py 均退出码 0；原文行与译文 Original 块逐行一致（含不可见字符与斜体标记） |
| 2026-09-10 | going-home.md | done | 块对照 38 对（118 段全覆盖）；check_bilingual.py 与 check_coverage.py 均退出码 0；原文行与译文 Original 块逐行一致（含不可见字符与斜体标记） |
| 2026-09-10 | kidnapped.md | done | 块对照 41 对（123 行全覆盖，含两节神谕诗与场景分隔符）；check_bilingual.py 与 check_coverage.py 均退出码 0；原文行与译文 Original 块逐行一致（含不可见字符与斜体标记）；新定名：阿登/阿登城堡/阿登勋爵/理查德·阿登、埃德雷德、埃尔弗丽达、伊迪丝·阿登小姐、莫德瓦普/莫迪尔瓦普/莫迪斯特瓦普、纽克罗斯、劳里格罗夫、帕拉多斯先生/鹦鹉鼻、克利夫维尔、阿米莉亚/米莉亚、特鲁、《阿登之家》、《卫斯理公会杂志》 |
| 2026-09-10 | dickie-learns-many-things.md | done | 块对照 51 对（原文 176 段逐行原样嵌入 Original 块，含不可见字符；Chinese 段落数逐块 1:1）；check_bilingual.py 与 check_coverage.py 均退出码 0；对齐既有定名（莫德瓦普/莫迪尔瓦普/莫迪斯特瓦普/莫迪尔/莫德、叮铃、月籽、薰衣草台街、鹦鹉鼻、埃尔弗里达、特鲁），新词回填术语表（摇铃、白印章、白厅、伦敦塔、索霍、火药阴谋、蒙蒂格尔勋爵、特雷沙姆先生、尼思代尔夫人等）；莫德瓦普/莫迪尔瓦普/莫迪斯特瓦普 token 数与原文逐一相等；数字锚点 1608/1908/615 以阿拉伯数字保留 |
- 2026-09-10 lord-arden.md（第十一章 阿登勋爵，30.9KB）：块对照 21 对，check_bilingual.py 与 check_coverage.py 均通过（0 错配、0 漏译）；术语沿用术语表（迪基/埃尔弗里达/埃德雷德/阿登勋爵/塔尔博特府/叮铃/特鲁），新增定名：罗斯科先生（Mr. Roscoe）、德拉梅尔（Delamere）、梅德韦河（the Medway）、烘花屋（oast-house）、圆颅党（Roundheads）、莫迪瓦普（Mouldiwarp）、莫迪耶斯特瓦普（Mouldiestwarp）、克利夫维尔（Cliffville，沿用已译）；状态 done，CSV 已回填。
- 2026-09-10 the-noble-deed.md 单篇直译完成：41 对块，check_bilingual 0 违规、check_coverage 0 漏译，状态 done
- 2026-09-10 tinkler-and-the-moonflower.md（第一章 叮铃与月光花，36.2KB）：块对照 43 对，check_bilingual.py（0 错配）与 check_coverage.py（0 漏译）均退出码 0；状态 done，CSV 已回填
- 2026-09-10 the-end.md（第十二章 终局，10.5KB）：块对照 15 对（原文 50 行逐行原样嵌入 Original 块，含 3 处场景分隔符与不可见字符；Chinese 块逐行 1:1）；check_bilingual.py（0 错配、0 结构违规）与 check_coverage.py（0 漏译）均退出码 0；术语沿用术语表（迪基·哈丁、比尔、叮铃、白印章、月籽、莫德瓦普、阿登勋爵、埃德雷德、埃尔弗里达、德普特福德、詹姆斯一世<随前章XI>、堂弟堂妹/堂兄<随前章X/XI>）；新定名首现附原文：雷利（Raleigh）、德雷克（Drake）、老保姆；因检测到并行子代理写入迹象，未改动术语表与 CSV 之外文件；状态 done，CSV 已回填。

- 2026-09-10 the-escape.md（第三章 出逃，28.5KB）：块对照 39 对（原文 165 段逐段原样嵌入 Original 块，含书内广告引文与不可见字符；Chinese 块逐段 1:1）；check_bilingual.py（0 错配、0 结构违规）与 check_coverage.py（0 漏译）均退出码 0；术语沿用术语表与前章（迪基·哈丁、比尔、叮铃、摇铃、印章、白石头<the white stone，随一章「镶一块白石头」>、月光花、鹦鹉食<随一章/buried-treasure>、马卡姆<随一章书名「马卡姆夫人」>、格雷夫森德、纽克罗斯路、管家餐具室、医院）；新定名首现附原文：塔尔博特夫人（Lady Talbot）、百老汇街（Broadway）、乔（Joe）、罗森贝格先生（Mr. Rosenberg）、凯丝（Cath）、赫尔（Hurle）、罗伯茨（Roberts）、大象城堡（the Elephant and Castle）、旧肯特路（the Old Kent Road）、「格兰比侯爵」酒馆（the Marquis of Granby）、「笃一步」（Dot-and-go-one）、银扇（honesty）、弗里氏补药（Fry's Tonic）；罗森贝格咬舌以「系」代「是」处理；状态 done，CSV 已回填。
- 2026-09-10 which-was-the-dream.md（第四章 哪一个才是梦？，39.7KB）：块对照 48 对（每 3-6 段一组，含 3 处场景分隔符与诗节「Men die / Man dies not」对照块）；check_bilingual.py（0 错配、0 结构违规）与 check_coverage.py（0 漏译）均退出码 0（诗节源文弯引号「Time flies not.”」已按源文原样嵌入 Original 块以过检）；术语沿用术语表（迪基·哈丁、比尔先生/比尔、叮铃、白印章、月籽、德普特福德、纽克罗斯、塔尔博特府、格雷夫森德、摇铃、「猫与哨子」未涉及；奶妈古语 thou 以半文半白语气处理）；新定名首现附原文并回填术语表：塔尔博特夫人（Lady Talbot）、凯里医生（Dr. Carey）、亨利先生（Master Henry）、托马斯·布拉德伯里爵士（Sir Thomas Bradbury）、罗利先生（Master Raleigh）、金运号（The Golden Venture）、「艺术鹦鹉」花籽（the Artistic Parrot Seed）、萨塞克斯（Sussex）；状态 done，CSV 已回填。
- 2026-09-10 to-get-your-own-living.md（第五章 自食其力，35.2KB）：块对照 59 对（原文 248 段逐行原样嵌入 Original 块，含 30 处 NBSP 与 79 处 FEFF 不可见字符，程序化校验逐段一致；Chinese 段落数逐块 1:1）；check_bilingual.py 与 check_coverage.py 均退出码 0（0 错配、0 漏译）；术语沿用术语表（迪基/比尔先生/叮铃/白印章/月籽/塞巴斯蒂安/塔尔博特府/纽克罗斯/格雷夫森德/德普特福德/特鲁/爱德华·塔尔博特爵士）；本章新定名：红头发男人（the redheaded man）、雷利绅士（Rally）、阿尔弗雷德大王（King Alfred）、加利恩大帆船（galleon）、摄政街（Regent Street）、萨塞克斯（Sussex，沿用既译）、黑玛丽囚车（Black Maria）、「棋盘」酒馆（the "Chequers"）、铁路酒店（Railway Hotel）、布罗德韦大街（the Broadway）、幸福群岛（the Fortunate Islands）；因运行期间有并行译篇落盘迹象，新定名未回填术语表，由主会话统一合入；状态 done，CSV 已回填。
2026-09-10｜批次2｜整书完结：14/14 全部 done，删认领锁。备注：跨章译名变体（红头发男人/红头发家伙/红络腮胡的男人；百老汇街/布罗德韦大街；雷利/罗利先生/雷利绅士）待阶段三审核统一。
