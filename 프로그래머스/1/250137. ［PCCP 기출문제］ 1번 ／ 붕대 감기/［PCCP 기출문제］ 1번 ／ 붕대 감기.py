def solution(bandage, health, attacks):
    t, x, y = bandage  
    max_health = health
    current_health = max_health
    continuity = 0 

    attack_dict = {time: damage for time, damage in attacks}

    for time in range(1, max(attack_dict.keys()) + 1):
        if time in attack_dict:
            current_health -= attack_dict[time]
            continuity = 0  
            if current_health <= 0:
                return -1  
        else:
            current_health += x
            current_health = min(current_health, max_health)  # Cap at max_health
            continuity += 1

            if continuity == t:
                current_health += y
                current_health = min(current_health, max_health)
                continuity = 0

    return current_health