from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
deq = deque()

for _ in range(n):
    command = input().split()

    if command[0] == 'push_front':
        deq.appendleft(int(command[1]))
    elif command[0] == 'push_back':
        deq.append(int(command[1]))
    elif command[0] == 'pop_front':
        if deq:
            print(deq.popleft())
        else:
            print(-1)
    elif command[0] == 'pop_back':
        if deq:
            print(deq.pop())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(deq))
    elif command[0] == 'empty':
        print(1 if not deq else 0)
    elif command[0] == 'front':
        print(deq[0] if deq else -1)
    elif command[0] == 'back':
        print(deq[-1] if deq else -1)
