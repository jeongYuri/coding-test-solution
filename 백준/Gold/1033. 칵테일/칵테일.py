import sys
import math
input = sys.stdin.readline

n = int(input())
arr = [[]for _ in range(n)]
visited = [False]*n
d = [0]*n
lcm = 1

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
def dfs(v):
    visited[v] = True
    for i in arr[v]:
        next = i[0]
        if not visited[next]:
            d[next] = d[v]*i[2]//i[1]
            dfs(next)
for i in range(n-1):
    a,b,p,q = map(int,input().split())
    arr[a].append((b,p,q))
    arr[b].append((a,q,p))
    lcm *=(p*q//gcd(p,q))
d[0] = lcm
dfs(0)
mgcd = d[0]

for i in range(1,n):
    mgcd = gcd(mgcd,d[i])
for i in range(n):
    print(int(d[i]//mgcd),end=' ')


