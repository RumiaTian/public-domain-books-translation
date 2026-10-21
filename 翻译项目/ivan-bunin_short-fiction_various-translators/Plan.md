# 翻译计划：布宁短篇集

## 本计划信息

- **项目名称**：ivan-bunin_short-fiction_various-translators
- **源文目录**：原文/
- **译文目录**：译文/
- **译文命名**：原名.zh-CN.md（放译文目录）
- **领域配置**：prompts/领域配置/小说文学.md
- **术语表**：术语表.md
- **执行模式**：委派（短篇集；见 WORKFLOW.md「单篇翻译流程」）

## 执行步骤

单篇 9 步（读配置 → 取 todo → doing → 读源文 → 翻译 → 自检 → check_bilingual.py → 双写 done → 日志）以 `prompts/翻译计划模板.md`「执行步骤」为准，本文件不重复。委派模式下由主 agent 派单，子代理简报含黄金样本与前篇末尾。

## 篇目清单

由 `translation_queue.csv` 管理（20 篇，约 533KB）。

## 运行日志

> 每次翻译完成后在此追加一行。

| 日期 | 篇目 | 结果 | 备注 |
|------|------|------|------|
| - | - | - | （尚未运行） |
| 2026-10-19 | a-compatriot.md | done | 一次性子代理翻译（全书首译篇），12 对块对照，check_bilingual 通过（退出码 0）。新增定名：Zotov 佐托夫、Nechaev 涅恰耶夫、Briansk 布良斯克、Iliyinka 伊林卡、Stariya Riyady 斯塔里亚·里亚德（老商场）、Sandunovskiya baths 桑杜诺夫浴室、Port Said 塞得港、Amur 阿穆尔、Manchuria 满洲、Philippine Islands 菲律宾群岛、Hindustan 印度斯坦、Southern Cross 南十字座、Canopus 老人星、Clouds of Magellan 麦哲伦云、Coal Sacks 煤袋、Alpha of the Centaur 半人马座阿尔法星、muzhik 庄稼汉 |
| 2026-10-19 | a-night-conversation.md | done | 一次性子代理翻译（58KB 分段流式落盘），54 对块对照，check_bilingual 通过（退出码 0）。新增定名：A Night Conversation 夜谈、Pashka 帕什卡、Theodot 费奥多特、Ivan 伊凡、Khomut 霍穆特、Kiriushka 基留什卡、Rogojkin 罗戈日金、Veretenkin 韦列坚金、Postnii 波斯特尼、Koslov 科兹洛夫、Liebedyana 列别佳尼、Eletzkaya province 叶列茨县、Zukhdens 祖赫坚、New Ceniyaks/Seniyaks 新谢尼亚克/谢尼亚克、Kursk 库尔斯克、Stanova 斯塔诺瓦、Prilepakh 普里列皮、Bochkov 博奇科夫、Mussin 穆辛、Kochergin 科切尔金、Kuzka 库兹卡、Pakhomka 帕霍姆卡、Ollka 奥莉卡、Andrushka 安德鲁什卡、Andrei Ivannov Bogdanov 安德烈·伊凡诺夫·博格丹诺夫、Dasha 达莎、Lily 莉莉、Youshkova 尤什科娃、Simashko 西马什科、Livingston 利文斯通、Baker 贝克、Naumov 纳乌莫夫、Nephedov 涅费多夫、Cheorchian 车臣人、Georgian 格鲁吉亚人、Assumption of the Holy Virgin 圣母安息节、Kiriki 基里基节、Capella 五车二星、borzoi 猎狼犬、young master 少东家、corn kiln 烘谷房、fortopianner 福尔捷皮安（钢琴） |
| 2026-10-19 | a-goodly-life.md | done | 一次性子代理翻译（63.5KB 分段流式落盘，6 段追加），42 对块对照，check_bilingual 通过（退出码 0）。新增定名：A Goodly Life 美好的一生、Nastasiya Semenovna Zhokhova 娜斯塔西娅·谢苗诺夫娜·若霍娃、Nastasiya/Nast/Nastechka 娜斯塔西娅/娜斯佳/娜斯坚卡、Vanniya 瓦尼亚（Vannka 万卡）、Kostiya 科斯佳、Meshcherina 梅谢里娜、Nikulin 尼库林、Samokhvalov 萨莫赫瓦洛夫、Matvei Ivannich 马特维·伊万尼奇、Liubov Ivanna 柳博芙·伊万娜、Nicanor Matveich 尼卡诺尔·马特维奇、Anna/Klasha 安娜/克拉莎、Vera 薇拉、Glukhaya Ulitza 格鲁哈亚街、Polkanikha 波尔卡尼哈、Chaikin 恰伊金、Phenia/Phenka 费尼娅/费恩卡、Kholin 霍林、Lagutin 拉古京、Nikolai Ivannich 尼古拉·伊万尼奇、Zadorsk 扎多尔斯克、Tsaritsin 察里津、Chernoslobodskaya cemetery 切尔诺斯洛博茨卡亚公墓、Skobele 斯科别列、Tula 图拉 |
2026-10-19 | an-evening-in-spring | ⏸️ 两次[1301]内容拦截（含古典文学免责重派），按降级协议保持todo跳过
| 2026-10-19 | aglaia.md | done | 一次性子代理翻译，12 对块对照，check_bilingual 通过（退出码 0）。新增定名：Aglaia 阿格拉娅、Anna 安娜（本篇）、Skuratovs 斯库拉托夫家、Sviyat-Oziero 斯维亚特-奥泽罗、Katherine 卡捷琳娜、Father Rodion 罗季翁神父、sarafan 萨拉凡、innocents 圣愚、Queen of Heaven 天上母后、Sergius of Radonezh 拉多涅日的谢尔盖、Simeon Stylites 柱头修士西缅、Fast of St. Peter 圣彼得斋期、Whitsuntide 圣灵降临节、Muscovy 莫斯科公国 |
2026-10-19 | foreword/endnotes | done | 前言（译者致谢）与15条尾注内联翻译（主代理微型件处理）；篇名暂用临时译名待各篇完成后统一
| 2026-10-19 | elijah-the-prophet.md | done | 一次性子代理翻译，12 对块对照，check_bilingual 通过（退出码 0）。篇名沿用 foreword 临时定名「先知以利亚」；源文 Setoiyon 为 Semyon 排印讹误，按上下文译谢苗。新增定名：Semyon Novikov 谢苗·诺维科夫、Nikon 尼康、Ovsiany Brod 奥夫夏尼-布罗德、St. Elijah's day 圣以利亚节、Yeletzk Ouyezd 叶列茨县、Predtechevskaya Volost 普列德捷切夫斯卡亚乡、Panteley 潘捷列伊、Anfiska 安菲斯卡、Kiev 基辅、White City 白城、Lord of the Sabaoth 万军之主、chiton 希顿长衣、verst 俄里 |
| 2026-10-19 | gautami.md | done | 一次性子代理翻译，15 对块对照，check_bilingual 通过（退出码 0）。篇名沿用 foreword 定名「乔达弥」；佛陀时代印度背景，佛教专名按通行汉译（世尊、黄衣僧团），末两段为法句偈颂体。新增定名：Gautami 乔达弥、Gautami the Lean 瘦乔达弥、the Blessed One 世尊、Himalayas 喜马拉雅山、satin trees 缎木树、kohl 眼墨、those that go clad in yellow 身披黄衣者的僧团 |
| 2026-10-19 | death.md | done | 一次性子代理翻译，20 对块对照，check_bilingual 通过（退出码 0）。新增定名：Death 死、The Leader 领袖、The Book 圣书、The Beloved 至爱者、Hebrews 希伯来人、Pharaoh 法老、Egypt 埃及、Promised Land 应许之地、Moab 摩押、Iscander the Two-Horned 双角的伊斯坎德尔、Land of Darkness 黑暗之国、Angel of the Winds 风之天使、Messenger of Death 死亡使者、Mogul 蒙古人、Atabek-Abou-Bekr 阿塔贝克·阿布·贝克尔、Fire-Worshippers 拜火教徒、The Eternal 永恒者、Sheikh Saadi 谢赫·萨阿迪、Sura 苏拉、《大消息》章、《离别》章、S'in 辛、Ghilliun 吉柳恩 |
2026-10-20 | gentle-breathing | done | 主模型直译（MCP分块管线）；布宁名篇，1块全篇，check PASS
2026-10-20 | figures | done | 主模型直译（MCP 8块）；篇名定为《数字》（学习数字的故事），foreword 同步修正 | 2026-10-20 | gentle-breathing | done | 主模型直译；布宁名篇，1块全篇，check PASS
2026-10-20 | kasimir-stanislavovitch | done | 主模型直译（MCP 1块）；车夫谐音布拉格/布拉圭、结尾断句字条照原文残句处理
2026-10-20 | the-grammar-of-love | done | 主模型直译（MCP 4块）；尾注〔10〕〔11〕锚点、花语列表与两段诗引对齐
2026-10-20 | son | done | 主模型直译（MCP 1块）；自杀契约场景按文学本位完整译出，作者括注按原文保留
2026-10-20 | i-say-nothing | done | 主模型直译（MCP 2块）；破木盆〔8〕锚点、俄式殴斗与乞丐圣歌完整译出
2026-10-20 | the-dreams-of-chang | done | 主模型直译（MCP 1块）；尾注〔14〕锚点、圣经纪引按和合本、Tao=道
2026-10-20 | the-gentleman-from-san-francisco | done | 主模型直译（MCP 2块）；劳伦斯/科捷良斯基合译名篇；启示录题词、魔鬼看船结尾完整
2026-10-20 | brethren | done | 主模型直译（MCP 2块）；锡兰车夫毒蛇自尽+英国人海上论道；经集题词、《婆娑罗树/乌鸦》传说完整
2026-10-20 | 🎉全书完成（19/20，1篇挂起）| 可译篇目全部done：10-19 晨间他流4篇+本会话接管（aglaia/death/elijah/gautami/foreword/endnotes），10-20 主模型直译模式完成 gentle-breathing/figures/kasimir/grammar-of-love/son/i-say-nothing/chang/gentle-from-san-francisco/brethren 九篇；an-evening-in-spring 两度[1301]挂起待人工
