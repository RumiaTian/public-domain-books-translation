# 翻译计划：针插之上

## 本计划信息

- **项目名称**：mary-de-morgan_on-a-pincushion
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/小说文学.md
- **术语表**：术语表.md
- **执行模式**：委派（短篇集；见 WORKFLOW.md「单篇翻译流程」）

## 执行步骤

单篇 9 步（读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志）以 `prompts/翻译计划模板.md`「执行步骤」为准，本文件不重复。委派模式下由主 agent 派单，子代理简报含黄金样本与前篇末尾。

## 篇目清单

由 `translation_queue.csv` 管理（8 篇，约 227KB）。

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
| 2026-08-21 | on-a-pincushion / a-toy-princess / siegfrid-and-handa | done | 三篇一批派发译成（2.0+23.6+26.7KB，7/115/80 对块，exit 0、0 可疑）；玩具公主口头语四句固定，歌谣按姊妹项目排式分行；术语表追加 30 条 |
| 2026-08-21 | the-hair-tree / the-seeds-of-love / the-story-of-the-opal / through-the-fire / the-story-of-vain-lamorna | done | 三子代理并行译成（54.8+30.1+15.6+51.8+22.6KB，均 exit 0、0 可疑，超 50KB 两篇按 §7 分段合并；各代理逐段机核 0 偏差）。全书 8/8（100%）收官 |
