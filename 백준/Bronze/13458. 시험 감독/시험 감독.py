import sys
import math
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
b, c = map(int, input().split())
res = 0
for i in range(n):
    res += 1  
    if nums[i] > b:
        res += math.ceil((nums[i]-b)/c) 
print(res)
