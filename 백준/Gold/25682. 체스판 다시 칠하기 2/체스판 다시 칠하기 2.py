import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())

board= [list(input().rstrip()) for _ in range(n)]
sum = [[0]*(m+1)for _ in range(n+1)]

for r in range(1,n+1):
    for c in range(1,m+1):
        if(r+c)%2==0:
            if board[r-1][c-1]=='B':
                sum[r][c] = sum[r-1][c]+sum[r][c-1]-sum[r-1][c-1]
            else:
                sum[r][c] = sum[r-1][c]+sum[r][c-1]-sum[r-1][c-1]+1
        else:
            if board[r-1][c-1]=='W':
                sum[r][c] = sum[r-1][c]+sum[r][c-1]-sum[r-1][c-1]
            else:
                sum[r][c] = sum[r-1][c]+sum[r][c-1]-sum[r-1][c-1]+1

max_ = -float('inf')
min_ = float('inf')
for r in range(k,n+1):
    for c in range(k,m+1):
        max_ = max(sum[r][c]-sum[r-k][c]-sum[r][c-k]+sum[r-k][c-k],max_)
        min_ = min(sum[r][c]-sum[r-k][c]-sum[r][c-k]+sum[r-k][c-k],min_)
print(min(min_,max_,k*k-min_,k*k-max_))