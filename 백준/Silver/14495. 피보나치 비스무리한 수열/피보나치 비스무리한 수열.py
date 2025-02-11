import sys
input = sys.stdin.readline


def fibo(n):
    if n <= 3:
        return 1 

    res = [0] * (n + 1) 
    res[1] = res[2] = res[3] = 1

    for i in range(4, n + 1):
        res[i] = res[i - 1] + res[i - 3]  

    return res[n]


n = int(input())
print(fibo(n))



