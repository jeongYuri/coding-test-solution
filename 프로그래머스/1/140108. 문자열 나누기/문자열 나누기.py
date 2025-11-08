def solution(s):
    answer = 0
    same, diff = 0, 0    
    x = ''               

    for ch in s:
        if same == 0:   
            x = ch
            same = 1
            diff = 0
        else:
            if ch == x:
                same += 1
            else:
                diff += 1
        
        if same == diff:  
            answer += 1
            same, diff = 0, 0 

    if same != 0:
        answer += 1

    return answer
