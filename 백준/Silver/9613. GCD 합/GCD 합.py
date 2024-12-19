import sys
import math
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    nums = list(map(int,input().split()))
    total_gcd = 0
    for i in range(1,len(nums)):
        for j in range(i+1, len(nums)):
            total_gcd  += math.gcd(nums[i],nums[j])
    print(total_gcd)