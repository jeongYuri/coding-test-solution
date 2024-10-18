from collections import defaultdict

def solution(weights):
    answer = 0
    weights.sort()
    count_map = defaultdict(int)
    
    for weight in weights:

        answer += count_map[weight]       
        count_map[weight] += 1
        if weight % 2 == 0:
            count_map[(weight // 2) * 3] += 1
        if weight % 3 == 0:
            count_map[(weight // 3) * 4] += 1
        count_map[weight * 2] += 1
    
    return answer