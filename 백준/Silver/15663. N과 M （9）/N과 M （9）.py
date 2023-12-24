n,m = map(int,input().split())
arr = sorted(list(map(int,input().split())))
visited = [False]*n
ans = []
def dfs():
    if len(ans)==m:
        print(*ans)
        return
    nov = 0
    for i in range(n):
        if arr[i]!=nov and not visited[i]:
            visited[i] = True
            ans.append(arr[i])
            nov = arr[i]
            dfs()
            visited[i]=False
            ans.pop()
dfs()
