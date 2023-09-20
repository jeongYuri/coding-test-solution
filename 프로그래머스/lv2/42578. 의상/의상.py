def solution(clothes):
    answer = 1
    closet = {}
    for clothe in clothes:
        key = clothe[1]
        value = clothe[0]
        if key in closet:
            closet[key].append(value)
        else:
            closet[key] = [value]
    for key in closet.keys():
        answer = answer * (len(closet[key]) +1)
    return answer -1
        