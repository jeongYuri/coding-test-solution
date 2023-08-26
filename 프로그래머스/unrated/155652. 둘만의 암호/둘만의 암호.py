def solution(s, skip, index):
    answer = ""  
    alpha = "abcdefghijklmnopqrstuvwxyz"   
    for word in skip: 
        if word in alpha:
            alpha = alpha.replace(word, "") 
    for i in s:
        change = alpha[(alpha.index(i) + index) % len(alpha)]
        answer += change
    
    return answer