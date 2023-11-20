res = 1
result = 0
arr = list(input())
stack = []

for i in range(len(arr)):
    if arr[i] == '(':
        res *= 2
        stack.append(arr[i])
    elif arr[i] == '[':
        res *= 3
        stack.append(arr[i])
    elif arr[i] == ')':
        if not stack or stack[-1] != '(':
            result = 0
            break
        if arr[i-1] == '(':
            result += res
        res //= 2
        stack.pop()
    elif arr[i] == ']':
        if not stack or stack[-1] != '[':
            result = 0
            break
        if arr[i-1] == '[':
            result += res
        res //= 3
        stack.pop()

if stack:
    print(0)
else:
    print(result)