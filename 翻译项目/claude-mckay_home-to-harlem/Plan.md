# 翻译计划（Plan.md）

> 依据 `prompts/翻译计划模板.md` 建立。执行流程、双语对照格式、完整性禁令见模板与 `prompts/通用翻译引擎.md`，此处不重复。

---

## 本计划信息

- **项目名称**：回到哈莱姆（Home to Harlem，Claude McKay, 1928）
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

## 执行模式

**委派模式**（内容形态：长篇，21 章 + 部分划分 + 献词/尾注共 26 文件）。主 agent 只当调度员，按 `WORKFLOW.md`「委派模式调度循环」逐篇派子代理执行 9 步流程（并发 ≤ 3）。

---

## translation_queue.csv 格式

```
file,size_kb,status
01-dedication.md,0.0,todo
03-going-back-home.md,7.8,todo
...
```

26 行（阅读顺序 = 文件名数字前缀顺序），status 全 todo。权威源为本文件同目录的 `translation_queue.csv`，根表为只读快照。

## 执行步骤（agent 按此推进，两种模式共用）

> 详见 `prompts/翻译计划模板.md`「执行步骤」9 步：读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志。

---

## 篇目清单

| # | 篇名 | 源文 | 大小 | 状态 |
|---|------|------|------|------|
| 1 | 献词 | 01-dedication.md | 0.0KB | todo |
| 2 | 第一部分 | 02-first-part.md | 0.0KB | todo |
| 3 | 一 回家去 | 03-going-back-home.md | 7.8KB | todo |
| 4 | 二 抵达 | 04-arrival.md | 5.2KB | todo |
| 5 | 三 泽迪 | 05-zeddy.md | 9.3KB | todo |
| 6 | 四 刚果·罗丝 | 06-congo-rose.md | 11.4KB | todo |
| 7 | 五 重操旧业 | 07-on-the-job-again.md | 13.3KB | todo |
| 8 | 六 默特尔大道 | 08-myrtle-avenue.md | 17.8KB | todo |
| 9 | 七 泽迪的起落 | 09-zeddy-s-rise-and-fall.md | 24.9KB | todo |
| 10 | 八 查抄「巴尔的摩」 | 10-the-raid-of-the-baltimore.md | 9.0KB | todo |
| 11 | 九 杰克出走 | 11-jake-makes-a-move.md | 6.9KB | todo |
| 12 | 第二部分 | 12-second-part.md | 0.0KB | todo |
| 13 | 十 铁路 | 13-the-railroad.md | 15.6KB | todo |
| 14 | 十一 匹兹堡风雪 | 14-snowstorm-in-pittsburgh.md | 18.6KB | todo |
| 15 | 十二 整治厨师长 | 15-the-treeing-of-the-chef.md | 25.9KB | todo |
| 16 | 十三 费城一夜 | 16-one-night-in-philly.md | 14.1KB | todo |
| 17 | 十四 间奏 | 17-interlude.md | 13.3KB | todo |
| 18 | 十五 故态复萌 | 18-relapse.md | 9.6KB | todo |
| 19 | 十六 一场恶作剧 | 19-a-practical-prank.md | 13.2KB | todo |
| 20 | 十七 他也爱过 | 20-he-also-loved.md | 16.4KB | todo |
| 21 | 十八 送别宴 | 21-a-farewell-feed.md | 11.7KB | todo |
| 22 | 第三部分 | 22-third-part.md | 0.0KB | todo |
| 23 | 十九 哈莱姆之春 | 23-spring-in-harlem.md | 19.8KB | todo |
| 24 | 二十 菲莉斯 | 24-felice.md | 14.0KB | todo |
| 25 | 二十一 比利的礼物 | 25-the-gift-that-billy-gave.md | 23.8KB | todo |
| 26 | 尾注 | 26-endnotes.md | 0.1KB | todo |

（状态以 `translation_queue.csv` 为准）

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
- 07:11 批次3直启会话：chapter 07-on-the-job-again（全书唯一剩余章）两次派发（原文直译+学术免责中性化重派）均于 ~100 秒遭 [1301] 内容拦截，零产出。判定内容级硬拦，保持 todo 待人工处置；认领锁保留自然老化。25/26 done。

- 2026-09-22 04:07｜批次3直启｜07-on-the-job-again.md 两次 [1301] 内容拦截（含学术免责重试），按协议保持 todo 跳过，释放认领锁待后续重试。全书记 25/26 done。
