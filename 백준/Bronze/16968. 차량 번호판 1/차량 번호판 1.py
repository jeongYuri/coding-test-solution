import string
import sys
input = sys.stdin.readline

word = input().strip()
ans = 1
prev = ''

for ch in word:
    if ch=='c':
        now = 26
    else:
        now = 10
    if ch==prev:
        now-=1
    ans*=now
    prev = ch
print(ans)
