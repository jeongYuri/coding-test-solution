import sys
input = sys.stdin.readline

n = int(input())
ranking = [int(input()) for _ in range(n)]
ranking.sort()
hab = 0
for i in range(n):
    hab += abs(ranking[i]-(i+1))
print(hab)