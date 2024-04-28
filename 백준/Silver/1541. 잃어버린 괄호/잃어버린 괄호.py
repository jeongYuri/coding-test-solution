import sys
text = sys.stdin.readline().strip().split('-')
nums = []
for i in text:
    cnt = 0
    for j in i.split('+'):
        cnt += int(j)
    nums.append(cnt)
result = nums[0]
for i in nums[1:]:
    result -= i
print(result)