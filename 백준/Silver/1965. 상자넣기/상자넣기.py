import sys
input = sys.stdin.readline

n = int(input())
box= list(map(int,input().split()))
dp =[1]*n
res = 0
for i in range(n):
    for j in range(i):
        if box[j]<box[i]:
            dp[i] = max(dp[i],dp[j]+1)
print(max(dp))