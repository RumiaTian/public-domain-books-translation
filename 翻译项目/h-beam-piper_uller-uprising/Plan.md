# 翻译计划：乌勒尔起义

## 本计划信息

- **项目名称**：h-beam-piper_uller-uprising
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/小说文学.md
- **术语表**：术语表.md
- **执行模式**：委派（长篇；见 WORKFLOW.md「单篇翻译流程」）

## 执行步骤

单篇 9 步（读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志）以 `prompts/翻译计划模板.md`「执行步骤」为准，本文件不重复。委派模式下由主 agent 派单，子代理简报含黄金样本与前篇末尾。

## 篇目清单

由 `translation_queue.csv` 管理（17 篇，约 309KB）。

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-09-04 | 前 9 章（dr-john-d-clark … commander-in-chief-front-and-center 等） | done | 前序会话完成，本次补记 |
| 2026-09-05 | on-satan-s-footstool | done | doing 断点验收回填；结构过检，仅数字锚点误报 |
| 2026-09-05 | of-princedoms… / rakkeed-stalin… / the-bad-news… / the-geek-luftwaffe… / the-reviewers-panned… / the-shadow-of-niflheim / you-can-depend… | done | 批次1派 3 并发子代理纯翻译直出；7 章 check 全过（4 章退出码 0，3 章仅数字锚点误报） |
| 2026-09-05 | 整书 17/17 完结 | ✅ | 删锁流转，转入审核阶段 |
