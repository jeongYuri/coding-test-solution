def solution(babbling):
    answer = 0
    bab = ["aya", "ye", "woo", "ma" ]        
    for b in babbling:
        for word in bab:
            if word*2 not in b:
                b = b.replace(word,' ')
        if b.isspace():
            answer +=1
    return answer