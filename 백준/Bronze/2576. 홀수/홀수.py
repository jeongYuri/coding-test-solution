import sys
input = sys.stdin.readline
nums = []
for _ in range(7):
    nums.append(int(input()))
odd_nums = [num for num in nums if num % 2 != 0]
if len(odd_nums)!=0:
    print(sum(odd_nums))
    print(min(odd_nums))
else:
    print(-1)