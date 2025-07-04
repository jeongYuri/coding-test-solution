import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int,input().split()))for _ in range(n)]

direction = [(1,0),(0,1)]
dp = [[0]*n for _ in range(n)]

dp[0][0] = 1

for x in range(n):
    for y in range(n):
        if x==y==n-1:
            print(dp[x][y])
            exit(0)
        dist = board[x][y]
        if x+dist<n:
            dp[x+dist][y] += dp[x][y]
        if y+dist<n:
            dp[x][y+dist]+= dp[x][y]