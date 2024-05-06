import sys
from collections import deque
input = sys.stdin.readline

s, b = map(int,input().split())
q = deque()
q.append(s)
board = [0] * 100001 #최대 크기
cnt , res = 0,0
while q:
    a = q.popleft()
    temp = board[a]
    if a==b:
        res = temp
        cnt +=1
        continue
    for i in [a-1,a+1,a*2]:
        if 0<=i<100001 and (board[i]==0 or board[i]==board[a]+1):
            board[i] = board[a]+1
            q.append(i)

print(res)
print(cnt)