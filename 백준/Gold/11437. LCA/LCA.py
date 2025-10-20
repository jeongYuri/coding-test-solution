import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
LOG = 21  

tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)

depth = [0] * (n+1)
visited = [False] * (n+1)
parent = [[0]*LOG for _ in range(n+1)] 

def dfs(node, d):
    visited[node] = True
    depth[node] = d
    for nxt in tree[node]:
        if not visited[nxt]:
            parent[nxt][0] = node
            dfs(nxt, d+1)

dfs(1, 0)

for k in range(1, LOG):
    for v in range(1, n+1):
        parent[v][k] = parent[parent[v][k-1]][k-1]
def lca(a, b):
    if depth[a] < depth[b]:
        a, b = b, a

    diff = depth[a] - depth[b]
    for k in range(LOG):
        if diff & (1 << k):
            a = parent[a][k]

    if a == b:
        return a

    for k in range(LOG-1, -1, -1):
        if parent[a][k] != parent[b][k]:
            a = parent[a][k]
            b = parent[b][k]

    return parent[a][0]

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))
