def solution(arr, queries):
    answer = []
    for s,e,k in queries:
        hubo = [i for i in arr[s:e+1] if i>k]
        if hubo:
            answer.append(min(hubo))
        else:
            answer.append(-1)
    return answer