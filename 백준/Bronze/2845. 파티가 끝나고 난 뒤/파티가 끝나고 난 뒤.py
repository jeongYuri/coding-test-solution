import sys
input = sys.stdin.readline
n,m = map(int,input().split())
nums = list(map(int,input().split()))
trust = n*m
ans = []
for i in range(5):
    ans.append(nums[i]-trust)
print(*ans)