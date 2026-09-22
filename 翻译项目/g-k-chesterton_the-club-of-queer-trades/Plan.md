# 翻译计划：奇行俱乐部

## 本计划信息

- **项目名称**：g-k-chesterton_the-club-of-queer-trades
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/小说文学.md
- **术语表**：术语表.md
- **执行模式**：委派（短篇集；见 WORKFLOW.md「单篇翻译流程」）

## 执行步骤

单篇 9 步（读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志）以 `prompts/翻译计划模板.md`「执行步骤」为准，本文件不重复。委派模式下由主 agent 派单，子代理简报含黄金样本与前篇末尾。

## 篇目清单

由 `translation_queue.csv` 管理（6 篇，约 246KB）。

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
| 2026-08-21 | the-tremendous-adventures-of-major-brown / the-painful-fall-of-a-great-reputation | done | 首批两篇译成（48.1+33.1KB，39/21 对块，均 exit 0、0 可疑）；奇行俱乐部定名，术语表追加 45 条 |
| 2026-08-21 | the-eccentric-seclusion-of-the-old-lady / the-noticeable-conduct-of-professor-chadd / the-singular-speculation-of-the-house-agent / the-awful-reason-of-the-vicar-s-visit | done | 两子代理并行译成（49.6+36.7+43.2+37.1KB，69/50/40/38 对块，均 exit 0、0 可疑，段落级机核全对齐；并发术语表冲突已互相对齐）。全书 6/6（100%）收官 |
