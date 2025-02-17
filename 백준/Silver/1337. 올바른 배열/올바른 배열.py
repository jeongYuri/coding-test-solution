import sys
input = sys.stdin.readline
def check(arr):
    arr.sort()
    n = len(arr)
    start = 0
    max_cnt = 0

    for end in range(n):
        while arr[end]-arr[start]>=5:
            start +=1
        current_window = end-start+1
        max_cnt = max(max_cnt,current_window)
    return max(0,5-max_cnt)
n = int(input())
numbers = list(int(input())for _ in range(n))

print(check(numbers))