#type define for binary
fire = 1        #炎
ice = 2         #氷
wind = 4        #風
lightning = 8   #雷
physical = 16    #物理
Quantum = 32     #量子
Imaginary = 64   #虚数

class charStatus:
    name = str
    type = 0
    level = 80
    Hitpoint = 0
    Speed = 0
    Attack = 0
    Defence = 0
    CritRate = 0
    CritDMG = 0
    BuffTakingDMG = 1
    SkillDMGRate = 0
    UltimateDMGRate = 0

    def AttackValue(self):
        return self.Attack

    def setJingliu(self):       #鏡流
        self.name = 'jingliu'
        self.type = ice
        self.Hitpoint = 1436
        self.Attack = 679
        self.Defence = 485
        self.Speed = 96
        self.SkillDMGRate = 5.0
        self.UltimateDMGRate = 6.0

    def setDanHeng_ILB(self):   #飲月君(Dan Heng - Imbibitor Lunae Build)
        self.name = 'DanHeng_ILB'
        self.type = Imaginary
        self.Hitpoint = 1241
        self.Attack = 698
        self.Defence = 363
        self.Speed = 102
        self.SkillDMGRate = 8.6
        self.UltimateDMGRate = 5.8

    def setSeele(self):         #ゼーレ
        self.name = 'Seele'
        self.type = Quantum
        self.Hitpoint = 931
        self.Attack = 640
        self.Defence = 363
        self.Speed = 115
        self.skillDMGRate = 2.2
        self.ultimateDMGRate = 4.25

    def setBlade(self):         #刃
        self.name = 'Blade'
        self.type = wind
        self.Hitpoint = 1436
        self.Attack = 679
        self.Defence = 485
        self.Speed = 96
        self.skillDMGRate = 0.72
        self.ultimateDMGRate = 0.72

    def setYanqing(self):       #チワワ(彦卿)
        self.name = 'Yanqing'
        self.type = ice
        self.Hitpoint = 892
        self.Attack = 679
        self.Defence = 4812
        self.Speed = 109
        self.skillDMGRate = 3.5
        self.ultimateDMGRate = 2.2

    def setArdenti(self):       #アルジェンティ
        self.name = 'Ardenti'
        self.type = physical
        self.Hitpoint = 1047
        self.Attack = 737
        self.Defence = 363
        self.Speed = 103
        self.skillDMGRate = 1.2
        self.ultimateDMGRate = 8.5