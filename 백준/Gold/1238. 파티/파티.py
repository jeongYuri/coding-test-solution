import sys
input = sys.stdin.readline
import heapq
INF = int(1e9)
n,m,x = map(int,input().split())

graph = [[]for _ in range(n+1)]
reverse_graph = [[]for _ in range(n+1)]

for _ in range(m):
    s,e,t = map(int,input().split())
    graph[s].append((e,t))
    reverse_graph[e].append((s,t))#역방향

def dijkstra(start, graph):
    distance = [INF]*(n+1)
    distance[start] = 0
    q = [(0,start)]

    while q:
        dist, now  = heapq.heappop(q)
        if distance[now]<dist:
            continue
        for next_node, weight in graph[now]:
            new_dist = dist+weight
            if new_dist<distance[next_node]:
                distance[next_node] = new_dist
                heapq.heappush(q,(new_dist,next_node))
    return distance
go = dijkstra(x,graph)
back = dijkstra(x,reverse_graph)
res = 0

for i in range(1,n+1):
    total = go[i]+back[i]
    res = max(res,total)
print(res)
