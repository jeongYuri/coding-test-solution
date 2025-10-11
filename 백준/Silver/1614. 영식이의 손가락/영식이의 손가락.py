import sys
input = sys.stdin.readline

h = int(input())
n = int(input())

if h == 0:
    print(n - 1)
elif h == 1:
    print(n * 8)
elif h == 2:
    print(n * 4 + (1 if n % 2 == 0 else 3))
elif h == 3:
    print(n * 4 + 2)
elif h == 4:
    print(n * 4 + (3 if n % 2 == 0 else 1))
else:
    print(n * 8 + 4)
