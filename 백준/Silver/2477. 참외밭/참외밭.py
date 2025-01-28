import sys
input = sys.stdin.readline

k = int(input())
info = []
for _ in range(6):
    d, l = map(int, input().split())
    info.append((d, l))

max_w_idx = 0
max_h_idx = 0
max_width = 0
max_height = 0

for i in range(6):
    d, length = info[i]
    if d == 1 or d == 2:  
        if length > max_width:
            max_width = length
            max_w_idx = i
    else:              
        if length > max_height:
            max_height = length
            max_h_idx = i

small_w = info[(max_w_idx + 3) % 6][1]
small_h = info[(max_h_idx + 3) % 6][1]

big_area = max_width * max_height
small_area = small_w * small_h
res = (big_area - small_area) * k
print(res)
