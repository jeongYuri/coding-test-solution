import heapq
import sys
input = sys.stdin.readline

ans, hab = 0,0
for i in range(10):
    hab+= int(input())
    if 100-ans>= abs(100-hab):
        ans = hab
print(ans)

