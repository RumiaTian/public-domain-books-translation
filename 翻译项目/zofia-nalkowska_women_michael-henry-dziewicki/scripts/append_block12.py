#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

path = r'C:\Users\HanTi\OneDrive\translate\翻译项目\zofia-nalkowska_women_michael-henry-dziewicki\译文\the-garden-of-red-flowers_part1.zh-CN.md'

content = """
===Original===
In his love-affairs, Wiazewski is just as fickle and as insatiable as Imszanski; but their "spheres of influence" are different. Wiazewski has a liking for seamstresses, shop-assistants, and so forth; whereas Imszanski is specially interested in cocottes (even his intrigue with Madame Wildenhoff is a case in point). Neither of the two has any great liking for the other, in spite of their mutually courteous bearing at all times. Imszanski has against my friend that he is too democratic: whereas Wiazewski looks on Imszanski as a fool.

The latter explains his dislike for demimondaines thus:

"I have a great liking for misdeeds, but not when committed by professional criminals."

The art of playing with his victims has been brought by him to the acme of perfection. To this end, he employs what naturalists call "mimicry." His features being rather common, he has no trouble in putting a girl off her guard; he makes up as a commercial man, or a lackey, or a waiter; and in such parts he expresses himself most eloquently in the slang of those classes, which he has picked up to perfection.

He is a thorough expert in the art of getting into touch with the minds of such people; and the ease with which he finds his way through a labyrinth of ideas quite unknown to us is truly admirable.

On principle, he is for continual change; but latterly he has been making an exception, and declares he has hit upon the right sort, or nearly so. For some time he has been "keeping company" with a girl, whom he has, on account of her exceptional qualities, distinguished from the common herd. I once saw her at his lodgings and was struck with her good looks.

He has been reading a letter from her today. I asked him to give it to me as a "document," which he very readily consented to do.

It runs thus:

===Chinese===
在情事方面，维亚泽夫斯基和伊姆尚斯基一样反复无常、永不餍足；但他们的"势力范围"不同。维亚泽夫斯基喜欢裁缝女工、女店员之类；而伊姆尚斯基则特别对风尘女子感兴趣（甚至他与维尔登霍夫夫人的私情就是一例）。两人对彼此都没有太多好感，尽管始终保持着彬彬有礼的姿态。伊姆尚斯基对我的朋友不满，认为他太民主了；而维亚泽夫斯基则视伊姆尚斯基为傻瓜。

后者这样解释他对风尘女子的厌恶：

"我非常喜欢恶行，但不喜欢职业罪犯犯下的恶行。"

他玩弄猎物的艺术已经被他臻于完美的境地。为此目的，他运用了博物学家所谓的"拟态"。他的相貌颇为普通，他毫不费力地便能让一个女孩放下戒备；他装扮成一个商人，或者一个仆从，或者一个侍者；在这些角色中，他以这些阶层的行话雄辩地表达自己——那是他完美地学来的。

他是与这类人的心灵建立联系的艺术的真正行家；他在我们完全陌生的思想迷宫中穿行自如的那份从容，确实令人钦佩。

原则上，他主张不断变换；但最近他却破例了，并宣称自己已经找到了合适的人选，或至少差不多了。有一段时间他一直在和一个女孩"交往"，他因为她的出众品质而将她与芸芸众生区别开来。我有一次在他的住所见过她，被她的美貌所打动。

他今天在读她的一封来信。我请他把信给我作为"文献"，他很爽快地答应了。

信的内容如下：
"""
with open(path, 'a', encoding='utf-8') as f:
    f.write(content)
print('Block 12 appended')
