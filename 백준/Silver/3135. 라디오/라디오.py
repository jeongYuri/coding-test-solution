import sys
input = sys.stdin.readline


a,b = map(int,input().split())
n = int(input())
button = [int(input()) for _ in range(n)]
clicks = abs(b-a)
for x in button:
    clicks = min(clicks,abs(b-x)+1)

print(clicks)