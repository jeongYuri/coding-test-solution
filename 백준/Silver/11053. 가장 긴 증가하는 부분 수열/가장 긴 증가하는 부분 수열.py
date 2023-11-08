import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = [1]*n

for cur in range(1,n):
  for j in range(cur):
    if arr[j]<arr[cur]:
      dp[cur] = max(dp[cur],dp[j]+1)
print(max(dp))
      