def solution(arr):
    cnt = 0
    n = len(arr)
    k = bin(n)
    if (n&(n-1))!=0:
        return arr + [0]*(2**(len(k)-2) - len(arr))
    else:
        return arr
        
    