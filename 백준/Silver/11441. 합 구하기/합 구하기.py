import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
m = int(input())
prefix =[0] *(n+1)
for i in range(1,n+1):
    prefix[i] = prefix[i-1]+nums[i-1]
for _ in range(m):
    i,j = map(int,input().split())
    hab = prefix[j] -prefix[i-1]
    print(hab)
