import sys
input = sys.stdin.readline

INF = 10**15
n = int(input())
dp = [[0] * n for _ in range(n)]

hang = []
for _ in range(n):
    r, c = map(int, input().split())
    hang.append((r, c))

for length in range(1, n):  # 구간 길이
    for i in range(n - length):  # 시작점
        j = i + length
        min_val = INF
        for k in range(i, j):  # 분할점
            cost = dp[i][k] + dp[k+1][j] + hang[i][0] * hang[k][1] * hang[j][1]
            if cost < min_val:
                min_val = cost
        dp[i][j] = min_val

print(dp[0][n-1])
