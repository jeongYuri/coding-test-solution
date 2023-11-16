import sys
from collections import deque
input = sys.stdin.readline


def dfs(s):
    visited[s] = True
    print(s, end=" ")
    for i in graph[s]:
        if not visited[i]:
            dfs(i)


def bfs(s):
    q = deque([s])
    visited[s] = True
    while q:
        n = q.popleft()
        print(n, end=" ")
        for i in graph[n]:
            if not visited[i]:
                visited[i] = True
                q.append(i)


n,m,v = map(int,input().split()) # v는 시작점
graph = [[] for _ in range(n+1)]

for _ in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
for i in graph:
    i.sort()

visited = [False]*(n+1)
dfs(v)
print()
visited = [False]*(n+1)
bfs(v)

