import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    text = input().rstrip()
    print(text[0]+text[-1])