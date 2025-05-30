import sys
input = sys.stdin.readline

a,k = map(int,input().split())
dp = [0] * (k+1)

for num in range(a,k):
    if num+1 <=k and (dp[num+1]==0 or dp[num+1]>dp[num+1]):
        dp[num+1] = dp[num]+1
    if num*2 <=k and (dp[num*2]==0 or dp[num*2]>dp[num+1]):
        dp[num*2] = dp[num]+1
print(dp[k])

