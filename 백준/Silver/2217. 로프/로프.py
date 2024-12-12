import sys
input = sys.stdin.readline

n = int(input())
lope = [int(input().strip()) for _ in range(n)]
lope.sort()
max_weight = 0
for i in range(n):
    current_weight = lope[i] * (n-i)
    max_weight = max(max_weight,current_weight)
print(max_weight)