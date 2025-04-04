import sys
import math
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    a,b = map(int,input().split())
    res = math.lcm(a,b)
    print(res)
