import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    keylogger = str(input()).rstrip()
    left_stack = []
    right_stack = []

    for char in keylogger:
        if char=='-':
            if left_stack:
                left_stack.pop()
        elif char=='<':
            if left_stack:
                right_stack.append(left_stack.pop())
        elif char=='>':
            if right_stack:
                left_stack.append(right_stack.pop())
        else:
            left_stack.append(char)
    print(''.join(left_stack)+''.join(reversed(right_stack)))