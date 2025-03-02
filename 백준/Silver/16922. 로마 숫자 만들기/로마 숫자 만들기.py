import sys
input = sys.stdin.readline
from itertools import combinations_with_replacement

roma = [1,5,10,50]
n = int(input())
unique = set()

for comb in combinations_with_replacement(roma, n):
    unique.add(sum(comb))
print(len(unique))


