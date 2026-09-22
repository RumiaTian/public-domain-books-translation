# -*- coding: utf-8 -*-
# 第十二章 12-xii.md 双语对照构建脚本：Original 块自源文程序化提取（字节保真），Chinese 块为译文。
SRC = r"原文/12-xii.md"
OUT = r"译文/12-xii.zh-CN.md"

lines = open(SRC, encoding="utf-8").read().split("\n")
assert lines[0] == "## XII"
assert lines[-1] == "" and len(lines) == 13

# (起始行, 结束行) 0-based 含端点；zh 为对应译文段列表
BLOCKS = [
    (1, 4, "The Earl of Emsworth sat", [
        "埃姆斯沃思伯爵坐在病床边，望着尊贵的弗雷迪，目光几乎称得上温柔。",
        "「我怕是，弗雷迪，我亲爱的孩子，这一回叫你受了大大的惊吓。」",
        "「呃？什么？是啊——可不！吓了个半死，老爸。」",
        "「我把这事通盘想过了，我的孩子，从前待你，我也许狠了点儿。等你脚踝一好，我决定恢复你的零用钱；你也可以回伦敦去，你在这乡下似乎过得并不快活。虽说天下凡是明白事理的人，怎么会更喜欢——」",
    ]),
    (5, 7, "started, popeyed", [
        "尊贵的弗雷迪一惊，眼珠子瞪得溜圆，一骨碌坐起身来。",
        "「我的老天！真格的？」",
        "他的父亲点了点头。",
    ]),
    (8, 11, "you really are a topper", [
        "「我说，老爸，你可真是个头等的大好人！真真是，你知道！你对乡下那份心思，我全明白——那些可爱的老鸟儿啊、老树啊，还有把那些该死的鼻涕虫从小天竺葵上撵下去啊，诸如此类；可不知怎么，这一套始终就没照样打动过我。大概我天生就是这路料。我喜欢柏油大街、人堆儿、躲出租汽车、上俱乐部会老兄们，再顺脚溜进帝国剧场（the Empire）耗上半个钟头，等等等等。还有，领零用钱这事，有那么股说不出的劲儿——我说不上来……总归是叫你挺起胸膛，觉得自己是个人物。我不知道怎么谢你才好，老爸！你——你真是个顶呱呱的痛快人！这是你这辈子办过的最漂亮的一桩事。我觉得自己像匹两岁口的小马。都不记得几时这么提气过了。我——我——真的，你知道，老爸，我真是感激得没治了。」",
        "「正是，」埃姆斯沃思勋爵说。「啊——不错。不过，弗雷迪，我的孩子，」他又添了一句，语调不无凄楚，「还有最后一件小事。你看，你是不是能够——费上一把劲——看在我的份上——这回努力别把自己变成——变成一个该死的大傻瓜？」",
        "他眼巴巴地望着自己的骨血。",
        "「老爸，」尊贵的弗雷迪斩钉截铁地说，「我保管痛痛快快地搏它一把！」",
    ]),
]

parts = ["## XII / 第十二章\n"]
for start, end, anchor, zh in BLOCKS:
    src_paras = lines[start:end + 1]
    assert anchor in src_paras[0], (start, anchor)
    assert all(p.strip() for p in src_paras)
    assert len(src_paras) == len(zh), (start, len(src_paras), len(zh))
    parts.append("===Original===\n" + "\n\n".join(src_paras) + "\n\n===Chinese===\n" + "\n\n".join(zh) + "\n")

with open(OUT, "w", encoding="utf-8", newline="\n") as f:
    f.write("\n".join(parts))
print("written", OUT)
