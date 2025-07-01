import sys
input = sys.stdin.readline
import heapq
INF = int(1e9)
v_cnt,e_cnt = map(int,input().split())
k = int(input())

graph = [[]for _ in range(v_cnt+1)]
dist = [INF]*(v_cnt+1)
for _ in range(e_cnt):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))

def digkstra(k):
    q = []
    heapq.heappush(q,(0,k)) #거리, 정점
    dist[k] = 0
    
    while q:
        di, now = heapq.heappop(q)
        if di>dist[now]:
            continue
        for neighbor, weight in graph[now]:
            cost = di+weight
            if cost<dist[neighbor]:
                dist[neighbor] = cost
                heapq.heappush(q,(cost,neighbor))
digkstra(k)

for i in range(1,v_cnt+1):
    if dist[i]==INF:
        print('INF')
    else:
        print(dist[i])
