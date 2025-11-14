def solution(babbling):
    answer = 0
    words = ["aya", "ye", "woo", "ma"]
    for bab in babbling:
        for word in words:
            if word*2 == bab:
                break
            if word==bab:
                answer+=1
                break
            if word in bab:
                bab = bab.replace(word, '.')
        if set(bab) == {'.'}:
            answer += 1
    return answer