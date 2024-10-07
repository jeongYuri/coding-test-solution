import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr1 = [list(map(int,input().split())) for _ in range(n)]
m,k = map(int,input().split())
arr2 = [list(map(int,input().split())) for _ in range(m)]

ans = [[0]*k for _ in range(n)]
for i in range(n):
    for j in range(k):
        for l in range(m):
            ans[i][j] += arr1[i][l] * arr2[l][j]
for i in ans:
    print(*i)