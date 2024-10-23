import sys
input = sys.stdin.readline

def min_time_to_reach(distance):
    max_distance = 5
    time = distance // max_distance
    if distance % max_distance > 0:
        time += 1
    return time


distance = int(input()) 
print(min_time_to_reach(distance))