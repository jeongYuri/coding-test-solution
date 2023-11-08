import sys,bisect
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = [sys.maxsize] * n

for i in range(0,n):
  idx = bisect.bisect_left(dp, arr[i])
  dp[idx] = arr[i]
print(bisect.bisect_left(dp, sys.maxsize))