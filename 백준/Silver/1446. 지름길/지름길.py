import sys
input = sys.stdin.readline

n,d = map(int,input().split())
dp = [i for i in range(d+1)]

short = []

for _ in range(n):
    start, end, length = map(int,input().split())
    if end-start>length:
        short.append((start, end, length))
short.sort()

for start, end , length in short:
    for i in range(1,d+1):
        if end==i:
            dp[i] = min(dp[i],dp[start]+length)
        else:
            dp[i] = min(dp[i],dp[i-1]+1)
print(dp[d])