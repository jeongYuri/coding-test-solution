import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(start):
    global cnt
    visited[start] = cnt
    cnt +=1

    for i in sorted(graph[start]):
        if visited[i]==0:
            dfs(i)



n, m, r = map(int, input().split()) #n은 정점의 수, m은 간선의 수, r은 시작 정점
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
cnt = 1
for _ in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(n+1):
    graph[i].sort()
dfs(r)
for i in range(1, n + 1):
    print(visited[i])