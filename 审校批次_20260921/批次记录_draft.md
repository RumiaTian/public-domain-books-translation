# 阶段三审校批次记录（2026-09-21）· 草稿

在池 **18 本**（可审池 19 本中 `james-mcintyre_poetry` 维持挂起，见 `译文缺陷取证_james-mcintyre_poetry_2026-09-16.md`）；并发上限 **5 个子代理**；按原文体积升序分派。
任务说明书：`审校批次_20260921/简报模板.md`；预检：`审校批次_20260921/预检/<项目名>.txt`；台账：`审校批次_20260921/批次台账.md`。

## 波次与状态

| # | 项目 | 原文KB | 等级 | A/B/C | 主 Agent 亲验 | 备注 |
|--:|---|--:|:--:|:--:|---|---|
| 1 | `arthur-quiller-couch_on-the-art-of-writing` | 365.2 | **C 需关注** | 5/3/4 | ✓ 缺失6处(epub有/译文无)+悬空冒号 | 初判 D，派发方按 B-5 归一为 C；须重抽 ch4/5/8/9 |
| 2 | `edgar-wallace_the-crimson-circle` | 367.9 | **A 优秀** | 0/2/6 | ✓ ch16章题/ch32 tin mug | 英文块词级零损 |
| 3 | `constance-holme_the-splendid-fairing` | 369.7 | **D 严重** | 1/7/7 | ✓ v-2 章末整节双侧同缺(7段/48%) | 挂起·待修：重做 v-2 |
| 4 | `sax-rohmer_brood-of-the-witch-queen` | 370.1 | **B 良好** | 1/2/3 | ✓ the-bats 段内漏句 | Set 译名两制 |
| 5 | `arthur-machen_the-hill-of-dreams` | 371.3 | **B 良好** | 0/3/4 | ✓ 「事地」「亲耳告解」 | 引号体例两制 |
| 6 | `algis-budrys_short-fiction` | 372.8 | **A 优秀** | 0/2/3 | — 无 A 级 | 精读7篇+3篇抽样(已披露) |
| 7 | `edison-marshall_shepherds-of-the-wild` | 375.7 | **B 良好** | 1/3/5 | ✓ xxvi 段4句漏3句 | 附录4项未抽(B) |
| 8 | `henry-van-dyke-jr_poetry` | 379.8 | **B 良好** | 2/11/4 | ✓ 两处副题双侧同缺 | 实为228首诗；缺10行题注出处(B) |
| 9 | `h-beam-piper_space-viking` | 381.4 | **B 良好** | 0/5/2 | ✓ Audhumla两形/ch22分隔线 | 术语表 Napolyan 建库笔误 |
| 10 | `dorothy-canfield-fisher_the-homemaker` | 382.8 | **B 良好** | 0/3/6 | ✓ 引号体例分裂(4章「」) | 附录4页未抽(B) |
| 11 | `ann-radcliffe_a-sicilian-romance` | 391.2 | **B 良好** | 0/4/5 | — 无 A 级 | 附页5件未抽(B) |
| 12 | `henry-handel-richardson_the-getting-of-wisdom` | 401.3 | **B 良好** | 1/4/6 | ✓ iv篇末句双侧同缺 | 第VI章书信错字为刻意镜像(非缺陷) |
| 13 | `xavier-de-maistre_short-fiction_various-translators` | 404.2 | **D 严重** | 1/2/4 | ✓ 唱词42行仅5行幸存 | 挂起·待修：重抽 prisoners |
| 14 | `h-m-tomlinson_gallions-reach` | 404.8 | **B 良好** | 1/4/6 | ✓ ch6 整段漏译(拆分掩盖) | 术语表自冲突；版式页5页(B) |
| 15 | `thea-von-harbou_metropolis_the-readers-library` | 412.2 | **B 良好** | 0/3/9 | ✓ 3组术语异写 | 首派遇 provider 错误，重派成功 |
| 16 | `p-g-wodehouse_indiscretions-of-archie` | 414.5 | **B 良好** | 0/4/3 | ✓ ch19/21 header块同缺+讹误 | 术语表 Lu 两行冲突 |
| 17 | `p-g-wodehouse_something-new` | 418.6 | **B 良好** | 0/4/4 | ✓ Freddie两制+衍字 | 英文块 EXACT 零损 |
| 18 | `georgette-heyer_the-masqueraders` | 505.5 | 进行中 | - | - | 两轮单代理派发均 provider 故障；改双代理分区审校 |

**当前小计（17/18）**：A 优秀 2 / B 良好 12 / C 需关注 1 / D 严重 2。

## 本批关键情报（判例）

1. **双侧同缺仍是最主要 A 级形态**（块对称/段数门禁全拦不住）：witch-queen(the-bats 段内句)、getting-of-wisdom(iv 末句)、van-dyke(两处副题)、de-maistre(唱词 37/42 行)、quiller-couch(6 处 773 字符)、archie(2 处 header 块)、splendid-fairing(v-2 章末 7 段)。
2. **新失效模式：段数对称下的整段置换**——gallions-reach ch6 第 4 块 EN=CN=3 段表面全对称，但中文第二段被换成无关内容，EN 第二段整段无译文（拆分掩盖）。**块对称 + 段数三方对齐都不足以排除漏译，必须逐段语义对齐**。
3. **抽取环节缺陷集中在 epub→原文 转换**：de-maistre 唱词 `<span>` 行与 `<header>` 说话人、archie 两处 `<header>` 标题块、quiller-couch 4 章、van-dyke 两处副题——建议在阶段一/二的抽取管线增加「epub 元素级清单比对」（song/header/blockquote 类元素计数对回）。
4. **预检假阳性高发**：本批 12+ 本报告指出预检「幽灵条目/落位偏低/残留」多为子串、斜体、连字符、`---` 行、大小写等口径问题（如 Bruce Cairn 7/742 实为 100% 落位、King Napolyan 为建库笔误）。**建议后续修订 `precheck_review.py`：按词条独立计数、剔除 `---`/标题行、处理斜体与撇号变体**。
5. **术语表自冲突多处**：`Lu`（archie 两行）、`Sinclair`（gallions 两条）、`Set`（witch-queen 回填说明不一致）、`Ivan/Cossacks`（de-maistre 表与正文冲突）、`tin/tin mug`（crimson-circle 合并定名致失真）——建库期条目质量需专项清理。
6. **D/C 口径裁决（本批定例）**：判 D 一律以 B-5 四条判据为准（B-4 只用于区分 A/B 级别）。quiller-couch 6 处零星缺失（0.17%）不触发 D → C 需关注 + 挂起·待修；de-maistre（篇内 26.8%）与 splendid-fairing（章末整节 48%）触发 (a)(b) → D。简报模板已同步此口径。
7. **provider 稳定性**：`metropolis` 首派被拒后重派成功；`masqueraders`（本批最大 505KB）两轮单代理派发均在 provider 侧失败（拒绝 / 上游 JSON 无效），改用**双代理分区审校**（A：数据层全书+ch01–17；B：ch18–33+专项④⑤与体例/一致性扫描），分区报告存 `审校批次_20260921/预检/masq_partA.md`、`masq_partB.md`，由派发方合并为正式报告并在报告内披露分区过程。

## 挂起·待修清单（须在阶段四打包前处置）

| 项目 | 挂起点 | 修复动作 | 复算 |
|---|---|---|---|
| `constance-holme_the-splendid-fairing` | v-2 章末 7 段双侧同缺（终场） | 重做该章后 7 段的块对照与译文 | `check_chapter_ratio.py` v-2 行；`check_coverage.py` |
| `xavier-de-maistre_short-fiction_various-translators` | prisoners 篇 42 行唱词 + 6 说话人标签未抽 | 重抽该篇 song div/header → 补译 | `check_source_coverage.py` 至缺失归零 |
| `arthur-quiller-couch_on-the-art-of-writing` | 6 处素材缺失（773 字符） | 重抽 chapter-4/5/8/9.xhtml → 补译 | `check_source_coverage.py` |
| `p-g-wodehouse_indiscretions-of-archie` | ch19/ch21 两处 header 标题块 | 重抽两章 header → 补译 | `check_source_coverage.py` |
| `henry-van-dyke-jr_poetry` | 10 行题注/出处缺失（B 级） | 重抽对应行 → 补译 | 同上 |
| 附录类（不阻塞发布，记 B）：`shepherds`(4项)/`homemaker`(4页)/`sicilian`(5件)/`gallions`(5页)/`archie`(术语表)/… | 出版方版式页未抽 | 视体例决定是否收录 | — |

## 完成动作

- [x] 18 本报告落盘（第 18 本分区合并中）
- [x] A/D 级缺陷主 Agent 亲验（17/17 已完成）
- [ ] `python scripts/refresh_progress.py` 刷新总控
- [ ] 本记录定稿至根目录 `阶段三审校批次记录_2026-09-21.md`
