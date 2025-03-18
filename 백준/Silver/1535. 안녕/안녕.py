import sys
input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))
h = list(map(int, input().split()))
dp = [0] * 101
for i in range(n):
    for j in range(100, p[i], -1):  
        dp[j] = max(dp[j], dp[j - p[i]] + h[i])
print(max(dp))
