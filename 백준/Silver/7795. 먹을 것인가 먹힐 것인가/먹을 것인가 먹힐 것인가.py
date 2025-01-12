import sys
from bisect import bisect_left

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b.sort()
    cnt = 0
    for i in range(n):
        cnt += bisect_left(b, a[i])
    print(cnt)
