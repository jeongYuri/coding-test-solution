import sys
import heapq
input = sys.stdin.readline
n,e = map(int,input().split())
graph = [[]for _ in range(n+1)]
INF = int(1e9)
for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
v1, v2 = map(int,input().split())

def dijkstra(start):
    dist = [INF]*(n+1)
    dist[start] = 0
    q = [(0,start)]

    while q:
        dis, node = heapq.heappop(q)
        if dist[node]<dis:
            continue
        for neighbor, weight in graph[node]:
            cost = dis+weight
            if cost<dist[neighbor]:
                dist[neighbor] = cost
                heapq.heappush(q,(cost, neighbor))
    return dist
d1 = dijkstra(1)
d_v1 = dijkstra(v1)
d_v2 = dijkstra(v2)
path1 = d1[v1] + d_v1[v2] + d_v2[n]
path2 = d1[v2] + d_v2[v1] + d_v1[n]

result = min(path1, path2)
print(result if result < INF else -1)