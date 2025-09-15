import sys
input = sys.stdin.readline

n,k = map(int,input().split())
value = list(int(input().rstrip()) for _ in range(n))
dp = [float('inf')] * (k + 1)

dp[0] = 0

for c in value:
    for i in range(c, k+1):
        dp[i] = min(dp[i],dp[i-c]+1)
print(dp[k] if dp[k] != float('inf') else -1)