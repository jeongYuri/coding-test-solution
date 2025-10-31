def solution(clothes):
    closet = {}
    for name, kind in clothes:
        closet[kind] = closet.get(kind, 0) + 1

    answer = 1
    for kind in closet:
        answer *= (closet[kind] + 1)

    return answer - 1