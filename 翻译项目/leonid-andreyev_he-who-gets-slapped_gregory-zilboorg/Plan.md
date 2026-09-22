# 翻译计划：挨打的人

## 本计划信息

- **项目名称**：leonid-andreyev_he-who-gets-slapped_gregory-zilboorg
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/小说文学.md
- **术语表**：术语表.md
- **执行模式**：连续（中篇；见 WORKFLOW.md「单篇翻译流程」）

## 执行步骤

单篇 9 步（读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志）以 `prompts/翻译计划模板.md`「执行步骤」为准，本文件不重复。连续模式下由主 agent 直接执行。

## 篇目清单

由 `translation_queue.csv` 管理（5 篇，约 142KB）。

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-08-26 | introduction / act-i 至 act-iv（全剧） | ✅ 5/5 done | 单子代理连续直出（前批 introduction+act-i，重启后续 act-ii/iii/iv）；五文件 check_bilingual 全 exit 0（16+42+44+30+31 对块）；人物口吻跨幕一致；约 20 条新术语已回填术语表 |
