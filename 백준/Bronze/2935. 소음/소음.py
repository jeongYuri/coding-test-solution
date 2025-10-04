import sys
input = sys.stdin.readline

a = int(input().rstrip())
b = str(input().strip())
c = int(input().rstrip())

if b=='*':
    print(a*c)
else:
    print(a+c)