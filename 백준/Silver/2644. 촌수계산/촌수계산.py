import sys
input = sys.stdin.readline
n = int(input()) #전체사람수
a,b = map(int,input().split()) # 두사람의 촌수를 알아야함
m = int(input()) #부모 자식들 간의 관계수 즉,,,약간 노드...?
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
result = []
for _ in range(m):
    x, y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(v,cnt):
    cnt +=1
    visited[v] = True
    if v== b:
        result.append(cnt)
    for i in graph[v]:
        if not visited[i]:
            dfs(i,cnt)
dfs(a,0)

if len(result)==0:
    print(-1)
else:
    print(result[0]-1)