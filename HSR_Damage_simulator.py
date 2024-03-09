# StarRail Theoritical & Max damage calculator
from HSR_simulater import charStatus as CS

Jingliu = CS.charStatus()
Jingliu.setJingliu()

print(Jingliu.Attack)

#enemy status define
enemy_week_type = 0
enemy_resist_type = 0
enemy_level = 90
Is_enemy_break = False

#buff define
buff_taking_damage = 0
buff_through_type = 0
buff_through_defence = 0

#debuff define
debuff_defence = 0
debuff_taken_damage = 0

def Crit_coefficient(Crit_damage, Crit_rate):
    return (Crit_damage / 100) * (Crit_rate / 100)

def defence_coefficient(character_level, enemy_level, debuff_defence, buff_through_defence):
    defence_through_rate = (debuff_defence + buff_through_defence) / 100
    if defence_through_rate > 1:
        defence_through_rate = 1
    
    enemy_defence = (200 + 10 * enemy_level) * (1 - defence_through_rate)
    return 1 - (enemy_defence / (enemy_defence + 200 + 10 * character_level))

def registance_coefficient(week_type, resist_type, character_type, buff_type_through):
    if int(week_type / character_type) % 10 == 1:
        return 1 + buff_type_through / 100
    
    if int(resist_type / character_type) % 10 == 1:
        return 1 + buff_type_through / 100 - 0.4
    
    return 1 + buff_type_through / 100 - 0.2

def IsBreak(Is_Enemy_break):
    if Is_Enemy_break == True:
        return 1.0
    else:
        return 0.9

def SkillDMG(self, BaseAttack, BaseHP, BaseDefence, IsBreak, EnemyType):
    if self.name == 'Jingliu':
        self.Attack += BaseAttack * 1.8
        self.CritRate += 0.5
    
    if self.name == 'DanHeng_ILB':
        self.BuffTakingDMG += 0.1
        self.CritDMG += 0.12