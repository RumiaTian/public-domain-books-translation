# Plan.md

## 本计划信息

- **项目名称**：pierre-souvestre_marcel-allain_fantomas_cranstoun-metcalfe（芳托马斯 Fantômas）
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
| `translation_queue.csv` | 任务队列（3 列） | 翻译前改 doing，完成改 done |
| `Plan.md`（本文件） | 执行步骤 + 运行日志 | agent 追加日志 |
| `原文/*.md` | 源文 | 不改 |
| `译文/*.zh-CN.md` | 译文产出（块对照双语） | 翻译 agent 产出 |

---

## 执行步骤

按 `prompts/翻译计划模板.md`「执行步骤」9 步推进（读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志）。本书为**长篇·委派模式**：主 agent 调度，每章下沉一次性子代理执行，并发 ≤ 3，简报见 `WORKFLOW.md`「子代理简报」。

---

## 篇目清单

| # | 章名（罗马数字） | 源文 | 大小 | 状态 |
|---|------|------|------|------|
| 1 | I The Genius of Crime | 01-the-genius-of-crime.md | 20.7KB | todo |
| 2 | II A Tragic Dawn | 02-a-tragic-dawn.md | 27.2KB | todo |
| 3 | III The Hunt for the Man | 03-the-hunt-for-the-man.md | 15.5KB | todo |
| 4 | IV No, I Am Not Mad | 04-no-i-am-not-mad.md | 20.7KB | todo |
| 5 | V Arrest Me | 05-arrest-me.md | 12.4KB | todo |
| 6 | VI Fantômas, It Is Death | 06-fantomas-it-is-death.md | 32.0KB | todo |
| 7 | VII The Criminal Investigation Department | 07-the-criminal-investigation-department.md | 25.7KB | todo |
| 8 | VIII A Dreadful Confession | 08-a-dreadful-confession.md | 19.5KB | todo |
| 9 | IX All for Honour | 09-all-for-honour.md | 23.4KB | todo |
| 10 | X Princess Sonia's Bath | 10-princess-sonia-s-bath.md | 26.3KB | todo |
| 11 | XI Magistrate and Detective | 11-magistrate-and-detective.md | 14.7KB | todo |
| 12 | XII A Knockout Blow | 12-a-knockout-blow.md | 15.7KB | todo |
| 13 | XIII Thérèse's Future | 13-therese-s-future.md | 13.2KB | todo |
| 14 | XIV Mademoiselle Jeanne | 14-mademoiselle-jeanne.md | 11.3KB | todo |
| 15 | XV The Mad Woman's Plot | 15-the-mad-woman-s-plot.md | 18.1KB | todo |
| 16 | XVI Among the Market Porters | 16-among-the-market-porters.md | 14.0KB | todo |
| 17 | XVII At the Saint-Anthony's Pig | 17-at-the-saint-anthony-s-pig.md | 19.7KB | todo |
| 18 | XVIII A Prisoner and a Witness | 18-a-prisoner-and-a-witness.md | 18.4KB | todo |
| 19 | XIX Jérôme Fandor | 19-jerome-fandor.md | 11.4KB | todo |
| 20 | XX A Cup of Tea | 20-a-cup-of-tea.md | 11.5KB | todo |
| 21 | XXI Lord Beltham's Murderer | 21-lord-beltham-s-murderer.md | 16.5KB | todo |
| 22 | XXII The Scrap of Paper | 22-the-scrap-of-paper.md | 8.6KB | todo |
| 23 | XXIII The Wreck of the Lancaster | 23-the-wreck-of-the-lancaster.md | 10.1KB | todo |
| 24 | XXIV Under Lock and Key | 24-under-lock-and-key.md | 12.7KB | todo |
| 25 | XXV An Unexpected Accomplice | 25-an-unexpected-accomplice.md | 9.8KB | todo |
| 26 | XXVI A Mysterious Crime | 26-a-mysterious-crime.md | 17.4KB | todo |
| 27 | XXVII Three Surprising Incidents | 27-three-surprising-incidents.md | 18.8KB | todo |
| 28 | XXVIII The Court of Assize | 28-the-court-of-assize.md | 15.1KB | todo |
| 29 | XXIX Verdict and Sentence | 29-verdict-and-sentence.md | 20.1KB | todo |
| 30 | XXX An Assignation | 30-an-assignation.md | 20.1KB | todo |
| 31 | XXXI Fell Treachery | 31-fell-treachery.md | 23.3KB | todo |
| 32 | XXXII On the Scaffold | 32-on-the-scaffold.md | 18.9KB | todo |

合计 32 章，约 562.8KB。

---

## 运行日志

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
