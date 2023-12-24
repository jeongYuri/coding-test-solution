def dfs(v):
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    for i in range(v,len(arr)):
        s.append(arr[i])
        dfs(i)
        s.pop()


n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
s = []
dfs(0)