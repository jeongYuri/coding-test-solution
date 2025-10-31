def solution(d, budget):
    d.sort()
    cnt,total = 0,0
    for money in d:
        if total+money<=budget:
            total+=money
            cnt+=1
        else:
            break
    return cnt