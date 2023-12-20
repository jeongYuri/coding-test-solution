import sys
from collections import deque
input = sys.stdin.readline
t = int(input())

for i in range(t):
    p = sys.stdin.readline().rstrip()
    n = int(input())
    arr = deque(sys.stdin.readline().rstrip()[1:-1].split(","))
    if n == 0:
        arr = deque()
    flag = 0
    reverse = 0
    for j in p:
        if j == 'R':
            reverse +=1
        elif j == 'D':
            if not arr:
                print("error")
                flag = 1
                break
            elif reverse %2==1:
                arr.pop()
            else:
                arr.popleft()
    if flag == 0:
        if reverse %2==1:
            arr.reverse()
        print("["+",".join(arr)+"]")