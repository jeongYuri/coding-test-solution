import re
from collections import deque

def cnt_path(n,m):
    dp = [[0]*m for _ in range(n)]
    dp[0][0] = 1

    for i in range(n):
        for j in range(m):
            if i>0:
                dp[i][j]+= dp[i-1][j]
            if j>0:
                dp[i][j]+=dp[i][j-1]
    return dp[n-1][m-1]
n,m, k = map(int,input().split())
if k==0:
    print(cnt_path(n,m))
else:
    k-=1
    kx,ky = divmod(k,m)
    first = cnt_path(kx+1,ky+1)
    second = cnt_path(n-kx,m-ky)
    print(first*second)

