import sys
input = sys.stdin.readline

n = int(input())
a,b = 1,0
for _ in range(n):
    a,b = b,a+b
print(a,b)