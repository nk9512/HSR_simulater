def addStatus(lightCone,char):
    char.HitPoint += lightCone.HitPoint
    char.Attack += lightCone.Attack
    char.Defence += lightCone.Defence

class LCStatus:
    name = 'str'
    HitPoint = 0
    Attack = 0
    Defence = 0

    def __init__(self) -> None:
        pass

    def set(self,char):
        if char.name == 'Jingliu':
            self.name = 'この身は剣なり'
            self.HitPoint = 1164
            self.Attack = 582
            self.Defence = 396
        
        addStatus(self,char)