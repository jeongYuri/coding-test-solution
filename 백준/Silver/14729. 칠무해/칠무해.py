import sys
input = sys.stdin.readline

n =int(input())
score = [float(input())for _ in range(n)]
score.sort()
res=score[:7]
for s in res:
    print(f"{s:.3f}") 
