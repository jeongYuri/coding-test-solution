def solution(array):
    answer = 0
    cnt = {}
    for ar in array:
        if ar not in cnt:
            cnt[ar] = 1
        else:
            cnt[ar]+=1
    max_val = max(cnt.values())
    answer = None
    for k in cnt:         
        if cnt[k] == max_val:
            if answer is None:
                answer = k
            else:
               
                return -1

    return answer