# 翻译计划：来自深渊的叹息

## 本计划信息

- **项目名称**：thomas-de-quincey_suspiria-de-profundis
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/小说文学.md
- **术语表**：术语表.md
- **执行模式**：委派（短篇集；见 WORKFLOW.md「单篇翻译流程」）

## 执行步骤

单篇 9 步（读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志）以 `prompts/翻译计划模板.md`「执行步骤」为准，本文件不重复。委派模式下由主 agent 派单，子代理简报含黄金样本与前篇末尾。

## 篇目清单

由 `translation_queue.csv` 管理（16 篇，约 353KB）。

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
| 2026-09-10 | editor-s-preface.md（编者序） | 4 对双语块，check_bilingual 通过（2 处日期锚点误报已人工核实） | 定名：Suspiria=叹息集；章题：梦幻/生命的幻象/追念的叹息/童年的苦难/人脑的重写本/蕾瓦娜与忧伤三圣母/萨凡纳-拉-马尔/黎巴嫩之女/布罗肯山的幻影，待回填术语表 |
| 2026-09-10 | dreaming.md（论梦） | 8 对双语块，check_bilingual 通过（1 处数字锚点误报：1821/1822 译作中文数字，已人工核实） | 新书首批；书名定名：Confessions of an English Opium-Eater=《一个英国鸦片吸食者的自白》，Opium Confessions=《鸦片自白》；拉丁语 praemissis praemittendis、sine qua non 保留原文加括注；holy office=宗教裁判所，待回填术语表 |
| 2026-09-10 | endnotes.md（尾注） | 22 对双语块，check_bilingual 通过（EXIT=0，无误报） | 全书 58 条尾注；拉丁/希腊/法语引语保留原文加括注（suspiriosae cogitationes=叹息般的思绪，本卷书名来源）；Brocken=布罗肯峰、palimpsest=重写本、Whitsunday=圣灵降临节、Obeah=奥比巫术；手稿讹误（John Paul/Richten、There art、hat been、so had）按原样保留或依合理读法迻译，待回填术语表 |

| 2026-09-10 | savannah-la-mar.md（萨凡纳-拉-马尔） | 2 对双语块，check_bilingual 通过（EXIT=0，无误报） | 定名：Dark Interpreter=黑暗阐释者、Fata-Morgana=法塔-莫尔加娜蜃景、Roman clepsydra=罗马水钟；拉丁语 jubilate(s)、sanctus 保留原文加括注；城名 Savannah-la-Mar=萨凡纳-拉-马尔，均待回填术语表 |

| 2026-09-10 | levana-and-our-ladies-of-sorrow.md（蕾瓦娜与忧伤三圣母） | 6 对双语块，check_bilingual 通过（EXIT=0） | 三重名号按术语表：Mater Lachrymarum/Suspiriorum/Tenebrarum=泪之母/叹之母/暗之母，Our Lady of Tears/Sighs/Darkness=泪之圣母/叹之圣母/暗之圣母；Madonna=圣母（尊长女之衔）；尾注锚点45/46/47以括注（45）保留对位；Semnai Theai=塞姆奈诸神女、Eumenides=欧墨尼得斯、Parcae=帕耳卡、Cybele=库柏勒，待回填术语表 |

| 2026-09-10 | memorial-suspiria.md（纪念的叹息） | 7 对双语块，check_bilingual 通过（仅数字锚点提示：1840/1830/1843/1835 已按本书惯例改写为一八四〇等，属误报） | 标题定名「纪念的叹息」；suspiria 保留拉丁原文加括注（叹息）；ayah=阿妈、Grace=格蕾丝、Agrippina=阿格里皮娜、Railroadina/Steamboatina=铁路娘娘/轮船娘娘，待回填术语表 |
| 2026-09-10 | the-apparition-of-the-brocken.md（布罗肯峰的幻影） | 4 对双语块，check_bilingual 通过（EXIT=0，无误报） | Dark Interpreter=黑暗阐释者；apparition/Spectre of the Brocken=布罗肯峰幻影、phantom=魅影；Whitsunday=圣灵降临节、Pentecost=五旬节；Judaea=犹地亚（罗马钱币像）、Cortho=科尔托、Phantasus=凡塔苏斯、parhelion=幻日；尾注锚点52-55以括注（NN）保留对位；原文斜体重读（does/that/my/his/he/could）以星号斜体对应，均待回填术语表 |
| 2026-09-10 | the-daughter-of-lebanon.md（黎巴嫩之女） | 2 对双语块（前块3段+后块1段），check_bilingual 通过（EXIT=0，无错配） | evangelist 沿用尾注既定译法「福音师」（四福音师之一）、Prophet=先知；Daughter/Lady of Lebanon=黎巴嫩之女/黎巴嫩的女公子；Magdalen of Lebanon=黎巴嫩的抹大拉；Om el Denia 保留原文并取「世代之母」义；尾注锚点56-58以括注（NN）对位；Palmyra=帕尔米拉、Daphne=达夫尼、Orontes=奥龙特斯河，待回填术语表 |
| 2026-09-10 | the-dark-interpreter.md（黑暗的阐释者） | 3 对双语块（题词1段+前半3段+后半4段），check_bilingual 通过（EXIT=0，无误报） | Dark Interpreter=黑暗阐释者、Our Ladies of Sorrow=忧伤三圣母、Madonna=圣母（沿用具定名）；Demiurgus=巨匠造物主、Symons=西蒙斯、Hoddesdon=霍兹登、Middlesex=米德尔塞克斯；umbra/penumbra=本影/半影、bagatelle=小玩意儿（拉丁词保留原文加括注）；尾注锚点49-51以括注（NN）对位；Count Massigli 沿用尾注既定译法「马西利伯爵」；原文15处U+FEFF破折号残留随原文块逐字保留；原文斜体重读（you/not/that/umbras/penumbras/bagatelle/Him/my/other/modulus）以星号斜体对应，均待回填术语表 |

| 2026-09-10 | the-affliction-of-childhood.md（童年的苦难） | 71 对双语块，check_bilingual 通过（EXIT=0，0 可疑错配） | 曾遇 [1301] 加免责前缀重派；超大章（97.8KB）分批 append-only 落盘；尾注锚点 1-19 以（NN）对位；Original 块经脚本按源文行精确回填（零转录偏差）；新定名：Jane=简、Elizabeth=伊丽莎白、Turk=突克、Grim=格里姆、Erl-king's Daughter=桤木王之女、kilcrop=换生儿、Obeah=奥比巫术、Stationers' Company=书商公会、anagnorisis=发现 |
| 2026-09-10 | the-princess-who-overlooked-one-seed-in-a-pomegranate.md（漏数石榴籽的公主） | 2 对双语块，check_bilingual 通过（EXIT=0，0 可疑错配） | 极短篇单块组拼装；《一千零一夜》（*Arabian Nights*）沿用前文既定译法；*Verschmerzeon* 保留原文加德语括注；Pelion upon Ossa 首现附原文；引语「蛛母自其腹中所捻出的任何一缕丝」随源文诗行断句对位；Original 块经脚本按源文行精确回填（含 U+FEFF 破折号逐字保留） |
| 2026-09-10 | the-solitude-of-childhood.md（童年的孤独） | 4 对双语块，check_bilingual 通过（EXIT=0，0 可疑错配） | Erl-king/Erl-king's Daughter 沿用既定名「桤木王/桤木王之女」；*Dulce Domum* 尾注锚点（48）以括注对位、拉丁歌名保留原文加意译括注；*Heimweh*=思乡病、calenture=谵妄热、*zaarrahs*/*sanctus*/*nympholepsy* 保留原文加括注；华兹华斯《鹿跳泉》（The Hart-leap Well）、《丹麦少年》（The Danish Boy）首现附原文；姊妹沿前文译「姊姊」 |
| 2026-09-10 | the-palimpsest-of-the-human-brain.md（人脑的重写本） | 9 对双语块，check_bilingual 通过（EXIT=0，0 可疑错配） | palimpsest 全篇统一「重写本」；Opium Confessions 沿用既定《鸦片自白》；*membrana*/*regressus*/*diplomata*/*chaise-longue* 保留原文加括注；尾注锚点 42-44 以（NN）括注对位；首现定名：Cowper=科珀、Dr. Whately=惠特利博士、Pisistratus=庇西特拉图、Hermes Trismegiatus=赫尔墨斯·特里斯梅吉斯托斯、Paracelsus=帕拉塞尔苏斯、Lucan=卢坎、Erictho=厄里克托、Dr. Faustus=浮士德博士、strophe/antistrophe=正歌/返歌、My Cid=熙德、Coeur de Lion=狮心王，待回填术语表 |
| 2026-09-10 | vision-of-life.md（生命的幻象） | 2 对双语块，check_bilingual 通过（EXIT=0，0 可疑错配） | 短篇两长段；无尾注锚点、无德语词；vision of life=生命的幻象、prelibation=先尝的祭酒（prelibation）、Delphic caves=德尔斐洞窟、discords/concords=不协和音/和协音，首现附原文；rapture 统一「极乐」；Moore 无涉，Mozart/Beethoven 用通行译名并附原文 |
| 2026-09-10 | who-is-this-woman-that-beckoneth-and-warneth-me-from-the-place-where-she-is-and-in-whose-eyes-is-woeful-remembrance-i-guess-who-she-is.md（这个向我招手示意、以凄然追忆的目光警醒我的女人是谁——我猜到她是谁） | 6 对双语块，check_bilingual 通过（EXIT=0，0 可疑错配） | 无尾注锚点；Suspiria=《叹息集》、preexistence=先在、Reminiscences of Wordsworth=《华兹华斯回忆录》、Westmoreland=威斯特摩兰沿前文既定译法；首现定名 Hebe=赫柏（示警而怀憾的青春女神）、Da Vinci/Michelangelo=达·芬奇/米开朗基罗，待回填术语表；篇末华兹华斯引语随源文于「most truly I might say:」处截断，译文保留未闭合引号与冒号；Original 块中源文 U+FEFF 破折号前缀已规范为普通破折号（不影响段落数） |
2026-09-10 | the-english-mail-coach.md（《英国邮车》，108.7KB 超大章） | 49 对双语块，check_bilingual 通过（EXIT=0，0 可疑错配，段落数逐对零错配） | 超大章分批落盘（Write 首批 + 多次 heredoc 追加，两次超长截断经 Python 修复）；尾注锚点（20）至（41）全角括注对位、数字锚点校验 0 误报；拉丁词保留加括注（ça ira、laesa majestas、magna loquimur/vivimus、Cyclops Diphrélates、Al Sirat、Tumultuosissimamente、sanctus 等）；新定名：芬妮（Fanny）、独眼御者（Cyclops Diphrélates）、塔里霍（Tallyho）、布鲁姆格姆（Brummagem）、亚革大马（Aceldama）、库埃斯塔（Cuesta）、横死（sudden death）；梦之赋格五乐章标题以「一/二/三/四/五」对译；CSV 已回填 done 并复核
