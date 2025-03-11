import sys
input = sys.stdin.readline

n,m = map(int,input().split())
array = [list(map(int, input().split())) for _ in range(n)]
dp = [[[float('inf')] * 3 for _ in range(m)] for _ in range(n)]

for j in range(m):
    dp[0][j][0] = array[0][j]
    dp[0][j][1] = array[0][j]
    dp[0][j][2] = array[0][j]

for i in range(1,n):
    for j in range(m):
        if j > 0:
            dp[i][j][0] = min(dp[i - 1][j - 1][1], dp[i - 1][j - 1][2]) + array[i][j]
        dp[i][j][1] = min(dp[i - 1][j][0], dp[i - 1][j][2]) + array[i][j]
        if j < m - 1:
            dp[i][j][2] = min(dp[i - 1][j + 1][0], dp[i - 1][j + 1][1]) + array[i][j]

answer = float('inf')
for j in range(m):
    answer = min(answer, dp[n-1][j][0], dp[n-1][j][1], dp[n-1][j][2])

print(answer)


