from itertools import permutations

def solution(k, dungeons):
    answer = 0
    for order in permutations(dungeons, len(dungeons)):
        fatigue = k     
        cnt = 0
        for need, cost in order:
            if fatigue >= need:
                fatigue -= cost
                cnt += 1
            else:
                break
        answer = max(answer, cnt)  
    return answer
