# 翻译计划（《莉莉丝》——乔治·麦克唐纳）

## 本计划信息

- **项目名称**：《莉莉丝》（George MacDonald, *Lilith: A Romance*, 1895）
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/小说文学.md
- **术语表**：术语表.md

## 文件分工

| 文件 | 作用 | 谁来改 |
|------|------|--------|
| `项目说明.md` | 项目基本信息、领域配置、篇目清单 | 人工 |
| `术语表.md` | 翻译硬约束层。每篇译完补充新词 | agent / 人工 |
| `translation_queue.csv` | 任务队列。每行一文件，`file, size_kb, status` 三列 | 翻译前改 doing，完成后改 done |
| `Plan.md`（本文件） | 执行步骤 + 运行日志 | agent 追加日志 |
| `原文/*.md` | 源文 | 不改 |
| `译文/*.zh-CN.md` | 译文产出（块对照双语） | 翻译 agent 产出 |

## 执行步骤

按 `prompts/翻译计划模板.md`「执行步骤」9 步推进（读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志）。本内容形态为「长篇」，走委派模式，每篇下沉到一次性子代理执行。

> 源文文件已按章序冠两位数序号前缀（00–48），`translation_queue.csv` 与下表均按此阅读顺序排列。

## 篇目清单

共 47 章（罗马数字 I–XLVII），另含卷首题辞（00）、卷尾尾注（48），合计 49 个文件。详见 `translation_queue.csv`。

| # | 章 | 源文 | 大小 | 状态 |
|---|----|------|------|------|
| — | 题辞（梭罗） | 00-epigraph.md | 2.1KB | todo |
| I | The Library | 01-the-library.md | 9.5KB | todo |
| II | The Mirror | 02-the-mirror.md | 4.2KB | todo |
| III | The Raven | 03-the-raven.md | 12.3KB | todo |
| IV | Somewhere or Nowhere? | 04-somewhere-or-nowhere.md | 12.6KB | todo |
| V | The Old Church | 05-the-old-church.md | 4.8KB | todo |
| VI | The Sexton’s Cottage | 06-the-sexton-s-cottage.md | 9.9KB | todo |
| VII | The Cemetery | 07-the-cemetery.md | 11.7KB | todo |
| VIII | My Father’s Manuscript | 08-my-father-s-manuscript.md | 9.7KB | todo |
| IX | I Repent | 09-i-repent.md | 9.7KB | todo |
| X | The Bad Burrow | 10-the-bad-burrow.md | 8.5KB | todo |
| XI | The Evil Wood | 11-the-evil-wood.md | 8.9KB | todo |
| XII | Friends and Foes | 12-friends-and-foes.md | 6.7KB | todo |
| XIII | The Little Ones | 13-the-little-ones.md | 16.3KB | todo |
| XIV | A Crisis | 14-a-crisis.md | 9.1KB | todo |
| XV | A Strange Hostess | 15-a-strange-hostess.md | 18.3KB | todo |
| XVI | A Gruesome Dance | 16-a-gruesome-dance.md | 16.0KB | todo |
| XVII | A Grotesque Tragedy | 17-a-grotesque-tragedy.md | 13.4KB | todo |
| XVIII | Dead or Alive? | 18-dead-or-alive.md | 16.3KB | todo |
| XIX | The White Leech | 19-the-white-leech.md | 10.3KB | todo |
| XX | Gone!—But How? | 20-gone-but-how.md | 7.9KB | todo |
| XXI | The Fugitive Mother | 21-the-fugitive-mother.md | 6.6KB | todo |
| XXII | Bulika | 22-bulika.md | 7.7KB | todo |
| XXIII | A Woman of Bulika | 23-a-woman-of-bulika.md | 4.4KB | todo |
| XXIV | The White Leopardess | 24-the-white-leopardess.md | 6.4KB | todo |
| XXV | The Princess | 25-the-princess.md | 15.0KB | todo |
| XXVI | A Battle Royal | 26-a-battle-royal.md | 8.0KB | todo |
| XXVII | The Silent Fountain | 27-the-silent-fountain.md | 6.6KB | todo |
| XXVIII | I Am Silenced | 28-i-am-silenced.md | 5.9KB | todo |
| XXIX | The Persian Cat | 29-the-persian-cat.md | 13.8KB | todo |
| XXX | Adam Explains | 30-adam-explains.md | 8.8KB | todo |
| XXXI | The Sexton’s Old Horse | 31-the-sexton-s-old-horse.md | 9.4KB | todo |
| XXXII | The Lovers and the Bags | 32-the-lovers-and-the-bags.md | 10.4KB | todo |
| XXXIII | Lona’s Narrative | 33-lona-s-narrative.md | 15.8KB | todo |
| XXXIV | Preparation | 34-preparation.md | 11.3KB | todo |
| XXXV | The Little Ones in Bulika | 35-the-little-ones-in-bulika.md | 9.7KB | todo |
| XXXVI | Mother and Daughter | 36-mother-and-daughter.md | 8.8KB | todo |
| XXXVII | The Shadow | 37-the-shadow.md | 5.5KB | todo |
| XXXVIII | To the House of Bitterness | 38-to-the-house-of-bitterness.md | 15.2KB | todo |
| XXXIX | That Night | 39-that-night.md | 22.2KB | todo |
| XL | The House of Death | 40-the-house-of-death.md | 23.7KB | todo |
| XLI | I Am Sent | 41-i-am-sent.md | 7.4KB | todo |
| XLII | I Sleep the Sleep | 42-i-sleep-the-sleep.md | 11.2KB | todo |
| XLIII | The Dreams That Came | 43-the-dreams-that-came.md | 16.2KB | todo |
| XLIV | The Waking | 44-the-waking.md | 9.7KB | todo |
| XLV | The Journey Home | 45-the-journey-home.md | 8.1KB | todo |
| XLVI | The City | 46-the-city.md | 7.6KB | todo |
| XLVII | The “Endless Ending” | 47-the-endless-ending.md | 2.9KB | todo |
| — | 尾注 | 48-endnotes.md | 0.2KB | todo |

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
