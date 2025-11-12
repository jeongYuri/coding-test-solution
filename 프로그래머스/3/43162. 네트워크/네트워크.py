def solution(n, computers):
    visited = [False]*n
    cnt = 0
    def dfs(node):
        visited[node] = True
        for i in range(n):
            if computers[node][i]==1 and not visited[i]:
                dfs(i)
    for i in range(n):
        if not visited[i]:
            dfs(i)
            cnt+=1
    return cnt