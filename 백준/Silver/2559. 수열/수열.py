import sys
input = sys.stdin.readline

n,k = map(int,input().split())
date = list(map(int,input().split()))

sums = sum(date[:k])
ans = sums
for i in range(k,n):
    sums += date[i] - date[i - k]
    ans = max(ans, sums)
print(ans)