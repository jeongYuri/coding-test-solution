import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    r,s = input().split()
    r = int(r)
    word = ''.join(w*r for w in s)
    print(word)