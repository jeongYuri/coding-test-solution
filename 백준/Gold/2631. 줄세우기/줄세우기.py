import sys
input = sys.stdin.readline

n = int(input())
child = list(int(input().rstrip())for _ in range(n))
dp= [1]*(n+1)

for i in range(n):
    for j in range(i):
        if child[j]<child[i]:
            dp[i] = max(dp[i],dp[j]+1)
print(n-max(dp))