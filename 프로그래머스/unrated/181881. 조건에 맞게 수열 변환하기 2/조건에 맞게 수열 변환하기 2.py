def solution(arr):
    x = -1 
    change = True
    
    while change:
        change = False
        x += 1         
        for i in range(len(arr)):
            if arr[i] > 50 and arr[i] % 2 == 0:
                arr[i] /= 2
                change = True
            elif arr[i] < 50 and arr[i] % 2 != 0:
                arr[i] = arr[i] * 2 + 1
                change = True
    
    return x