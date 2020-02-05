from bf import BF

#实验数据，在这里输入男生的各种数据哦
# 依次输入
# personality：数组：[性格温和程度，责任心，幽默感，爱心]，取值范围 -3～3，0是标准值（一般值），越高越好，以下同理
# appearence：外貌，取值范围 -3～3
# weight：体重，输入体重（斤）
# height ：身高，输入身高（cm）
# habby ：爱好，取值范围 -3～3
# caringbaby：照顾baby能力，取值范围 -3～3
# sports：爱好运动程度，取值范围 -3～3
# houseworking：做家务能力，取值范围 -3～3
# money：经济能力，取值范围 -3～3

person1=BF()
person2=BF()
person1.bfchosing([0,2,0,2],2,144,172,2,1,0,0,1) #俺爸为例，基本合格，charming=1600
person2.bfchosing([2,2,0,1],1,140,175,1,1,0,1,1) #我的大概标准，2000

PERSON=[person1,person2]

for i in PERSON:
    print('魅力分值 charming value：',i.charmvalue)

