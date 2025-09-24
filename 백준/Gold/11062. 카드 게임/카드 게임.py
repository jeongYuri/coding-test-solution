import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    cards = list(map(int, input().split()))
    dp = [[0]*n for _ in range(n)]
    if n%2 == 1:
        for i in range(n):
            dp[i][i] = cards[i]
    for l in range(2, n+1):
        for i in range(n-l+1):
            j = i+l-1
            if l%2 == n%2:
                dp[i][j] = max(cards[i] + dp[i+1][j], cards[j] + dp[i][j-1])
            else:
                dp[i][j] = min(dp[i+1][j], dp[i][j-1])
    print(dp[0][n-1])