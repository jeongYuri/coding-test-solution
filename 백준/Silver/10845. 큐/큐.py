import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
qu = deque()
for i in range(n):
    text = input().split()
    if text[0]=='push':
        qu.append(text[1])
    elif text[0] =='pop':
        if len(qu)==0:
            print(-1)
        else:
            print(qu.popleft())
    elif text[0] =='size':
        print(len(qu))
    elif text[0]=='empty':
        if len(qu)==0:
            print(1)
        else:
            print(0)
    elif text[0] =='front':
        if len(qu)==0:
            print(-1)
        else:
            print(qu[0])
    elif text[0]=='back':
        if len(qu)==0:
            print(-1)
        else:
            print(qu[-1])
