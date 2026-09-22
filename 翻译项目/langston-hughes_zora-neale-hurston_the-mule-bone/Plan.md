# 翻译计划（langston-hughes_zora-neale-hurston_the-mule-bone）

## 本计划信息

- **项目名称**：langston-hughes_zora-neale-hurston_the-mule-bone（Zora Neale Hurston）
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/小说文学.md
- **术语表**：术语表.md

## 文件分工

| 文件 | 作用 | 谁来改 |
|------|------|--------|
| `项目说明.md` | 项目基本信息、领域配置 | 人工 |
| `术语表.md` | 翻译硬约束层，每篇译完补充新词 | agent / 人工 |
| `translation_queue.csv` | 任务队列（file,size_kb,status） | 翻译前改 doing，完成后改 done（双写根表） |
| `Plan.md`（本文件） | 执行步骤 + 运行日志 | agent 追加日志 |
| `原文/*.md` | 源文 | 不改 |
| `译文/*.zh-CN.md` | 译文产出（块对照双语） | 翻译 agent 产出 |

执行步骤按 `prompts/翻译计划模板.md`（9 步：读配置→取 todo→doing→读源文→翻译→自检→check_bilingual→双写 done→日志）。

## 篇目清单

共 5 篇，见 `translation_queue.csv`（合计 123KB）。

## 运行日志

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-08-24 | act-1.md | 完成 | 82KB→译文141KB，36 对块，check_bilingual 退出码 0。首译定基调：对白「**人物名**：台词」、舞台指示斜体*（……）*（循 hamilton 体例）；南方黑人民俗方言以活泼乡土口语白话传达（不造怪异拼写）；Lawd→主啊、I God→我的上帝（克拉克口头禅）、nigger→黑鬼（中性直译）；术语表已回填定名 |
| 2026-08-24 | act-2.md | 完成 | 17KB，8 对块，check_bilingual 退出码 0。新增人物定名：露西·泰勒姊妹、托马斯姊妹、琼斯姊妹（艾达）、霍伊特、布伦特太太、奇尔德斯牧师、刘易斯姊妹、玛丽·埃拉、威利；告示日期数字按阿拉伯数字加空格书写以过校验锚点 |
| 2026-08-24 | act-3.md | 完成 | 24KB，5 对块，check_bilingual 退出码 0。铁路道口一场：吹牛对歌两段顺口溜按中文韵语再造；书名曲名《你尽管走，去哈里木法克斯……》意译保留 |
| 2026-08-24 | dramatis-personae.md | 完成 | 1.7KB，1 对块（19 条人物），check_bilingual 退出码 0。人物表逐条附原文（英文）标注 |
| 2026-08-24 | endnotes.md | 完成 | 43B，1 对块，check_bilingual 退出码 0。尾注 Loins 为第一幕「缰套1」脚注之校勘注，译作「腰身（loins）」，保留 ↩︎ 符号 |

全部 5 篇完成（5/5，无 doing 残留）。
