import sys
input = sys.stdin.readline
def swap(candy,x1,y1,x2,y2):
    candy[x1][y1],candy[x2][y2] = candy[x2][y2],candy[x1][y1]
    #두 위치의 사탕을 교환하는 함수
def cnt_candy(candy, n):
    max_candy = 0
    for i in range(n):
        row_cnt = 1
        for j in range(1,n):
            if candy[i][j] == candy[i][j-1]:
                row_cnt+=1
            else:
                max_candy = max(max_candy,row_cnt)
                row_cnt =1
        max_candy = max(max_candy,row_cnt)
    for j in range(n):
        col_cnt = 1
        for i in range(1,n):
            if candy[i][j]== candy[i-1][j]:
                col_cnt+=1
            else:
                max_candy = max(max_candy, col_cnt)
                col_cnt =1
        max_candy = max(max_candy,col_cnt)
    return max_candy
n = int(input())
candy = [list(input().strip()) for _ in range(n)]
max_candy = 0

for i in range(n):
    for j in range(n):
        if j+1<n:
            swap(candy,i,j,i,j+1)
            max_candy = max(max_candy,cnt_candy(candy,n))
            swap(candy,i,j,i,j+1) #원상복구
        if i+1<n:
            swap(candy, i,j,i+1,j)
            max_candy = max(max_candy,cnt_candy(candy,n))
            swap(candy, i,j,i+1,j)
print(max_candy)