class BF():

    # personality:性格，包含[温和程度，责任心，幽默感，是否有爱心]
    # hobby 习惯，包含是否爱吸烟喝酒，极度的为-3，以及是否爱唱歌绘画跳舞啥的
    # 初始值为0，表示标准值，负数为负值，正数为正值，有等级之分，一般为-3～+3之间，但如果达到某种程度，可能直接提前pass(return FALSE)
    # charming 魅力总值
    def __init__(self):

        self.personality = None
        self.appearence = 0
        self.weight = 0
        self.height = 0
        self.habby = 0
        self.caringbaby = 0
        self.sports = 0
        self.houseworking = 0
        self.money = 0

    def bfchosing(self, personality:list, appearance:int, weight:int, height:int, hobby:int, caringbaby:int, sports:int, houseworking:int, money:int):
        charming = 1000 #初始值

        # section 1:personality:-3~+3,分值-400～+500
        self.pncharming = 0
        if personality[0] < 0:  # 脾气不好的pass
            return False

        if personality[1] < 0:  # 没有责任心的pass
            return False

        if personality[2] == -3 or personality[3] == -3:  # 极度没有爱心和幽默感的pass
            return False

        for i in personality[0:2]:
            self.pncharming += i * 100  # 温和性格和责任心很重要哦
        for J in personality[2:]:
            if J<0:
                self.pncharming -= 100
            elif J>0:
                self.pncharming += 100  # 设置个最大值500,性格每人个根据自己实际需求进行调整
        if self.pncharming > 500:
            self.pncharming=500  #设置最大值500
        charming += self.pncharming


        # section 2:appearance:-3~+3，分值0～100
        if appearance == -3:  # 丑到极限pass
            return False
        if appearance > 0:
            charming += 100  # 咱不是外貌协会的，不管多好看只加100，一般丑的不加不减


        # section 3: weight:120~140，分值-100～+100
        if weight < 120:  # 体重小于120的,每少重10斤减100分值，最多扣100或加100
            if weight < 110:
                charming -= 100
        elif weight > 140:
            if weight > 150:
                charming -= 100  # 体重大于140的,每超重10斤减100分值
        # 体重正常范围不增不减


        # section4:height 175为界，分值-100～+100
        if height < 175:
            if height < 173:
                charming -= 100  # 小于175，每小2cm，减100分值
        else:
            if height > 177:
                charming += 100  # 大于175，每大2cm，加100分值


        # section5: hobby:-3~+3，分值100
        if hobby <= -2:
            return False  # 有较严重不良爱好，直接pass
        elif hobby >= 0:
            charming += 100  # 无不良爱好，加100


        # section6: caringbaby： -3～3，最大值200，分值-100～200
        self.cbcharming = 0
        if caringbaby > 0:
            self.cbcharming += caringbaby * 100
        elif caringbaby<0:  # 不会照顾孩子的通通减100
            self.cbcharming -= 100

        if self.cbcharming >= 200:
            self.cbcharming =200 #最大值200

        charming += self.cbcharming


        # section7：sports：-3～+3，分值100
        if sports > 0:
            charming += 100


        # section8: houseworking 做家务能力： -3～3 ;0代表家务平分，分值-100～300
        if houseworking <= -2 and money < 2:
            return False  # 不会做家务还很穷，直接pass
        else:
            charming += houseworking * 100


        # section9:money -3~=3 ,-3~3代表 大负债，中负债，小负债，平民，小康，中产，富裕。分值0～300
        if money < 0:
            return False  # 欠债养活不了自己的还是算了吧
        else:
            charming += money * 100

        self.charmvalue = charming

        if charming<1500: #小于1500，回炉重造.大家对我1500的设置是否合理呀？？？
            return False

        return charming

#charming在某个范围，可以根据实际需求进行变更哦



