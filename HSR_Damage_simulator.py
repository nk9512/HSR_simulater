# StarRail Theoritical & Max damage calculator
fire = 0
ice = 1
wind = 2
physic = 3

def registance_coefficient(week_attribute, resist_attribute, character_attribute):
    
    attribute_registance = 1 - 
    
    return attribute_registance

def Theoritical_damage_calc(base_multiplar, attack_power, crit_damagactere, crit_rate, buff_damage, coefficient_of_defence, coefficient_of_registance, bool_break):
    base_damage = attack_power * base_multiplar
    
    crit_damage /= 100
    crit_rate /= 1
    Theoritical_of_crit = 1 + crit_damage * crit_rate
    
    character_damage = base_damage * Theoritical_of_crit * buff_damage
    Theoritical_damage = character_damage * coefficient_of_registance
    return Theoritical_damage

Crit_damage = 210
Crit_rate = 35
Attack_power = 2250
base_multiplar = 0

buff_damage = 48.8

debuff_defence = 0
debuff_registace = 0

defensive_value = 0

Theoritical_damage_calc(base_multiplar, Crit_damage,Crit_rate,Attack_power,buff_damage,defensive_value,debuff_defence,debuff_registace)