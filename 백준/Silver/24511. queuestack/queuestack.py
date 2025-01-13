import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
m = int(input())
c = list(map(int,input().split()))
qs = deque()
for i in range(n):
    if a[i] == 0:
        qs.append(b[i])
res =[]
for x in c:
    qs.appendleft(x)
    out = qs.pop()
    res.append(out)
print(*res)
