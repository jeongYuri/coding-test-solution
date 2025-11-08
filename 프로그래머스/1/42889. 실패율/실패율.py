from collections import Counter
def solution(n, stages):
    answer = []
    length = len(stages)
    count = Counter(stages)
    
    for stage in range(1,n+1):
        if length == 0:
            answer.append((stage,0))
        else:
            fail = count[stage]/length
            answer.append((stage, fail))
            length -= count[stage]
    answer.sort(key = lambda x:(-x[1],x[0]))
    return [stage for stage, _ in answer]