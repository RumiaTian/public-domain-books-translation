# 翻译计划（philip-francis-nowlan_the-airlords-of-han）

## 本计划信息

- **项目名称**：philip-francis-nowlan_the-airlords-of-han（The Airlords Of Han）
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

共 16 篇，见 `translation_queue.csv`（合计 172KB）。

## 运行日志

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| 2026-08-23 | chapter-1.md | 完成 | I 空主被围；10.2KB；8 对块；check 退出码 0。新定名：波-坦（Bos-Tan）、阿-拉-纳（Ah-la-nah）、阿尔图纳帮（Altoonas）、利科明帮（Lycomings）、长枪手（long-gunner），余对齐前作黄金样本 |
| 2026-08-23 | chapter-2.md | 完成 | II "地面船"来犯；12.2KB；9 对块；check 退出码 0。新定名：哈丹头领（Handan）、卡萨曼（Casaman）、沃恩（Warn）、米夫林（Mifflin）、温斯洛帮（Winslows）、影盾（umbra-shield）、斧枪（ax-gun）、交界头领（Contact Boss）、乌尔特隆灯（ultronolamp）、湮灭护幕 |
| 2026-08-23 | chapter-3.md | 完成 | III 我们"击沉"地面船；7.5KB；8 对块；check 退出码 0。新定名：临时总头领（Boss Pro Tem）、电子镜（electronoscope）、穿透定时火箭 |
| 2026-08-23 | chapter-4.md | 完成 | IV 汉人电子射线科学；7.9KB；8 对块；check 退出码 0。新定名：远程超波镜（telultroscope）、启动电/拽电/亚裂解电、供力器（powerizer）、感应静电电池组、离子磁线圈、引反接收器、双联同步器 |
| 2026-08-23 | chapter-5.md | 完成 | V 美国超波科学；8.9KB；9 对块；check 退出码 0。新定名：超子（ultron 粒子）、梅特隆（metultron）、卡特隆（katultron）、聚焦电池（foco）、超光（ultralight）、辉点、帮际网络 |
| 2026-08-23 | chapter-6.md | 完成 | VI 一场不对等的决斗；8.8KB；9 对块；check 退出码 0。新定名：现役军官/基地军官（Active/Base Officer）、电子电话（electronophone）、操纵室、空腔艇首 |
| 2026-08-23 | chapter-7.md | 完成 | VII 被俘！；9.4KB；10 对块；check 退出码 0。新定名：圣-兰（San-Lan）、恩卢伊-莫克（Nlui-Mok）、全体汉人至荣空主 |
| 2026-08-23 | chapter-8.md | 完成 | VIII 催眠酷刑；11.3KB；10 对块；check 退出码 0。新定名：鄂-兰（Ngo-Lan）、露-燕（Lu-Yan）、电子记录仪（electronorecordograph）、气窝战术 |
| 2026-08-23 | chapter-9.md | 完成 | IX 纽-约的陷落；13.2KB；15 对块；check 退出码 0。新定名：卢-洛（Lui-Lok）、利-洪（Lip-Hung）、伦-达克（Ron-Dak）、生育教育署、末日之指（对齐前作） |
| 2026-08-23 | chapter-10.md | 完成 | X 壮丽之城洛-坦的生活；14.8KB；16 对块；check 退出码 0。新定名：菲斯-科（Fis-Ko）、满-丁（Man-Din）、苦力（Ku-Li）、奇-令（Ki-Ling）、云-云（Yun-Yun 工会）、血亲王（Princes of the Blood）、帝国投资信托 |
| 2026-08-23 | chapter-11.md | 完成 | XI 林中人进攻；10.7KB；9 对块；check 退出码 0。新定名：逆裂解机（reverse disintegrator）、执政元帅（Executive Marshal）、战略局、戈克-曼岭（Gok-Man）、穹屏、斥候线 |
| 2026-08-23 | chapter-12.md | 完成 | XII 神秘的"空球"；10.0KB；13 对块；check 退出码 0。新定名：空球（air ball）、遥控火箭 |
| 2026-08-23 | chapter-13.md | 完成 | XIII 逃亡！；15.2KB；13 对块；check 退出码 0。新定名：萨-卢斯（Sa-Lus）、联邦议会（Federal Council）、空中鱼雷（air torpedo）、谷门（Valley Gate）、计账机 |
| 2026-08-23 | chapter-14.md | 完成 | XIV 洛-坦的覆灭；12.2KB；12 对块；check 退出码 0。新定名：出发场（jump-off）、远程超波镜（telultrono scope）|
| 2026-08-23 | chapter-15.md | 完成 | XV 反击；8.7KB；10 对块；check 退出码 0。新定名：科罗拉多联盟、吉姆·霍尔韦尔（Jim Hallwell）、滚动弹幕、无线电扰频 |
| 2026-08-23 | chapter-16.md | done | 断点恢复：在盘完整文件取证回收（exit 0、0 可疑，末段完整），主代理代校验双写 done。全书 16/16（100%）收官 |
