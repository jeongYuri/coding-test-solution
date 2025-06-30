import sys
import math
input = sys.stdin.readline
INF = int(1e9)
n = int(input()) #도시 수
m = int(input()) #버스 수
info = [[INF]*n for _ in range(n)]

for i in range(n):
    info[i][i] = 0 #자기 자신은 0

for _ in range(m):
    a,b,c = map(int,input().split()) #a:버스 시작, b:버스 도착, c: 비용
    info[a-1][b-1] = min(info[a-1][b-1],c)

for k in range(n):
    for i in range(n):
        for j in range(n):
            info[i][j] = min(info[i][j],info[i][k]+info[k][j])
for i in range(n):
    for j in range(n):
        if info[i][j]==INF:
            print(0,end=" ")
        else:
            print(info[i][j],end=" ")
    print()

