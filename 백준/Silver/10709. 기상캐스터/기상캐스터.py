import sys
input = sys.stdin.readline


h,w = map(int,input().split())
res = [[-1]*w for _ in range(h)]
sky = [str(input().rstrip())for _ in range(h)]
for i in range(h):
    last_c = -1
    for j in range(w):
        if sky[i][j] =='c':
            res[i][j] = 0
            last_c = j
        elif sky[i][j]=='.' and last_c !=-1:
            res[i][j] = j- last_c
for row in res:
    print(*row)