import sys

n = int(sys.stdin.readline())
expected_sum = sum(range(1, n))

line = sys.stdin.readline().rstrip()
actual_sum = 0
current_number = ""

for ch in line:
    if ch.isdigit():
        current_number += ch
    else:
        actual_sum += int(current_number)
        current_number = ""

actual_sum += int(current_number)

print(actual_sum - expected_sum)
