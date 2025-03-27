import sys
input = sys.stdin.readline


def factorial(n,p):
    cnt = 0
    while n>=p:
        cnt += n//p
        n//=p
    return cnt
def zero(n,m):
    cnt_2 = factorial(n,2) - factorial(m,2)- factorial(n-m,2)
    cnt_5 = factorial(n,5) - factorial(m,5)- factorial(n-m,5)
    return min(cnt_2,cnt_5)

n,m  = map(int,input().split())

print(zero(n,m))