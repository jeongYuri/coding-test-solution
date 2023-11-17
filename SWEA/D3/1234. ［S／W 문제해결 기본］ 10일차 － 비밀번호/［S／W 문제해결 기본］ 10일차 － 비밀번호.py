for tc in range(1, 11):
    n, num = map(int, input().split())
    nums = list(map(int, str(num)))
    stack = []
    for i in range(len(nums)):
        if len(stack) == 0:
            stack.append(nums[i])
        elif nums[i] == stack[-1]:
            stack.pop()
        elif nums[i] != stack[-1]:
            stack.append(nums[i])
    result = int("".join(map(str, stack)))
    print(f'#{tc} {result}')