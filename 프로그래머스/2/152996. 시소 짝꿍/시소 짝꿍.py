from collections import Counter
def solution(weights):
    answer = 0
    cnt =Counter(weights)
    for k, v in cnt.items():
        if v>1:
            answer += v *(v-1)//2
        
    weights = list(set(weights))
    for item in weights:
        for check in (3/4, 2/3,2/4):
            if item * check in weights:
                answer += cnt[item] *cnt[item*check]
    return answer