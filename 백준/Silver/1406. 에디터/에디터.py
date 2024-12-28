import sys
input = sys.stdin.readline
left =  list(input().strip())
right = []
n = int(input())

for _ in range(n):
    command = input().strip().split()
    if command[0] == 'L' and left:
        right.append(left.pop())
    elif command[0] == 'D' and right:
        left.append(right.pop())
    elif command[0] == 'P':
        left.append(command[1])
    elif command[0] == 'B' and left:
        left.pop()
print(''.join(left+right[::-1]))