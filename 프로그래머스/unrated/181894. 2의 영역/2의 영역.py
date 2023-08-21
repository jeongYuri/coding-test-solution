def solution(arr):
    start = -1
    end = -1
    for i,num in enumerate(arr):
        if num==2:
            start = i if start == -1 else start
            end = i
    if start == -1:
        return [-1]
    else:
        return arr[start:end+1]
    