import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int, input().split())
q = deque()
q.append(n)
board = [-1] * 100001  
board[n] = 0  

while q:
    a = q.popleft()
    if a == k:
        print(board[a])
        break
    if 0 <= a * 2 < 100001 and board[a * 2] == -1:
        board[a * 2] = board[a]
        q.appendleft(a * 2) 
    for i in [a - 1, a + 1]:
        if 0 <= i < 100001 and board[i] == -1:
            board[i] = board[a] + 1
            q.append(i)
