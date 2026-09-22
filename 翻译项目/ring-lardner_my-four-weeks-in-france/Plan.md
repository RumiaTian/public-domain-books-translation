# 翻译计划（我在法国的四个星期）

## 本计划信息

- **项目名称**：我在法国的四个星期
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/小说文学.md
- **术语表**：术语表.md

## 文件分工

| 文件 | 作用 | 谁来改 |
|------|------|--------|
| `项目说明.md` | 项目基本信息、领域配置、篇目清单 | 人工 |
| `术语表.md` | 翻译硬约束层。每篇译完补充新词 | agent / 人工 |
| `translation_queue.csv` | 任务队列。每行一文件，`file, size_kb, status` 三列 | 翻译前改 doing，完成后改 done |
| `Plan.md`（本文件） | 执行步骤 + 运行日志 | agent 追加日志 |
| `原文/*.md` | 源文 | 不改 |
| `译文/*.zh-CN.md` | 译文产出（块对照双语） | 翻译 agent 产出 |

## 执行步骤

按 `prompts/翻译计划模板.md`「执行步骤」9 步推进（读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志）。中篇连续模式，由主 agent 自己逐章执行。

## 篇目清单

| # | 篇名 | 源文 | 大小 | 状态 |
|---|------|------|------|------|
| 1 | 一、躲着潜艇去报道天下头等大赛 | 01-dodging-submarines-to-cover-the-biggest-game-of-all.md | 19.9KB | todo |
| 2 | 二、到了巴黎，见识种种怪事 | 02-i-get-to-paris-and-encounter-some-strange-sights.md | 23.0KB | todo |
| 3 | 三、想上美军营地，一路倒霉 | 03-i-try-to-get-to-the-american-camp-but-meet-disaster.md | 20.7KB | todo |
| 4 | 四、终于到了美军营地——我的所见 | 04-finally-i-get-to-the-american-camp-what-i-find-there.md | 24.1KB | todo |
| 5 | 五、我在英国前线的历险 | 05-my-adventures-at-the-british-front.md | 27.8KB | todo |
| 6 | 六、我怎么没能把某少校的车开到某某营地 | 06-how-i-didn-t-drive-major-blank-s-car-to-camp-such-and-such.md | 15.6KB | todo |
| 7 | 七、动身回国，顺道停伦敦 | 07-i-start-home-with-a-stopover-at-london.md | 23.8KB | todo |
| 8 | 八、回到老家，开始答问题 | 08-back-in-old-o-say-i-start-answering-questions.md | 15.3KB | todo |

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
| 2026-08-14 | 01–08 全部 8 篇 | done ×8（全书 8/8 译完） | exit 0 |
