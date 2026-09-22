# 翻译计划（南极：沙克尔顿最后远征记）

## 本计划信息

- **项目名称**：南极：沙克尔顿最后远征记（South，欧内斯特·沙克尔顿）
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/学术著作.md
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

## 篇目清单

> 原文已按罗马数字章序加数字前缀（01—24）。共 24 篇，详见 `translation_queue.csv`。

| # | 篇名（章序） | 源文 | 状态 |
|---|------|------|------|
| 1 | 献词 | 01-dedication.md | todo |
| 2 | 前言 | 02-preface.md | todo |
| 3 | 插图目录 | 03-list-of-illustrations.md | todo |
| 4 | 第一章 驶入威德尔海 | 04-into-the-weddell-sea.md | todo |
| 5 | 第二章 新陆地 | 05-new-land.md | todo |
| 6 | 第三章 冬季数月 | 06-winter-months.md | todo |
| 7 | 第四章 坚忍号之殇 | 07-loss-of-the-endurance.md | todo |
| 8 | 第五章 海上营地 | 08-ocean-camp.md | todo |
| 9 | 第六章 其间行军 | 09-the-march-between.md | todo |
| 10 | 第七章 忍耐营地 | 10-patience-camp.md | todo |
| 11 | 第八章 逃出坚冰 | 11-escape-from-the-ice.md | todo |
| 12 | 第九章 驶艇之旅 | 12-the-boat-journey.md | todo |
| 13 | 第十章 横穿南乔治亚 | 13-across-south-georgia.md | todo |
| 14 | 第十一章 营救 | 14-the-rescue.md | todo |
| 15 | 第十二章 象岛 | 15-elephant-island.md | todo |
| 16 | 第十三章 罗斯海支队 | 16-the-ross-sea-party.md | todo |
| 17 | 第十四章 麦克默多海峡越冬 | 17-wintering-in-mcmurdo-sound.md | todo |
| 18 | 第十五章 布设补给点 | 18-laying-the-depots.md | todo |
| 19 | 第十六章 极光号漂流 | 19-the-aurora-s-drift.md | todo |
| 20 | 第十七章 最后的救援 | 20-the-last-relief.md | todo |
| 21 | 第十八章 最后阶段 | 21-the-final-phase.md | todo |
| 22 | 附录一 | 22-appendix-i.md | todo |
| 23 | 附录 麦克默多海峡的远征小屋 | 23-the-expedition-huts-at-mcmurdo-sound.md | todo |
| 24 | 尾注 | 24-endnotes.md | todo |

## 执行步骤

按 `prompts/翻译计划模板.md`「执行步骤」9 步推进（读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志）。

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-08-14 | - | 建项目 | 从 待翻译/ernest-shackleton_south.epub 提取正文 24 篇（约 850KB），按罗马数字章序重命名加数字前缀，建术语表（船/地/人/动物/探险术语），生成队列。领域=学术著作，形态=长篇，模式=委派 |
