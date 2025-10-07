import sys
import math
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    print(int(math.isqrt(n)))