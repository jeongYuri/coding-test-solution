import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

piece = [1,1,2,2,2,8]
now = list(map(int,input().split()))

for i in range(6):
    now[i] = piece[i]- now[i]
print(*now)
