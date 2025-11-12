from collections import deque

def bfs(graph, start, visited):
    q = deque([start])
    visited[start] = True
    cnt = 0
    while q:
        v = q.popleft()
        cnt += 1
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
    return cnt

def solution(n, wires):
    ans = n - 2
    for i in range(len(wires)):
        tmps = wires.copy()
        graph = [[] for _ in range(n + 1)]
        visited = [False] * (n + 1)
        tmps.pop(i)  

        for x, y in tmps:  
            graph[x].append(y)
            graph[y].append(x)

        start = 1  
        cnts = bfs(graph, start, visited)
        other_cnt = n - cnts
        ans = min(ans, abs(cnts - other_cnt))  

    return ans
