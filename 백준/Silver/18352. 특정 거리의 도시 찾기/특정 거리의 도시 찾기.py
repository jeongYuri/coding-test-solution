import sys
input = sys.stdin.readline
n,m,k,x = map(int,input().split())
from collections import deque
dist = [[] for _ in range(n+1)]
answer = []
visited = [-1]*(n+1)

def bfs(v):
    q = deque()
    q.append(v)
    visited[v]+=1
    while q:
        now = q.popleft()
        for i in dist[now]:
            if visited[i]==-1:
                visited[i] = visited[now]+1
                q.append(i)
for _ in range(m):
    a,b = map(int,input().split())
    dist[a].append(b)

bfs(x)
for i in range(n+1):
    if visited[i]==k:
        answer.append(i)
if not answer:
    print(-1)
else:
    for i in sorted(answer):
        print(i)