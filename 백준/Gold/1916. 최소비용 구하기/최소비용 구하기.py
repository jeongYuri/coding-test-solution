import sys
import heapq
input = sys.stdin.readline
n = int(input())
m = int(input())
INF = int(1e9)

def dijstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, node = heapq.heappop(q)
        if distance[node]<dist:
            continue
        for city, cost in graph[node]:
            new_cost = dist+cost
            if distance[city]>new_cost:
                distance[city] = new_cost
                heapq.heappush(q,(new_cost, city))

graph = [[] for _ in range(n+1)]
for _ in range(m):
    s,e,c = map(int,input().split())
    graph[s].append((e,c))

start,end = map(int,input().split())
distance = [INF]*(n+1)
dijstra(start)

print(distance[end])