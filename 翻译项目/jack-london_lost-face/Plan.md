# 翻译计划（jack-london_lost-face）

## 本计划信息

- **项目名称**：jack-london_lost-face（Lost Face）
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

共 7 篇，见 `translation_queue.csv`（合计 222KB）。

## 运行日志

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
| 2026-08-27 | to-build-a-fire / lost-face / that-spot / flush-of-gold / the-passing-of-marcus-obrien / the-wit-of-porportuk / trust | done | 委派子代理译完全书 7 篇（生火14块/丢脸19块/那块斑点8块/金霞20块/马库斯之死23块/波珀图克51块/信任18块），全部 check 0 错配；术语表扩至 150+ 条（育空/克朗代克/瑟克尔城等淘金地名与船名）。波珀图克与信任两篇曾因[1308]额度中断，由断点续作子代理按段落级断点追加完成（波珀图克 178/226 续至全）。**全书 7/7 收官（100%）** |
