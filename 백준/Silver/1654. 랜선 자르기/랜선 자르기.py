import sys
input = sys.stdin.readline
k,n = map(int,input().split())
lensun = [int(input()) for _ in range(k)]
start, end = 1, max(lensun)
while start<= end:
    mid = (start+end)//2
    line = sum(i//mid for i in lensun)
    if line>=n:
        start = mid+1
    else:
        end = mid-1
print(end)