def speed_simulate(character_speed, character_name, range_round):
    Attacker_AP = 0
    Supporter_AP = 0
    acted_count = [0,0]
    
    round_count = 50 + range_round * 100
    
    for round in range(round_count):
        Attacker_AP += character_speed[0]
        Supporter_AP += character_speed[1]
        if Attacker_AP >= 10000:
            Attacker_AP = 0
            acted_count[0] += 1
            print(character_name[0])
            print(round)
        if Supporter_AP >= 10000:
            Supporter_AP = 0
            acted_count[1] += 1
            print(character_name[1],round)
            if character_name[1] == 'sparkle':
                Attacker_AP += 5000
            if character_name[1] == 'bronya':
                Attacker_AP += 10000
            if Attacker_AP >= 10000:
                Attacker_AP = 0
                acted_count[0] += 1
                print(character_name[0],round)
    print(character_name[0],acted_count[0])
    print(character_name[1],acted_count[1])

def main():
    name = [str,str]
    speed = [float,float]
    
    Attacker_name = 'Jingliu' #鏡流
    Attacker_speed = 136
    supporter_name = 'sparkle' #花火
    supporter_speed = 134
    
    name[0] = Attacker_name
    speed[0] = Attacker_speed
    name[1] = supporter_name
    speed[1] = supporter_speed
    
    speed_simulate(speed,name,1)

main() 