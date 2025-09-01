import sys
import heapq
input = sys.stdin.readline
n,k = map(int, sys.stdin.readline().split())
jew = []
for _ in range(n):
    heapq.heappush(jew,list(map(int,input().split())))

bags = []
for _ in range(k):
    bags.append(int(input()))

bags.sort()

ans = 0
tmp = []

for bag in bags:
    while jew and bag >= jew[0][0]:
        pop_item = heapq.heappop(jew)
        heapq.heappush(tmp, -pop_item[1])
    if tmp:
        ans -= heapq.heappop(tmp)
    elif not jew:
        break

print(ans)