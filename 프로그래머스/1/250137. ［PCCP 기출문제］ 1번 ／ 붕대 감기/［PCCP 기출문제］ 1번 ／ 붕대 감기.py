def solution(bandage, health, attacks): #bandage는 붕대감기, health는 최대 체력, attacks는 몬스터
    t, h, p = bandage
    max_health = health
    current_health = max_health
    conti = 0
    
    attack_dict = {time:damage for time, damage in attacks}
    
    for time in range(1, max(attack_dict.keys())+1):
        if time in attack_dict:
            current_health -= attack_dict[time]
            conti = 0
            if current_health<=0:
                return -1
        else:
            current_health += h   
            current_health = min(current_health, max_health)
            conti +=1
            
            if conti == t:
                current_health += p
                current_health  = min(current_health, max_health)
                conti = 0
    return current_health
    