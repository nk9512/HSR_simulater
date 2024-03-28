# StarRail Theoritical & Max damage calculator
import characterStatus as CS
import enemyStatus as ES
import LightConeStatus as LS

Jingliu = CS.charStatus()
Jingliu.set('Jingliu')

print(Jingliu.Attack)

LCStatus = LS.LCStatus()
LCStatus.set('Jingliu')

print(Jingliu.Attack)

deer = ES.enemyStatus()
deer.set('deer')

def Crit_coefficient(char):
    return (char.CritDMG / 100) * (char.CritRate / 100)

def defence_coefficient(char, enemy):
    defence_through_rate = (enemy.debuffDefence + char.buffThroughDefence) / 100
    if defence_through_rate > 1:
        defence_through_rate = 1
    
    enemy_defence = (200 + 10 * enemy.level) * (1 - defence_through_rate)
    return 1 - (enemy_defence / (enemy_defence + 200 + 10 * char.level))

def registance_coefficient(char, enemy):
    if int(enemy.weekType / char.type) % 2 == 1:
        return 1 + (char.buffTypeThrough + enemy.debuffResistance) / 100
    
    if int(enemy.resistType / char.type) % 2 == 1:
        return 1 + (char.buffTypeThrough + enemy.debuffResistance) / 100 - 0.4
    
    return 1 + (char.buffTypeThrough + enemy.debuffResistance) / 100 - 0.2

def IsBreak(Is_Enemy_break):
    if Is_Enemy_break == True:
        return 1.0
    else:
        return 0.9

def SkillDMG(char, enemy, BaseAttack, BaseHP, BaseDefence):
    BaseDMG = 0
    if char.name == 'Jingliu':
        char.Attack += BaseAttack * 1.8
        char.CritRate += 0.5
        BaseDMG = char.Attack
    
    if char.name == 'DanHeng_ILB':
        char.BuffTakingDMG += 0.1
        char.CritDMG += 0.12
    
    Crit = Crit_coefficient(char)
    Defence_coefficient = defence_coefficient(char, enemy)
    Type_coefficient = registance_coefficient(char, enemy)
    Break_coefficient = IsBreak(enemy.IsBreak)
    
    BaseDMG * char.BuffTakingDMG * Crit * Defence_coefficient * Type_coefficient * Break_coefficient * enemy.debuffTakenDMG