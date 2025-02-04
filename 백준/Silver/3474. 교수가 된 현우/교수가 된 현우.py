import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    cnt = 0
    i = 5
    while i<=n:
        cnt +=n//i
        i*=5
    print(cnt)