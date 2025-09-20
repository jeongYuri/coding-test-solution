import sys
input = sys.stdin.readline
from collections import Counter
n,k = map(int,input().split())
arr = list(map(int,input().split()))
cnt = Counter()

l = 0
ans = 0

for i in range(n):
    cnt[arr[i]]+=1
    while cnt[arr[i]]>k:
        cnt[arr[l]]-=1
        l+=1
    ans = max(ans, i-l+1)
print(ans)
