import sys
input = sys.stdin.readline
n = int(input())
dp= [0]*11
dp[1] = 0
dp[2] = 1

for i in range(3,n+1):
    for j in range(1,i//2+1):
        dp[i] = max(dp[i],j*(i-j)+dp[j]+dp[i-j])
print(dp[n])