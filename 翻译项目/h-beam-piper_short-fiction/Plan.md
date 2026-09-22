# 翻译计划（H. Beam Piper 短篇小说集）

## 本计划信息

- **项目名称**：h-beam-piper_short-fiction
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

## translation_queue.csv 格式

```
file,size_kb,status
time-and-time-again.md,38.9,todo
he-walked-around-the-horses.md,43.9,todo
...
```

| 字段 | 含义 | 取值 |
|------|------|------|
| `file` | 源文文件名（在 `原文/` 目录下） | 如 `time-and-time-again.md` |
| `size_kb` | 源文大小（KB）。>50KB 为长文，按通用翻译引擎第七节分段 | 数字 |
| `status` | 翻译状态 | `todo` 待译 / `doing` 翻译中 / `done` 已完成 |

## 执行步骤

按 `prompts/翻译计划模板.md`「执行步骤」9 步推进（读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志）。本项目为短篇集，委派模式：主 agent 只当调度员，逐篇派子代理执行；平行时间系列（police-operation → last-enemy → temple-trouble → time-crime）按 spine 顺序相邻，译时注意系列术语一致。

## 篇目清单

| # | 篇名（暂定译名） | 源文 | 大小 | 状态 |
|---|------|------|------|------|
| 1 | Time and Time Again（一次又一次） | time-and-time-again.md | 38.9KB | todo |
| 2 | He Walked Around the Horses（他绕过了马匹） | he-walked-around-the-horses.md | 43.9KB | todo |
| 3 | Police Operation（警察行动）△平行时间 | police-operation.md | 71.5KB | todo |
| 4 | The Mercenaries（雇佣兵） | the-mercenaries.md | 50.6KB | todo |
| 5 | Last Enemy（最后的敌人）△平行时间 | last-enemy.md | 140.7KB | todo |
| 6 | Flight from Tomorrow（逃离明天） | flight-from-tomorrow.md | 45.4KB | todo |
| 7 | Rebel Raider（叛军掠袭者） | rebel-raider.md | 84.0KB | todo |
| 8 | Operation R.S.V.P.（敬候回函行动） | operation-r-s-v-p.md | 14.1KB | todo |
| 9 | Dearest（最亲爱的） | dearest.md | 37.2KB | todo |
| 10 | Temple Trouble（神庙风波）△平行时间 | temple-trouble.md | 70.1KB | todo |
| 11 | Day of the Moron（低能者之日） | day-of-the-moron.md | 65.3KB | todo |
| 12 | Genesis（创世记） | genesis.md | 47.0KB | todo |
| 13 | Null-A.B.C.（非A.B.C.，与麦圭尔合写） | null-a-b-c.md | 204.5KB | todo |
| 14 | The Return（回归，与麦圭尔合写） | the-return.md | 62.2KB | todo |
| 15 | Time Crime（时间罪案）△平行时间 | time-crime.md | 213.2KB | todo |
| 16 | Omnilingual（全语言）☆未来史 | omnilingual.md | 93.9KB | todo |
| 17 | Lone Star Planet（孤星行星，与麦圭尔合写） | lone-star-planet.md | 172.6KB | todo |
| 18 | The Edge of the Knife（刀锋）☆未来史 | the-edge-of-the-knife.md | 93.2KB | todo |
| 19 | The Keeper（守冠人）☆未来史 | the-keeper.md | 50.9KB | todo |
| 20 | Graveyard of Dreams（梦想的坟场）☆未来史 | graveyard-of-dreams.md | 45.2KB | todo |
| 21 | Ministry of Disturbance（骚乱部）☆未来史 | ministry-of-disturbance.md | 94.9KB | todo |
| 22 | Hunter Patrol（猎手巡逻队，与麦圭尔合写） | hunter-patrol.md | 65.1KB | todo |
| 23 | Crossroads of Destiny（命运的十字路口） | crossroads-of-destiny.md | 25.2KB | todo |
| 24 | The Answer（答案） | the-answer.md | 25.1KB | todo |
| 25 | Oomphel in the Sky（天上的乌姆菲尔）☆未来史 | oomphel-in-the-sky.md | 99.1KB | todo |
| 26 | Naudsonce（纳多森斯）☆未来史 | naudsonce.md | 95.2KB | todo |
| 27 | A Slave Is a Slave（奴隶就是奴隶）☆未来史 | a-slave-is-a-slave.md | 126.0KB | todo |
| 28 | Endnotes（尾注） | endnotes.md | 0.4KB | todo |

> △ = 平行时间系列（Paratime）；☆ = 人类未来史系列。篇名暂定译名仅供调度参考，最终以各篇译文标题行「英文 / 中文」为准。

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
