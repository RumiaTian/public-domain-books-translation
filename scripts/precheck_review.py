# -*- coding: utf-8 -*-
"""审校派发前预检（阶段三辅助工具）

用途：对一批待审项目做程序化预检，输出供审校子代理简报使用的要点：
  1) 块对称（===Original=== / ===Chinese=== 计数）与段数对比（含不对称文件清单）
  2) 英文残留计数（剔除）中文（English） 首现括注后的拉丁词频）
  3) 术语表硬约束行落位（源侧/译侧掩码计数，"最长优先"避免子串重复计数）
     + 幽灵条目（源 0 次）与归一残留（备注中"X已改/已归一"的旧形实测）

用法：
  python scripts/precheck_review.py <项目名> [<项目名> ...]
  python scripts/precheck_review.py --all-in <列表文件名>     # 每行一个项目名

注意：术语落位计数含噪声（复合词、别称、复数），仅供简报"疑似清单"，最终以审校员实测为准。
"""
import re, os, sys, csv, glob, collections, io

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJ = os.path.join(ROOT, '翻译项目')

# 阅读序陷阱书的显式序（字母序 ≠ 阅读序）；未列出的项目按文件名排序（数字前缀安全）
READ_ORDER = {
'edward-payson-roe_driven-back-to-eden': ['dedication.md','preface.md','a-problem.md','i-state-the-case.md','new-prospects.md','a-momentous-expedition.md','a-country-christmas-in-a-city-flat.md','a-bluff-friend.md','mr-jones-shows-me-the-place.md','telling-about-eden.md','breaking-camp.md','scenes-on-the-wharf.md','a-voyage-up-the-hudson.md','a-march-evening-in-eden.md','rescued-and-at-home.md','self-denial-and-its-reward.md','our-sunny-kitchen.md','making-a-place-for-chickens.md','good-bargains-in-maple-sugar.md','butternuts-and-bobsey-s-peril.md','john-jones-jun.md','raspberry-lessons.md','the-vandoo.md','early-april-gardening.md','a-bonfire-and-a-feast.md','no-blind-drifting.md','owls-and-antwerps.md','a-country-sunday.md','strawberry-visions-and-pertaters.md','corn-color-and-music.md','we-go-a-fishing.md','weeds-and-working-for-dear-life.md','nature-smiles-and-helps.md','cherries-berries-and-berry-thieves.md','given-his-choice.md','given-a-chance.md','we-shall-all-earn-our-salt.md','a-thunderbolt.md','rallying-from-the-blow.md','august-work-and-play.md','a-trip-to-the-seashore.md','a-visit-to-houghton-farm.md','hoarding-for-winter.md','autumn-work-and-sport.md','thanksgiving-day.md','we-can-make-a-living-in-eden.md','list-of-illustrations.md'],
'thomas-de-quincey_suspiria-de-profundis': ['editor-s-preface.md','dreaming.md','the-affliction-of-childhood.md','the-english-mail-coach.md','the-palimpsest-of-the-human-brain.md','vision-of-life.md','memorial-suspiria.md','levana-and-our-ladies-of-sorrow.md','the-solitude-of-childhood.md','the-dark-interpreter.md','the-apparition-of-the-brocken.md','savannah-la-mar.md','the-daughter-of-lebanon.md','the-princess-who-overlooked-one-seed-in-a-pomegranate.md','who-is-this-woman-that-beckoneth-and-warneth-me-from-the-place-where-she-is-and-in-whose-eyes-is-woeful-remembrance-i-guess-who-she-is.md','endnotes.md'],
'edgar-wallace_the-avenger': ['the-headhunter.md','mr-sampson-longvale-calls.md','the-niece.md','the-leading-lady.md','mr-lawley-foss.md','the-master-of-griff.md','the-swords-and-bhag.md','bhag.md','the-ancestor.md','the-open-window.md','the-mark-on-the-window.md','a-cry-from-a-tower.md','the-trap-that-failed.md','mendoza-makes-a-fight.md','two-from-the-yard.md','the-brown-man-from-nowhere.md','mr-foss-makes-a-suggestion.md','the-face-in-the-picture.md','the-midnight-visit.md','a-narrow-escape.md','the-erasure.md','the-head.md','clues-at-the-tower.md','the-marks-of-the-beast.md','the-man-in-the-car.md','the-hand.md','the-caves.md','the-tower.md','bhag-s-return.md','the-advertisement.md','john-percival-liggitt.md','gregory-s-way.md','the-trap-that-failed-2.md','the-search.md','what-happened-to-adele.md','the-escape.md','at-the-tower-again.md','the-cavern-of-bones.md','michael-knows-for-sure.md','the-widow.md','the-death.md','camera.md'],
'wilkie-collins_the-haunted-hotel': ['dedication.md','part-1.md','chapter-1.md','chapter-2.md','chapter-3.md','chapter-4.md','part-2.md','chapter-5.md','chapter-6.md','chapter-7.md','chapter-8.md','chapter-9.md','chapter-10.md','chapter-11.md','chapter-12.md','part-3.md','chapter-13.md','chapter-14.md','chapter-15.md','part-4.md','chapter-16.md','chapter-17.md','chapter-18.md','chapter-19.md','chapter-20.md','chapter-21.md','chapter-22.md','chapter-23.md','chapter-24.md','chapter-25.md','chapter-26.md','chapter-27.md','chapter-28.md','epilogue.md'],
'cicely-hamilton_theodore-savage': ['i.md','ii.md','iii.md','iv.md','v.md','vi.md','vii.md','viii.md','ix.md','x.md','xi.md','xii.md','xiii.md','xiv.md','xv.md','xvi.md','xvii.md','xviii.md','xix.md','xx.md','xxi.md','xxii.md','xxiii.md'],
'john-w-campbell_islands-of-space': ['prologue.md','chapter-1.md','chapter-2.md','chapter-3.md','chapter-4.md','chapter-5.md','chapter-6.md','chapter-7.md','chapter-8.md','chapter-9.md','chapter-10.md','chapter-11.md','chapter-12.md','chapter-13.md','chapter-14.md','chapter-15.md','chapter-16.md','chapter-17.md','chapter-18.md','chapter-19.md','chapter-20.md','chapter-21.md','chapter-22.md','chapter-23.md','endnotes.md'],
}


def _natkey(s):
    """自然排序键：chapter-2 排在 chapter-10 之前（避免 sorted() 的字典序陷阱）。"""
    return [int(t) if t.isdigit() else t.lower() for t in re.split(r'(\d+)', s)]


def files_sorted(book):
    d = os.path.join(PROJ, book, '原文')
    fs = [f for f in os.listdir(d) if f.endswith('.md')]
    if book in READ_ORDER:
        return READ_ORDER[book]
    return sorted(fs, key=_natkey)


def zh_blocks(text):
    return [m.group(1) for m in re.finditer(r'===Chinese===\n(.*?)(?====Original===|\Z)', text, re.S)]


def en_blocks(text):
    return [m.group(1) for m in re.finditer(r'===Original===\n(.*?)(?====Chinese===|\Z)', text, re.S)]


def paras(s):
    return [l for l in s.split('\n') if l.strip()]


def strip_parens(s):
    prev = None
    while prev != s:
        prev = s
        s = re.sub(r'（[^（）]*）', '', s)
        s = re.sub(r'\([^()]*\)', '', s)
    return s


def norm_en(s):
    s = s.replace('\u2019', "'").replace('\u2018', "'")
    s = re.sub(r'\.', '', s)
    s = re.sub(r'\s+', ' ', s)
    return s.lower()


def src_variants(cell):
    out = []
    cell = cell.strip()
    v1 = strip_parens(cell)
    v2 = re.sub(r'[()（）]', '', cell)
    for base in (v1, v2, cell):
        for part in re.split(r'\s*/\s*|\s+or\s+', base):
            part = part.strip().strip('*').strip()
            if part:
                out.append(part)
    seen = set(); res = []
    for x in out:
        k = norm_en(x)
        if k and k not in seen:
            seen.add(k); res.append(x)
    return res


def tgt_main(cell):
    cell = cell.strip()
    base = re.split(r'[（(]', cell)[0].strip()
    if not base:
        base = cell
    return [p.strip() for p in re.split(r'\s*[／/]\s*', base) if p.strip()]


def mask_count(items, text, label):
    norm_items = []
    for key, needle in items:
        n = norm_en(needle) if label == 'en' else needle
        if label == 'zh':
            norm_items.append((len(needle), key, needle))
        else:
            norm_items.append((len(n), key, n))
    norm_items.sort(key=lambda x: -x[0])
    work = text
    counts = collections.Counter()
    for ln, key, needle in norm_items:
        if not needle:
            continue
        if label == 'en':
            pat = re.escape(needle)
            if re.fullmatch(r"[a-z'\- ]+", needle) and ' ' not in needle:
                pat = r'\b' + pat + r'\b'
            matches = list(re.finditer(pat, work))
        else:
            matches = list(re.finditer(re.escape(needle), work))
        if matches:
            counts[key] += len(matches)
            work = re.sub(re.escape(needle), lambda m: '\x00' * len(m.group(0)), work)
    return counts


def parse_terms(gt):
    terms = []
    for line in gt.split('\n'):
        line = line.strip()
        if not line.startswith('|') or set(line) <= set('|- :'):
            continue
        cells = [x.strip() for x in line.strip('|').split('|')]
        if len(cells) < 2:
            continue
        if cells[0] in ('原文', '源词', '术语', '专名', '中文') or cells[1] in ('译法', '出现次数', '定名'):
            continue
        if re.fullmatch(r'\d+', cells[1] or ''):
            continue
        terms.append((cells[0], cells[1], cells[2] if len(cells) > 2 else ''))
    return terms


def precheck(book, buf):
    def P(*a):
        print(*a, file=buf)
    pdir = os.path.join(PROJ, book)
    if not os.path.isdir(pdir):
        P("### %s  <项目不存在>" % book); return
    order = files_sorted(book)
    P("=" * 100)
    P("### %s  (%d files)" % (book, len(order)))
    tot_o = tot_c = tot_po = tot_pc = 0
    asym_files = []
    eng_res = collections.Counter()
    all_zh = []; all_en = []
    for f in order:
        zhp = os.path.join(pdir, '译文', f.replace('.md', '.zh-CN.md'))
        enp = os.path.join(pdir, '原文', f)
        if not os.path.exists(zhp):
            P("  !! 译文缺失: %s" % f); continue
        t = open(zhp, encoding='utf-8').read()
        o = t.count('===Original==='); c = t.count('===Chinese===')
        tot_o += o; tot_c += c
        zbs = zh_blocks(t); ebs = en_blocks(t)
        po = sum(len(paras(b)) for b in ebs); pc = sum(len(paras(b)) for b in zbs)
        tot_po += po; tot_pc += pc
        if o != c or po != pc:
            asym_files.append((f, o, c, po, pc))
        all_zh.append('\n'.join(zbs))
        all_en.append(open(enp, encoding='utf-8').read())
    text_zh = '\n'.join(all_zh)
    text_en = norm_en('\n'.join(all_en))
    clean_zh = strip_parens(text_zh)
    for m in re.finditer(r"[A-Za-z][A-Za-z'\-]{1,}", clean_zh):
        eng_res[m.group(0)] += 1
    P("  块: O=%d C=%d %s | 段: EN=%d CN=%d %s" % (
        tot_o, tot_c, "OK" if tot_o == tot_c else "!!不对称",
        tot_po, tot_pc, "OK" if tot_po == tot_pc else "!!差 %d" % (tot_po - tot_pc)))
    for f, o, c, po, pc in asym_files[:25]:
        P("     [不对称] %-52s O=%d C=%d 段EN=%d 段CN=%d" % (f, o, c, po, pc))
    top = eng_res.most_common(10)
    P("  英文残留(剔括注) top: %s" % (', '.join('%s×%d' % (w, n) for w, n in top) if top else '无'))
    pdoc = os.path.join(pdir, '项目说明.md')
    if os.path.exists(pdoc):
        dt = open(pdoc, encoding='utf-8').read()
        m = re.search(r'## 备注\s*\n+(.*)', dt, re.S)
        if m:
            note = m.group(1).strip()
            if note and note != '（无）':
                P("  项目说明备注: %s" % note.replace('\n', ' / ')[:500])
    gp = os.path.join(pdir, '术语表.md')
    gt = open(gp, encoding='utf-8').read()
    terms = parse_terms(gt)
    hard = [(s, t, n) for (s, t, n) in terms if t and re.search(r'[\u4e00-\u9fff]', t)]
    if hard:
        P("  -- 术语表硬约束行 %d 条:" % len(hard))
        en_items = []
        for i, (s, t, n) in enumerate(hard):
            for v in src_variants(s):
                en_items.append((i, v))
        en_counts = mask_count(en_items, text_en, 'en')
        zh_items = []
        for i, (s, t, n) in enumerate(hard):
            for m in tgt_main(t):
                zh_items.append((i, m))
        zh_counts = mask_count(zh_items, text_zh, 'zh')
        for i, (s, t, n) in enumerate(hard):
            sc = en_counts.get(i, 0); tc = zh_counts.get(i, 0)
            flags = []
            if sc == 0:
                flags.append('★源0次(幽灵?)')
            elif tc == 0:
                flags.append('★译0次(未落位?)')
            elif sc >= 3 and tc < sc * 0.6:
                flags.append('落位偏低 %d/%d' % (tc, sc))
            for vm in re.findall(r'[“"「]([^”"」]{1,12})[”"」]', n):
                if re.search(r'[\u4e00-\u9fff]', vm) and vm not in t:
                    vc = len(re.findall(re.escape(vm), text_zh))
                    if vc:
                        flags.append('残留「%s」×%d' % (vm, vc))
            for vm in re.findall(r'([^\s（()），,、：:]{2,12})(?:已改|已归一|已统一)', n):
                if vm not in t:
                    vc = len(re.findall(re.escape(vm), text_zh))
                    if vc:
                        flags.append('残留「%s」×%d' % (vm, vc))
            extra = (' ' + ' '.join(flags)) if flags else ''
            P("     %-30s → %-20s 源×%-5d 译×%-5d%s" % (s[:30], t[:20], sc, tc, extra))


def main(argv):
    books = []
    if argv and argv[0] == '--all-in':
        with open(argv[1], encoding='utf-8') as f:
            books = [l.strip() for l in f if l.strip()]
    else:
        books = argv
    if not books:
        print(__doc__)
        return
    buf = io.StringIO()
    for b in books:
        precheck(b, buf)
    out = buf.getvalue()
    print(out)


if __name__ == '__main__':
    main(sys.argv[1:])
