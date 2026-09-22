import re

def translate(text):
    # Normalize: remove zero-width spaces, normalize dashes, strip whitespace
    # We also remove the backlink symbol if present
    clean = text.replace('\ufeff', '').replace('—', '—').strip()
    if clean.endswith('↩︎'):
        clean = clean[:-1].strip()
    if clean.endswith('↩'):
        clean = clean[:-1].strip()
        
    translations = {
        "From our experience of over a quarter of a century, writing rhymes on local subjects, we find they are preserved more carefully, and are more impressed on people’s minds than prose articles on the same subjects. This has induced us to compile this little volume. Please accept this apology. —The Author":
            "根据我们二十多年来撰写关于本地题材韵文的经验，我们发现这些韵文比同类题材的散文文章保存得更为仔细，也更深入人心。这促使我们汇编了这本小书。请接受我们的歉意。——作者",
        "The oration on the above interesting occasion was delivered by the late Hon. William H. Merritt, projector of the Welland Canal. He served at the battle when a young man. We witnessed the interesting ceremony and shall never forget it. —The Author":
            "上述有趣场合的演讲由已故尊敬的威廉·H·梅里特先生发表，他是威兰运河的发起人。他在年轻时参加过那场战役。我们见证了那场感人的仪式，永远不会忘记。——作者",
        "The nurls and birds’ eyes and curls were highly prized in furniture thirty years ago, when we used the smooth plain.":
            "三十年前，当人们使用光滑的素面时，旋钮、鸟眼纹和卷纹在家具中备受珍视。",
        "James Noxon, Mayor.":
            "詹姆斯·诺克森，市长。",
        "Tom Moore paddled his own canoe along the Canadian shore of Lake Erie and was enraptured with the view. He landed and remained over night at a farm house. His “Canadian Boat Song” is immortal.":
            "汤姆·摩尔划着自己的独木舟沿着伊利湖的加拿大海岸航行，被那里的景色迷住了。他上岸并在一间农舍过夜。他的《加拿大船歌》是不朽的。",
        "The valley of the Thames we presume includes Stratford on the north and Woodstock and Ingersoll on the south. The Avon, on whose banks Stratford is located, joins the Thames near St. Mary’s. The middle branch flows throngh Embro and Thamesford, the south and middle branches unite and flow through Dorchester and Westminster and blend with the northern branch at London, where it deviates to Elgin in the south.":
            "我们推测泰晤士河谷包括北部的斯特拉特福以及南部的伍德斯托克和英格索尔。斯特拉特福所在的埃文河在圣玛丽附近汇入泰晤士河。中间支流流经恩布罗和泰姆斯福德，南部和中部支流汇合，流经多切斯特和威斯敏斯特，并在伦敦与北部支流汇合，随后向南转向埃尔金。",
        "Some imagine the Thames is too insignificant a stream to be sung in verse. “Distance lends enchantment to the view,” and they fancy the old Scottish rivers are more worthy of song; but many of them are polluted of late years with vile odors from factories; and, as the county of Oxford is agreeably diversified with hills and dales, the clear, sparkling stream, flowing over a pebbly bottom, is indeed “a thing of beauty and a joy forever.”":
            "有些人认为泰晤士河是一条太微不足道的小溪，不值得在诗中歌颂。‘距离给景色增添了魅力’，他们幻想古老的苏格兰河流更值得歌颂；但近年来，其中许多河流都被工厂排出的恶臭污染了；而牛津郡的山峦和幽谷错落有致，景色宜人，这条清澈、波光粼粼的溪流流经布满卵石的河底，确实是‘美的事物，也是永恒的喜悦’。",
        "Among the earliest champions of the Factory System of making cheese were Messrs. Chadwick, Casswell and Ballantyne. The North Oxford Company were awarded the highest honor at the Centennial Exhibition. Messrs. J. L. Grant & Co. have a fine large cold storage warehouse on the G.T.R., and the C.P.R. have erected one on their line, which is leased by Mr. Riley. Ingersoll being the great dairy centre of Ontario it was deemed requisite to have those facilities for preserving the cheese in the hot season. The following is a list of the most prominent cheese factories in this district and the salesmen thereof:":
            "查德威克、卡斯韦尔和巴兰坦先生是奶酪工厂制度最早的倡导者。北牛津公司在百年博览会上获得了最高荣誉。J. L. 格兰特公司在大干线铁路沿线拥有一座大型冷藏仓库，加拿大太平洋铁路公司也在其线路上建立了一座，由赖利先生租赁。英格索尔作为安大略省重要的乳制品中心，拥有这些设施对于在炎热季节保存奶酪是必要的。以下是该地区最著名的奶酪工厂及其销售员名单：",
        "Dereham and West Oxford—W. Nancekivell.":
            "迪勒姆和西牛津——W. 南斯基维尔。",
        "Harris Street—T. R. Mayberry.":
            "哈里斯街——T. R. 梅伯里。",
        "W. Oxford—G. Galloway.":
            "西牛津——G. 盖洛韦。",
        "N. Oxford—D. J. Dundass.":
            "北牛津——D. J. 邓达斯。",
        "Maple Leaf—Thomas Caddy.":
            "枫叶——托马斯·卡迪。",
        "W. Zorra—John Blair.":
            "西佐拉——约翰·布莱尔。",
        "Burnside—H. George.":
            "伯恩赛德——H. 乔治。",
        "Gore—H. C. Hopkins.":
            "戈尔——H. C. 霍普金斯。",
        "Salford—Foster & Gregg.":
            "索尔福德——福斯特与格雷格。",
        "Mt. Elgin—W. Tripp.":
            "埃尔金山——W. 特里普。",
        "Brownsville—Hopkins & Fulton.":
            "布朗斯维尔——霍普金斯与富尔顿。",
        "Prouse’s—T. Prouse.":
            "普劳斯——T. 普劳斯。",
        "Kintore—G. Alderson.":
            "金托尔——G. 奥尔德森。",
        "Harrietsville—R. Facey.":
            "哈里茨维尔——R. 费西。",
        "East Nissouri—W. J. Walker.":
            "东尼索里——W. J. 沃克。",
        "Cold Springs—H. Matheson.":
            "寒泉——H. 马西森。",
        "Dorchester—L. D. Monk.":
            "多切斯特——L. D. 蒙克。",
        "Lawson—N. Wilford.":
            "劳森——N. 威尔福德。",
        "Wilkinson—J. H. Wilkinson.":
            "威尔金森——J. H. 威尔金森。",
        "Dereham and Norwich Union—W. Fewster.":
            "迪勒姆与诺里奇联合——W. 尤斯特。",
        "Verschoyle—James Hunter.":
            "弗舒尔——詹姆斯·亨特。",
        "Avon and Firby—W. Kirkly.":
            "埃文与弗比——W. 柯克利。",
        "Thamesford—F. Patterson.":
            "泰姆斯福德——F. 帕特森。",
        "Lyons—James Mitchell.":
            "莱昂斯——詹姆斯·米切尔。",
        "Lakeside—T. Marshall.":
            "湖滨——T. 马歇尔。",
        "Belmont—John Evans.":
            "贝尔蒙特——约翰·埃文斯。",
        "Cherry Hill—H. Webster.":
            "切里山——H. 韦伯斯特。",
        "Grand Master Brigade Col. Moffat, of London.":
            "伦敦旅长莫法特上校。",
        "Mrs. Traill lives near Peterboro. Mrs. Moody died in Toronto. I sent her a copy of my poems in 1885, and she thanked me for the same through a friend as she was in feeble health at the time.":
            "特雷尔夫人住在彼得伯勒附近。穆迪夫人在多伦多去世。1885年，我寄给她一本我的诗集，她当时身体虚弱，通过一位朋友向我表示感谢。",
        "Niagara, once the capital and business centre of Upper Canada, and also an important fortress. It is located at the mouth of the Niagara River.":
            "尼亚加拉，曾是上加拿大的首府和商业中心，也是一座重要的要塞。它位于尼亚加拉河口。",
        "A flock of geese, by there loud cackle in the midst of a dark night, saved the city of Rome from being captured by the Barbarians.":
            "一群鹅在黑暗的夜晚发出响亮的鸣叫声，使罗马城免于被野蛮人占领。",
        "Mrs. Mary McKay McLeod, the author of some fine poems on Scottish and Canadian subjects.":
            "玛丽·麦凯·麦克劳德夫人，创作了一些关于苏格兰和加拿大题材的优秀诗歌。",
        "John Sandfield McDonald.":
            "约翰·桑德菲尔德·麦克唐纳。",
        "Sir John A. McDonald, Canada’s most celebrated statesman.":
            "约翰·A·麦克唐纳爵士，加拿大最著名的政治家。",
        "We have been congratulated by many on the truthfullness of the “Canadian Romance.” They declare it is not a romance but a true picture of rise and progress of worthy industrious people in Canada.":
            "许多人称赞《加拿大传奇》的真实性。他们宣称这不是传奇，而是对加拿大值得尊敬的勤劳人民兴起与进步的真实写照。",
        "Mathew Arnold saw fit to say that Longfellow was not the National Poet of America, but we presume few believed him; one of Longfellow’s grandest pieces, the scene is set in Canada.":
            "马修·阿诺德竟然说朗费罗不是美国的民族诗人，但我们相信很少有人相信他；朗费罗最伟大的作品之一，场景设定在加拿大。",
        "Alas, the reapers and mowers have displaced the Bonnie Lasses in the fields, 1884.":
            "唉，收割者和割草者已经取代了田野里的漂亮姑娘们，1884年。",
        "The Royal Stuarts are owners of large estates on the banks of the Findhorn and their great rivals were near by the Royal Comyns. The Lion Hunter Gordon Comyn was of this stock. Professor J. S. Blockie has written a fine poem on the wars of the rival houses. “Mere where the dark water’d stream rushes free child of the mountain.”":
            "皇家斯图亚特家族在芬德河畔拥有大片地产，而他们伟大的对手皇家科明家族就在附近。‘猎狮人’戈登·科明就是这个家族的成员。J. S. 布洛克教授为这两大家族的战争创作了一首优美的诗。\n“唯有在那里，深色的水流如大山的自由之子般奔腾。”",
        "Lord Rae, chief of the clan McKay. The family formerly owned large estates in Sutherland, which they lost. The present Lord Rae was born in Holland, and he married a rich lady with an estate near Edinbursh. He is one of the foremost scientific men in Britain at the present time, and he frequently presides at assemblies both in London and Edinburgh for the advancement of education and science.":
            "雷勋爵，麦凯家族的首领。该家族以前在萨瑟兰拥有大片地产，后来失去了。现任雷勋爵出生于荷兰，他娶了一位在爱丁堡附近拥有地产的富有的女士。他是目前英国最杰出的科学家之一，并经常在伦敦和爱丁堡主持旨在促进教育和科学发展的集会。",
        "Mr. T. D. Millar has just secured, Sept., 1884, the first prize for cheese at the great cheese fair at Amsterdam, Holland. They weighed over 600 pounds each, and were manufactured by the burnside Factory of Dorchester. The Galloway Factory is manufacturing several cheese weighing one ton each. The mammoth cheese, alluded to in cheese ode, was manufactured by Mr. Tames Harris, Ingersoll Factory. The Dunn Cheese Factory, North Oxford, secured first prize at the great Centennial Exhibition, but where all factories produce such excellent cheese perhaps it would be making invidious distinctions to specify the honours won by any particular factory. The West Oxford Company have recently built a fine factory on the Culloden Road.":
            "T. D. 米勒先生于1884年9月在荷兰阿姆斯特丹举行的大型奶酪博览会上刚刚获得奶酪一等奖。这些奶酪每块重达600多磅，由多切斯特的伯恩赛德工厂制造。盖洛韦工厂正在制造几块重达一吨的奶酪。歌词颂歌中提到的巨大奶酪是由英格索尔工厂的詹姆斯·哈里斯先生制造的。北牛津的邓恩奶酪工厂在百年博览会上获得了一等奖，但由于所有工厂都生产如此优质的奶酪，指明任何特定工厂所获得的荣誉也许是不公平的区别对待。西牛津公司最近在卡洛登路建造了一座精美的工厂。",
        "Entwining of the thistle around the maple tree, Scotia’s sons have indented their names deep in Canadian history. The names of McDonald, McKenzie, Cameron and Mowat stand conspicuous, and Brown second to none. For wealth, enterprise and benevolence those Montreal Scotsmen stand high, Sir Donald A. Smith, Sir George Stephens and Duncan McIntyre.":
            "蓟花环绕枫树，苏格兰的儿子们将他们的名字深深地刻在加拿大的历史中。麦克唐纳、麦肯齐、卡梅伦和莫瓦特的名字格外醒目，而布朗也不遑多让。在财富、进取心和仁慈方面，这些蒙特利尔苏格兰人地位崇高，如唐纳德·A·史密斯爵士、乔治·斯蒂芬斯爵士和邓肯·麦金泰尔。",
        "The most celebrated lady traveller in Britain is Miss Cumming, a niece of the Lion Hunter. She has written several volumes of her travels in distant lands.":
            "英国最著名的女性旅行家是卡明小姐，她是‘猎狮人’的侄女。她写了好几卷关于她在远方土地旅行的书。",
        "Battle of the Thames won by American Cavalry.":
            "泰晤士河战役由美国骑兵赢得。",
        "Woodstock hath now breadth as well as length.":
            "伍德斯托克现在既有广度也有长度。",
        "Dick was both a geologist and botanist and was of great service to Hugh Millar.":
            "迪克既是一位地质学家也是一位植物学家，他对休·米勒帮助很大。",
        "Edward is a shoemaker by trade, remarkable for his knowledge of the lower grades of animated nature.":
            "爱德华是一名鞋匠，以对低级生物界的了解而闻名。",
        "Mr. Stanley Simpson.":
            "斯坦利·辛普森先生。",
        "Mr. James Sinclair of this town has written a fine piece remonstrating against the removal of the sword of Wallace from its old place of safety, Dunbarton Castle.":
            "本镇的詹姆斯·辛克莱先生写了一篇优秀的文章，反对将华莱士之剑从其古老的安身之所——丹巴顿城堡移走。",
        "According to E. A. Poe the Albatross sleeps in air.":
            "根据爱伦·坡的说法，信天翁在空中睡眠。",
        "See Coleridge’s Ancient Mariner for the calamity befell a crew for wantonly killing this bird.":
            "参见柯勒律治的《古舟子咏》，讲述了一群船员因肆意杀害这只鸟而遭遇的灾难。",
        "Though we have described the above cheese as mighty, yet it did not contain a single mite. The late Daniel Pheisan took a deep interest in the great cheese, and in promoting cheese factories, he became wealthy and died in Woodstock. Mr. Robert Facy was the cheesemaker at Mr. Harris, Factory the time when the big cheese was made.":
            "虽然我们将上述奶酪描述为巨大，但它并没有包含一只小虫（mite，双关语，既指‘微小’也指‘小虫’）。已故的丹尼尔·费桑对这种巨大的奶酪以及推广奶酪工厂深感兴趣，他变得富有并在伍德斯托克去世。罗伯特·费西先生是哈里斯先生工厂的奶酪制造者，当时正是制造巨型奶酪的时候。",
        "The above factory is now the North Oxford Company’s.":
            "上述工厂现在属于北牛津公司。",
        "That enterprising Scotsman, Duncan McIntyre, of Montreal, was the first enthusiastic promoter of the above mine, and in conjunction with Sir D. A. Snuth and Sir George, now Lord, Mount Steven, built the C.P. Railway.":
            "那位富有进取心的苏格兰人，蒙特利尔的邓肯·麦金泰尔，是上述矿山第一位热心的推动者，他与D. A. 史密斯爵士和乔治爵士（现为史蒂文勋爵）共同修建了加拿大太平洋铁路。",
        "James Sutherland, M.P., re-elected at Buffalo, June, 1891.":
            "詹姆斯·萨瑟兰，议员，于1891年6月在布法罗再次当选。",
        "The executioner was Radcliff.":
            "刽子手是拉德克利夫。"
    }
    return translations.get(clean, "Translation not found")

with open("C:\\Users\\HanTi\\OneDrive\\translate\\翻译项目\\james-mcintyre_poetry\\原文\\endnotes.md", "r", encoding="utf-8") as f:
    content = f.read()

# Remove the first line "## Endnotes"
content = content.replace("## Endnotes", "", 1)

# Split by "- " which marks each note
notes = re.split(r'\n- \s*\n', content)
notes = [n.strip() for n in notes if n.strip()]

output = "## Endnotes / 尾注\n\n"
for note in notes:
    # Clean up the note text (remove multiple spaces/newlines)
    clean_note = re.sub(r'\s+', ' ', note).strip()
    
    # Remove the back-link symbol (Leftwards Arrow with Hook + Variation Selector)
    if '↩' in clean_note:
        clean_note = clean_note.split('↩')[0].strip()
        
    cn = translate(clean_note)
    
    output += f"===Original===\n\n- \n\n{clean_note} ↩︎\n\n===Chinese===\n\n- \n\n{cn} ↩︎\n\n"

with open("C:\\Users\\HanTi\\OneDrive\\translate\\翻译项目\\james-mcintyre_poetry\\译文\\endnotes.zh-CN.md", "w", encoding="utf-8") as f:
    f.write(output)

print("Translation completed.")
