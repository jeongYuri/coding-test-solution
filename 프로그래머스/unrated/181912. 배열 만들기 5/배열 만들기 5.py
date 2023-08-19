def solution(intStrs, k, s, l):
    answer = []
    for i in intStrs:
        intS = i[s:s+l]
        if int(intS)>k:
            answer.append(int(intS))
    return answer