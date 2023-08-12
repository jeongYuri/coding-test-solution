def solution(babbling):
    bab = ["aya","ye","woo","ma"]
    answer = 0
    for word in babbling:
        for text in bab:
            if text *2 not in word:
                word=word.replace(text,' ')
        if word.isspace():
            answer +=1
    return answer