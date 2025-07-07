import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[]*2 for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[b].append(a) #a가 b를 신뢰한다

def bfs(start):
    visited = [False] * (n + 1)
    visited[start] = True
    q = deque([start])
    count = 1

    while q:
        now = q.popleft()
        for next_node in graph[now]:
            if not visited[next_node]:
                visited[next_node] = True
                count += 1
                q.append(next_node)
    return count

max_count = 0
res = []

for i in range(1, n + 1):
    count = bfs(i)
    if count > max_count:
        max_count = count
        res = [i]
    elif count == max_count:
        res.append(i)

print(*res)