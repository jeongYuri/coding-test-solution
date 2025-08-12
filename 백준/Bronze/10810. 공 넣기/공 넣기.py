import sys
input = sys.stdin.readline

n,m = map(int,input().split())
basket = [list(map(int,input().split())) for _ in range(m)]
arr = [0]*n
for i,j,k in basket:
    for t in range(i-1,j):
        arr[t] = k
print(*arr)
