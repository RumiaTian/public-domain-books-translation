# Plan（《英语如她所言》翻译计划）

> 从 `prompts/翻译计划模板.md` 复制建立。执行步骤、CSV 格式等通用规范见模板，此处为本书实例。

---

## 本计划信息

- **项目名称**：pedro-carolino_jose-da-fonseca_english-as-she-is-spoke（《英语如她所言》，佩德罗·卡罗利诺 / 若泽·达·丰塞卡）
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
| `术语表.md` | 翻译硬约束层（本书核心是「照错译错」策略）。每篇译完补充新词 | agent / 人工 |
| `translation_queue.csv` | 任务队列。每行一文件，`file, size_kb, status` 三列 | 翻译前改 doing，完成后改 done |
| `Plan.md`（本文件） | 执行步骤 + 运行日志 | agent 追加日志 |
| `原文/*.md` | 源文（错误英语为内容本体，一字不改） | 不改 |
| `译文/*.zh-CN.md` | 译文产出（块对照双语） | 翻译 agent 产出 |

---

## 篇目清单

| # | 篇名 | 源文 | 大小 | 状态 |
|---|------|------|------|------|
| 1 | 引言（James Millington） | 01-introduction.md | 11.4KB | done |
| 2 | 作者原序 | 02-authors-preface.md | 1.9KB | done |
| 3 | 词汇表：人 | 03-of-the-man.md | 4.9KB | done |
| 4 | 常用短语 | 04-familiar-phrases.md | 3.1KB | done |
| 5–40 | 常用对话 36 篇 | 05-…md ~ 40-…md | 0.1–1.1KB | done |
| 41 | 书信范文 | 41-familiar-letters.md | 1.1KB | done |
| 42 | 轶事 | 42-anecdotes.md | 6.1KB | done |
| 43 | 成语与谚语 | 43-idiotisms-and-proverbs.md | 1.8KB | done |

（36 篇对话逐篇明细见 `translation_queue.csv`，权威状态以 CSV 为准）

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
| 2026-08-18 | 22-with-a-watch-maker / 23-for-to-visit-a-sick / 24-for-to-travel / 25-with-a-inn-keeper / 26-from-the-house-keeping / 27-for-the-comedy | done（各篇 check_bilingual.py 退出码 0，块对 4/12/11/5/5/19） | 对话逐条对照；照错译错：arrested a coach=逮捕了一辆马车、bat buffoons=蝙蝠丑角、parlour=客厅（正厅误作）、her/they 人称误用照译她/他们 |
| 2026-08-18 | 28-the-hunting / 29-the-fishing / 30-with-a-furniture-tradesman / 31-for-embarking-one-s-self / 32-with-a-gardener / 33-the-books-and-of-the-reading / 34-the-field | done（退出码 0，块对 11/5/4/4/8/2/2） | 野兔 him 照译「他」；thumbs=拇指（英寸误作）；cup the trees=杯剪；fumed=熏（施肥误作）；You mistake you=您弄错了您 |
| 2026-08-18 | 35-the-writing / 36-with-a-bookseller / 37-with-a-dentist / 38-with-a-laundress / 39-for-to-swim / 40-the-french-language | done（退出码 0，块对 5/9/9/2/3/7） | pens spit=笔吐唾沫；row=划（游泳误作）；appleed my self=把自己苹果上去；flay it=剥它的皮；mamel 造词=瓷琅 |
| 2026-08-18 | 41-familiar-letters / 42-anecdotes / 43-idiotisms-and-proverbs | done（退出码 0，块对 3/14/47） | 书信保留 ## 小节；轶事按 --- 14 则逐块对照；Gossip=嚼舌的；Boileau 双关零注释直译（喝红酒/让-燕麦）；He sin in trouble water=他在浑水里犯罪；craunch the marmoset=把小狨猴嚼得咯吱响 |
| 2026-08-18 | 01-introduction | done（退出码 0，块对 13） | Millington 引言按正经维多利亚散文译；引文内错误英语照错译错并与正文各篇口径对齐；法语/葡语引文保留原文；引言中成语引句已对齐 43 篇译法 |
| 2026-08-18 | 02-authors-preface / 03-of-the-man / 04-familiar-phrases | done（退出码 0，块对 4 / 36 小节 / 103） | 原序整篇洋径浜照字面硬译；词表 36 组双列表逐格直译（quater master=四等主人、Cooper=箍桶匠、keel=龙骨）；短语 102 条逐条对照＋End First Part's |
| 2026-08-18 | 05-…-21 共 17 篇对话（05 早安 / 06 晨访 / 07 穿衣 / 08 散步 / 09 天气 / 10 写信 / 11 赌博 / 12 裁缝 / 13 理发师 / 14 早餐 / 15 打听 / 16 买布 / 17 正餐 / 18 讲法语 / 19 看城 / 20 探人 / 21 骑马） | done（各篇退出码 0） | 对话逐条列表对照；For to 标题照「为了去……」生硬结构；半过三点/太阳躺下了/她在四点钟做起魔鬼来/唱一块场地（area←aire 误查按错词译）；deer/swill/witch 类英语层面错拼按意图译 |
