import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
w = []
for i in range(n):
    w.append(input().rstrip())

for i in range(n):
    q = deque(w[i])
    while True:
        q.append(q.popleft())
        save = "".join(q)
        if save == w[i]:
            break
        if save in w:
            idx = w.index(save)
            w.pop(idx)
            w.insert(idx, w[i])
w = set(w)
print(len(w))