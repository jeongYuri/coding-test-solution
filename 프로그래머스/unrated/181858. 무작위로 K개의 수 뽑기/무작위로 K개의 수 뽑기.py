def solution(arr, k):
    answer = []
   
    for i in arr:
        if len(answer)<k and i not in answer:
            answer.append(i)
    while len(answer) < k:
            answer.append(-1)
            
    return answer