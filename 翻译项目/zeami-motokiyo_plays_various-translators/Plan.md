# 翻译计划（Plan.md）——zeami-motokiyo_plays

> 本项目 Plan.md 从 `prompts/翻译计划模板.md` 复制填充。执行步骤照模板 9 步推进，此处不重复；运行日志在文末追加。

---

## 本计划信息

- **项目名称**：zeami-motokiyo_plays_various-translators（世阿弥能剧集·诸家英译）
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

## translation_queue.csv 格式

```
file,size_kb,status
foreword.md,0.5,todo
takasago.md,13.3,todo
...
```

| 字段 | 含义 | 取值 |
|------|------|------|
| `file` | 源文文件名（在 `原文/` 目录下） | 如 `takasago.md` |
| `size_kb` | 源文大小（KB） | 数字 |
| `status` | 翻译状态 | `todo` 待译 / `doing` 翻译中 / `done` 已完成 |

---

## 篇目清单

| # | 篇名 | 源文 | 大小 | 状态 |
|---|------|------|------|------|
| 1 | 前言（Foreword） | foreword.md | 0.5KB | todo |
| 2 | 高砂（Takasago） | takasago.md | 13.3KB | todo |
| 3 | 樱川（Sakuragawa） | sakuragawa.md | 11.1KB | todo |
| 4 | 砧（Kinuta） | kinuta.md | 11.2KB | todo |
| 5 | 须磨源氏（Suma Genji） | suma-genji.md | 5.0KB | todo |
| 6 | 锦木（Nishikigi） | nishikigi.md | 13.8KB | todo |
| 7 | 山姥（Yamanba） | yamanba.md | 9.0KB | todo |
| 8 | 敦盛（Atsumori） | atsumori.md | 10.5KB | todo |
| 9 | 尾注（Endnotes） | endnotes.md | 7.7KB | todo |

- 执行模式：**委派**（短篇集）——每篇下沉一次性子代理执行 9 步；并发 ≤ 3。
- 顺序说明：按原书 spine 顺序排列（前言在前、尾注殿后）；各剧独立，可乱序派发，但 endnotes.md 建议最后译（便于统一注释编号对应）。

---

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-08-18 | foreword.md（前言） | done | 0.5KB，1 对块，check 退出码 0，首译定基调 |
| 2026-08-18 | takasago.md（高砂） | done | 13.3KB，67 对块，check 退出码 0，逐块行数对应；尾注 1–27 保留；术语表已回填新词 |
| 2026-08-18 | sakuragawa.md（樱川） | done | 11.1KB，55 对块，check 退出码 0，逐块行数对应；尾注 28–37 保留；⋮ 省略号保留；术语表回填并修正 Sakura 条目（狂女之子，少年樱） |
| 2026-08-18 | kinuta.md（砧） | done | 11.2KB，45 对块，check 退出码 0，逐块行数对应；尾注 38–39 保留；正旋/反旋、hera 拟声等按术语表；术语表回填《砧》篇新词 |
| 2026-08-18 | suma-genji.md（须磨源氏） | done | 5.0KB，25 对块，check 退出码 0，逐块行数对应；尾注 40–47 保留；青海波、桐壶、澪标、乙女、藤裏叶等《源氏》帖名按通行译法，首现附原文 |
| 2026-08-18 | nishikigi.md（锦木） | done | 13.8KB，74 对块，check 退出码 0，源文 289 行全覆盖（含 U+FEFF/U+200A 等不可见字符照搬）；无尾注标记；Kefu 汉字未敢臆改，沿用《砧》Kinshu 先例保留罗马字；术语表回填《锦木》篇新词 |
| 2026-08-18 | yamanba.md（山姥） | done | 9.0KB，57 对块，check 退出码 0，源文 60 行全覆盖（U+FEFF 词连接符等照搬）；无尾注标记；野口语体按对话感处理；Azero 峠仿 Kinshu/Kefu 例保留罗马字；术语表回填《山姥》篇新词 |
| 2026-08-18 | atsumori.md（敦盛） | done | 10.5KB，58 对块，check 退出码 0，源文 207 行全覆盖；尾注 48–54 保留核对；Waley 译本名笛（小枝/蝉丸/青叶/盐灶）、十念、寿永、间狂言等按术语表及通行译法；术语表回填《敦盛》篇新词 |
| 2026-08-18 | endnotes.md（尾注） | done | 7.7KB，54 对块（注 1–54 逐条对照），check 退出码 0，源文 59 行全覆盖；注 3、35 多段对应；汉字俗谚罗马字照搬并附译意；蒂津、巴克勒、于勒·罗曼等新词回填术语表。**全项目 9 篇全部 done，收官** |
