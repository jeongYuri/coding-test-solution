import sys
import math
input = sys.stdin.readline

n = int(input())
mosq = {}
for _ in range(n):
    e,x = map(int,input().split())
    mosq[e] = mosq.get(e,0)+1
    mosq[x] = mosq.get(x,0)-1

mos_cnt = -1
mos_time = [None,None]

check = False
mos = sorted(mosq.keys())
sum_mos = 0

for time in mos:
    sum_mos += mosq[time]
    if sum_mos> mos_cnt:
        mos_cnt = sum_mos
        mos_time[0] = time
        check = True
    elif sum_mos<mos_cnt and check:
        mos_time[1] = time
        check = False
if check:
    mos_time[1] = time
print(mos_cnt)
print(mos_time[0],mos_time[1])