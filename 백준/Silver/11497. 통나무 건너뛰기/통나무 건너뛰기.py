import sys
input = sys.stdin.readline
from collections import deque
t = int(input())
while t:
    t-=1
    n = int(input())
    length = list(map(int,input().split()))
    length.sort()
    dq = deque()

    for i in range(n):
        if i%2==0:
            dq.appendleft(length[i])
        else:
            dq.append(length[i])
    res = 0
    for i in range(len(dq)):
        diff = abs(dq[i]-dq[(i+1)%(len(dq))])
        res = max(diff,res)
    print(res)

