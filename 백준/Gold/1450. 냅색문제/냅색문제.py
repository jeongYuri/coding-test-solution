import sys
input = sys.stdin.readline
from bisect import bisect_right
n,c = map(int,input().split())
weight = list(map(int,input().split()))

mid = n//2
left = weight[:mid]
right = weight[mid:]

def get_subsums(arr):
    subsum = [0]
    for a in arr:
        subsum+=[a+s for s in subsum]
    return subsum

left_s = get_subsums(left)
right_s = get_subsums(right)
right_s.sort()

cnt = 0
for s in left_s:
    idx = bisect_right(right_s, c-s)
    cnt += idx

print(cnt)