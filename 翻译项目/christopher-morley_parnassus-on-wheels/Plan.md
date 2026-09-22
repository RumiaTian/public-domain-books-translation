# 翻译计划：流动的帕纳索斯

## 本计划信息

- **项目名称**：christopher-morley_parnassus-on-wheels
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/小说文学.md
- **术语表**：术语表.md
- **执行模式**：委派（长篇；见 WORKFLOW.md「单篇翻译流程」）

## 执行步骤

单篇 9 步（读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志）以 `prompts/翻译计划模板.md`「执行步骤」为准，本文件不重复。委派模式下由主 agent 派单，子代理简报含黄金样本与前篇末尾。

## 篇目清单

由 `translation_queue.csv` 管理（17 篇，约 190KB）。

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-08-27 | 全书 17 章 | 完成 17/17 | 昨撞[1308]限额中断后由并行批次补完；抽验 letter-to-david-grayson/vi/xv 全过 |
| 2026-08-26 | dedication / a-letter / i | done | 委派子代理，3 件 check 全过；回填安德鲁·麦吉尔等 16 条定名 |
| 2026-08-26 | ii / iii / iv | done | 委派子代理，check 全过；iv 由主代理验收回填（代理停滞后恢复） |
| 2026-08-26 | v / vi / vii | done | 委派子代理（停滞重派 1 次成功），check 全过 |
| 2026-08-26 | viii / ix / x | done | 委派子代理（停滞重派 1 次成功），check 全过；x 漏译段已补 |
| 2026-08-26 | xi / xii / xiii / xiv / xv | done | 委派子代理，check 全过 |
| 2026-08-26 | 全书 17/17 done | 完结 | 主代理全书术语归一（波特维戈/幸福与乡巴佬），抽验全过、CSV 无 doing；refresh_progress 已刷新 |
