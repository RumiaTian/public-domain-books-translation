# Plan（《皮史密斯进城记》翻译计划）

> 从 `prompts/翻译计划模板.md` 复制建立。执行步骤、CSV 格式等通用规范见模板，此处为本书实例。

---

## 本计划信息

- **项目名称**：p-g-wodehouse_psmith-in-the-city（《皮史密斯进城记》，P. G. 伍德豪斯）
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/小说文学.md
- **术语表**：术语表.md

---

## 文件分工

| 文件 | 作用 | 谁来改 |
|------|------|--------|
| `项目说明.md` | 项目基本信息、领域配置、篇目清单 | 人工 |
| `术语表.md` | 翻译硬约束层。每篇译完补充新词 | agent / 人工 |
| `translation_queue.csv` | 任务队列。每行一文件，`file, size_kb, status` 三列 | 翻译前改 doing，完成后改 done |
| `Plan.md`（本文件） | 执行步骤 + 运行日志 | agent 追加日志 |
| `原文/*.md` | 源文 | 不改 |
| `译文/*.zh-CN.md` | 译文产出（块对照双语） | 翻译 agent 产出 |

---

## 篇目清单

| # | 篇名 | 源文 | 大小 | 状态 |
|---|------|------|------|------|
| 0 | 献词 | 00-dedication.md | 0.0KB | todo |
| 0 | 序言 | 00-preface.md | 0.1KB | todo |
| 1 | 比克斯代克先生走到投球手手臂后面 | 01-mr-bickersdyke-walks-behind-the-bowler-s-arm.md | 13.5KB | todo |
| 2 | 迈克听到坏消息 | 02-mike-hears-bad-news.md | 7.1KB | todo |
| 3 | 新时代开始了 | 03-the-new-era-begins.md | 9.6KB | todo |
| 4 | 商界生涯的第一步 | 04-first-steps-in-a-business-career.md | 10.5KB | todo |
| 5 | 另一个人 | 05-the-other-man.md | 8.1KB | todo |
| 6 | 皮史密斯解说 | 06-psmith-explains.md | 10.2KB | todo |
| 7 | 进入冬季营房 | 07-going-into-winter-quarters.md | 10.8KB | todo |
| 8 | 友善的当地人 | 08-the-friendly-native.md | 12.0KB | todo |
| 9 | 闹鬼的比克斯代克先生 | 09-the-haunting-of-mr-bickersdyke.md | 9.1KB | todo |
| 10 | 比克斯代克先生向选民演讲 | 10-mr-bickersdyke-addresses-his-constituents.md | 11.3KB | todo |
| 11 | 被人误解 | 11-misunderstood.md | 9.7KB | todo |
| 12 | 简而言之 | 12-in-a-nutshell.md | 11.0KB | todo |
| 13 | 迈克又被调动 | 13-mike-is-moved-on.md | 7.0KB | todo |
| 14 | 沃勒先生显露新面目 | 14-mr-waller-appears-in-a-new-light.md | 10.8KB | todo |
| 15 | 公地上的风波 | 15-stirring-times-on-the-common.md | 12.3KB | todo |
| 16 | 后续发展 | 16-further-developments.md | 9.6KB | todo |
| 17 | 星期日晚餐 | 17-sunday-supper.md | 11.7KB | todo |
| 18 | 皮史密斯有个发现 | 18-psmith-makes-a-discovery.md | 9.7KB | todo |
| 19 | 爱德华生病 | 19-the-illness-of-edward.md | 9.9KB | todo |
| 20 | 关于一张支票 | 20-concerning-a-cheque.md | 7.4KB | todo |
| 21 | 皮史密斯展开调查 | 21-psmith-makes-inquiries.md | 11.0KB | todo |
| 22 | 并采取行动 | 22-and-takes-steps.md | 5.6KB | todo |
| 23 | 比克斯代克先生作出让步 | 23-mr-bickersdyke-makes-a-concession.md | 13.8KB | todo |
| 24 | 骚动之气 | 24-the-spirit-of-unrest.md | 8.3KB | todo |
| 25 | 在电话边 | 25-at-the-telephone.md | 7.1KB | todo |
| 26 | 传达消息 | 26-breaking-the-news.md | 8.0KB | todo |
| 27 | 在罗德球场 | 27-at-lord-s.md | 12.2KB | todo |
| 28 | 皮史密斯安排前程 | 28-psmith-arranges-his-future.md | 8.2KB | todo |
| 29 | 以及迈克的前程 | 29-and-mike-s.md | 11.3KB | todo |
| 30 | 最后的伤别离 | 30-the-last-sad-farewells.md | 7.3KB | todo |

（权威状态以 `translation_queue.csv` 为准）

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-09-02 | 全书 32 件（献词＋序＋30 章） | 完成 32/32 | 批次1三段并行（98.3/93.1/102.8KB，12+9+11 件全单发）零[1301][1302][1308]；32 件全量过检零告警；术语表旧种子（皮史密斯/罗德板球场/新亚细亚银行）经查证系未译项目模板而非既有译文，零泄漏，本批确立系列规范定名（普史密斯/新亚银行/洛兹板球场/同志）；板球术语规范化；普史密斯浮夸长句与同志口癖全篇贯穿 |
