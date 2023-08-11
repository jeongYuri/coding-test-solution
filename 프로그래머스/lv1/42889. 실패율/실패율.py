def solution(N, stages):
    total = len(stages)
    count = {}
    for i in range(1,N+1):
        if total !=0:
            cnt = stages.count(i)
            fail = cnt/total
            count[i]= fail
            total -= cnt
        elif total ==0:
            count[i] = 0
    sorted_stage = sorted(count,key=lambda x:count[x] ,reverse =True )
    return sorted_stage