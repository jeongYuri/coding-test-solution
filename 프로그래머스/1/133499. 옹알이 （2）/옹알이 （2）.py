def solution(babbling):
    answer = 0
    word = ["aya", "ye", "woo", "ma"]
    for b in babbling:
        temp = b
        valid = True
        for w in word:
            if w*2 in temp:
                valid = False
                break
        if not valid:
            continue
        for w in word:
            temp = temp.replace(w," ")
        if temp.strip()=="":
            answer+=1
    return answer