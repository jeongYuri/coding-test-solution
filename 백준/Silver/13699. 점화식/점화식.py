import sys
input = sys.stdin.readline

n = int(input())
dp = [0]*(n+1)
dp[0] = 1
for k in range(1,n+1):
    for i in range(k):
        dp[k]+= dp[i]*dp[k-i-1]
print(dp[n])