import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
numbers = list(map(int,input().split()))

total = sum(numbers)
hab = 0

for number in numbers:
    total -= number
    hab += number * total
print(hab)