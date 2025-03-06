import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
cards = list(map(int,input().split()))
cards.reverse()

res = deque()
stack = [i for i in range(n, 0, -1)]

for skill in cards:
    if skill == 1:
        res.append(stack.pop())
    elif skill == 2:
        res.insert(-1, stack.pop())
    else:
        res.appendleft(stack.pop())

res.reverse()
print(*res)





