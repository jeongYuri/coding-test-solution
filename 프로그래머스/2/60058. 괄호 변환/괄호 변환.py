def is_balanced(s):
    count = 0  
    for char in s:
        if char == '(':
            count += 1
        else:
            count -= 1
    return count == 0


def is_correct(s):

    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        else:
            if not stack: 
                return False
            stack.pop()
    return len(stack) == 0 


def solution(p):

    if not p or is_correct(p):
        return p

    for i in range(2, len(p) + 1, 2):
        if is_balanced(p[:i]):
            u = p[:i]
            v = p[i:]
            break

    if is_correct(u):
        return u + solution(v)

    corrected = '(' + solution(v) + ')'
    for char in u[1:-1]:  
        corrected += ')' if char == '(' else '('
    return corrected
