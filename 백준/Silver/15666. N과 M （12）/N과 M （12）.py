n,m = map(int,input().split())
arr = sorted(list(map(int,input().split())))
ans = []
def dfs(s):
    if len(ans)==m:
        print(*ans)
        return
    nov = 0
    for i in range(s,n):
        if nov != arr[i]:
            ans.append(arr[i])
            nov = arr[i]
            dfs(i)
            ans.pop()
dfs(0)
