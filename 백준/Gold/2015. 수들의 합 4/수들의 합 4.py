import sys

input = sys.stdin.readline

n,k = map(int,input().split())
arr = list(map(int,input().split()))
cnt = 0 #정답 개수
prefix_sum = 0 #누적합
prefix_cnt = {0: 1} # 초기 값: 누적 합이 0인 경우를 고려해 {0:1} 저장

for num in arr:
    prefix_sum += num
    if prefix_sum-k in prefix_cnt:
        cnt += prefix_cnt[prefix_sum-k]
    prefix_cnt[prefix_sum] = prefix_cnt.get(prefix_sum,0)+1
print(cnt)
