import sys
import math
input = sys.stdin.readline
def lcm(a,b):
    return a//math.gcd(a,b)*b
n = int(input())
for _ in range(n):
    a,b = map(int,input().split())
    res = lcm(a,b)
    print(res)

