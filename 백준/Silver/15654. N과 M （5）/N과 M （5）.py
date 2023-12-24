def dfs(v):
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    for i in arr:
        if i not in s:
            s.append(i)
            dfs(i+1)
            s.pop()


n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
s = []
dfs(1)