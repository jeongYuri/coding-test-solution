import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
q = deque()
for _ in range(t):
    text = input().split()
    if text[0]=='push':
        q.append(text[1])
    elif text[0]=='pop':
        if len(q)==0:
            print(-1)
        else:
            print(q.popleft())
    elif text[0]=='size':
        print(len(q))
    elif text[0]=='empty':
        if len(q)==0:
            print(1)
        else:
            print(0)
    elif text[0]=='front':
        if len(q)==0:
            print(-1)
        else:
            print(q[0])
    elif text[0]=='back':
        if len(q)==0:
            print(-1)
        else:
            print(q[-1])