import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    q = deque([start])
    visited[start] = 1
    cnt = 2
    while(q):
        x = q.popleft()
        for nx in graph[x]:
            if visited[nx] ==0:
                visited[nx] = cnt
                cnt +=1
                q.append(nx)

n,m,r = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)
for _ in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
for i in range(n+1):
    graph[i].sort()
bfs(r)

for i in range(1, n + 1):
    print(visited[i])