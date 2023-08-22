def solution(arr):
    stk = []
    i=0
    while(len(arr)>i):
        if len(stk) == 0:
            stk.append(arr[i])
            i+=1
        elif len(stk) != 0 and stk[-1] < arr[i]:
            stk.append(arr[i])
            i+=1
        elif len(stk) != 0 and stk[-1] >= arr[i]:
            stk.remove(stk[-1])
    return stk
