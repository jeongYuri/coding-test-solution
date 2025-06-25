import sys
input = sys.stdin.readline

n,k = map(int,input().split())
bus = k
for i in range(n):
    t,h = map(int,input().split())
    bus-= h
    bus+=t
print("비와이")