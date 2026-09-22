# 翻译计划（星裔）

## 本计划信息

- **项目名称**：andre-norton_star-born
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
00-epigraph.md,0.2,todo
01-shooting-star.md,18.6,todo
02-planetfall.md,19.1,todo
...
```

| 字段 | 含义 | 取值 |
|------|------|------|
| `file` | 源文文件名（在 `原文/` 目录下） | 如 `01-shooting-star.md` |
| `size_kb` | 源文大小（KB）。>50KB 为长文，按通用翻译引擎第七节分段 | 数字 |
| `status` | 翻译状态 | `todo` 待译 / `doing` 翻译中 / `done` 已完成 |

## 执行步骤

按 `prompts/翻译计划模板.md`「执行步骤」9 步推进（读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志）。

## 篇目清单

| # | 章题（罗马数字照搬） | 源文 | 状态 |
|---|------|------|------|
| 0 | 题词（Tas Kordov） | 00-epigraph.md | todo |
| 1 | I Shooting Star | 01-shooting-star.md | todo |
| 2 | II Planetfall | 02-planetfall.md | todo |
| 3 | III Snake-Devil’s Trail | 03-snake-devil-s-trail.md | todo |
| 4 | IV Civilization | 04-civilization.md | todo |
| 5 | V Banded Devil | 05-banded-devil.md | todo |
| 6 | VI Treasure Hunt | 06-treasure-hunt.md | todo |
| 7 | VII Many Eyes, Many Ears | 07-many-eyes-many-ears.md | todo |
| 8 | VIII Airlift | 08-airlift.md | todo |
| 9 | IX Sea Gate | 09-sea-gate.md | todo |
| 10 | X The Dead Guardians | 10-the-dead-guardians.md | todo |
| 11 | XI Espionage | 11-espionage.md | todo |
| 12 | XII Alien Patrol | 12-alien-patrol.md | todo |
| 13 | XIII A Hound Is Loosed | 13-a-hound-is-loosed.md | todo |
| 14 | XIV The Prisoner | 14-the-prisoner.md | todo |
| 15 | XV Arena | 15-arena.md | todo |
| 16 | XVI Surprise Attack | 16-surprise-attack.md | todo |
| 17 | XVII Destruction Unleashed | 17-destruction-unleashed.md | todo |
| 18 | XVIII Not Yet— | 18-not-yet.md | todo |

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-09-09 | 全书 19 篇（00-题词 + 01–18 章） | 完结 +19 | 批次2；A 段（00-09）+ B 段（10-18）双子代理并发，19 文件 check_bilingual 全部一次通过；跨段术语分歧统一（stun gun→眩晕枪、the Burn-Off→大焚掠、duck-dog 合行）；术语表增补 40 余条 |
