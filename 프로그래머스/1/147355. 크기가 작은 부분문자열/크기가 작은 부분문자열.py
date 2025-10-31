def solution(t, p):
    cnt = 0
    n = len(p)
    for i in range(len(t) - n + 1):  
        if int(t[i:i+n]) <= int(p):
            cnt += 1
    return cnt