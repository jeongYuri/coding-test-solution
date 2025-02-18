import sys
from collections import defaultdict
input = sys.stdin.readline

n,k = map(int,input().split())

max_x = 1_000_000
bucket = [0]*(max_x+1)

for _ in range(n):
    g,x = map(int,input().split())
    bucket[x]+=g #좌표 x 에 얼음 g를 더함


window = 2*k +1 #커버할 수 있는 범위 선택
current_sum = sum(bucket[:window])
max_ice = current_sum

for i in range(1, max_x - 2 * k + 1):
    current_sum -= bucket[i - 1]
    if i + 2 * k <= max_x:
        current_sum += bucket[i + 2 * k]  # 오른쪽 끝 값 추가

    max_ice = max(max_ice, current_sum)  # 최댓값 갱신
print(max_ice)