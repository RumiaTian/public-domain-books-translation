# 翻译计划：奥尔尼圣诗集

## 本计划信息

- **项目名称**：john-newton_william-cowper_olney-hymns
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/小说文学.md
- **术语表**：术语表.md
- **执行模式**：委派（短篇集；见 WORKFLOW.md「单篇翻译流程」）

## 执行步骤

单篇 9 步（读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志）以 `prompts/翻译计划模板.md`「执行步骤」为准，本文件不重复。委派模式下由主 agent 派单，子代理简报含黄金样本与前篇末尾。

## 篇目清单

由 `translation_queue.csv` 管理（5 篇，约 378KB）。

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-08-21 | endnotes.md | 完成 | 尾注33条；Book/Hymn译作卷/圣诗，Olney=奥尔尼 |
| 2026-08-21 | on-occasional-subjects.md | 完成 | 第二卷100首，check_bilingual通过（100对，0错配） |
| 2026-08-21 | on-select-texts-of-scripture.md | 完成 | 第一卷141首，check_bilingual通过（141对，0错配） |
| 2026-08-21 | on-the-rise-progress-changes-and-comforts-of-the-spiritual-life | doing | 两次派发均触 [1301]（简报侧输入拦截，代理未启动）；status 保持 doing 留待后续时段再试 |
| 2026-08-22 | on-the-rise-progress-changes-and-comforts-of-the-spiritual-life | 完成 | 第三卷107首，check_bilingual通过（107对，0错配）；牛顿71首/库珀36首；分3段（1-25/26-58/59-107）机械拼接保真原文块（含ufeff与尾注锚点27-33） |
| 2026-08-22 | preface.md | 完成 | 序言散文7块对，check_bilingual唯一提示为尾注日期锚点误报（February 15, 1779→1779年2月15日，数字齐全）；全项目5篇收官 |
