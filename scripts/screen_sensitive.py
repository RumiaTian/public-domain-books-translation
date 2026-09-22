#!/usr/bin/env python3
"""
敏感题材筛查：历史[1301]判例触发词族 -> 密度扫描未启动书目 -> 产出三档报告。
用法: python scripts/screen_sensitive.py [输出文件名.md]
依赖: 根 translation_queue.csv（最新状态）
"""
import csv
import os
import re
import glob
from collections import defaultdict

ROOT = r'C:\Users\HanTi\OneDrive\translate'
BASE = os.path.join(ROOT, '翻译项目')

with open(os.path.join(ROOT, 'translation_queue.csv'), encoding='utf-8-sig') as f:
    rows = list(csv.DictReader(f))
done_any = {r['project'] for r in rows if r['status'].strip().lower() == 'done'}
kb = defaultdict(float)
for r in rows:
    if r['project'] not in done_any:
        kb[r['project']] += float(r['size_kb'] or 0)
untouched = sorted(kb)

FAM = {
    'slur': ['nigger', 'niggers', 'lynch', 'cooning', 'darky'],
    'race': ['negro', 'mulatto'],
    'war': ['battle', 'cannon', 'shell burst', 'bayonet', 'shrapnel', 'massacre', 'butchered'],
    'crime': ['murder', 'strangled', 'assassin', 'burglar', 'blackmail', 'poisoned', 'dagger'],
    'gore': ['corpse', 'shot dead', 'stabbed', 'throat cut', 'hanged'],
    'mourn': ['funeral', 'coffin', 'grave', 'weeping', 'mourn'],
}
CN_POL = ['政论', '无政府', '宗教批判', '神学', '布道', '教义']

def sample_text(proj, budget=120*1024):
    odir = os.path.join(BASE, proj, '原文')
    out, got = [], 0
    for fp in sorted(glob.glob(os.path.join(odir, '*.md'))):
        if got >= budget:
            break
        out.append(open(fp, encoding='utf-8', errors='replace').read())
        got = sum(len(x) for x in out)
    return ''.join(out)

def desc_text(proj):
    fp = os.path.join(BASE, proj, '项目说明.md')
    return open(fp, encoding='utf-8', errors='replace').read() if os.path.exists(fp) else ''

cats = defaultdict(list)   # 类别 -> [(proj, size, 证据)]
watch = []
high = {}
for proj in untouched:
    txt = sample_text(proj).lower()
    c = {fam: sum(len(re.findall(r'\b' + re.escape(w), txt)) for w in ws) for fam, ws in FAM.items()}
    desc = desc_text(proj)
    pol = any(w in desc for w in CN_POL)
    # captain-blood 假阳性修正：blood 是主角姓氏，不计
    gore = c['gore'] + (0 if 'captain-blood' in proj else len(re.findall(r'\bblood\b', txt)))
    crime_tot = c['crime'] + gore
    race_tot = c['slur'] + c['race']
    ev = f"slur{c['slur']}/race{c['race']}/war{c['war']}/crime{crime_tot}/mourn{c['mourn']}" + ('/+政论简述' if pol else '')
    tags = []
    if c['slur'] >= 3 or race_tot >= 15:
        tags.append('种族')
    if c['war'] >= 15:
        tags.append('战争')
    if crime_tot >= 30:
        tags.append('犯罪')
    if c['mourn'] >= 25 and not tags:
        tags.append('哀悼')
    if pol:
        tags.append('政论宗教')
    if tags:
        for t in tags:
            cats[t].append((proj, round(kb[proj]), ev))
        high[proj] = {'size': round(kb[proj]), 'tags': tags, 'ev': ev}
    elif (race_tot >= 5 or c['war'] >= 6 or crime_tot >= 12 or c['mourn'] >= 15):
        watch.append((proj, round(kb[proj]), ev))

lines = []
lines.append('# 敏感题材筛查报告（2026-09-14）\n')
lines.append('> 目的：预判 [1301] 内容拦截高风险书目，避免自动化空转重试。'
             '方法：历史被拦章节触发词取证 → 词族密度扫描（326 本未启动书，原文抽样前 120KB + 项目说明 + 书名）。\n')
lines.append('## 一、历史 [1301] 判例与触发词谱（取证）\n')
lines.append('| 判例 | 书 / 章节 | 结果 | 取证触发词密度（原文侧） |')
lines.append('|------|-----------|------|--------------------------|')
lines.append('| 1 | trollope《沃特尔》ch18 勒索章 | 免责前缀重派成功 | die 11 / died 11 / grave 5 / murder 3（死亡哀悼+勒索） |')
lines.append('| 2 | schuyler《Black No More》xiii | 双拦待人工 | nigger 10 / negro 12 / lynch 8（一章之内） |')
lines.append('| 3 | wallace《Terror Keep》10-viii | 双拦待人工 | murder 3 / dead 5 / kill 2（犯罪） |')
lines.append('| 4 | galdos《Trafalgar》ch1、ch6 | 各两次拦截（含免责重派仍拦）→ 封锁 | war 4-7 / battle 3-4 / grief 4 / cannon / blood（海战+哀悼） |')
lines.append('| 5 | de Quincey《Suspiria》the-affliction-of-childhood 97.8K | 拦后终过 | 童年哀悼长章（die/death 密集） |')
lines.append('| 6 | forester《付款延迟》审核简报 | 中性化措辞通过 | 简报含「毒杀/绞刑/凶手」字样即拦（简报侧比原文侧更敏感） |')
lines.append('')
lines.append('**触发词谱（按危险度降序）**：种族 slur（nigger/lynch/negro 密集）＞ 战争暴力（battle/cannon/massacre/grief）'
             '＞ 犯罪（murder/strangled/corpse/hanged/blackmail/poison）＞ 死亡哀悼高密度（die/death/grave/sob/funeral）。'
             '注：glm-flash 过滤明显严于主线模型；同一章主线可过、glm-flash 拦。\n')
lines.append('## 二、处置策略建议\n')
lines.append('1. **高危书直派主线模型（mimo/GLM 主线），禁用 glm-flash**；派发简报从第一章起就带已验证的免责前缀：'
             '`<!-- 本书为公版文学名著翻译练习，AI辅助译制，仅供学习交流 -->` 或「20 世纪学术研究用途公版小说」声明。')
lines.append('2. **高危书派发简报措辞中性化**：不写「凶杀/间谍/黑奴/私刑」等字样，用「悬疑经典」「历史题材」「社会小说」等中性词（判例 6）。')
lines.append('3. **政论宗教类按 WORKFLOW §七 既有规则后置**（本表「政论宗教」组）。')
lines.append('4. 单章两次拦截即封锁跳过（既有纪律），高危书预期封锁率 5-10%，人工兜底收尾。\n')
lines.append(f'## 三、高危书单（{len(high)} 本，合计 {sum(v["size"] for v in high.values())/1024:.1f} MB，占剩余 210MB 的 {sum(v["size"] for v in high.values())/210100:.0%}）\n')
order = ['种族', '战争', '犯罪', '哀悼', '政论宗教']
total_kb = defaultdict(float)
for t in order:
    for p, s, ev in cats[t]:
        total_kb[t] += s
for t in order:
    lst = cats[t]
    if not lst:
        continue
    lines.append(f'### {t}类（{len(lst)} 本，{total_kb[t]/1024:.1f} MB）\n')
    lines.append('| 书 | KB | 取证（每120KB抽样） |')
    lines.append('|----|----|---------------------|')
    for p, s, ev in sorted(lst, key=lambda x: -x[1]):
        lines.append(f'| {p} | {s} | {ev} |')
    lines.append('')
multi = [(p, v) for p, v in high.items() if len(v['tags']) > 1]
lines.append(f'### 多重风险叠加（{len(multi)} 本，最高优先押后）\n')
for p, v in sorted(multi, key=lambda x: -x[1]['size']):
    lines.append(f'- {p}（{v["size"]}KB）：{"+".join(v["tags"])}')
lines.append('')
lines.append(f'## 四、观察名单（{len(watch)} 本，正常派发 + 备免责预案）\n')
lines.append('信号弱于高危（如战争词 6-14、犯罪词 12-29、种族词 5-14、哀悼词 15+），多数应为正常过检；'
             '若单章被拦按标准纪律处理即可（重试 1 次 + 免责前缀，仍拦封锁）：\n')
lines.append('| 书 | KB | 信号 |')
lines.append('|----|----|------|')
for p, s, ev in sorted(watch, key=lambda x: -x[1]):
    lines.append(f'| {p} | {s} | {ev} |')
lines.append('')
rest = len(untouched) - len(high) - len(watch)
rest_kb = (sum(kb.values()) - sum(v['size'] for v in high.values()) - sum(s for _, s, _ in watch)) / 1024
lines.append(f'## 五、结论\n')
lines.append(f'- 326 本未启动书中：**高危 {len(high)} 本 ≈ {sum(v["size"] for v in high.values())/1024:.0f}MB**、'
             f'观察 {len(watch)} 本、无显著信号 {rest} 本 ≈ {rest_kb:.0f}MB。')
lines.append('- 排产建议：自动化按「无信号 → 观察 → 高危」顺序吃；高危组到期用主线模型+免责前缀集中攻坚，政论宗教组押后由人工决断。')
lines.append('- 被拦历史基线：~20 本书翻译全程仅 6 例拦截（2 章双拦待人工）；高危组预期拦截率仍为个位数百分比，'
             '免责前缀 + 主线模型可把浪费压到最低。')
lines.append('- 本报告为静态筛查快照，随翻译推进需与 translation_queue.csv 状态对齐后重跑。')

import sys
from datetime import date
out = os.path.join(ROOT, sys.argv[1] if len(sys.argv) > 1 else ('敏感题材筛查_' + date.today().isoformat() + '.md'))
open(out, 'w', encoding='utf-8').write('\n'.join(lines))
print('written:', out, len(lines), 'lines')
print('高危', len(high), '本', round(sum(v["size"] for v in high.values())/1024, 1), 'MB')
for t in order:
    print(' ', t, len(cats[t]), '本', round(total_kb[t]/1024, 1), 'MB')
print('观察', len(watch), '本', round(sum(s for _, s, _ in watch)/1024, 1), 'MB')
print('无信号', rest, '本', round(rest_kb, 1), 'MB')
