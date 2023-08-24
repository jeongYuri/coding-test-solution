def solution(l, r):
    answer = []
    for num in range(l,r+1):
        if not set(str(num)) - set(['0', '5']):
            answer.append(num)
    if len(answer)==0:
        return [-1]
    return answer