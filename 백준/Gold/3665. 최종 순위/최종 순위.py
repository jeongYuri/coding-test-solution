import sys
from collections import deque
input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    n = int(input())
    last_year = list(map(int,input().split()))
    m = int(input())
    graph = [[False]*(n+1) for _ in range(n+1)]
    indegree =[0]*(n+1)

    for i in range(n):
        for j in range(i+1,n):
            higher = last_year[i]
            lower = last_year[j]
            if not graph[higher][lower]:
                graph[higher][lower] = True
                indegree[lower]+=1

    for _ in range(m):
        a,b = map(int,input().split())
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[b]-=1
            indegree[a]+=1
        else:
            graph[b][a] = False
            graph[a][b] = True
            indegree[a]-=1
            indegree[b]+=1
    q = deque()
    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)

    res = []
    certain = True
    cycle = False

    for i in range(n):
        if not q:
            cycle = True
            break
        if len(q)>1:
            certain = False
        now = q.popleft()
        res.append(now)
        for nxt in range(1,n+1):
            if graph[now][nxt]:
                indegree[nxt]-=1
                if indegree[nxt]==0:
                    q.append(nxt)
    if cycle:
        print("IMPOSSIBLE")
    elif not certain:
        print("?")
    else:
        print(" ".join(map(str, res)))