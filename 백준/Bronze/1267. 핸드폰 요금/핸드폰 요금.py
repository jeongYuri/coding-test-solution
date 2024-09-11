import sys
input = sys.stdin.readline

n = int(input().strip())
call = list(map(int, input().strip().split()))
young_total = 0
minsik_total = 0
for time in call:
    young_total += (time // 30 + 1) * 10
    minsik_total += (time // 60 + 1) * 15

if young_total < minsik_total:
    print('Y', young_total)
elif young_total > minsik_total:
    print('M', minsik_total)
else:
    print('Y M', young_total)