def solution(array, commands):
    answer = []
    for comd in commands:
        ary = array[comd[0]-1:comd[1]]
        ar1 = sorted(ary)
        ar2 = ar1[comd[2]-1]
        answer.append(ar2)
    return answer


