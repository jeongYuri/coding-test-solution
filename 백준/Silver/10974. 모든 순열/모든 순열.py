import sys
input = sys.stdin.readline

n = int(input().rstrip())
res = []
def dfs():
    if len(res)==n:
        print(*res)
        return
    for i in range(1,n+1):
        if i not in res:
            res.append(i)
            dfs()
            res.pop()

dfs()