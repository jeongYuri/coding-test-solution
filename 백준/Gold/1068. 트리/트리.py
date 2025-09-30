import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
visited = [False] * n
tree = [[] for _ in range(n)]
ans = 0
p = list(map(int, input().split()))

for i in range(n):
    if p[i] != -1:
        tree[i].append(p[i])
        tree[p[i]].append(i)
    else:
        root = i

delete = int(input())

def dfs(current_node):
    global ans
    is_leaf = True
    for neighbor in tree[current_node]:
        if not visited[neighbor] and neighbor != delete:
            visited[neighbor] = True
            is_leaf = False
            dfs(neighbor)

    if is_leaf:
        ans += 1

if delete == root:
    print(0)
else:
    visited[root] = True   
    dfs(root)
    print(ans)
