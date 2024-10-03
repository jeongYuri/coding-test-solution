import sys
input = sys.stdin.readline

n = int(input())
f = int(input())

base = (n // 100) * 100
res = 0

for i in range(100):
    if ((base + i) % f == 0):
        res = i
        break

print("{:02d}".format(res))