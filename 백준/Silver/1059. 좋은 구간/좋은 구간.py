import sys
input = sys.stdin.readline

l = int(input())
s = list(map(int,input().split()))
n = int(input())
ans = []

if n in s:
    print(0)
else:
    s.append(n)
    s.sort()
    idx = s.index(n)
    left = s[idx-1] if idx>0 else 0
    right = s[idx+1]
    print((n-left)*(right-n)-1)

