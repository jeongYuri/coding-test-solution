import sys
input = sys.stdin.readline

t = int(input())
turn = list(map(int,input().split()))
turn.sort()
total_time = 0
for i in range(t):
    total_time += turn[i] * (t - i)

print(total_time)