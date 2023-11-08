import sys,bisect
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = [1] * n

for cur in range(1,n):
  for front in range(cur):
    if arr[front]<arr[cur]:
      dp[cur] = max(dp[cur],dp[front]+1)
print(max(dp))
length = max(dp)
answer = []
for i in range(n-1,-1,-1):
  if dp[i]==length:
    answer.append(arr[i])
    length -=1
answer.reverse()
for i in answer:
  print(i, end=' ')