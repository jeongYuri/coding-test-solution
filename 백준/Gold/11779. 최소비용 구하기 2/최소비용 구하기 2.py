import heapq
import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
city = [[]for _ in range(n+1)]
for _ in range(m):
    s,e,c = map(int,input().split())
    city[s].append((e,c))
start, end = map(int,input().split())
INF = float('inf')
dist = [INF]*(n+1)
prev = [0]*(n+1)
dist[start] = 0
heap = [(0,start)]

while heap:
    cost,now = heapq.heappop(heap)
    if dist[now]<cost:
        continue
    for nxt, nxt_cost in city[now]:
        new = cost+nxt_cost
        if new<dist[nxt]:
            dist[nxt] = new
            prev[nxt] = now
            heapq.heappush(heap,(new,nxt))
path = []
cur = end
while cur!=0:
    path.append(cur)
    cur = prev[cur]
path.reverse()
print(dist[end])
print(len(path))
print(*path)