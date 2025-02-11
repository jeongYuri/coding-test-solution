import sys
import math
input = sys.stdin.readline

n = int(input())
left, right = 0, n
while left < right:
    mid = (left + right) // 2
    if mid * mid >= n:
        right = mid 
    else:
        left = mid + 1 

print(left)



