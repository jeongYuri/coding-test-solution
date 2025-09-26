import sys
input =sys.stdin.readline

n = int(input())
schedules = []
for _ in range(n):
    s,e = map(int,input().split())
    schedules.append((s,e))
max_day = 365
if n>0:
    max_day = max(max(e for s,e in schedules),1000)
height_array = [0]*(max_day+2)
for s,e in schedules:
    for day in range(s,e+1):
        height_array[day]+=1
total_area = 0
width = 0
max_height = 0

for day in range(1, max_day+2):
    current_height = height_array[day]
    if current_height>0:
        width+=1
        max_height = max(max_height,current_height)
    else:
        if width>0:
            area = width *max_height
            total_area += area
        width = 0
        max_height = 0
print(total_area)