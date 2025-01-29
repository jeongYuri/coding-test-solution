import sys
from itertools import product

input = sys.stdin.readline

n, k = map(int, input().split())
length = len(str(n))
numbers = sorted(map(str, input().split()), reverse=True) 

while length > 0:
    temp = list(product(numbers, repeat=length))
    res = [int(''.join(i)) for i in temp if int(''.join(i)) <= n]

    if res:
        print(max(res))
        break
    length -= 1