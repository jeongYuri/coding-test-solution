def solution(citations):
    answer = 0
    citations.sort(reverse = True)
    for i,non in enumerate(citations):
        if non>=i+1:
            answer = i+1
        else:
            break
    return answer