import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    su1 = set(map(int, input().split()))
    m = int(input())
    su2 = list(map(int, input().split()))
    for s2 in su2:
        print(1 if s2 in su1 else 0)
