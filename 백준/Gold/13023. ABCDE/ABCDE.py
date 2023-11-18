import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n,m = map(int,input().split())
arrive = False
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)

def dfs(now, depth):
    global arrive
    if depth == 5:
        arrive = True
        return
    visited[now] = True
    for i in graph[now]:
        if not visited[i]:
            dfs(i,depth+1)
    visited[now] = False

for _ in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(n):
    dfs(i,1)
    if arrive:
        break

if arrive:
    print(1)
else:
    print(0)