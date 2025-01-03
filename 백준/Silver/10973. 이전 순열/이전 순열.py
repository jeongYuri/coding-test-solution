import sys
input = sys.stdin.readline

def prev_permutation(arr):
    i = len(arr) - 1
    while i > 0 and arr[i - 1] <= arr[i]:
        i -= 1
    if i == 0:
        return False
    j = len(arr) - 1
    while arr[j] >= arr[i - 1]:
        j -= 1
    arr[i - 1], arr[j] = arr[j], arr[i - 1]
    arr[i:] = arr[i:][::-1]
    return True

n = int(input())
arr = list(map(int, input().split()))
if prev_permutation(arr):
    print(*arr)
else:
    print(-1)
