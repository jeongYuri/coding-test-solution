import sys
input = sys.stdin.readline
n = int(input())  

for _ in range(n):
    d, f, p = map(float, input().split())
    cost = d * f * p
    print(f"${cost:.2f}")  