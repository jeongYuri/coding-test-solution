import sys
sys.setrecursionlimit(2000)
input = sys.stdin.readline
def factorial(num):
    if num ==0 or num==1:
        return 1
    else:
        return num*factorial(num-1)
n,k = map(int,input().split())
res = (factorial(n)//(factorial(n-k)*factorial(k)))
print(res%10007)

