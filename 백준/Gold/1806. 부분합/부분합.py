import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
right = 0
arr_sum = 0  # 초기 합을 0으로 
length = n + 1  # 초기 길이를 n+1로 

while right < n:
    arr_sum += arr[right]  # 오른쪽 값 추가

    while arr_sum >= s:  # 조건을 만족하면 최소 길이 갱신
        length = min(length, right - left + 1)
        arr_sum -= arr[left]  
        left += 1  

    right += 1  

# 길이가 갱신되지 않았다면 0
print(length if length != n + 1 else 0)