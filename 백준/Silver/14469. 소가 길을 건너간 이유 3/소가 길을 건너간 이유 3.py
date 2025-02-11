import sys
input = sys.stdin.readline

n = int(input())

cows = [tuple(map(int, input().split())) for _ in range(n)]
cows.sort()  

current_time = 0

for arrival, check in cows:
    if current_time > arrival:
        current_time += check  
    else:
        current_time = arrival + check  

print(current_time)


