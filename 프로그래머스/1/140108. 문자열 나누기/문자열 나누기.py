def solution(s):
    answer = 1
    start = s[0]
    same = 0
    differ = 0
    
    for i in s:
        if differ != 0 and same ==differ:
            answer +=1
            same, differ = 0,0
            start = i
        if start==i:
            same +=1
        else:
            differ +=1
    
        
    return answer