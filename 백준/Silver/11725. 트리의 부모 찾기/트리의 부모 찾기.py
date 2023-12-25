import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

t = int(input())
tree = [[] for _ in range(t+1)]
visited = [0]*(t+1)

def dfs(s):
    for i in tree[s]:
        if visited[i]==0:
            visited[i] = s
            dfs(i)

for _ in range(t-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

dfs(1)

for i in range(2,t+1):
    print(visited[i])
