# 翻译计划：温哥华传说

## 本计划信息

- **项目名称**：e-pauline-johnson_legends-of-vancouver
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/小说文学.md
- **术语表**：术语表.md
- **执行模式**：委派（长篇；见 WORKFLOW.md「单篇翻译流程」）

## 执行步骤

单篇 9 步（读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志）以 `prompts/翻译计划模板.md`「执行步骤」为准，本文件不重复。委派模式下由主 agent 派单，子代理简报含黄金样本与前篇末尾。

## 篇目清单

由 `translation_queue.csv` 管理（19 篇，约 160KB）。

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-08-27 | 全书 19 章 | 完成 19/19 | 昨撞[1308]限额中断后由并行批次补完；抽验 royal-mohawk-chief/deep-waters/tulameen-trail 全过 |
| 2026-08-26 | the-lure-in-stanley-park / the-siwash-rock / the-tulameen-trail | done | 委派子代理，3 章 check 全过（退出码 0） |
| 2026-08-26 | the-recluse / the-sea-serpent | done | 委派子代理，2 章 check 全过 |
| 2026-08-26 | 全书 19/19 done | 完结 | 术语表回填 15 条定名；主代理抽验 5 文件全过、CSV 无 doing；refresh_progress 已刷新 |
