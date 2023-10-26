def solution(array, commands):
    answer = []
    for com in commands:    
        arra = array[com[0]-1:com[1]]
        arr1  = sorted(arra)
        arr2 = arr1[com[2]-1]
        answer.append(arr2)
    return answer
   