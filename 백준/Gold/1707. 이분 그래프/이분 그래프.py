import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(start, group):
    visited[start] = group
    for i in graph[start]:
        if not visited[i]:
            if not dfs(i, -group):
                return False
        elif visited[i] == visited[start]:
            return False
    return True

tc = int(input())
for _ in range(tc):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    visited = [0] * (V+1)

    for _ in range(E):
        u, w = map(int, input().split())
        graph[u].append(w)
        graph[w].append(u)

    res = True
    for i in range(1, V+1):
        if not visited[i]:
            if not dfs(i, 1):
                res = False
                break

    print("YES" if res else "NO")
