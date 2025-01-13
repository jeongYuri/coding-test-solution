import sys
import heapq
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1
q = deque()
res= []
for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)

while q:
    current = q.popleft()
    res.append(current)

    for next_node in graph[current]:
        indegree[next_node] -= 1
        if indegree[next_node] == 0:
            q.append(next_node)

print(" ".join(map(str, res)))