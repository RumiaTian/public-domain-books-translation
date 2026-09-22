# Plan.md — edgar-rice-burroughs_thuvia-maid-of-mars

## 本计划信息

- **项目名称**：edgar-rice-burroughs_thuvia-maid-of-mars（《火星少女图维亚》）
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
| `原文/*.md` | 源文（14 章 + Endnotes） | 不改 |
| `译文/*.zh-CN.md` | 译文产出（块对照双语） | 翻译 agent 产出 |

---

## 篇目清单

| # | 章名 | 源文 | 大小 | 状态 |
|---|------|------|------|------|
| 1 | I Carthoris and Thuvia | carthoris-and-thuvia.md | 20.0KB | todo |
| 2 | II Slavery | slavery.md | 17.7KB | todo |
| 3 | III Treachery | treachery.md | 9.9KB | todo |
| 4 | IV A Green Man's Captive | a-green-man-s-captive.md | 18.3KB | todo |
| 5 | V The Fair Race | the-fair-race.md | 24.0KB | todo |
| 6 | VI The Jeddak of Lothar | the-jeddak-of-lothar.md | 14.0KB | todo |
| 7 | VII The Phantom Bowmen | the-phantom-bowmen.md | 17.6KB | todo |
| 8 | VIII The Hall of Doom | the-hall-of-doom.md | 18.1KB | todo |
| 9 | IX The Battle in the Plain | the-battle-in-the-plain.md | 16.1KB | todo |
| 10 | X Kar Komak the Bowman | kar-komak-the-bowman.md | 17.7KB | todo |
| 11 | XI Green Men and White Apes | green-men-and-white-apes.md | 21.3KB | todo |
| 12 | XII To Save Dusar | to-save-dusar.md | 15.5KB | todo |
| 13 | XIII Turjun the Panthan | turjun-the-panthan.md | 19.9KB | todo |
| 14 | XIV Kulan Tith's Sacrifice | kulan-tith-s-sacrifice.md | 22.0KB | todo |
| 15 | Endnotes（度量衡表） | endnotes.md | 0.7KB | todo |

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-08-30 | 全书 15 篇（14 章 + Endnotes） | done 15/15 | 批次2上锁（08-29 23:07）后 3 并行子代理 5/5/5 一次跑通，无 [1301]/[1308]；3 章 >20KB（fair-race/kulan-tith/green-men）按完整块流式落盘无半块残留。各段收尾对齐后主 agent 全量复验 check 15/15 exit 0，CSV 15 done 无残留；机械回改 1 处（金色悬崖→金崖）；修正术语表初版 Tario/Jav 派系标注颠倒（经原文 the-phantom-bowmen ch52 铁证核对），译文本就按原文无返工 |
