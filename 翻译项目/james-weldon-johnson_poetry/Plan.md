# 翻译计划：詹姆斯·韦尔登·约翰逊诗集

## 本计划信息

- **项目名称**：james-weldon-johnson_poetry
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/小说文学.md
- **术语表**：术语表.md
- **执行模式**：委派（短篇集；见 WORKFLOW.md「单篇翻译流程」）

## 执行步骤

单篇 9 步（读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志）以 `prompts/翻译计划模板.md`「执行步骤」为准，本文件不重复。委派模式下由主 agent 派单，子代理简报含黄金样本与前篇末尾。

## 篇目清单

由 `translation_queue.csv` 管理（67 篇，约 103KB）。

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-08-26 | 全部 67 篇（a-banjo-song 至 you-s-sweet-to-yo-mammy-jes-de-same） | 完成 | 批量子代理一次译完；check_bilingual.py 全部通过，队列无剩余 todo |
