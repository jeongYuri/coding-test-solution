import re
import sys
input = sys.stdin.readline

n = int(input())
start = 1 #맨 처음 공의 위치
for _ in range(n):
    x,y = map(int,input().split())
    if start == y:
        start = x
    elif start ==x:
        start = y
print(start)