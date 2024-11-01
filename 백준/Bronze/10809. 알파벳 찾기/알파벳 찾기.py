import sys
input = sys.stdin.readline

s = input()
c = 'abcdefghijklmnopqrstuvwxyz'
for i in c:
    print(s.find(i),end=" ")