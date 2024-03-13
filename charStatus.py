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
    buffTakingDMG = 1
    buffThroughType = 0
    buffThroughDefence = 0
    SkillDMGRate = 0
    UltimateDMGRate = 0

    def set(self,name):
        if name == 'Jingliu':       #鏡流
            self.name = 'Jingliu'
            self.type = ice
            self.Hitpoint = 1436
            self.Attack = 679
            self.Defence = 485
            self.Speed = 96
            self.SkillDMGRate = 5.0
            self.UltimateDMGRate = 6.0
            
        if name == 'DanHeng_ILB':   #飲月君(Dan Heng - Imbibitor Lunae Build)
            self.name = 'DanHeng_ILB'
            self.type = Imaginary
            self.Hitpoint = 1241
            self.Attack = 698
            self.Defence = 363
            self.Speed = 102
            self.SkillDMGRate = 8.6
            self.UltimateDMGRate = 5.8
        
        if name == 'Seele':         #ゼーレ
            self.name = 'Seele'
            self.type = Quantum
            self.Hitpoint = 931
            self.Attack = 640
            self.Defence = 363
            self.Speed = 115
            self.skillDMGRate = 2.2
            self.ultimateDMGRate = 4.25

        if name == 'Blade':         #刃
            self.name = 'Blade'
            self.type = wind
            self.Hitpoint = 1436
            self.Attack = 679
            self.Defence = 485
            self.Speed = 96
            self.skillDMGRate = 0.72
            self.ultimateDMGRate = 0.72
        
        if name == 'Yanqing':       #チワワ(彦卿)
            self.name = 'Yanqing'
            self.type = ice
            self.Hitpoint = 892
            self.Attack = 679
            self.Defence = 4812
            self.Speed = 109
            self.skillDMGRate = 3.5
            self.ultimateDMGRate = 2.2

        if name == 'Ardenti':       #アルジェンティ
            self.name = 'Ardenti'
            self.type = physical
            self.Hitpoint = 1047
            self.Attack = 737
            self.Defence = 363
            self.Speed = 103
            self.skillDMGRate = 1.2
            self.ultimateDMGRate = 8.5
    
    def setAttack(self, Attack):
        self.Attack = Attack
    
    def setHP(self, HP):
        self.Hitpoint = HP
    
    def setDefence(self, Defence):
        self.Defence = Defence
    
    def setCrit(self, CritDMG, CritRate):
        self.CritDMG = CritDMG
        self.CritRate = CritRate
    
    def setSpeed(self, Speed):
        self.Speed = Speed