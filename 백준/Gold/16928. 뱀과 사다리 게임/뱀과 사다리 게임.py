import sys
input = sys.stdin.readline
from collections import deque
ladder = dict()
n,m = map(int,input().split())
snake = dict()
board = [0]*101
visited = [False]*101
for _ in range(n):
    a, b = map(int,input().split())
    ladder[a] = b
for _ in range(m):
    a, b = map(int,input().split())
    snake[a] = b

q = deque([1])
while q:
    x =q.popleft()
    if x==100:
        print(board[x])
        break
    for dice in range(1,7):
        next_b = x+dice
        if next_b <=100 and not visited[next_b]:
            if next_b in ladder.keys():
                next_b = ladder[next_b]
            if next_b in snake.keys():
                next_b = snake[next_b]
            if not visited[next_b]:
                visited[next_b] = True
                board[next_b] = board[x]+1
                q.append(next_b)