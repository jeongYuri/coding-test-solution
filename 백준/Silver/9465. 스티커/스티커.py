import sys
input = sys.stdin.readline
t = int(input()) #테스트케이스

for _ in range(t):
    n = int(input()) #정수의 수
    dp = [list(map(int,input().split())) for _ in range(2)]
    if n>1:
        dp[0][1]+=dp[1][0]
        dp[1][1]+=dp[0][0]
    for i in range(2,n):
        dp[0][i]+=max(dp[1][i-1],dp[1][i-2])
        dp[1][i]+=max(dp[0][i-1],dp[0][i-2])
    print(max(dp[0][n-1],dp[1][n-1]))
