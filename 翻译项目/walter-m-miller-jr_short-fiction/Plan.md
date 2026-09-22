# 翻译计划：小沃尔特·米勒短篇集

## 本计划信息

- **项目名称**：walter-m-miller-jr_short-fiction
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/小说文学.md
- **术语表**：术语表.md
- **执行模式**：委派（短篇集；见 WORKFLOW.md「单篇翻译流程」）

## 执行步骤

单篇 9 步（读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志）以 `prompts/翻译计划模板.md`「执行步骤」为准，本文件不重复。委派模式下由主 agent 派单，子代理简报含黄金样本与前篇末尾。

## 篇目清单

由 `translation_queue.csv` 管理（7 篇，约 311KB）。

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-09-05 | conditionally-human / way-of-a-rebel / the-ties-that-bind / it-takes-a-thief / check-and-checkmate / death-of-a-spaceman / the-hoofer（全书 7 篇） | done | 批次1委派 3 并发子代理纯翻译直出（各篇独立流式分批落盘）；3 篇退出码 0，4 篇仅数字锚点误报（CJK 边界正则失配，数字实存） |
| 2026-09-05 | 整书 7/7 完结 | ✅ | 删锁流转，转入审核阶段 |
