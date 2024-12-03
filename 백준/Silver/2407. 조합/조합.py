import math
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
def nCm(n,r):
    return math.factorial(n)//(math.factorial(r)*math.factorial(n-r))
res = nCm(n,m)
print(res)