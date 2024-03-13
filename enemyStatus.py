fire = 1        #炎
ice = 2         #氷
wind = 4        #風
lightning = 8   #雷
physical = 16    #物理
Quantum = 32     #量子
Imaginary = 64   #虚数

class enemyStatus:
    name = str
    level = 90
    weekType = 0
    resistType = 0
    debuffDefence = 0
    debuffTakenDMG = 0
    debuffResistance = 0
    IsBreak = False

    def set(self,str):
        if str == 'deer':         #鹿
            self.name = 'deer'
            self.weekType = fire + ice + Quantum
            return 'deer'
    
    def breaking(self):
        self.IsBreak = True
    
    def setLevel(self,level):
        self.level = level