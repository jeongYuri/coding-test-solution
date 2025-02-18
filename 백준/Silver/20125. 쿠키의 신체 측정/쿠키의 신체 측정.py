import sys
input = sys.stdin.readline

#머리 위치 찾기
def head_idx(arr):
    for i in range(n):
        for j in range(n):
            if arr[i][j]=='*': #쿠키의 신체 부분
                return i,j
#왼쪽 팔길이
def dhls_handy(y,x):
    cnt = 0
    for i in range(x-1, -1,-1):
        cnt +=1
        if cookie[y][i]=='_':
            return cnt-1
    return cnt
#오른쪽 팔길이
def dh_handy(y,x):
    cnt = 0
    for i in range(x+1, n,1):
        cnt +=1
        if cookie[y][i]=='_':
            return cnt -1
    return cnt
#허리 길이
def waist(y,x):
    cnt = 0
    for i in range(y,n):
        cnt +=1
        if cookie[i][x]=='_':
            break
    return cnt -1
#다리 길이
def leg(y,x):
    cnt = 1
    for i in range(y,n):
        if cookie[i][x]=='_':
            break
        cnt +=1
    return cnt-1

n = int(input())
cookie = [list(input())for _ in range(n)]

y,x = head_idx(cookie)
print(y+2,x+1)
print(dhls_handy(y+1,x),end=' ')
print(dh_handy(y+1,x),end = ' ')
waist_cnt = waist(y+2,x)
print(waist_cnt,end=' ')
print(leg(y+waist_cnt+2, x-1),end=' ')
print(leg(y+waist_cnt+2, x+1), end =' ')

