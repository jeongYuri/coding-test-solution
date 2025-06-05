import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
memo = {}
def fibo(n):
    if n in  memo:
        return memo[n]
    if n==0:
        memo[0] = 0
    elif n==1:
        memo[1] = 1
    else:
        memo[n] = fibo(n-1)+fibo(n-2)
    return memo[n]

t = int(input())
print(fibo(t))




