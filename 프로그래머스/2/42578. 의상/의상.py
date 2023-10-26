def solution(clothes):
    answer = 1
    closet = {}
    for clothe in clothes:
        key = clothe[1]
        value = clothe[0]
        if key not in closet:
            closet[key] = [value]
        else:
            closet[key].append(value)
    for ck in closet.keys():
        answer = answer * (len(closet[ck])+1)
    return answer-1