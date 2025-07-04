import sys
input = sys.stdin.readline

n, m = map(int, input().split())

hangA = [list(map(int, input().rstrip())) for _ in range(n)]
hangB = [list(map(int, input().rstrip())) for _ in range(n)]

cnt = 0

def flip(i, j):
    for x in range(i, i+3):
        for y in range(j, j+3):
            hangA[x][y] = 1 - hangA[x][y]  

if n < 3 or m < 3:
    if hangA != hangB:
        print(-1)
    else:
        print(0)
    sys.exit()

for i in range(n - 2):
    for j in range(m - 2):
        if hangA[i][j] != hangB[i][j]:
            flip(i, j)
            cnt += 1

if hangA != hangB:
    print(-1)
else:
    print(cnt)
