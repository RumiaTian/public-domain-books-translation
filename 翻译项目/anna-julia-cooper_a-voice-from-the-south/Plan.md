# 翻译计划：anna-julia-cooper_a-voice-from-the-south

## 本计划信息

- **项目名称**：anna-julia-cooper_a-voice-from-the-south（《来自南方的声音》 A Voice from the South, Anna Julia Cooper, 1892）
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/学术著作.md
- **术语表**：术语表.md
- **内容形态 / 执行模式**：短篇集 / 委派（8 篇独立论文 + 卷首题词/献词/部题/尾注，共 14 个文件，约 346KB 源文）

---

## 文件分工

| 文件 | 作用 | 谁来改 |
|------|------|--------|
| `项目说明.md` | 项目基本信息、领域配置、篇目清单 | 人工 |
| `术语表.md` | 翻译硬约束层。每篇译完补充新词 | agent / 人工 |
| `translation_queue.csv` | 任务队列。每行一文件，`file, size_kb, status` 三列 | 翻译前改 doing，完成后改 done |
| `Plan.md`（本文件） | 执行步骤 + 运行日志 | agent 追加日志 |
| `原文/*.md` | 源文 | 不改 |
| `译文/*.zh-CN.md` | 译文产出（逐段对照双语） | 翻译 agent 产出 |

---

## translation_queue.csv 格式

```
file,size_kb,status
01-epigraph.md,0.1,todo
02-dedication.md,0.4,todo
...
```

| 字段 | 含义 | 取值 |
|------|------|------|
| `file` | 源文文件名（在 `原文/` 目录下） | 如 `05-womanhood-a-vital-element-in-the-regeneration-and-progress-of-a-race.md` |
| `size_kb` | 源文大小（KB）。>50KB 为长文，按通用翻译引擎第七节分段 | 数字 |
| `status` | 翻译状态 | `todo` 待译 / `doing` 翻译中 / `done` 已完成 |

---

## 执行步骤（agent 按此推进，两种模式共用）

> **谁执行**由 `项目说明.md` 的「内容形态」字段决定（见 `WORKFLOW.md`「判断内容形态」）：本项目为短篇集 → **委派模式**，子代理逐篇执行本流程。

### 1. 读配置（每次翻译前必读）
```
1. 本项目 Plan.md（本文件）
2. 项目说明.md
3. 术语表.md
4. prompts/通用翻译引擎.md
5. prompts/领域配置/学术著作.md
6. 译文/ 下任意一篇已完成的 .zh-CN.md（作为风格黄金样本，照此风格译；无则跳过）
```

### 2. 取任务
读 `translation_queue.csv`，取第一个 `status=todo` 的行。先 `ls 译文/` 检查该篇译文是否已存在：
- 已存在 → 直接改 `done`，跳到步骤 8。
- 不存在 → 把该行 `status` 改为 `doing` 并保存 CSV，继续。

### 3. 读源文
读 `原文/对应文件名`。

### 4. 翻译
产出到 `译文/对应文件名去.md加.zh-CN.md`。

**双语对照格式、标记规则、完整性禁令**：见 `prompts/通用翻译引擎.md` 第五、六节（标记成对、标题合并「英文 / 中文」、不跳过不缩写、UTF-8 无 BOM）。此处不重复。

**本流程专有提醒**：
- 逐段对照原文，绝不漏译、不合并段落、不缩写、不总结，尤其结尾别截断。
- 严守术语表：遇表内源词必译为指定译法。新词自行确定统一译法，首次附原文「中文（English）」。
- 术语表「人物」多用通行译名；法语/拉丁语短语保留原文随文括注意译。
- 长文（源文 >50KB，本项目中为 11、12 两篇）分段处理见通用翻译引擎第七节。

### 5. 自检
- 完整性：源文每一段都在译文 Original 块中出现，末尾无截断。
- 块对称：Original/Chinese 数量相等，每块内段数对应。
- 标题格式：全部「英文 / 中文」合并。
- 术语一致：抽查 5 个术语词（如 Negro／colored／Black Woman／Wimodaughsis），全文译法统一。
- 不满足则改到满足。

### 6. 自动检查
```
python scripts/check_bilingual.py 译文/对应篇名.zh-CN.md
```
结构契约满足（标记成对、标题合并格式、可疑错配少）则继续；有违规回步骤 4 修订。

### 7. 回填状态（双写）
检查通过后，`status` 从 `doing` 改 `done`，改两处：
- ① 项目 `translation_queue.csv` 该行；
- ② 根 `translation_queue.csv` 中 `<本项目名>,<本篇名>` 那一行（`WORKFLOW.md`「双写状态」）。

### 8. 追加日志
在本文件「运行日志」追加一行。

### 9. 循环
回到步骤 2，取下一篇 `todo`，直到全部 `done`。委派模式下由主 agent 决定是否继续派单（见 `WORKFLOW.md`「委派模式调度循环」）。

---

## 篇目清单

| # | 篇名 | 源文 | 大小 | 状态 |
|---|------|------|------|------|
| 1 | 卷首题词 | 01-epigraph.md | 0.1KB | done |
| 2 | 献词 | 02-dedication.md | 0.4KB | done |
| 3 | 我们的存在理由（卷首自陈） | 03-our-raison-detre.md | 2.8KB | done |
| 4 | 第一部「女高音助奏」部题 | 04-soprano-obligato.md | 0.5KB | done |
| 5 | 女性品格：种族新生与进步的关键要素 | 05-womanhood-a-vital-element-in-the-regeneration-and-progress-of-a-race.md | 44.7KB | done |
| 6 | 女子高等教育 | 06-the-higher-education-of-women.md | 37.9KB | done |
| 7 | 女性对阵印第安人 | 07-woman-versus-the-indian.md | 54.7KB | todo |
| 8 | 美国女性地位 | 08-the-status-of-woman-in-america.md | 21.6KB | done |
| 9 | 第二部「随意合奏」部题 | 09-tutti-ad-libitum.md | 0.7KB | todo |
| 10 | 美国有种族问题吗？若有，如何解决为佳？ | 10-has-america-a-race-problem-if-so-how-can-it-best-be-solved.md | 29.4KB | todo |
| 11 | 美国文学之一面 | 11-one-phase-of-american-literature.md | 62.8KB | todo |
| 12 | 我们的价值何在 | 12-what-are-we-worth.md | 68.6KB | todo |
| 13 | 信念的收益 | 13-the-gain-from-a-belief.md | 21.6KB | todo |
| 14 | 尾注 | 14-endnotes.md | 0.6KB | todo |

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-09-25 | 01-epigraph.md | done | 卷首题词（无署名诗节），双语 1 对块，check_bilingual/check_coverage 均 exit 0 |
| 2026-09-25 | 02-dedication.md | done | 献词（致阿内特主教），双语 1 对块，双脚本均 exit 0 |
| 2026-09-25 | 03-our-raison-detre.md | done | 卷首自陈，双语 7 对块（逐段），双脚本均 exit 0；新词：Tawawa Chimney Corner=塔瓦瓦炉畔、cadenza=华彩乐段、cul de sac=死胡同 |
| 2026-09-25 | 04-soprano-obligato.md | done | 第一部题（乔治·艾略特题诗两节），双语 1 对块，双脚本均 exit 0；新词：George Eliot=乔治·艾略特 |
| 2026-09-25 | 05-womanhood-a-vital-element-in-the-regeneration-and-progress-of-a-race.md | done | 摘要：双语 86 对块（逐段对照，含 2 首引诗）；首篇论文，库珀宣读于华盛顿有色人教士与平信徒大会：从基督教与封建制度两大源头论证女性品格乃种族新生与进步的关键要素，落脚南方黑人妇女与有色女孩的处境及教会的两处疏忽；check_bilingual 退出码 0，check_coverage 退出码 0；新定译名：新教圣公会（Protestant Episcopal Church）、公理会（Congregationalists）、《南方的黑人妇女》（克拉梅尔论文）、白十字联盟（White Cross League）、司铎（圣公会 priest）／牧师（他派 minister）、上帝休战（Truce of God）、获释奴隶（Freedmen）、天女（houri），另定麦考莱、爱默生、塔西佗、基佐、乔叟、拜伦、华兹华斯、查理曼、罗耀拉、阿佩莱斯、马丁·R·德拉尼等人物通行译名（均已回填术语表） |
| 2026-09-25 | 06-the-higher-education-of-women.md | done | 摘要：双语 67 对块（逐段，含 4 处引诗/引文块）；内容：女子高等教育之历史（1801 马雷夏尔《女子当学字母吗》→ 1833 首开淑女课程 → 当代 198/207 所高校），论女性影响对文明的调和、两性真理互补、有色女性高等教育统计（菲斯克 12 人居首）与作者本人求学经历，末吁为女子设学金；check_bilingual/check_coverage 均 exit 0；新定译名：马修·阿诺德、格兰特·艾伦、玛丽·A·利弗莫尔、萨福、阿斯帕西娅、莱辛、费奈隆、萨克雷、拜伦、爱默生、珀西瓦尔·洛厄尔《远东之魂》、雅古（Iagoo）、奥林皮娅·富尔维娅·莫拉塔、舒瓦西神父、丰唐日公爵夫人、居伊昂夫人、曼特农夫人、马金博士、韦尔斯利、安娜堡、利文斯通、亚特兰大大学、华盛顿中学、萨利克法、fait accompli=既成事实、laissez faire=放任主义、diapason=洪钟之音、dominant seventh=属七和弦、蓝袜子女学究、木兰香脂水、三R 等 |
| 2026-09-25 | 08-the-status-of-woman-in-america.md | done | 摘要：双语 37 对块（逐段，含 2 首引诗）；内容：第一部末篇，库珀论美国妇女地位——以哥伦布发现新大陆四百周年（芝加哥庆典、妇女管理委员会）切题，历数玛丽·莱昂、迪克斯、海伦·亨特·杰克逊、卢克丽霞·莫特等妇女功业，划分发现／拓居／财富生产／积累四时期，预言道德观念时代妇女当定基调（W.C.T.U. 为征）；中段论有色妇女兼遭妇女问题与种族问题、南方黑人妇女维系共和党票仓；末列哈珀、特鲁斯、史密斯、厄尔利、布里格斯、格里姆克、布朗、科平八位黑人妇女先驱，归结有色妇女独掌种族未来明暗之责任；check_bilingual 退出码 0，check_coverage 退出码 0；新定译名 15 条：基督教妇女禁酒联合会（W.C.T.U.）、妇女管理委员会（Board of Lady Managers）、积累时期（Accumulative Period）、大老党（Grand Old Party）、霍利奥克（Holyoke）、妇女问题（woman question）、一碗红豆汤（mess of pottage）、mauvais succes／en rapport／coigne of vantage（保留原文括注），及弗朗西丝·沃特金斯·哈珀、阿曼达·史密斯、萨拉·伍德森·厄尔利、玛莎·布里格斯、夏洛特·福尔坦·格里姆克、哈莉·奎因·布朗、范妮·杰克逊·科平等人物（均已回填术语表） |
| 2026-09-25 | 07-woman-versus-the-indian.md | done | 摘要：双语 74 对块（逐段对照，含 4 首引诗/警句）；评述安娜·肖牧师 1891 年全国妇女理事会论文：从维莫达西斯肤色风波切入，论证美国女性对美国礼俗之责、南方女性两大谬误（奴隶制记忆托词与「社会平等」中词歧义）、科科伦美术馆拒收有色学员事件与南北政治寓言（林肯老爹/阿拉贝拉），终篇归旨「女性的事业即弱者的事业」，印第安人、黑人、女性同得权利；check_bilingual 退出码 0，check_coverage 退出码 0；新定译名 27 条：黑小子（darkey）、黑白混血者（mulatto）、「社会平等」（social equality）、种姓（Caste）、白板（tabula rasa）、中词歧义（ambiguous middle）、金律（Golden Rule）、狄奥尼修斯（Dionysius）、征服者威廉、「五月花号」、林肯老爹、阿拉贝拉（Arabella）、吉托（Guiteau）、「棉花为王」、科科伦美术馆（Corcoran）、「编辑的抽屉」（Editor's Drawer）、《杰克盖的房子》、德尔萨特（Delsarte）、腓力与阿尔瓦、帕提亚人/米底人/以拦人等（均已回填术语表） |
| 2026-09-25 | 09-tutti-ad-libitum.md | done | 摘要：双语 3 对块；第二部「随意合奏」（Tutti ad Libitum）部题：罗伯特·勃朗宁题诗两首（一论民族乃众人趋赴更完满生命之尝试，一论共同难题在不悬想空中楼阁、先察何者可能再使之美好）＋菲利克斯·霍尔特（Felix Holt）引语（世间最大问题乃让人人分得属「人」的自由份额、监督治理者尽心与否）；check_bilingual 退出码 0，check_coverage 退出码 0；新词：罗伯特·勃朗宁、菲利克斯·霍尔特（Felix Holt，乔治·艾略特小说人物） |
| 2026-09-25 | 10-has-america-a-race-problem-if-so-how-can-it-best-be-solved.md | done | 摘要：双语 54 对块（逐段，含 4 首引诗/歌谣：《麦克白》女巫谣、席勒《钟之歌》德文原诗照录附自译、「金子投炉」诗两章）；第二部首篇：以「和平有两种」（压制之死寂 vs 活力调适）开题，借基佐《文明史》论证单一原则/单一种族独尊必致停滞（埃及、印度、希腊、黑劳士），欧洲多元素冲突平衡诞育自由；斥「美国属于美国人」排外喧嚣（红种人、五月花号 1620 与首批非洲人 1619 对照），断言美国乃诸力收拢一台、专制偏见终将窒息的终极竞技场；继而以大火异象喻上帝推动之文明进程（权宜之计皆徒然，唯以金投炉、经火炼而更贵）；后半自问自答——种族问题乃美国进步之保证，黑人因子不可替代（压舱物、守法敬权、信神），引克拉梅尔「全能者扶起卑微民族绝非为卑贱目的」作结；check_bilingual 退出码 0，check_coverage 退出码 0；新定译名 23 条：丹纳（Taine）、托克维尔（De Tocqueville）、冯·霍尔斯特（Von Holtz）、地米斯托克利（Themistocles）、席勒（Schiller）、勒南（Renan）、佛陀、埃尔吉娃（Elgiva）、小杰克·霍纳（Jack Horner）、黑劳士（Helots）、首陀罗、帕利亚（Pariah 贱民）、图兰种族（Turanian）、哥特人/匈奴人/汪达尔人/朱特人等蛮族民系、保王党人/圆颅党人、托利党人/辉格党人、教皇派/重仪文派、弗吉尼亚第一家族（F.F.V.）、完全产权（fee-simple）、龙舌兰（century plant）、imprimis/sine qua non/modus vivendi 拉丁语保留、「人总是人」（彭斯 a man's a man for a' that）、祖母式的政府（均已回填术语表「第 10 篇新增」节） |
| 2026-09-25 | 12-what-are-we-worth.md | done | [1308] 额度中断断点验收：译文已完整落盘（78 对双语块，逐段对照），check_bilingual 退出码 0、check_coverage 退出码 0（全覆盖），回填 done；原译员子代理死于收尾前，本行由调度方补记 |
| 2026-09-27 | 14-endnotes.md | done | 全书尾注 7 条（各注一条双语块，共 7 对）：注 1 为首篇宣读场合（1886 华盛顿新教圣公会有色人教士大会），注 2/3 巴斯科姆（Bascom）及其《英国文学》出处，注 4 克拉梅尔博士小册子，注 5 ’91 报告全国司铎 26 名及金堂（King Hall）院长，注 6 ’86 年以来毕业五人，注 7 康奈尔大学首位有色女毕业生（1890 理科课程）；注释编号与 ↩︎ 照搬，弯引号、不换行空格逐字保留，术语按术语表（司铎/新教圣公会/霍华德大学/金堂等）；check_bilingual 退出码 0（7 对块、标题合并满足、0 错配）、check_coverage 退出码 0（全覆盖），回填 done |
| 2026-09-27 | 13-the-gain-from-a-belief.md | done | 摘要：双语 31 对块（逐段对照，含 2 首引诗：Think it truly 三行诗、丁尼生《艺术之宫》五行）；全书压卷篇「信念的收益」：以市场中孤独的怀疑者形象开篇，代拟其唯物论—不可知论独白（休谟→孔德〔sexe aimant 括注〕→密尔/斯宾塞/刘易斯→英格索尔《我为什么是个不可知论者》），「彼界之外是黑暗与永恒沉默」；继以「寻常人感受不推理」自陈立场，论信念乃英雄气概、献身与牺牲之本（「法兰西需要一种宗教」、麦考莱笔下罗耀拉「我相信」、奴隶兄弟追北极星「人总是人」），末引丁尼生诗归于「就在这个世界」助人活进彼界、世界当向前推进一代；check_bilingual 退出码 0（31 对块、0 可疑错配），check_coverage 退出码 0（无漏译）；新定译名 16 条：英格索尔（Ingersoll）、《我为什么是个不可知论者》、帕斯卡尔、里克特（Richter）、赫胥黎教授、G. H. 刘易斯、路德／萨克森修士、西班牙狂热者、保罗／穆罕默德、丁尼生《艺术之宫》引诗、无知论（Nescience）、「黑人问题」、南方「懦夫」、人总是人（a man's a man）、鬼火（will-o-the-wisp）等（均已回填术语表「第 13 篇新增」节） |
| 2026-09-27 | 11-one-phase-of-american-literature.md | done | 摘要：双语 75 对块（逐段对照，含 7 组诗行引用块：洛威尔两行、弥尔顿《失乐园》夏娃初醒诗节分 3 段、梅奥引文、「石榴」两行、《伏都预言》17 节全录、勃朗宁一行、《麦克白》夫人两行，诗均自译存味）；第二部第二篇「美国文学之一面」：论美国文学须自具民族特性（夜莺让位反舌鸟），作家二分——为艺术而艺术（莎翁、艾略特、坡）与布道训诫（弥尔顿、卡莱尔、图尔吉）；评黑人题材写作——斯托夫人之后多为证明论点而扭曲艺术（酸菜笑话讽概括癖），重点析图尔吉六部小说（法官化身的擦鞋匠）与凯布尔（南方良知之化身）之别；斥豪威尔斯《义不容辞的义务》有色教会一幕失实（奎尔普对照、十六分之一血统说），兼评匿名《哈罗德》与唐纳利《于格特医生》；《伏都预言》评为「白人的自我剖白」，推南方两大梦魇（黑人政治主宰、种族消融）并以镇静剂与补剂为喻开方；末归于「画布正等待黑人自己的画笔」（哈里斯编雷穆斯故事对照乔叟证英语）、「有个小子正在你们中间记着笔记」与「认识你自己」；check_bilingual 退出码 0（75 对块、0 可疑错配），check_coverage 退出码 0（137 源段全覆盖）；新定译名 40 余条：莫里斯·汤普森、卡莱尔、E·P·罗、H·W·格雷迪、布莱登/斯卡伯勒/普赖斯/富钦、梅奥/帕克赫斯特博士、伊格内修斯·唐纳利、阿尔伯里·A·惠特曼、罗达·奥尔德盖特、凯列班、凯德蒙、大数人扫罗、古利奈人、比昂、南妮；《一位王室绅士》《向凯撒申诉》《炽热的犁铧》《帕克托卢斯·普赖姆》《向法老申诉》等 15 种书名篇名；伏都（Voodoo）、四分之一混血女子（quadroon）、拉扎罗尼（lazzaroni）、《帕克》杂志、波旁先生、哥伦布博览会、海上王者、「永恒之女性」、「认识你自己」等（均已回填术语表「第 11 篇新增」节） |
