def solution(arr):
    ans = []
    stack = []
    for a in arr:
        if not stack or stack[-1]!=a:
            stack.append(a)
    return stack