def solution(k, tangerine):
    answer = 0
    dic = {}
    for a in tangerine:
        if a in dic:
            dic[a]+=1
        else:
            dic[a]=1
    for v in sorted(dic.values(), reverse = True):
        k -=v
        answer +=1
        if k<=0:
            break
    return answer