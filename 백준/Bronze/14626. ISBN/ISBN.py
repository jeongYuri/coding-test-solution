import sys
input = sys.stdin.readline

isbn = input().rstrip()
arr = list(isbn)
temp = 0
hubo = 0  # 훼손된 자리 가중치
damaged_idx = -1

for i in range(12):
    if arr[i] != '*':
        if i % 2 == 0:
            temp += int(arr[i]) * 1
        else:
            temp += int(arr[i]) * 3
    else:
        damaged_idx = i
        hubo = 1 if i % 2 == 0 else 3

checksum = int(arr[-1])

for candidate in range(10):
    if (temp + candidate * hubo + checksum) % 10 == 0:
        print(candidate)
        break
