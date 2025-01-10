import sys
input = sys.stdin.readline

def dfs(node):
    if not graph[node]:
        return 1
    leaf = 0
    for child in graph[node]:
        leaf+= dfs(child)
    return leaf

n = int(input())
parents = list(map(int, input().split()))
delete= int(input())
graph = [[] for _ in range(n)]
root = 0

for i in range(n):
    if parents[i] == -1:  # 부모노드
        root = i
    else:
        graph[parents[i]].append(i)

if delete == root:
    print(0)
else:
    for children in graph:
        if delete in children:
            children.remove(delete)
            break
    result = dfs(root)
    print(result)
