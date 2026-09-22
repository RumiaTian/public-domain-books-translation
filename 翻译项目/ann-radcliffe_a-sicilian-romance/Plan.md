# 翻译计划（Plan.md）— ann-radcliffe_a-sicilian-romance

---

## 本计划信息

- **项目名称**：ann-radcliffe_a-sicilian-romance（一部西西里的罗曼史 / A Sicilian Romance）
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/小说文学.md
- **术语表**：术语表.md

---

## 文件分工

| 文件 | 作用 | 谁来改 |
|------|------|--------|
| `项目说明.md` | 项目基本信息、领域配置、篇目清单 | 人工 |
| `术语表.md` | 翻译硬约束层。每篇译完补充新词 | agent / 人工 |
| `translation_queue.csv` | 任务队列。每行一文件，`file, size_kb, status` 三列 | 翻译前改 doing，完成后改 done |
| `Plan.md`（本文件） | 执行步骤 + 运行日志 | agent 追加日志 |
| `原文/*.md` | 源文 | 不改 |
| `译文/*.zh-CN.md` | 译文产出（块对照双语） | 翻译 agent 产出 |

---

## translation_queue.csv 格式

```
file,size_kb,status
00-preface.md,2.6,todo
01-i.md,27.7,todo
...
```

| 字段 | 含义 | 取值 |
|------|------|------|
| `file` | 源文文件名（在 `原文/` 目录下） | 如 `01-i.md` |
| `size_kb` | 源文大小（KB）。>50KB 为长文，按通用翻译引擎第七节分段 | 数字 |
| `status` | 翻译状态 | `todo` 待译 / `doing` 翻译中 / `done` 已完成 |

---

## 执行步骤（agent 按此推进，两种模式共用）

> **谁执行**由 `项目说明.md` 的「内容形态」字段决定（见 `WORKFLOW.md`「判断内容形态」）：本项目为长篇 → 委派模式，由子代理逐篇执行本流程。无论谁执行，这 9 步不变。

### 1. 读配置（每次翻译前必读）
```
1. 本项目 Plan.md（本文件）
2. 项目说明.md
3. 术语表.md
4. prompts/通用翻译引擎.md
5. prompts/领域配置/小说文学.md
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
- 逐块对照原文，绝不漏译、不合并段落、不缩写、不总结，尤其结尾别截断。
- 严守术语表：遇表内源词必译为指定译法。新词自行确定统一译法，首次附原文「中文（English）」。
- 人物/语气/风格全文一致（文学类尤其重要），照黄金样本风格译。
- 长文（源文 >50KB）分段处理见通用翻译引擎第七节（本篇目 03-iii.md 约 65KB）。

### 5. 自检
- 完整性：源文每一段都在译文 Original 块中出现，末尾无截断。
- 块对称：Original/Chinese 数量相等，每块内段数对应。
- 标题格式：全部「英文 / 中文」合并。
- 术语一致：抽查 5 个术语词，全文译法统一。
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
| 0 | Preface（框架引言） | 00-preface.md | 2.6KB | done |
| 1 | Chapter I | 01-i.md | 27.7KB | todo |
| 2 | Chapter II | 02-ii.md | 44.2KB | todo |
| 3 | Chapter III | 03-iii.md | 65.2KB | todo |
| 4 | Chapter IV | 04-iv.md | 36.2KB | todo |
| 5 | Chapter V | 05-v.md | 13.9KB | todo |
| 6 | Chapter VI | 06-vi.md | 16.6KB | todo |
| 7 | Chapter VII | 07-vii.md | 6.8KB | todo |
| 8 | Chapter VIII | 08-viii.md | 15.7KB | todo |
| 9 | Chapter IX | 09-ix.md | 16.8KB | todo |
| 10 | Chapter X | 10-x.md | 18.9KB | todo |
| 11 | Chapter XI | 11-xi.md | 23.2KB | todo |
| 12 | Chapter XII | 12-xii.md | 19.1KB | todo |
| 13 | Chapter XIII | 13-xiii.md | 26.3KB | todo |
| 14 | Chapter XIV | 14-xiv.md | 28.0KB | todo |
| 15 | Chapter XV | 15-xv.md | 20.6KB | todo |
| 16 | Chapter XVI | 16-xvi.md | 9.4KB | todo |

（共 17 篇，约 391KB；权威进度以 `translation_queue.csv` 为准）

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-09-16 | 00-preface.md | 完成 | 2 对块（1:1、2:2）；check_bilingual 退出码 0；首立全书体例——首现附原文：西西里（Sicily）、马齐尼（Mazzini）、院长（the Abate，斜体保留）；superior 依术语表译「住持」；原文 U+FEFF×2、弯引号、*Abate* 斜体程序化提取、字节级保留 |
| 2026-09-16 | 01-i.md | 完成 | 7 对块（22 段，3+3+3+3+3+3+4）；check_bilingual 退出码 0、0 可疑错配；标题「## I / 第一章」；术语按表：朱莉娅/埃米莉娅/德·梅农夫人/文森特/罗伯特/小费迪南德/希波利图斯·德·韦雷萨伯爵/玛丽亚·德·韦洛尔诺/路易莎·贝尔尼尼；南塔=南楼系、the lute=鲁特琴；首现附原文：那不勒斯/卡拉布里亚/墨西拿海峡/西西里/埃特纳火山/巴勒莫/塔索/圣尼古拉修道院；phaenomenon/massey/fabrick 等旧拼写照今义译；U+FEFF×9、弯引号程序化提取字节级保留 |
| 2026-09-16 | 02-ii.md | 完成 | 26 对块（36 段+诗 1 块）；check_bilingual 退出码 0、0 可疑错配、52 标记；标题「## II / 第二章」；本章首现附原文：韦雷萨伯爵/希波利图斯/穆里亚尼伯爵/玛蒂尔达·康斯坦扎/德拉·法泽利侯爵/马齐尼/南楼/路易莎·德·贝尔尼尼/贝尔尼尼伯爵/德莫纳山谷/奥兰多/德·梅农骑士/玛丽亚·德·韦洛尔诺；德·梅农夫人长篇插叙按引语段约定（段首开引号、末段闭合）；窗下夜歌 8 行保留 > 前缀行式对译，英文侧单空格排版行为源文伪影，语义逐行对应；U+FEFF×15、弯引号、行尾空格程序化提取字节级保留 |
| 2026-09-16 | 04-iv.md | 完成 | 19 对块（48 段+酒神歌 1 块）；check_bilingual 退出码 0、0 可疑错配；标题「## IV / 第四章」；术语按表：朱莉娅/埃米莉娅/德·梅农夫人/小费迪南德/希波利图斯/卢奥沃公爵（单称依语境「老公爵」）/罗伯特/南楼南塔系/匪帮 banditti；本章首现附原文：莉赛特（Lisette）/安东尼（Anthony）/格雷戈里（Gregory）/理查德（Richard）/里卡尔多（Riccardo，公爵之子、匪首）/巴克斯（Bacchus）/马伦蒂诺森林（the forest of Marentino，全书首现）；desend/habiliments 等旧拼写照今义译；酒歌 3 节 12 行保留 > 前缀行式对译、*sober* 斜体保留；U+FEFF×20、弯引号、诗歌空行/单空格排版行程序化提取字节级保留 |
| 2026-09-16 | 03-iii.md | 完成 | 34 对块（正文 24 块 119 段 + 暮歌 10 节 40 行分 10 块；65.2KB 超大章 4 批拼合：L1-113/L114-146/L147-167/L168-182）；check_bilingual 退出码 0、0 可疑错配；标题「## III / 第三章」；原文行程序化提取、字节级一致（源文 L2-182 共 119 非空白行逐一比对 identical；U+FEFF×65、U+200A×2 全在原文块，译文块 0 隐形字符；诗区 30 个单空格排版行原样保留）；术语按表：朱莉娅/埃米莉娅/小费迪南德/希波利图斯/德·梅农夫人/侯爵夫人/卢奥沃公爵/罗伯特/文森特/南楼南塔系/匪帮 banditti/鲁特琴；本章首现附原文：希波利图斯（Hippolitus）/洛梅利侯爵/德拉·坎波家/亨利·德拉·坎波/卡拉布里亚/意大利；暮歌 10 节 40 行保留 > 前缀行式对译（译文行尾双空格硬换行）、*could*/*but*/*route* 斜体保留；建议术语表新增：洛梅利侯爵（Marquis de Lomelli，希波利图斯至亲、病故留产）、德拉·坎波家/亨利·德拉·坎波（Henry della Campo，与马齐尼家三代宿仇、南楼被囚死者） |
| 2026-09-16 | 05-v.md | 完成 | 7 对块（22 段，3+3+3+3+3+3+4）；check_bilingual 退出码 0、0 可疑错配；标题「## V / 第五章」；卢奥沃公爵追踪线全章单称 the duke 依语境统译「公爵」；术语按表：住持（the Superior，本章酗酒修道院住持，区别于圣奥古斯丁修道院「院长」）/修士/修会服色/修道院/马齐尼城堡；本章首现附原文：意大利（Italy）/朱莉娅（Julia）/马齐尼城堡（the castle of Mazzini）；住持醉宴祝酒辞 “Profusion and confusion” 译「奢靡无度，乱作一团！」；uncertainity/lighting 等旧拼写照今义译；league 译「里格」；U+FEFF×2（第 19 段两处破折号前）、弯引号程序化提取字节级保留 |
| 2026-09-16 | 07-vii.md | 完成 | 2 对块（源文为 2 个超长段，块对照 1:1 段对应）；check_bilingual 退出码 0、0 处疑错配；标题「## VII / 第七章」；术语表新增：卡泰丽娜（Caterina）/卡洛（Carlo）/尼科洛（Nicolo）/法里尼（Farrini）；本章首现附原文：德·梅农夫人/朱莉娅/费迪南德（此处指小费迪南德）/埃米莉娅/那不勒斯；引文 "from Nature up to Nature's God" 直译并保留弯引号；syren（塞壬）、chesnut、'ere 等旧拼讹拼照今义译；内嵌 U+FEFF×3（长破折号前）程序化提取，原文块字节级一致 |
| 2026-09-16 | 06-vi.md | 完成 | 5 对块（13 段，3+3+3+3+1）；check_bilingual 退出码 0、0 可疑错配；标题「## VI / 第六章」；术语按表：小费迪南德/朱莉娅/埃米莉娅/德·梅农夫人/侯爵夫人/希波利图斯/卢奥沃公爵（单称依语境「老公爵/公爵」）/南楼南塔系/马伦蒂诺森林；德拉·坎波沿用 ch03 译名不附原文；本章首现附原文：彼得（Peter）/卡利尼（Calini，德·梅农夫人故乡、退隐修道院地）；橡木客厅沿用 ch01 译名；U+FEFF×17、U+200A×1（’Tis 前）程序化提取、原文块与源文字节级一致，译文块 0 隐形字符；建议术语表新增地名：卡利尼（Calini） |
| 2026-09-16 | 08-viii.md | 完成 | 8 对块（16 段，2+2+2+1+2+3+2+2）；check_bilingual 退出码 0、0 可疑错配；标题「## VIII / 第八章」；术语按表：朱莉娅/德·梅农夫人/卢奥沃公爵/圣奥古斯丁修道院/希波利图斯/埃米莉娅/马齐尼城堡/里格；本章新名首现附原文：卡特琳娜（Caterina）/费里尼村（Ferrini，第 4 段讹拼 Farrini 照今义统一）/马尔西（Marcy）/阿祖利亚（Azulia）/穆拉尼侯爵（Marquis Murani，与 ch02 Count Muriani 原文拼写不同，暂按两人处理）/院长（*Padre Abate* 斜体保留）；the marchioness＝继室侯爵夫人；Entendered 讹拼照今义译「历经忧患」；U+FEFF×3 与弯引号程序化提取、原文块字节级一致 |
| 2026-09-16 | 09-ix.md | 完成 | 15 对块（正文 14 块 39 段 + 希波利图斯颂歌 1 块按源文 64 行结构镜像对译）；check_bilingual 退出码 0、0 可疑错配；标题「## IX / 第九章」；原文行程序化提取、Original 块与源文切片字节级一致（U+FEFF×19 全部保留于原文块、译文块 0 隐形字符；诗区单空格行/空行排版骨架逐行镜像）；术语按表：朱莉娅/德·梅农夫人/希波利图斯·德·韦雷萨伯爵/科尔内莉娅/圣奥古斯丁修道院/那不勒斯/马齐尼城堡/住持（the Superior，区别于院长 the Abate）；本章新名首现附原文：安杰洛（Angelo）/马里内利侯爵（the Marquis Marinelli）/阿尔维纳（Alverna，颂歌首行）；assume/receive the veil 译「领纱出家／领受圣纱」；admited/Enthron’d/madd’ning 等旧拼诗拼照今义译；建议术语表新增：安杰洛（Angelo，科尔内莉娅恋人、后入圣奥古斯丁修道院隐居）、马里内利侯爵（Marquis Marinelli，曾向科尔内莉娅提亲）、阿尔维纳（Alverna，颂歌咏叹之山） |
| 2026-09-16 | 10-x.md | 完成 | 9 对块（26 段，3+3+3+3+3+3+3+2+3）；check_bilingual 退出码 0、0 可疑错配；标题「## X / 第十章」；术语按表：朱莉娅/德·梅农夫人/卢奥沃公爵/科尔内莉娅/侯爵；本章首现附原文：朱莉娅（Julia）/德·梅农夫人（Madame de Menon）/院长（the *Abate*，斜体保留）/卢奥沃公爵（the Duke de Luovo）/科尔内莉娅（Cornelia）/修士（friar）；the Superior 本章与 the Abate 同指圣奥古斯丁修道院首脑，统一译「院长」并首现附原文（the Superior）；院长训话称呼 Daughter 译「我的孩子」、Holy father 译「圣父」；thoughful 等旧拼写照今义译；行尾统一 LF、无 BOM（Windows write_text 默认 CRLF 已显式修正）；U+FEFF×20、弯引号程序化提取、原文块 26/26 段与源文字节级一致；建议术语表 the Superior 备注补注第 X 章语境同指 the Abate 时统一译「院长」 |
| 2026-09-16 | 12-xii.md | 完成 | 10 对块（正文 9 块 31 段 + 风暴四行诗 1 块按源文 10 行结构镜像对译）；check_bilingual 退出码 0、0 可疑错配；标题「## XII / 第十二章」；术语按表：朱莉娅/小费迪南德/德·梅农夫人/文森特/院长（the Padre Abate）/侯爵的手下/里格/马齐尼城堡；英文块程序化从源文行提取，U+FEFF 隐形字符字节级保留 |
| 2026-09-16 | 11-xi.md | 完成 | 7 对块（23 段，4+3+2+2+4+4+4）；check_bilingual 退出码 0、0 可疑错配；标题「## XI / 第十一章」；术语按表：朱莉娅/德·梅农夫人/希波利图斯/小费迪南德/卢奥沃公爵/科尔内莉娅/文森特/马齐尼城堡/圣奥古斯丁修道院；the Superior 本章与 the Abate 同指圣奥古斯丁修道院首脑，循 ch10 先例统一译「院长」；本章首现附原文：朱莉娅（Julia）/德·梅农夫人（Madame de Menon）/终傅圣事（extreme unction）/院长（the Padre Abate）/科尔内莉娅（Cornelia）/希波利图斯（Hippolitus）/文森特（Vincent）/马齐尼城堡（the castle of Mazzini）/卢奥沃公爵（the Duke de Luovo）/圣纱（the veil）/小费迪南德（Ferdinand）/献身祝圣（consecration）/铁栅（the grate）/韦雷萨伯爵（the Count de Vereza）/意大利（Italy）/圣奥古斯丁修道院（the abbey of St. Augustin）；assume/adopt the veil 译「领受圣纱/领纱出家」；院长称呼 Daughter 循 ch10 译「我的孩子」；the turned his horse/inpracticable/preparations were began 等讹拼照今义译；原文行程序化提取，U+FEFF×16、NBSP×1 字节级保留，原文块 23/23 段与源文逐一比对一致；行尾 LF、无 BOM（write_text 默认 CRLF 已显式修正） |
| 2026-09-16 | 13-xiii.md | 完成 | 13 对块（39 段，每块 3 段）；check_bilingual 退出码 0、0 可疑错配；标题「## XIII / 第十三章」；原文段落程序化提取、Original 块与源文字节级一致（7 处 U+FEFF 长破折号原样保留）；术语按表：希波利图斯/朱莉娅/科尔内莉娅/德·梅农夫人/小费迪南德/圣奥古斯丁修道院/匪帮（banditti）；the duke 依语境指卢奥沃公爵、the Padre Abate 与 the Abate 同指统一「院长」；本章首现附原文：希波利图斯（Hippolitus）/卡拉布里亚（Calabria）/科尔内莉娅（Cornelia）/朱莉娅（Julia）/马齐尼城堡/西西里（Sicily）/圣奥古斯丁修道院/意大利（Italy）/小费迪南德（Ferdinand）/德·梅农夫人/匪帮（banditti）/保罗（Paulo）；讹拼 skriek/suspence 照今义译；术语表追加：保罗（Paulo，ch13 匪帮成员） |
| 2026-09-16 | 14-xiv.md | 完成 | 20 对块（59 段，19 块×3 段+尾块 2 段）；check_bilingual 退出码 0、0 可疑错配；标题「## XIV / 第十四章」；原文段落程序化提取、Original 块与源文字节级一致（14 行含 U+FEFF 长破折号原样保留）；术语按表：朱莉娅/小费迪南德/希波利图斯/埃米莉娅/德·梅农夫人/卢奥沃公爵/玛丽亚·德·韦洛尔诺/文森特/匪帮（banditti）/南楼系/马齐尼城堡/圣奥古斯丁修道院/那不勒斯/巴勒莫/里格；the duke 依语境指卢奥沃公爵；本章首现附原文：朱莉娅（Julia）/小费迪南德（Ferdinand）/希波利图斯（Hippolitus）/匪帮（banditti）/帕利尼（Palini）/巴勒莫（Palermo）/埃米莉娅（Emilia）/马齐尼城堡（the castle of Mazzini）/南楼（the southern buildings）/玛丽亚·德·韦洛尔诺（Maria de Vellorno）/文森特（Vincent）/那不勒斯（Naples）/圣奥古斯丁修道院（the abbey of St. Augustin）/德·梅农夫人（Madame de Menon）/卢奥沃公爵（the Duke de Luovo）；讹拼 prophanation/desparation/creek/craggs/vermil 照今义译；本章 the marchioness 均指生母路易莎，称谓统一「侯爵夫人」；建议术语表追加：帕利尼（Palini，镇名，附近有两座修道院）；建议 Vincent 备注补注：另指城堡老仆（奉命看守被囚的侯爵夫人者，ch14 南楼之谜关键人物，与闹鬼故事中的第三代侯爵文森特同名异人） |
| 2026-09-16 | 16-xvi.md | 完成 | 7 对块（18 段，3+3+3+3+3+3+1；第 6 块尾镜像源文 --- 分隔线）；check_bilingual 退出码 0、0 可疑错配；标题「## XVI / 第十六章」；原文段落程序化提取、Original 块与源文字节级一致（5 处 U+FEFF＋1 处 NBSP 原样保留）；术语按表：小费迪南德/朱莉娅/埃米莉娅/希波利图斯/德·梅农夫人/卢奥沃公爵/侯爵夫人/南楼系/马齐尼城堡/马伦蒂诺森林/巴勒莫/那不勒斯；本章首现附原文：小费迪南德（Ferdinand）/南楼（the southern buildings）/侯爵夫人（the marchioness）/朱莉娅（Julia）/匪帮（banditti）/巴勒莫（Palermo）/马伦蒂诺森林（the forest of Marentino）/希波利图斯（Hippolitus）/马齐尼城堡（the castle of Mazzini）/卢奥沃公爵（the Duke de Luovo）/意大利（Italy）/西西里（Sicily）/埃米莉娅（Emilia）/那不勒斯（Naples）/德·梅农夫人（Madame de Menon）/圣奥古斯丁修道院（St. Augustin’s）/马齐尼第六代侯爵（the sixth Marquis de Mazzini）；斜体 *that which is right* 保留为 *合乎正道之事*；全书末章大结局（生母之谜揭晓与团圆收束），章节文件收尾 |
| 2026-09-16 | 15-xv.md | 完成 | 16 对块（40 源文段：3+4+3+3+4+2+3+2+1+绝笔信引用块 3 行+2+1+1+2+3+3）；check_bilingual 退出码 0、0 可疑错配；标题「## XV / 第十五章」；英文块自源文逐行字节级提取（U+FEFF×30/U+200A/NBSP 原样保留）；新人物 Baptista＝巴蒂斯塔、the Cavalier de Vincini＝德·温奇尼骑士（头衔用法，与 chevalier de Menon 同构译「骑士」，建议术语表增补）；the convent of St. Nicolo 按既有 St. Nicholas 条统一「圣尼古拉修道院」 |

## 2026-09-16 完书收尾（主 Agent）

- **全书 17/17 done**（批次1直启·default-translator·c3，20:33–21:29 约 56 分钟）。
- 主 Agent 验收 17 件全过检（check_bilingual 退出码 0）；65.2KB 超大章 03-iii 四批 append-only 攻坚成功（119 非空行逐行 identical）。
- 撞名两组裁定统一：Caterina=卡泰丽娜（ch08 改4处）、Ferrini（讹拼 Farrini）=费里尼（ch07 改1处）；the Superior/the Abate 同指语境统一「院长」（X/XI 章扩注）；Vincent 同名异人备注（侯爵 vs 看守老仆）。
- **Original 块字节保真硬约束（开书派单首立）全程生效**：各章程序化提取+逐行 identical 断言，U+FEFF/U+200A/NBSP 计数全等（homemaker 教训落地）。
- 术语表并发回填 14 轮（含代理自补 Paulo/卡泰丽娜等，重复表头与 the Superior 重复条目已程序化清理，63+ 行全唯一）。
- 事故账：13-xiii/14-xiv 两行遭并行代理陈旧读-改-写竞态回滚 todo（译文与验收俱在），主 Agent 依地面真值裁定恢复 done；两代理曾误触根 CSV（恒等操作零影响）。
- 认领锁已删除，流转完成。
