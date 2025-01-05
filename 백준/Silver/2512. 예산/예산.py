import sys
sys.setrecursionlimit(2000)
input = sys.stdin.readline
n = int(input())
cost = list(map(int,input().split()))
m = int(input())

start,end = 0,max(cost)
res = 0
while start<=end:
    mid = (start+end)//2
    total = 0
    for c in cost:
        if c>mid:
            total += mid
        else:
            total +=c
    if total >m:
        end = mid-1
    else:
        res = mid
        start = mid+1
print(res)