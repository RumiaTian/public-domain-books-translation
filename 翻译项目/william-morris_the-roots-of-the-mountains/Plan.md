# 翻译计划（群山之根）

## 本计划信息

- **项目名称**：群山之根
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
| 2026-08-10 | - | 建项目 | 从 待翻译/群山之根 epub 提取正文、建术语表初版、生成队列 |
| 2026-08-10 | 第一章 Of Burgstead and Its Folk and Its Neighbours | done | 黄金样本；39677 字节；check exit=0；11 块对照、25 段原文逐段对齐 0 错配；修正 Original 块误增词 rosage；术语表首填人物/地名/术语三表 |
| 2026-08-12 | 第四十九章 Dallach Fareth to Rosedale（达拉赫奔赴玫瑰谷） | done | 12.0KB；check exit=0；16 块对照、24 段原文 0 错配；新词：Crow the Shaft-speeder=疾箭者克劳（克劳之别号，建议补入术语表） |
| 2026-08-12 | 第五十九章 面神对新娘之托得偿（全书末章） | done | 10.8KB；check exit=0；11 块对照、38 段原文成对对齐 0 错配；新词：Hart of Highcliff=高崖之鹿（弓娥之夫别号）、the Sheepcotes=牧羊之民（变体）、the Day of the Victory=胜利之日、the Folk-thing=民众大会 |
| 2026-08-12 | 第四十四章 犍牛族、桥族与公牛族人之猛攻 | done | 13.2KB；check exit=0；11 块对照、14 段原文成对对齐 0 错配；新词：Iron-hand=铁手（公牛族勇士）、the Barley-scythe=麦镰（铁手之古剑）、War-well=战井（桥族之长）、Wolf of Whitegarth=白院之狼、Long-hand of Oakholt=橡林之长手、Chip-driver=碎木（高崖之鹿之剑）、Red-wolf=红狼、War-grove=战林、Wood-wicked=林狡、the Bent of the Bowmen=弓手坡；注意源文 song arose 处歌辞缺失（空行），忠实照译未臆造 |
| 2026-08-12 | 第三章 众人于厅中谈论诸事 | done | 12.1KB；check exit=0；15 块对照、29 段原文成对对齐 0 错配；新词：the Foes of the Gods=众神之敌、Kobbolds=地精、Wights（通名）=妖灵、the Day of the Warding of the Ways=大道守卫之日、Midsummer=仲夏、the Feast of the Eve of the Wedding=婚礼前夜宴席、Wolves of the Holy Places=圣地之狼；注意源文 Redesman 唱段歌辞缺失（sang: 后空行），忠实照译未臆造 |
| 2026-08-12 | 第二十六章 门会之终（the ending of the gate-thing） | done | 13.9KB；check exit=0；21 块对照、49 段原文成对对齐 0 错配；术语全遵表（Gate-thing=门会、the Holy Thing=神圣议事会、blood-wite=血金、the Death Tarn=死潭、the Holy Boar=圣猪、Yule=岁末冬至节）；新词：Fork-beard of Lea=草地之叉须（minor 人名，首次附原文）、virgin of war=战阵处女（新娘自誓之词）、Castle of Love=爱情之堡（新娘誓词中比喻）；自检修正一处 neither/neither 误植 → 既不/也不 |
| 2026-08-12 | 第四十一章 大军离幽谷：第一日之程 | done | 10.6KB；check exit=0；14 块对照、16 段原文成对对齐 0 错配；注意源文第5段末"and this is some of what they sang:"后歌辞缺失（空行），忠实照译未臆造；新词：Red-mouthed Wolf=赤口狼、Sun-burst=旭日旗（狼族阵前两面旌旗）、gerfalcon=矛隼、bossed shield=中央圆凸之盾（盾阔山形之喻） |
