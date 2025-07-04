import sys
input = sys.stdin.readline

n  = int(input())
board = [list(map(int,input().split()))for _ in range(n)]

dp = [[0]*n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if i==j == n-1:
            print(dp[i][j])
            exit(0)
        dist = board[i][j]
        if i+dist<n:
            dp[i+dist][j] += dp[i][j]
        if j+dist<n:
            dp[i][j+dist] += dp[i][j]