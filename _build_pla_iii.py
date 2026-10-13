# -*- coding: utf-8 -*-
# 构建 iii.zh-CN.md：原文行从源文件逐字复制，译文按块对照插入
import sys

SRC = r'C:\Users\HanTi\Desktop\translate\翻译项目\percy-marks_the-plastic-age\原文\iii.md'
DST = r'C:\Users\HanTi\Desktop\translate\翻译项目\percy-marks_the-plastic-age\译文\iii.zh-CN.md'

src = open(SRC, encoding='utf-8').read()
assert '\r' not in src, 'source has CR'
lines = src.split('\n')
if lines and lines[-1] == '':
    lines = lines[:-1]
# 行索引（0 起）：0=标题## III, 1..23=段1..23, 24=---, 25..36=段24..35
title = lines[0] + ' / 第三章'
paras = lines[1:24] + lines[25:37]  # 35 段，逐字保留
sep_idx = 24  # --- 位于段23与段24之间（段号 1..23 前半，24..35 后半）

T = []
T.append('接下来那几天，卡尔（Carl）和休（Hugh）几乎什么也没干，光排队了。他们排队注册；排队缴学费；排队同卡尔弗校长（President Culver）握手；排队同新生教务长进行两分钟十足无用的谈话；排队等候在公共食堂里分派座位。卡尔提议，他和休睡前也到书房里排一回队，免得手生。然后，他们还不得不去听各科教师轮番登台开讲，讲大学的习俗、大学的礼数、大学的荣誉、大学的一切一切。听到第六场，休已是身心俱疲、稀里糊涂，便问卡尔，他如今对大学究竟是个什么东西，可算有点概念了没有。')
T.append('“是的，”卡尔回答，“这是一所专为乖男孩们开办的淑女学校。”')
T.append('“唉，”休绝望地说，“要是再听上两场这种高尚得不得了的演讲，我就要去买醉了。我有一种预感：大学根本不是这些老家伙说的那副样子。反正我希望不是。”')
T.append('“当然不是。我说，何必再等那两场该死的玩意儿来要你的命？”他从书桌抽屉里掏出一只小酒瓶，殷勤地递了过来。')
T.append('休笑了。“这可是你自己说的，那玩意儿是猫尿，打什么赌你都不肯喝。再说，你知道我滴酒不沾。我还指望挣上一枚校名首字母徽章呢，可得保持状态。”')
T.append('“说的是。只可惜不知道该拿这瓶毒药怎么办。要是把它搁在这儿，管楼的老太婆准会翻出来，那时候就只有求上帝保佑咱们了。我告诉你吧：今晚天黑以后，咱们把它带下去，毒一毒亲爱的老印第安湖（Indian Lake）的湖水。”')
T.append('“行啊。对了，我得赶紧走了；我跟导师约好了。但愿不用排队。”')
T.append('队是不用排了——人家还准许他坐——可他足足等了一个半钟头。终于，一个学生从里间办公室走了出来，里面一个粗哑的嗓音喊道：“下一个！”')
T.append('“简直跟理发店一个样。”休走进那间小办公室时，这个念头在脑中一闪而过。')
T.append('一张办公桌后面坐着一个少年老成的男人，正翻弄着文件。休进来时，他抬眼瞟了一下，朝身旁的一把椅子摆了摆手。休坐下，盯着自己的脚。')
T.append('“嗯，让我看看。你的名字是——什么来着？”')
T.append('“卡弗，先生。休·卡弗（Hugh Carver）。”')
T.append('导师凯恩教授（Professor Kane）瞟了一眼几页记录。“哦，是了，梅里敦高中（Merrytown High School）毕业，学历完备合格。你打算读文学士（A.B.）还是理学士（B.S.）？”')
T.append('“我——我不知道。”')
T.append('“读理学士，得修一年大学拉丁文；读文学士，除此之外还得至少修两年希腊文。”')
T.append('“哦！”休又惊又乱。他知道父亲是文学士，可他听高中校长说过，如今希腊文一点用处也没有。他猛然记起来了：校长劝他读理学士；校长说那更实用。')
T.append('“我看我还是读理学士吧。”他小声说。“很好。”凯恩教授到这时还没有看过休一眼，拿起一张选课卡。“有中间名吗？”他突兀地问。')
T.append('“有的，先生——默雷迪思（Meredith）。”')
T.append('凯恩在卡片顶端潦草地写下 H. M. Carver，接着便飞快地填了起来。他把所用符号匆匆解释了一遍，可是对课程本身只字未提。填完选课单，他又把它誊到另一张卡上，一张递给休，另一张插进了卡片盒。')
T.append('“还有别的事吗？”他问道，头一回把那张淡金头发、木然无表情的脸转向了休。')
T.append('休站起身来。他有一打问题想问。“没有了，先生。”他答道。“那么，很好。我是你的常任导师。需要帮助时就到我这里来。再见。”')
T.append('“再见，先生。”休走出门去，那个粗哑的嗓音随即吼道：“下一个！”离门最近的男孩起身走进了这方圣殿。')
T.append('休走到露天里，盯着卡片上那些象形文字直发愣。“我猜它们总归有些意思，”他暗自思忖，“可我怎么才能弄明白呢？”一阵突如其来的恐惧使他脸色发白。“我笃定会走错地方。哦，老天爷！”')
T.append('接着，高年级学生到了，差不多有七百人。安静的校园顿时变成了一个激荡着欢呼与问候的疯人院。“嗨，杰克。暑假过得好吗？”……“好啊，汤姆，老伙计，见你回来我真是太高兴啦。”……“把手伸过来，老哥们儿；见到你真是太好了。”到处都是同一套问候：“暑假过得好吗？欢迎回来。”人人彼此直呼其名；人人握手握得出奇地起劲，往往同时还攥住对方的胳膊。这些家伙在校园里转来转去，好不趾高气扬！他们既不心慌，也不胆怯；他们知道该怎么办。')
T.append('休头一回感到一阵思乡的刺痛；头一回，他意识到自己还不算大学里的一员。他紧紧粘着卡尔，还有萨里堂（Surrey）里另外一两个新近攀熟的男孩；卡尔也紧紧粘着休，小心掩饰着自己心里那种渺小怯懦的感受。头一回，*他*意识到自己不过是个新生——而他不喜欢这样。')
T.append('后来，酝酿了一天上下的紧张气氛突然爆发了。高年级学生传下号令，要全体新生戴上娃娃帽——一种缀着鲜亮橙色纽扣的傻里傻气的蓝色小帽。从那一刻起，每个新生都在劫难逃。干活就是他们的命，而且有的是活儿。“喂，新生，把我的箱子搬上去。对，说你呢，新生——就你那两条细腿。你，还有你那位胖朋友，把我的箱子搬到四楼去——要是摔了，我就拧断你们这两个蠢货的脖子。”……“新生！到车站去把我的手提箱取来。喏，取件牌。识相就快去快回。”……“新生！上二十八号楼（Hill Twenty-eight）去，把床拼装起来。”……“新生！到我房间来。我要你挂画。”')
T.append('幸而这份苦役为期不长，可在干着的当儿，休被支使得团团转，前所未有。而他乐在其中。他爱他那顶缀着橙色纽扣的蓝帽子；他爱那些管他叫新生、差他遣去的高年级学生；他连自己吭哧吭哧搬上楼的那些箱子都爱。他得到了承认——诚然，只是被当作一名杂役，但到底是承认了；他终于成了桑福德学院（Sanford College）的一分子。更有甚者：有一个把他支使得最凶的人，别着一枚纽德尔塔（Nu Delta）徽章——那是他父亲当年兄弟会的标志。他为那个人跑腿跑得又快又心甘情愿，结果那位英雄断定，这个新生“非常非常蠢”。')
T.append('当天夜里，休和卡尔坐在萨里堂 19 号房里歇他们酸痛的骨头，一个坐长沙发，一个坐皮面的莫里斯椅（Morris chair）。')
T.append('“真够来劲的，是不是？”休说，舒舒服服地伸展着四肢。')
T.append('“来劲个鬼！他们这算什么路数？”')
T.append('“别理会；明年就轮到咱们发号施令了。”')
T.append('“可不是，”卡尔斩钉截铁地说，点上一支烟，“到时候瞧我让那帮小新生跑断腿。”他环顾房间，一脸心满意足。“嘿，咱们这地方够俏的，是不是？”')
T.append('休也赞羡地四下打量。墙壁几乎被遮了个严实：几面锦旗，一条巨大的桑福德毛毯——这是休最大的贡献——卡尔的凯恩毛毯，“后宫”佳丽的照片，大学运动员和电影泳装女郎的海报，几只烟斗架，还有三幅马克斯菲尔德·帕里什（Maxfield Parrish）的版画。')
T.append('“这可真不赖，”休自豪地说。“咱们就差一根理发店的转花柱和一块路名牌了。”')
T.append('“不出这个星期，就把它们弄到手。”这话斩钉截铁。')

assert len(T) == 35, f'译文段数 {len(T)} != 35'

# 块分组（源段号 1..35，闭区间）
groups = [(1, 5), (6, 9), (10, 13), (14, 18), (19, 23), (24, 27), (28, 32), (33, 35)]

out = [title, '']
for gi, (a, b) in enumerate(groups):
    out.append('===Original===')
    for i in range(a - 1, b):
        out.append('')
        out.append(paras[i])
    out.append('')
    out.append('===Chinese===')
    for i in range(a - 1, b):
        out.append('')
        out.append(T[i])
    out.append('')
    # 场景分隔符：源段 23 与 24 之间
    if b == 23:
        out.append('---')
        out.append('')

text = '\n'.join(out).rstrip('\n') + '\n'
with open(DST, 'w', encoding='utf-8', newline='\n') as f:
    f.write(text)

# 自检 1：原文块段落与源逐字一致
import re
MARK = re.compile(r'^={3,}\s*(original|chinese)\s*={0,}\s*$', re.IGNORECASE)
cur, buf, orig_blocks, zh_blocks = None, [], [], []
for ln in text.split('\n'):
    m = MARK.match(ln)
    if m:
        if cur == 'original':
            orig_blocks.append([p for p in '\n'.join(buf).strip().split('\n\n') if p])
        if cur == 'chinese':
            zh_blocks.append([p for p in '\n'.join(buf).strip().split('\n\n') if p])
        cur, buf = m.group(1).lower(), []
        continue
    buf.append(ln)
if cur == 'original':
    orig_blocks.append([p for p in '\n'.join(buf).strip().split('\n\n') if p])

flat = [p for blk in orig_blocks for p in blk]
print('Original 块数:', len(orig_blocks), '| Chinese 块数:', len(zh_blocks))
print('Original 段落总数:', len(flat))
assert flat == paras, '原文块与源段不一致！'
# 场景分隔符被吸入第 5 个中文块，剔除后核对中文段数
zh_flat = []
for bi, blk in enumerate(zh_blocks):
    if bi == 4 and blk and blk[-1].strip() == '---':
        blk = blk[:-1]
    zh_flat.extend(blk)
print('Chinese 段落总数:', len(zh_flat))
assert len(zh_flat) == 35, '译文段数不对'

# 自检 2：特殊字符计数（原文区）
import collections
src_cnt = collections.Counter(ch for ch in src if ord(ch) > 127)
dst_orig = '\n\n'.join(flat)
do_cnt = collections.Counter(ch for ch in dst_orig if ord(ch) > 127)
print('特殊字符（源 vs 译文原文区）:')
for ch in sorted(set(src_cnt) | set(do_cnt), key=ord):
    s, d = src_cnt.get(ch, 0), do_cnt.get(ch, 0)
    flag = 'OK' if s == d else '!!MISMATCH!!'
    print(f'  U+{ord(ch):04X} {s} vs {d} {flag}')
assert src_cnt == do_cnt, '特殊字符计数不一致'
# 自检 3：无 BOM、LF、无制表符/NBSP 混入
raw = open(DST, 'rb').read()
assert not raw.startswith(b'\xef\xbb\xbf'), 'BOM!'
assert b'\r' not in raw, 'CRLF!'
assert b'\t' not in raw and b'\xc2\xa0' not in raw.replace(b'\xe2\x80\x8a', b'') , 'tab or NBSP!'
print('写入完成:', DST, len(raw), 'bytes')
