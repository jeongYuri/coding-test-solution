import sys
input = sys.stdin.readline
import math
import heapq
sys.setrecursionlimit(10 ** 8)
n = int(input())
star = []
for i in range(n):
    x,y = map(float,input().split())
    star.append((x,y))

memo = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        memo[i][j] = math.sqrt((star[i][0] - star[j][0])**2 + (star[i][1]-star[j][1])**2)
sums = 0
visited = set()
mh = []
heapq.heappush(mh,(0,0))

while len(visited)<=n-1:
    cost, cur = heapq.heappop(mh)
    if cur in visited:
        continue
    visited.add(cur)
    sums+=cost
    for to in range(n):
        if cur != to and to not in visited:
            heapq.heappush(mh,(memo[cur][to],to))
print(f"{sums:.2f}")