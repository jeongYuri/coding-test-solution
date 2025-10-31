def solution(arr, divisor):
    answer = []
    for n in arr:
        if n%divisor==0:
            answer.append(n)
    answer.sort()
    if len(answer)==0:
        return [-1]
    else:
        return answer