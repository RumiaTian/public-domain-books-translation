# -*- coding: utf-8 -*-
"""审校报告统计（阶段三辅助工具）

扫描 翻译项目/*/审核报告.md，抽取「审校日期」与「质量等级」，按月份汇总 A/B/C/D 分布。
历史报告等级写法不统一（"A 优秀" / "A 级（优秀）" / "A-（优秀·出版预备级）" / 单品字母 "A"），
本脚本以「含等级关键词的行」为准，尽量不误抓正文里的"无 A 级缺陷"之类表述。

用法：
  python scripts/review_stats.py                 # 全量 + 按月分布
  python scripts/review_stats.py --before 2026-09-01 [--list]
"""
import re, os, sys, glob, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJ = os.path.join(ROOT, '翻译项目')

DATE_PATS = [
    r'(20\d{2})[-/](\d{1,2})[-/](\d{1,2})',
    r'(20\d{2})\s*年\s*(\d{1,2})\s*月\s*(\d{1,2})\s*日',
]
GRADE_WORDS = ['优秀', '良好', '需关注', '严重']
FIELD = r'(?:质量等级|质量评级|综合质量评定|综合评级|总体评级|审校等级|审校判定结论|等级判定|评级|等级)'


def grade_on_line(ln):
    """从单行抽取等级：优先「字母+质量词」，退化到括号/冒号内的单品字母。"""
    wm = re.search(r'(' + '|'.join(GRADE_WORDS) + r')', ln)
    lm = re.search(r'(?<![A-Za-z])([A-D])(?![\u4e00-\u9fff])\s*[+\-]?', ln)
    if lm:
        return lm.group(1) + (' ' + wm.group(1) if wm and wm.start() > lm.start() else '')
    m2 = (re.search(r'([A-D])\s*[+\-]\s*(?:级)?', ln)
          or re.search(r'[（(【\s]([A-D])\s*[）)】]', ln)
          or re.search(r'[:：]\s*\*{0,2}([A-D])\b', ln))
    return m2.group(1) if m2 else None


def find_dates(line):
    out = []
    for p in DATE_PATS:
        for m in re.finditer(p, line):
            y, mo, d = (int(g) for g in m.groups())
            out.append('%04d-%02d-%02d' % (y, mo, d))
    return out


def parse(path):
    txt = open(path, encoding='utf-8', errors='ignore').read()
    lines = txt.split('\n')
    dates, grades = [], []
    for i, ln in enumerate(lines):
        if re.search(r'(?:审校|审核|复核)日期', ln):
            dates += [('field', d) for d in find_dates(ln)]
        if not re.search(FIELD, ln):
            continue
        raw = grade_on_line(ln)
        if raw is None:
            # 等级常落在标题行的下一行（LaTeX 加粗行、独立判定行）
            for nxt in lines[i + 1:i + 3]:
                if not nxt.strip():
                    continue
                raw = grade_on_line(nxt)
                if raw:
                    break
        if raw:
            grades.append(raw)
    # 日期兜底：正文里任意日期（仅当字段行没有时）
    if not dates:
        for ln in lines:
            ds = find_dates(ln)
            if ds:
                dates += [('loose', d) for d in ds]
    d = None
    if dates:
        d = sorted(set(x[1] for x in dates))[0]
    g = grades[0] if grades else None
    letter = None
    if g:
        lm = re.search(r'([A-D])', g)
        letter = lm.group(1) if lm else None
    return d, g, letter, ('field' if dates and dates[0][0] == 'field' else 'loose')


def main(argv):
    before = None
    if '--before' in argv:
        before = argv[argv.index('--before') + 1]
    show_list = '--list' in argv
    rows = []
    for rp in glob.glob(os.path.join(PROJ, '*', '审核报告.md')):
        proj = os.path.basename(os.path.dirname(rp))
        d, g, letter, dsrc = parse(rp)
        rows.append((proj, d, g, letter, dsrc))
    print("报告总数: %d" % len(rows))
    nodate = [r for r in rows if not r[1]]
    print("无日期: %d %s" % (len(nodate), [r[0] for r in nodate][:20]))
    loose = [r for r in rows if r[3] == 'loose']
    print("日期为正文兜底(非字段行): %d" % len(loose))
    nol = [r for r in rows if not r[3]]
    print("无等级: %d %s" % (len(nol), [r[0] for r in nol][:30]))
    # 按月
    bym = collections.Counter()
    for r in rows:
        if r[1]:
            bym[r[1][:7]] += 1
    print("\n按月分布:")
    for k in sorted(bym):
        print("  %s : %d" % (k, bym[k]))

    sel = [r for r in rows if r[1] and (before is None or r[1] < before)]
    print("\n=== 日期 < %s 共 %d 本 ===" % (before or '无限制', len(sel)))
    cnt = collections.Counter(r[3] or '?' for r in sel)
    print("等级分布: " + '  '.join('%s×%d' % (k, cnt[k]) for k in sorted(cnt)))
    if show_list:
        for proj, d, g, letter, _ in sorted(sel, key=lambda x: (x[1], x[0])):
            print("  %s  %-6s %s" % (d, letter or '?', proj))


if __name__ == '__main__':
    main(sys.argv[1:])
