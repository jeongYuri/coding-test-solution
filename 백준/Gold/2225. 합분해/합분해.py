import sys
input = sys.stdin.readline

n,k = map(int,input().split())

MOD = 1000000000

dp = [[0]*(n+1) for _ in range(k+1)]
for j in range(n+1):
    dp[1][j] = 1
for i in range(2,k+1):
    for j in range(n+1):
        for l in range(j+1):
            dp[i][j] = (dp[i][j]+dp[i-1][j-l])%MOD

for i in range(2,k+1):
    for j in range(n+1):
        if j==0:
            dp[i][j] = 1
        else:
            dp[i][j] = (dp[i-1][j]+dp[i][j-1])%MOD

print(dp[k][n])
