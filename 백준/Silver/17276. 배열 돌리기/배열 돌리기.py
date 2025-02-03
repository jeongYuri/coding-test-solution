import sys
input = sys.stdin.readline

t = int(input())

def rotate_45(arr,n):
    new_arr = [row[:]for row in arr]

    mid = n//2

    for i in range(n):
        new_arr[i][mid] = arr[i][i] #주대각선->중앙열
        new_arr[i][n-1-i] = arr[i][mid] #중앙열-> 부대각선
        new_arr[mid][i] = arr[n-1-i][i]  # 중앙행->반대각선
        new_arr[i][i] = arr[mid][i] #부대각선->중앙행
    return new_arr

for _ in range(t):
    n, d = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    rotate_cnt = (d//45)%8 #360돌면 원상복구되므로 8번이상 돌 필요 ㄴ

    if rotate_cnt <0:
        rotate_cnt += 8
    for _ in range(rotate_cnt):
        arr = rotate_45(arr, n)

    for row in arr:
        print(*row)