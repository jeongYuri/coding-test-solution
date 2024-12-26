import sys
sys.setrecursionlimit(10**6)  #재귀 깊이 제한을 늘리기위해
input = sys.stdin.readline

t = int(input())
def cycles(n,arr):
    visited = [False] * (n+1)
    cnt = 0
    def dfs(node):
        while not visited[node]:
            visited[node] = True
            node = arr[node]

    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)
            cnt += 1

    return cnt
for _ in range(t):
    n = int(input())
    arr =[0] + list(map(int,input().split()))
    print(cycles(n,arr))


