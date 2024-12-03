import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    cnt = 0
    x1,y1,x2,y2 = map(int,input().split())
    n = int(input()) #행성계의 개수 n
    for i in range(n):
        cx,cy,cr = map(int,input().split()) #행성계의 중점과 반지름
        dist1 = (x1-cx)**2 + (y1-cy)**2
        dist2 = (x2-cx)**2 + (y2-cy)**2
        if (dist1<cr**2 and dist2>cr**2) or (dist1>cr**2 and dist2 <cr**2):
            cnt +=1
    print(cnt)

