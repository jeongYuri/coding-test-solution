import sys
input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    t, r = input().split()
    t = int(t)
    ans = ''.join(c * t for c in r)
    print(ans)