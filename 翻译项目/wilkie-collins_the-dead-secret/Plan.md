# Plan.md — wilkie-collins_the-dead-secret

## 本计划信息

- **项目名称**：wilkie-collins_the-dead-secret（死秘密（Wilkie Collins: The Dead Secret, 1857））
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
| `原文/*.md` | 源文（29 文件） | 不改 |
| `译文/*.zh-CN.md` | 译文产出（块对照双语） | 翻译 agent 产出 |

执行步骤按 `prompts/翻译计划模板.md`「执行步骤」9 步推进；执行模式为委派（长篇），由子代理逐章执行。

---

## 篇目清单

| # | 篇名 | 源文 | 大小 | 状态 |
|---|------|------|------|------|
| 1 | I.1 The Twenty-Third of August, 1829 | 01-the-twenty-third-of-august-1829.md | 31.2KB | todo |
| 2 | I.2 The Child | 02-the-child.md | 10.5KB | todo |
| 3 | I.3 The Hiding of the Secret | 03-the-hiding-of-the-secret.md | 19.5KB | todo |
| 4 | II.1 Fifteen Years After | 04-fifteen-years-after.md | 30.6KB | todo |
| 5 | II.2 The Sale of Porthgenna Tower | 05-the-sale-of-porthgenna-tower.md | 27.0KB | todo |
| 6 | II.3 The Bride and Bridegroom | 06-the-bride-and-bridegroom.md | 34.6KB | todo |
| 7 | III.1 Timon of London | 07-timon-of-london.md | 29.6KB | todo |
| 8 | III.2 Will They Come? | 08-will-they-come.md | 10.2KB | todo |
| 9 | III.3 Mrs. Jazeph | 09-mrs-jazeph.md | 23.7KB | todo |
| 10 | III.4 The New Nurse | 10-the-new-nurse.md | 48.1KB | todo |
| 11 | III.5 A Council of Three | 11-a-council-of-three.md | 16.1KB | todo |
| 12 | III.6 Another Surprise | 12-another-surprise.md | 14.6KB | todo |
| 13 | IV.1 A Plot Against the Secret | 13-a-plot-against-the-secret.md | 34.4KB | todo |
| 14 | IV.2 Outside the House | 14-outside-the-house.md | 34.2KB | todo |
| 15 | IV.3 Inside the House | 15-inside-the-house.md | 37.7KB | todo |
| 16 | IV.4 Mr. Munder on the Seat of Judgment | 16-mr-munder-on-the-seat-of-judgment.md | 33.5KB | todo |
| 17 | IV.5 Mozart Plays Farewell | 17-mozart-plays-farewell.md | 31.1KB | todo |
| 18 | V.1 An Old Friend and a New Scheme | 18-an-old-friend-and-a-new-scheme.md | 16.5KB | todo |
| 19 | V.2 The Beginning of the End | 19-the-beginning-of-the-end.md | 18.9KB | todo |
| 20 | V.3 Approaching the Precipice | 20-approaching-the-precipice.md | 25.0KB | todo |
| 21 | V.4 Standing on the Brink | 21-standing-on-the-brink.md | 19.7KB | todo |
| 22 | V.5 The Myrtle Room | 22-the-myrtle-room.md | 33.7KB | todo |
| 23 | V.6 The Telling of the Secret | 23-the-telling-of-the-secret.md | 21.4KB | todo |
| 24 | VI.1 Uncle Joseph | 24-uncle-joseph.md | 32.8KB | todo |
| 25 | VI.2 Waiting and Hoping | 25-waiting-and-hoping.md | 35.1KB | todo |
| 26 | VI.3 The Story of the Past | 26-the-story-of-the-past.md | 35.4KB | todo |
| 27 | VI.4 The Close of Day | 27-the-close-of-day.md | 37.2KB | todo |
| 28 | VI.5 Forty Thousand Pounds | 28-forty-thousand-pounds.md | 19.5KB | todo |
| 29 | VI.6 The Dawn of a New Life | 29-the-dawn-of-a-new-life.md | 4.7KB | todo |

> 六个 Book（部）题名已并入该部首章（`# Book N` 行），派单时随首章翻译。

---

## 运行日志

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
