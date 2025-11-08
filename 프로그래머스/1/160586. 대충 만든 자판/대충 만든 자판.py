def solution(keymap, targets):
    answer = []
    d ={}
    for key in keymap:
        for i,ch in enumerate(key):
            if ch not in d or d[ch]>i+1:
                d[ch]  = i+1
    for target in targets:
        total = 0
        for ch in target:
            if ch not in d:
                total =-1
                break
            total+= d[ch]
        answer.append(total)
    return answer