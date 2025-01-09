import sys
input = sys.stdin.readline

n = int(input())
number = [float(input()) for _ in range(n)]
dp =[0.0]*n
dp[0] =  number[0]
ans = dp[0]
for i in range(n):
    dp[i] = max(number[i],dp[i-1]*number[i])
    ans = max(ans, dp[i])
print(f"{ans:.3f}")