# 翻译计划（mary-weston-fordham_magnolia-leaves）

## 本计划信息

- **项目名称**：mary-weston-fordham_magnolia-leaves（Magnolia Leaves）
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

共 5 篇，见 `translation_queue.csv`（合计 102KB）。

## 运行日志

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-08-24 | dedication.md | 成功 | 1 块对照，check_bilingual 退出码 0；首译定基调：人名首现附原文，「Leaves」译「叶」呼应书名《木兰叶》 |
| 2026-08-24 | foreword.md | 成功 | 2 块对照（正文+署名），退出码 0；布克·T·华盛顿序；日期用「1897 年 12 月 6 日」数字空格式以过锚点校验 |
| 2026-08-24 | in-memoriam.md | 成功 | 15 块对照（14 首悼亡诗，末篇含讣告散文块+诗块），退出码 0；人名首现附原文；讣告年份数字保留（1884/92/1792/1812）；源文制表符噪声行对称清理，诗行逐行对照、诗节空行同位；前次代理产出的 dedication/foreword 双后缀文件已重命名为 .zh-CN.md 并复验通过 |
| 2026-08-24 | magnolia-leaves.md | 成功 | 52 块对照（全书 52 首诗，每首一块；Chicago Ode/Dying Girl/Uranne 块内保留 --- 分节），退出码 0；86KB 长文按引擎第七节分 9 段翻译再合并；Uranne 叙事诗逐行对照；人名意象全书统一（Hurra→万岁、Forget-Me-Not→勿忘我、Pale Face→白面孔） |
| 2026-08-24 | preface.md | 成功 | 2 块对照（正文+署名），退出码 0；循 foreword 体例。全书 5 篇全部完成 |
