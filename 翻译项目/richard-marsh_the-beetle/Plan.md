# Plan.md

## 本计划信息

- **项目名称**：richard-marsh_the-beetle（甲虫）
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md
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

按 `prompts/翻译计划模板.md`「执行步骤」9 步推进。委派模式由子代理逐篇执行。

---

## 篇目清单（按四卷叙事顺序）

> 本书分四卷，每卷换一叙述者。文件名已加两位数字前缀（00–51），CSV 按此前缀排序生成，翻译严格按此序推进。

| 章号 | 篇名 | 叙述者 | 源文文件 |
|------|------|--------|----------|
| 卷一首 | Book I The House with the Open Window | — | 00-the-house-with-the-open-window.md |
| I | Outside | 霍尔特 | 01-outside.md |
| II | Inside | 霍尔特 | 02-inside.md |
| III | The Man in the Bed | 霍尔特 | 03-the-man-in-the-bed.md |
| IV | A Lonely Vigil | 霍尔特 | 04-a-lonely-vigil.md |
| V | An Instruction to Commit Burglary | 霍尔特 | 05-an-instruction-to-commit-burglary.md |
| VI | A Singular Felony | 霍尔特 | 06-a-singular-felony.md |
| VII | The Great Paul Lessingham | 霍尔特 | 07-the-great-paul-lessingham.md |
| VIII | The Man in the Street | 霍尔特 | 08-the-man-in-the-street.md |
| IX | The Contents of the Packet | 霍尔特 | 09-the-contents-of-the-packet.md |
| 卷二首 | Book II The Haunted Man | — | 10-the-haunted-man.md |
| X | Rejected | 阿瑟顿 | 11-rejected.md |
| XI | A Midnight Episode | 阿瑟顿 | 12-a-midnight-episode.md |
| XII | A Morning Visitor | 阿瑟顿 | 13-a-morning-visitor.md |
| XIII | The Picture | 阿瑟顿 | 14-the-picture.md |
| XIV | The Duchess’ Ball | 阿瑟顿 | 15-the-duchess-ball.md |
| XV | Mr. Lessingham Speaks | 阿瑟顿 | 16-mr-lessingham-speaks.md |
| XVI | Atherton’s Magic Vapour | 阿瑟顿 | 17-atherton-s-magic-vapour.md |
| XVII | Magic?—Or Miracle? | 阿瑟顿 | 18-magic-or-miracle.md |
| XVIII | The Apotheosis of the Beetle | 阿瑟顿 | 19-the-apotheosis-of-the-beetle.md |
| XIX | The Lady Rages | 阿瑟顿 | 20-the-lady-rages.md |
| XX | A Heavy Father | 阿瑟顿 | 21-a-heavy-father.md |
| XXI | The Terror in the Night | 阿瑟顿 | 22-the-terror-in-the-night.md |
| XXII | The Haunted Man | 阿瑟顿 | 23-the-haunted-man.md |
| 卷三首 | Book III The Terror by Night and the Terror by Day | — | 24-the-terror-by-night-and-the-terror-by-day.md |
| XXIII | The Way He Told Her | 马乔里 | 25-the-way-he-told-her.md |
| XXIV | A Woman’s View | 马乔里 | 26-a-woman-s-view.md |
| XXV | The Man in the Street | 马乔里 | 27-the-man-in-the-street.md |
| XXVI | A Father’s No | 马乔里 | 28-a-father-s-no.md |
| XXVII | The Terror by Night | 马乔里 | 29-the-terror-by-night.md |
| XXVIII | The Strange Story of the Man in the Street | 马乔里 | 30-the-strange-story-of-the-man-in-the-street.md |
| XXIX | The House on the Road from the Workhouse | 马乔里 | 31-the-house-on-the-road-from-the-workhouse.md |
| XXX | The Singular Behaviour of Mr. Holt | 马乔里 | 32-the-singular-behaviour-of-mr-holt.md |
| XXXI | The Terror by Day | 马乔里 | 33-the-terror-by-day.md |
| 卷四首 | Book IV In Pursuit | — | 34-in-pursuit.md |
| XXXII | A New Client | 钱普内尔 | 35-a-new-client.md |
| XXXIII | What Came of Looking Through a Lattice | 钱普内尔 | 36-what-came-of-looking-through-a-lattice.md |
| XXXIV | After Twenty Years | 钱普内尔 | 37-after-twenty-years.md |
| XXXV | A Bringer of Tidings | 钱普内尔 | 38-a-bringer-of-tidings.md |
| XXXVI | What the Tidings Were | 钱普内尔 | 39-what-the-tidings-were.md |
| XXXVII | What Was Hidden Under the Floor | 钱普内尔 | 40-what-was-hidden-under-the-floor.md |
| XXXVIII | The Rest of the Find | 钱普内尔 | 41-the-rest-of-the-find.md |
| XXXIX | Miss Louisa Coleman | 钱普内尔 | 42-miss-louisa-coleman.md |
| XL | What Miss Coleman Saw Through the Window | 钱普内尔 | 43-what-miss-coleman-saw-through-the-window.md |
| XLI | The Constable—His Clue—and the Cab | 钱普内尔 | 44-the-constable-his-clue-and-the-cab.md |
| XLII | The Quarry Doubles | 钱普内尔 | 45-the-quarry-doubles.md |
| XLIII | The Murder at Mrs. ’Enderson’s | 钱普内尔 | 46-the-murder-at-mrs-enderson-s.md |
| XLIV | The Man Who Was Murdered | 钱普内尔 | 47-the-man-who-was-murdered.md |
| XLV | All That Mrs. ’Enderson Knew | 钱普内尔 | 48-all-that-mrs-enderson-knew.md |
| XLVI | The Sudden Stopping | 钱普内尔 | 49-the-sudden-stopping.md |
| XLVII | The Contents of the Third-Class Carriage | 钱普内尔 | 50-the-contents-of-the-third-class-carriage.md |
| XLVIII | The Conclusion of the Matter | 钱普内尔 | 51-the-conclusion-of-the-matter.md |

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
