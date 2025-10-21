import sys
input = sys.stdin.readline

s = input().strip()
p = input().strip()

n,m = len(s),len(p)
dp = [float('inf')] * (m+1)
dp[0] = 0

for i in range(m):
    for j in range(n):
        length = 0
        while j+length<n and i+length<m and s[j+length]==p[i+length]:
            length+=1
            dp[i+length] = min(dp[i+length],dp[i]+1)
print(dp[m])