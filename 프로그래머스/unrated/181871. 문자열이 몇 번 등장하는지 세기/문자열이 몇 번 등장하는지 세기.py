def solution(myString, pat):
    cnt = 0
    for i in range(len(myString)):
        if myString[i:].startswith(pat):
            cnt +=1
    return cnt
