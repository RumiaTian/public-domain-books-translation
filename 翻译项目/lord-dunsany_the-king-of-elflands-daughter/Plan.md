# 翻译计划（精灵国王的女儿）

## 本计划信息

- **项目名称**：精灵国王的女儿
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

按 `prompts/翻译计划模板.md`「执行步骤」9 步推进（读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志）。

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-08-10 | - | 建项目 | 从 待翻译/精灵国王的女儿 epub 提取正文、建术语表初版、生成队列 |
| 2026-08-10 | 一 厄尔议会的图谋（the-plan-of-the-parliament-of-erl） | done | 23858 字节，check_bilingual exit=0（10 对块、标题合并满足、无误报）；黄金样本，作为全书风格基准；术语补充见下 |
| 2026-08-10 | 四 阿尔韦里克多年后重归人世（alveric-comes-back-to-earth-after-many-years） | done | 14887 字节，check_bilingual exit=0（5 对块、标题合并满足、无误报）；术语补充：the Freer=教士、Christom rites=基督圣礼、the Vale of Erl=厄尔之谷、the guarding wood=护卫之林、the frontier/barrier of twilight=暮色的边境/屏障、mermaid=美人鱼 |
| 2026-08-11 | 七 巨怪之来（the-coming-of-the-troll） | done | 10.2KB，check_bilingual exit=0（18 对块、标题合并满足、无误报）；术语补充：buttercups=毛茛、hare=野兔、Noman's Dog=无人之犬、Thing-over-the-Border=边境那边的东西、troll-talk=巨怪语、changeling=调包儿、tarns=幽潭、parchment=羊皮纸 |
| 2026-08-11 | 十四 探寻精灵山脉（the-quest-for-the-elfin-mountains） | done | 19.8KB，check_bilingual exit=0（10 对块、标题合并满足、无误报）；术语补充见下 |
| 2026-08-11 | 二十九 诱引沼泽之民（the-luring-of-the-people-of-the-marshes） | done | 20.0KB，check_bilingual exit=0（19 对块、标题合并满足、无误报）；术语补充：the people of the marshes=沼泽之民、green plover=绿鸻、teal=水凫、rooks=秃鼻鸦、jackdaws(既有)=寒鸦 |
| 2026-08-11 | 本会话续译7篇（lirazel-remembers/lurulu-watches/arrival-of-the-rune/horn-of-alveric/last-great-rune/magical-sword/twelve-old-men） | done | 委派7篇全 exit0。术语补充：trollberries=巨怪莓、water-wagtail=鹡鸰、holm-oaks=圣栎、Ziroonderel=齐龙德尔泽尔（术语表两处冲突，按黄金样本多数派取齐龙德尔泽尔）、Niv=尼夫/Zend=曾德/Thyl=锡尔/Vand=范德/Narl=纳尔/Oth=奥斯/Threl=斯瑞尔、雷石之铁=thunderbolt-iron、月晕=moon-halo。本项目 36/36 全部译完 |
