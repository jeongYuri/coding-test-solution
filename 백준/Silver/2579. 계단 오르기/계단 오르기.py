import sys
input = sys.stdin.readline

n = int(input())
dp = [0]* n
stair = [int(input().strip()) for _ in range(n)]
if n>0:
    dp[0] = stair[0]
if n>1:
    dp[1] = stair[0] + stair[1]
if n>2:
    dp[2] = max(stair[0]+stair[2],stair[1]+stair[2])
for i in range(3, n):
    dp[i] = max(dp[i-2] + stair[i], dp[i-3] + stair[i-1] + stair[i])
print(dp[-1])