def solution(elements):
    answer = set()
    n = len(elements)
    elements += elements[:-1]
    for limit in range(1,n+1):
        for i in range(n):
            answer.add(sum(elements[i:i+limit]))
    return len(answer)