import sys
input = sys.stdin.readline

text = str(input()).rstrip()
n = int(input())
rings = [input().rstrip() for _ in range(n)]
cnt = 0
for ring in rings:
    ring = ring+ring
    if text in ring:
        cnt +=1

print(cnt)
