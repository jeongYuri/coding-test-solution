import sys
input = sys.stdin.readline
H, W, X, Y = map(int, input().strip().split())
B = [list(map(int, input().strip().split())) for _ in range(H+X)]
for i in range(X,H):
    for j in range(Y,W):
        B[i][j] = B[i][j] - B[i-X][j-Y]
for result in B[:H] :
    print(*result[:W])
