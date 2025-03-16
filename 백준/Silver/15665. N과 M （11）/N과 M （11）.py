import sys
input = sys.stdin.readline

from itertools import product

n,m = map(int, input().split())
arr= sorted(set(map(int, input().split())))

for numbers in product(arr, repeat=m):
    print(*numbers)
