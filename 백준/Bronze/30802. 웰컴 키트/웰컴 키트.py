import sys
import math

input = sys.stdin.readline
n = int(input())
sizes = map(int, input().split())
t, p = map(int, input().split())
count = 0
for size in sizes:
    if size > 0:
        count += math.ceil(size / t)

print(count)
print(n // p, n % p)