# Plan.md

## 本计划信息

- **项目名称**：john-william-polidori_the-vampire（吸血鬼）
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md
- **领域配置**：prompts/领域配置/小说文学.md
- **术语表**：术语表.md

---

## 文件分工

| 文件 | 作用 | 谁来改 |
|------|------|--------|
| `项目说明.md` | 项目基本信息、领域配置、篇目清单 | 人工 |
| `术语表.md` | 翻译硬约束层 | agent / 人工 |
| `translation_queue.csv` | 任务队列（3 列） | 翻译前改 doing，完成改 done |
| `Plan.md`（本文件） | 执行步骤 + 运行日志 | agent 追加日志 |
| `原文/*.md` | 源文 | 不改 |
| `译文/*.zh-CN.md` | 译文产出（块对照双语） | 翻译 agent 产出 |

---

## 执行步骤

按 `prompts/翻译计划模板.md`「执行步骤」9 步推进（读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志）。委派模式由子代理逐篇执行。

---

## translation_queue.csv

```
file,size_kb,status
extract-of-a-letter-from-geneva.md,9.9,todo
introduction.md,5.9,todo
the-vampire.md,46.1,done
```

---

## 篇目清单

| # | 篇名 | 源文 | 大小 | 状态 |
|---|------|------|------|------|
| 1 | 日内瓦来信节选 | extract-of-a-letter-from-geneva.md | 9.9KB | todo |
| 2 | 导言 | introduction.md | 5.9KB | todo |
| 3 | 吸血鬼（正篇） | the-vampire.md | 46.1KB | done |

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-08-08 | 日内瓦来信节选（extract-of-a-letter-from-geneva.md） | 通过 | check exit=0；5 对块对照；拜伦《恰尔德·哈罗德》第三歌暴风雨三节诗句保留引用块分行；补注 Bonnet/Bonstetten/Chillon/Coppet/Chamouny/Stratford 等地名及 Phantasmagoriana/Christabel/ébauches 等作品名 |
| 2026-08-08 | 导言（introduction.md） | 通过 | check exit=0；6 对块对照（含拜伦《异教徒》诗句引用块）；术语照表：吸血鬼/马德雷加/卡绍维亚/海杜克/哈达格尼/阿诺德·保罗/洛林/异教徒；补注 Southey《Thalaba》译《萨拉萨》、Oneiza 奥妮扎、Tournefort 图内福尔、Calmet 卡尔梅；末段吸血鬼同义异称 Vroucolocha/Vardoulacha/Goul/Broucoloka 用音译+「食尸鬼」；阿拉伯数字 1732 保留以满足校验数字锚点 |
| 2026-08-08 | 吸血鬼（正篇 the-vampire.md） | 通过 | check exit=0；23 对块对照；术语照表：鲁思文勋爵/奥布里/伊安忒/默瑟夫人/马斯登伯爵；首现附原文 Lord Ruthven（鲁思文勋爵）、Aubrey（奥布里）、Ianthe（伊安忒）、Lady Mercer（默瑟夫人）；the ton 译「上流社交界」附原文、ennui 译「倦怠」附原文；地名补注：布鲁塞尔/罗马/雅典/士麦那/加来/那不勒斯/奥特朗托（Otranto）；专有补注：克什米尔蝴蝶（Kashmere）、保萨尼亚斯（Pausanias）、亚塔罕弯刀（yataghans）、法罗赌局（faro table）；临终誓约「一年零一日」为关键情节锚点；结尾双段（奥布里吐血而亡、鲁思文遁去、妹妹为吸血鬼所噬）完整译出无截断 |
