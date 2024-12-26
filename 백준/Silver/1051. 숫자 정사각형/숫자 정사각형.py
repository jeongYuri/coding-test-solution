import sys
input = sys.stdin.readline

n,m = map(int,input().split())
board = [list(map(int,input().rstrip())) for _ in range(n)]
size = min(n,m)
def find_len(s):
    for i in range(n-s+1):
        for j in range(m-s+1):
            if board[i][j] == board[i][j+s-1] == board[i+s-1][j] == board[i+s-1][j+s-1]:
                return True
    return False
for k in range(size, 0,-1):
    if find_len(k):
        print(k**2)
        break