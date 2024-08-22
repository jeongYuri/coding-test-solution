import sys
input = sys.stdin.readline
def count(k, n):
    dp = [[0] * (n + 1) for _ in range(k + 1)]
    for i in range(1, n + 1):
        dp[0][i] = i
    for i in range(1, k + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[k][n]

tc = int(input().strip())
results = []

for _ in range(tc):
    k = int(input().strip())
    n = int(input().strip())
    results.append(count(k, n))

for result in results:
    print(result)
