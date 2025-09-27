import sys
from collections import deque
input = sys.stdin.readline

n,m,start = map(int,input().split())
graph = [[]for _ in range(n+1)]
for _ in range(m):
    s,e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)
visited = [False]*(n+1)
for i in range(n+1):
    graph[i].sort()
def dfs(v):
    print(v,end=' ')
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
visited = [False]*(n+1)
dfs(start)
def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = True
    while q:
        now = q.popleft()
        print(now,end=' ')
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
print()
visited = [False]*(n+1)
bfs(start)