import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
left, right, cnt = 0,0,0
infos = defaultdict(int)
ans = 0
while right<n:
    if infos[arr[right]]==0:
        cnt +=1
    infos[arr[right]]+=1
    while cnt>2:
        infos[arr[left]] -=1
        if infos[arr[left]]==0:
            cnt -=1
        left +=1
    ans = max(ans,right-left+1)
    right +=1
print(ans)