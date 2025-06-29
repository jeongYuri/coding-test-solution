import sys
input = sys.stdin.readline

n,k = map(int,input().split())
p = 1000000007

def factorial(n):
    result = 1
    for i in range(2, n+1):
        result = (result * i) % p
    return result


def square(n,k):
    if k==0:
        return 1
    elif k==1:
        return n

    tmp = square(n,k//2)
    if k % 2:
        return tmp * tmp * n % p
    else:
        return tmp * tmp % p

top = factorial(n)
bot = factorial(n-k) * factorial(k)%p
print(top*square(bot,p-2)%p)