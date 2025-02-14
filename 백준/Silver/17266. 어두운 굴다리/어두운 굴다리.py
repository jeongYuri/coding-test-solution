import sys
input = sys.stdin.readline
def is_possible(location, height, N, M):
    if height - location[0] < 0:
        return False
    for i in range(1, M):
        if location[i] - location[i-1] > 2 * height:
            return False
    if N - location[-1] > height:
        return False
    return True
N = int(input())
M = int(input())

x = list(map(int, input().split()))
start = 1
end = N
answer = N
while start <= end:
    mid = (start + end) // 2
    if is_possible(x, mid, N, M):
        answer = mid
        end = mid - 1
    else:
        start = mid + 1
print(answer)
