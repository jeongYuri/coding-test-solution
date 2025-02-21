import sys
input = sys.stdin.readline
MOD = 1000000009

n, m = map(int, input().split())
grid = [input().strip() for _ in range(n)]

dp = [[0] * m for _ in range(n)]
dp[n - 1][m - 1] = 1

for i in range(n - 1, -1, -1):
    for j in range(m - 1, -1, -1):
        if i == n - 1 and j == m - 1:
            continue

        char = grid[i][j]
        if char == 'E':
            if j + 1 < m:
                dp[i][j] = dp[i][j + 1]
        elif char == 'S':
            if i + 1 < n:
                dp[i][j] = dp[i + 1][j]
        elif char == 'B':
            right_val = dp[i][j + 1] if j + 1 < m else 0
            down_val = dp[i + 1][j] if i + 1 < n else 0
            dp[i][j] = (right_val + down_val) % MOD

ans = 0
for i in range(n):
    for j in range(m):
        ans = (ans + dp[i][j]) % MOD
print(ans)

