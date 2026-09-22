# 翻译计划：化装舞会者

## 本计划信息

- **项目名称**：georgette-heyer_the-masqueraders
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/小说文学.md
- **术语表**：术语表.md
- **执行模式**：委派（长篇；见 WORKFLOW.md「单篇翻译流程」）

## 执行步骤

单篇 9 步（读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志）以 `prompts/翻译计划模板.md`「执行步骤」为准，本文件不重复。委派模式下由主 agent 派单，子代理简报含黄金样本与前篇末尾。

## 篇目清单

由 `translation_queue.csv` 管理（33 篇，约 506KB）。

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-09-19 | dedication.md | done | 献词微件，1 块对照，check_bilingual 退出码 0 |
| 2026-09-19 | arrest-of-mr-merriot.md | done | 11 块对照（55 段镜像），check_bilingual 退出码 0；Merriot＝梅里奥特（与术语表定名一致），术语表追加 14 行 |
| 2026-09-19 | challenge-to-mr-merriot.md | done | 16 块对照（57 段镜像），check_bilingual 退出码 0；术语表追加 19 行，Merriot 与并行单对齐＝梅里奥特 |
| 2026-09-19 | journey-s-end.md | done | 19 块对照（75 段），check_bilingual 退出码 0 |
| 2026-09-19 | arrival-of-a-large-gentleman.md | done | 20 块对照（90 段镜像），check_bilingual 退出码 0；原文字节级程序化提取（含 FEFF/NBSP 照留），术语表追加 8 行（Letitia/Kate/Peter/Gretna Green/Gloucestershire/Grayson Court/Stilton/Adonis） |
| 2026-09-19 | meeting-in-arlington-street.md | done | 20 块对照（98 段镜像），check_bilingual 退出码 0；原文程序化提取（6 处 FEFF 照留），普鲁登丝＝姐姐、罗宾＝弟弟定序，对白「」嵌套『』，术语表追加 2 行（Lord Barham／Lady Fanshawe） |
| 2026-09-19 | a-taste-of-a-large-gentleman-s-temper.md | done | 25 块对照（111 段镜像），check_bilingual 退出码 0；原文程序化提取（FEFF×11／NBSP×14／hair space×3 照留），Letitia 依术语表定名莉蒂西娅，the mountain 指称沿用「那座山」（与 XV 章一致），术语表追加 8 行（Lady Dorling/Ranelagh Gardens/Wych End/Jollyot/the large gentleman/faro/picquet/guinea） |
| 2026-09-19 | sir-humphrey-grayson-waits-upon-mr-merriot.md | done | 11 块对照（47 段镜像），check_bilingual 退出码 0；原文程序化提取（FEFF×1／NBSP×7 照留），Letitia＝莉蒂西娅、Madam Kate＝凯特小姐、Oh lud＝哎呀老天／ecod＝乖乖（与前章对齐），术语表追加 2 行（Black Pompey/chicken-skin fan） |
| 2026-09-19 | my-lord-barham-in-arlington-street.md | done | 16 块对照（67 段镜像），check_bilingual 退出码 0；原文程序化提取（FEFF×10／NBSP×8 照留），巴勒姆口头禅引用处照表作「我运筹成了」、自述变体作「我总会运筹成功的」，my lord／my lady 叙述沿用「勋爵大人／夫人」，术语表追加 10 行（Tyburn/Half Moon Street/St. James's/Murray of Broughton/Jonah/Robin Lacey/Colney/Daughtry/Vanilov/Hanover） |
| 2026-09-19 | passage-of-arms-between-prudence-and-sir-anthony.md | done | 16 块对照（88 段镜像），check_bilingual 退出码 0；原文程序化提取（FEFF×12／NBSP×1／hair space×1 照留），the mountain＝那座大山、little man＝小个子照表，my lady 叙述沿用「夫人」，法语 *bon papa*／*mon enfant* 照原文保留，术语表追加 6 行（the Pretender/Whig/Grand Tour/Kensington/Fanshawe/the lost Viscount） |
| 2026-09-19 | my-lord-barham-becomes-mysterious.md | done | 13 块对照（60 段镜像），check_bilingual 退出码 0；原文程序化提取（FEFF×5／NBSP×9 照留），口头禅变体 I achieve＝「运筹成了一桩奇迹／把不可能都运筹成了」（与「我运筹成了」家族对齐），术语表追加 5 行（Black Domino/euchre/angel cake/fichu/baronet） |
| 2026-09-19 | mistress-prudence-to-herself.md | done | 12 块对照（44 段镜像），check_bilingual 退出码 0；原文程序化提取（FEFF×12／NBSP×5／hair space×3 照留），章题 Mistress Prudence to Herself＝普鲁登丝小姐的独白（呼应章末 mistress of one’s thoughts），口头禅引用照表作「我运筹成了」，法语 *voyez vous*／*parole d’honneur*／*Peste* 等照原文保留，my lady 叙述沿用「夫人」，术语表追加 7 行（Sir Roger Lowestoft/Marthe/his Grace of Cumberland/little fierce George/the bonnie prince/Jacobite/Frankfort） |
| 2026-09-19 | the-ride-through-the-night.md | done | 17 块对照（69 段镜像），check_bilingual 退出码 0；原文程序化提取（FEFF×4 照留），夜骑追逐节奏与初吻场景依原文张力行文，Needs must when the old gentleman drives 化用谚语作「老先生赶车，由不得人不坐呀」，普鲁对爵士维持「您＋爵士」的揶揄敬称、安东尼对普鲁用「你」，术语表追加 3 行（Rufus/roan/Matthew） |
| 2026-09-19 | sudden-and-startling-appearance-of-the-old-gentleman.md | done | 16 块对照（65 段镜像），check_bilingual 退出码 0；原文程序化提取（FEFF×11／NBSP×8 照留），巴勒姆勋爵假扮失踪的子爵亮相昆斯伯里晚会，小个子／猛犸／泰伯恩照表，法语 *Mon cher*／*magnifique*／*Voyons*／*A demain*／*bon papa* 照原文保留，my cabbage＝我的小卷心菜，her Grace 叙述作「殿下」，术语表追加 8 行（Queensberry/Selwyn/Gunning/Peterson/Carslake/Cloverly/Farnborough/Margrave） |
| 2026-09-19 | tortuous-methods-of-my-lord-barham.md | done | 12 块对照（61 段镜像），check_bilingual 退出码 0；原文程序化提取（FEFF×17／NBSP×1 照留），Nemesis＝涅墨西斯、巴勒姆的特雷梅因照表沿用，罗宾称父「先生」、my lord 叙述作「勋爵大人」与既译各章对齐，术语表追加 5 行（Vauxhall Gardens/Barnet/Finchley Common/Nemesis/Letitia 澄清行）；本单原派 the-unfinished-word.md 不存在，按 CSV size 升序改译（the-ride-through-the-night 与并行代理撞单让渡后顺延） |
| 2026-09-19 | the-polite-world-receives-mr-and-miss-merriot.md | done | 23 块对照（86 段镜像），check_bilingual 退出码 0；原文程序化提取（FEFF×12／NBSP×13／hair space×3 照留），the large gentleman＝大块头绅士、my cabbage＝我的小卷心菜、the Honourable＝尊贵的（沿用既译），皮克牌术语 point／quarte／quinte／quatorze 作「同花／四连张／五连张／十四分的四张王后」、repique＝瑞皮克满贯，章题定名「上流社交界接纳梅里奥特兄妹」，术语表追加 14 行（Walpole/Gilly Williams/Sir Francis Jollyot/lansquenet/ratafie/canary/negus/Troubridge/Kestrel/Clarges Street/repique/sponging house/Bel/Apollo） |
| 2026-09-19 | a-lady-in-distress.md | done | 31 块对照（126 段镜像），check_bilingual 退出码 0；原文程序化提取（FEFF×28／NBSP×66／hair space×5 照留），章题定名「落难的小姐」（呼应章内 beauty in distress＝佳人落难），凯特场合 my lady／Madam 叙述与称呼作「小姐」、法语 *En avant*／*en demie toilette*／beau geste 照原文保留，little man 照表作「小个子」，术语表追加 14 行 |
| 2026-09-19 | my-lady-lowestoft.md | done | 13 块对照（77 段镜像），check_bilingual 退出码 0；原文程序化提取（FEFF×16／NBSP×10 照留），the mountain＝那座山、mammoth＝猛犸、my lady 叙述＝夫人、Madam Prudence／Madam Robin 叙述依表作「普鲁登丝小姐／罗宾小姐」（对齐 I 章先例与术语表），法语 *bon papa*／*tiens*／*Mon Dieu*／*A vrai dire*／*Voyons*／*gamin*／*Bien, madame*／*Tenez*／*monsieur habillé en dame* 照原文保留，讹拼 To be franks 于原文块照留，章题定名「洛斯托夫特夫人」，术语表追加 10 行（Culloden/Perth/Dieppe/Florence/Stewart Charles/German George/Cumberland/Thérèse de Brûton/attainder/the mountain）；本单为中断重派、首译从零完成 |
| 2026-09-19 | the-black-domino.md | done | 27 块对照（150 段镜像），check_bilingual 退出码 0；原文程序化提取（FEFF×10／NBSP×5 照留），Black Domino＝黑衣多米诺、the Unknown／*l'Inconnu*＝无名氏（法语自称照录斜体）、Letitia＝莉蒂西娅、the large figure 作「大块头的身影」呼应大块头绅士、法语 *Mon Dieu*／*vaurien*／*Du vrai*／*N'est-ce pas*／*Hé*／*Adieu, ma belle* 照原文保留（intrigante／pièce de résistance／*bon papa* 首现括注），章题定名「黑衣多米诺」（依术语表定名），术语表追加 8 行（l'Inconnu／minuet／quadrille／claret／美人贴／tricorne／haresfoot／彩色多米诺配色） |
| 2026-09-19 | mohocks-abroad.md | done | 22 块对照（89 段镜像），check_bilingual 退出码 0；原文程序化提取（FEFF×11／NBSP×29／hair space×2 照留），Mohocks＝摩霍克匪徒照表，take a chair＝坐轿椅（sedan chair＝轿椅），Oh lud＝哎呀老天／ecod＝乖乖沿既译，法语 *mal-à-la-tête*／*bon papa*／*Seulement*／Au revoir 照原文保留，my lady 叙述沿用「夫人」，章题定名「摩霍克匪徒横行」，术语表追加 6 行（Charing Cross／Strawberry Hill／the Spectator／Dendy／Proudie／sedan chair） |
| 2026-09-19 | encounter-at-white-s.md | done | 26 块对照（96 段镜像），check_bilingual 退出码 0；原文程序化提取（NBSP×36 照留），怀特俱乐部／法罗牌／皮克牌／兰斯克内牌／莫利纽克斯照表，my lord 叙述＝勋爵大人，common 双关作「不入流」（寻常赌棍→不入流的营生），Ecod＝乖乖／Gad＝天哪沿既译，斜体 *lackey* 照录作*听差*，法语借词 perruquier／roué 未斜体径译（假发师／老浪子，首现括注），章题定名「怀特俱乐部的一场遭遇」，术语表追加 13 行（Fontenoy/Clevedale/Munich/Turin/Rome/Lady Barham/pink salon/oriole window/perruquier/roué/snuffbox/Tare an' 'ouns/lackey） |
| 2026-09-19 | unaccountable-behaviour-of-sir-anthony-fanshawe.md | done | 19 块对照（110 段镜像），check_bilingual 退出码 0；原文程序化提取（FEFF×19／NBSP×43 照留），加利亚诺系新出场人物（全名吉罗拉莫·加利亚诺／昵称加利／仆人蒂诺），*Le Baiser de la Morte*＝死亡之吻（法语照录斜体）、*Sapristi*／Bacchus 照原文保留，the large gentleman＝大块头绅士、the Honourable Charles＝尊贵的查尔斯（沿用既译）、the small sword＝小剑、grey mare＝灰母马，决斗自格雷律师学院广场移师加利亚诺剑室，章题定名「安东尼·范肖爵士的反常行径」，术语表追加 11 行（Galliano／Girolamo Galliano／Gally／Tino／Farraday／Haymarket／Grey's Inn Fields／Le Baiser de la Morte／the small sword／Sa-sa／rappee） |
| 2026-09-19 | sad-falling-out-of-friends.md | done | 16 块对照（90 段镜像），check_bilingual 退出码 0；原文程序化提取（FEFF×17／NBSP×49／hair space×1 照留），Dev＝德夫（Devereux 昵称）、my lord/my lady 叙述沿用「勋爵大人／夫人」，金额作中文数字（一万英镑／二十几尼），讹拼 Lord Barharn 照留原文块，章题定名「朋友反目」，术语表追加 4 行（Galliano/Dev/Carslake/Lord George Murray） |
| 2026-09-19 | ingenuity-of-my-lord-barham.md | done | 22 块对照（107 段镜像），check_bilingual 退出码 0；原文程序化提取（FEFF×21／NBSP×43 照留），马卡姆上门讹诈、勋爵以格雷森旧信反制并布下私奔换信之局，my lord 叙述＝勋爵大人、运筹家族词与「我运筹成了」系对齐、the Honourable Charles＝尊贵的查尔斯沿用既译、乔治·默里勋爵沿用 XVII 章定名，章题定名「巴勒姆勋爵的巧思」，术语表追加 5 行（quizzing-glass/Burgundy/Bute/Henry/ale；George Murray 已存在沿用） |
| 2026-09-19 | the-large-gentleman-is-awake.md | done | 27 块对照（112 段镜像），check_bilingual 退出码 0；原文程序化提取（FEFF×22／NBSP×6／hair space×1 照留），大块头绅士／小个子照表，普鲁对爵士「您＋爵士」、安东尼对普鲁「你」，wolf 意象统一作「那匹狼」（吓狼／废掉那匹狼），法语借词 sangfroid 未斜体径译作镇定自若，章题定名「大块头绅士醒了」，术语表追加 7 行（Grey's Inn Fields／Newmarket／Burgundy／Borgia／Mr. Fire-Eater／small sword／sangfroid）
| 2026-09-19 | proceedings-of-mr-markham.md | done | 18 块对照（66 段镜像），check_bilingual 退出码 0；原文程序化提取（FEFF×9／NBSP×23／hair space×2 照留，标题行 NBSP 保真），Letty＝莱蒂、姑母与既译对齐，布特勋爵与并行 XX 章正文「布特（Bute）」一致，O mountain＝大山／the mountain＝那座山照表，术语表追加 7 行（Lord Bute/London Bridge/North Road/Hop o’ my Thumb/midget/molehill/大格雷森小姐），章题定名「马卡姆先生的行径」 |
| 2026-09-19 | the-fight-by-moonlight.md | done | 13 块对照（55 段镜像），check_bilingual 退出码 0；原文程序化提取（行中 FEFF×5／NBSP×20 照留），无名氏月下拦截私奔驿车、以公平决斗诛马卡姆并交还格雷森旧信，the Unknown＝无名氏／the small sword＝小剑照表，Madam（莱蒂场合）随凯特惯例作「小姐」，击剑术语 quarte＝第四式、forte／foible＝强部／弱部、time-thrust＝时机突刺（首现附原文），法语 *Au revoir, ma belle!* 照原文斜体保留，格雷戈里·马卡姆尸身收束，章题定名「月光下的搏斗」，术语表追加 6 行（quarte/forte-foible/time-thrust/blunderbuss/footpad/Au revoir, ma belle） |
| 2026-09-19 | return-of-miss-grayson.md | done | 20 块对照（79 段镜像），check_bilingual 退出码 0；原文程序化提取（FEFF×13／NBSP×8／hair space×1 照留），罗宾决斗诛马卡姆后树丛换装接回莱蒂、护送至格雷森府，莱蒂当父焚信吐真相并宣布将嫁无名氏、姑母考狄利娅首现，*en avant* 照录斜体、the Unknown＝无名氏照表、Miss Prue＝普鲁小姐／Master Robin＝罗宾少爷、time-thrust 与大格雷森小姐沿用 XXIII 既立定名，章题定名「格雷森小姐归来」，术语表追加 5 行（Cordelia／Madeira／barker／Madam Anxiety／'Pon rep） |
| 2026-09-19 | mystery-of-the-masked-man.md | done | 32 块对照（114 段镜像），check_bilingual 退出码 0；原文程序化提取（FEFF×11／NBSP×18／发丝空格×1 照留，原文块 114 段逐行保真复核），time-thrust＝时机突刺／blunderbuss＝大口径短铳沿用 XXIII–XXIV 定名，High Toby＝拦路行劫、chefs d’oeuvres 法语照录首现括注、postilion＝前骑驿仆，my lord／my lady 叙述＝勋爵大人／夫人，Tare an’ ’ouns＝天杀的／Egad＝乖乖／Faith＝说真的／’Pon my soul＝我以灵魂起誓沿既译，章题定名「蒙面人之谜」，术语表追加 7 行（time-thrust 与 blunderbuss 已存在沿用） |
| 2026-09-19 | violence-on-the-king-s-high-road.md | done | 17 块对照（79 段镜像），check_bilingual 退出码 0；原文程序化提取（FEFF×7／NBSP×11 照留），安东尼爵士途中截下约翰、二人蒙面劫囚救普鲁登丝，大块头绅士／菊花青马照表，叙述层 my lord＝勋爵大人、约翰对白 his lordship/my lord＝老爷，dooty＝职责所在沿 XXVI 定名，剑杖／矮林／barker＝手枪（首现括注），马修正文首现括注，章题定名「王家大道上的暴行」（对齐 XXV 章 the King’s Highway＝王家大道定名） |
| 2026-09-19 | exit-miss-merriot.md | done | 19 块对照（83 段镜像），check_bilingual 退出码 0；原文程序化提取（FEFF×24／NBSP×4／hair space×1 照留），女装线谢幕章：别了彼得·梅里奥特、罗宾卸下凯特作派夜遁赴『拉伊之骄傲』号，巴勒姆勋爵雷霆训诫（巴勒姆的特雷梅因／尊贵的普鲁登丝·特雷梅因），那座山／勋爵大人／罗宾少爷／普鲁小姐照表，my lady 叙述沿用「夫人」，法语 *affreux*／*Du vrai*／*bon papa* 照录斜体、point-de-vice／je ne sais quoi 照留、dégagé 未斜体径译（首现括注），Oh lord＝哎呀老天／egad＝天哪沿既译，章题定名「梅里奥特小姐退场」，术语表追加 15 行 |
| 2026-09-19 | triumph-of-lord-barham.md | done | 25 块对照（121 段镜像），check_bilingual 退出码 0；原文程序化提取（FEFF×16／NBSP×76／发丝空格×1 照留，Original 块与源文 121/121 字节一致复核通过），格罗夫纳广场身份听证收官：笔迹→微型画像→贺拉斯《颂歌》藏素描→伯顿家兄妹认亲环环立证、勋爵收宅告辞，my lord 叙述＝勋爵大人、堂亲称呼沿 XX 章判例、主张人／冒牌货措辞对齐既译，法语 *Voyons* 照录斜体、damme＝妈的照表，钟点与金额作中文数字，章题定名「巴勒姆勋爵的凯旋」，术语表追加 16 行 |
| 2026-09-19 | the-honourable-robin-tremaine.md | done | 26 块对照（114 段镜像），check_bilingual 退出码 0；原文程序化提取（FEFF×37／NBSP×18／hair space×1 照留，弯引号照存），罗宾以真名回归怀特俱乐部、向格雷森父女揭明无名氏与凯特身份的收束章，the Honourable＝尊贵的、巴勒姆的特雷梅因／勋爵大人叙述层照表，l'Inconnu＝*l'Inconnu*（无名氏）照录斜体、de rigueur 法语借词未斜体径译（必不可少的规矩），Gad＝天哪／'Pon my soul＝我以灵魂起誓／Faith＝说真的沿既译，普鲁登丝＝家姐／令姐、罗宾＝弟弟定序与 XXXII 衔接，章题定名「尊贵的罗宾·特雷梅因」，术语表追加 4 行（de rigueur/punch/taffety/point 花边；Clapperly＝克拉珀利已由并行 XXX 章入表，沿用定名） |
| 2026-09-19 | 【整书完结】 33/33 done | done | 《化装舞会者》批次1第36册整书流转：本日直启 18 章验收（I/III/VI/VIII/IX/XIII/XVI/XVII/XVIII/XX/XXI/XXIII/XXIV/XXV/XXVII/XXVIII/XXX/XXXI），含 2 个断点重置章（III/XXI 首译重派）；全章一次过检零拦截零回滚；主 agent 跨章裁定 2 组（Tare an' 'ouns=天杀的、damme=妈的 多章统一）；术语表并发回填约百条零冲突；核心定名：梅里奥特兄妹/普鲁登丝/巴勒姆勋爵（我运筹成了）/黑衣多米诺/无名氏/大块头绅士/那座山 |
