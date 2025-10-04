import sys
input = sys.stdin.readline

t = int(input())
ch,sa = 100,100
for _ in range(t):
    c,s = map(int,input().split())
    if c<s:
        ch-=s
    elif c>s:
        sa-=c
print(ch)
print(sa)