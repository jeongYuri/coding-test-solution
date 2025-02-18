import sys
from collections import defaultdict
input = sys.stdin.readline

n,k = map(int,input().split())

bucket = [0]*1000001
last_idx = 0

for _ in range(n):
    g,x = map(int,input().split())
    bucket[x]=g #좌표 x 에 얼음 g를 더함
    last_idx = max(last_idx, x)

size = 2*k +1 #커버할 수 있는 범위 선택
current_sum = sum(bucket[:size])
max_ice = current_sum

for end in range(size,last_idx+1):
    current_sum += bucket[end]-bucket[end-size]
    max_ice = max(max_ice,current_sum)
print(max_ice)