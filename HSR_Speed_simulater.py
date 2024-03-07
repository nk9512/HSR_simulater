

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
            print(character_name[0],round)
        if Supporter_AP >= 10000:
            Supporter_AP = 0
            acted_count[1] += 1
            print(character_name[1],round)
            if character_name[1] == "花火":
                Attacker_AP += 5000
            if character_name[1] == "ブローニャ":
                Attacker_AP += 10000
            if Attacker_AP >= 10000:
                Attacker_AP = 0
                acted_count[0] += 1
                print(character_name[0],round)
    print(character_name[0],acted_count[0])
    print(character_name[1],acted_count[1])

def main(Attacker_name, Attacker_speed, supporter_name, supporter_speed, round):
    name = [str,str]
    speed = [float,float]
    
    name[0] = Attacker_name
    speed[0] = Attacker_speed
    name[1] = supporter_name
    speed[1] = supporter_speed
    
    speed_simulate(speed,name,round)

main("鏡流",135,"花火",134,1) 