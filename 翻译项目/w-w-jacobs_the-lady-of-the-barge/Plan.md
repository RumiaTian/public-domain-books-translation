# Plan.md — w-w-jacobs_the-lady-of-the-barge

## 本计划信息

- **项目名称**：w-w-jacobs_the-lady-of-the-barge（驳船上的夫人（W. W. Jacobs: The Lady of the Barge, 1902））
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
| `原文/*.md` | 源文（12 文件） | 不改 |
| `译文/*.zh-CN.md` | 译文产出（块对照双语） | 翻译 agent 产出 |

执行步骤按 `prompts/翻译计划模板.md`「执行步骤」9 步推进。

---

## 篇目清单

| # | 篇名 | 源文 | 大小 | 状态 |
|---|------|------|------|------|
| 1 | a-golden-venture | a-golden-venture.md | 22.1KB | todo |
| 2 | a-mixed-proposal | a-mixed-proposal.md | 21.4KB | todo |
| 3 | a-tiger-s-skin | a-tiger-s-skin.md | 24.8KB | todo |
| 4 | an-adulteration-act | an-adulteration-act.md | 22.2KB | todo |
| 5 | bill-s-paper-chase | bill-s-paper-chase.md | 21.7KB | todo |
| 6 | captain-rogers | captain-rogers.md | 22.2KB | todo |
| 7 | cupboard-love | cupboard-love.md | 21.5KB | todo |
| 8 | in-the-library | in-the-library.md | 19.6KB | todo |
| 9 | the-lady-of-the-barge | the-lady-of-the-barge.md | 23.2KB | todo |
| 10 | the-monkey-s-paw | the-monkey-s-paw.md | 22.1KB | todo |
| 11 | the-well | the-well.md | 23.7KB | todo |
| 12 | three-at-table | three-at-table.md | 13.5KB | todo |

---

## 运行日志

| 日期 | 事件 | 备注 |
|------|------|------|
| 2026-08-17 | 建项目 | epub 提取 12 篇，术语表初版建成 |
| 2026-08-18 | the-monkey-s-paw.md 译毕 | check_bilingual 退出码 0；25 对块、144 段全覆盖无漏译；术语表猴爪篇补词 6 条（赫伯特/莫里斯/军士长/莫与梅金斯/拉伯纳姆别墅/《一千零一夜》） |
| 2026-08-18 | the-lady-of-the-barge.md 译毕 | check_bilingual 退出码 0（0 错配）；32 对块、161 段全覆盖无漏译；术语表补「驳船上的夫人篇专词」11 条（露西/路易莎与露露/约翰/阿拉贝拉号/科尔舍姆/格林尼治/斯库纳帆船/驳船佬/安息日浸礼会/卫斯理派/彼列的儿子） |
| 2026-08-18 | the-well.md 译毕 | check_bilingual 退出码 0（0 错配）；31 对块、167 段全覆盖无漏译；术语表补「井篇专词」5 条（杰姆/奥莉芙/威尔弗雷德·卡尔/乔治/克罗伊斯） |
| 2026-08-18 | three-at-table.md 译毕 | check_bilingual 退出码 0（0 错配）；17 对块、69 段全覆盖无漏译；术语表补「三人同桌篇专词」6 条（阿什维尔/安妮/皇家乔治/波尔图酒/隐多珥的女巫/约拿）；项目 12 篇全部完成，收官 |
