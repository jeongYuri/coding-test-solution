import sys
input = sys.stdin.readline

n = int(input())
meet = set()

for _ in range(n):
    a,b = input().split()
    if a=='ChongChong' or b=='ChongChong':
        meet.add(a)
        meet.add(b)
    if a in meet or b in meet:
        meet.add(a)
        meet.add(b)
print(len(meet))