# Plan.md — g-d-h-cole_the-brooklyn-murders

## 本计划信息

- **项目名称**：g-d-h-cole_the-brooklyn-murders（布鲁克林命案（G. D. H. Cole: The Brooklyn Murders, 1923））
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
| `原文/*.md` | 源文（37 文件） | 不改 |
| `译文/*.zh-CN.md` | 译文产出（块对照双语） | 翻译 agent 产出 |

执行步骤按 `prompts/翻译计划模板.md`「执行步骤」9 步推进；执行模式为委派（长篇），由子代理逐章执行。

---

## 篇目清单

| # | 篇名 | 源文 | 大小 | 状态 |
|---|------|------|------|------|
| 1 | I A Family Celebration | 01-a-family-celebration.md | 15.7KB | todo |
| 2 | II Sir Vernon's Will | 02-sir-vernon-s-will.md | 9.1KB | todo |
| 3 | III Murder | 03-murder.md | 19.1KB | todo |
| 4 | IV What Joan Found in the Garden | 04-what-joan-found-in-the-garden.md | 19.5KB | todo |
| 5 | V Plain as a Pikestaff | 05-plain-as-a-pikestaff.md | 20.4KB | todo |
| 6 | VI A Pause for Reflection | 06-a-pause-for-reflection.md | 21.7KB | todo |
| 7 | VII The Case Against Walter Brooklyn | 07-the-case-against-walter-brooklyn.md | 13.7KB | todo |
| 8 | VIII A Review of the Case | 08-a-review-of-the-case.md | 11.4KB | todo |
| 9 | IX Walter Brooklyn's Explanation | 09-walter-brooklyn-s-explanation.md | 7.4KB | todo |
| 10 | X Charis Lang | 10-charis-lang.md | 22.6KB | todo |
| 11 | XI Joan Takes Up the Case | 11-joan-takes-up-the-case.md | 20.6KB | todo |
| 12 | XII Robert Ellery | 12-robert-ellery.md | 17.9KB | todo |
| 13 | XIII An Arrest | 13-an-arrest.md | 17.2KB | todo |
| 14 | XIV Mainly a Love Scene | 14-mainly-a-love-scene.md | 12.8KB | todo |
| 15 | XV To and Fro | 15-to-and-fro.md | 10.0KB | todo |
| 16 | XVI A Link in the Chain | 16-a-link-in-the-chain.md | 19.6KB | todo |
| 17 | XVII The Lovely Lady | 17-the-lovely-lady.md | 15.9KB | todo |
| 18 | XVIII The Case for the Defence | 18-the-case-for-the-defence.md | 14.8KB | todo |
| 19 | XIX The Police Have Their Doubts | 19-the-police-have-their-doubts.md | 12.2KB | todo |
| 20 | XX Superintendent Wilson Thinks It Out | 20-superintendent-wilson-thinks-it-out.md | 9.1KB | todo |
| 21 | XXI Don Quixote | 21-don-quixote.md | 18.6KB | todo |
| 22 | XXII The Spaniard Does His Bit | 22-the-spaniard-does-his-bit.md | 11.2KB | todo |
| 23 | XXIII Walter Brooklyn Goes Free | 23-walter-brooklyn-goes-free.md | 15.0KB | todo |
| 24 | XXIV A Fresh Start | 24-a-fresh-start.md | 20.3KB | todo |
| 25 | XXV Raising the Wind | 25-raising-the-wind.md | 21.1KB | todo |
| 26 | XXVI Two Men Strike a Bargain | 26-two-men-strike-a-bargain.md | 12.9KB | todo |
| 27 | XXVII Robert Ellery's Idea | 27-robert-ellery-s-idea.md | 18.9KB | todo |
| 28 | XXVIII The Superintendent's Theory | 28-the-superintendent-s-theory.md | 9.6KB | todo |
| 29 | XXIX The Lie of the Land | 29-the-lie-of-the-land.md | 11.0KB | todo |
| 30 | XXX A Letter and Its Consequences | 30-a-letter-and-its-consequences.md | 12.1KB | todo |
| 31 | XXXI A Button in a Bag | 31-a-button-in-a-bag.md | 17.8KB | todo |
| 32 | XXXII Sir John Bunnery | 32-sir-john-bunnery.md | 9.9KB | todo |
| 33 | XXXIII On the Tiles | 33-on-the-tiles.md | 12.7KB | todo |
| 34 | XXXIV The Stable-Yard | 34-the-stable-yard.md | 14.5KB | todo |
| 35 | XXXV An Order for Bulbs | 35-an-order-for-bulbs.md | 5.0KB | todo |
| 36 | XXXVI An Afternoon Call | 36-an-afternoon-call.md | 17.1KB | todo |
| 37 | XXXVII A Happy Ending | 37-a-happy-ending.md | 10.2KB | todo |

---

## 运行日志

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
