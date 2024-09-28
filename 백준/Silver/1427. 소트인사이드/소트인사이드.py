import sys
input = sys.stdin.readline

n = input().rstrip()
nums = [int(digit) for digit in n]
nums.sort(reverse=True)
print(''.join(map(str, nums)))
