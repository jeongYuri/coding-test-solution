def int_to_base(num, base):
    if num < base:
        return str(num)
    digits = ''
    while num > 0:
        digits = str(num % base) + digits
        num //= base
    return digits

def base_to_int(num_str, base):
    if num_str == '0':
        return 0
    if max(num_str) >= str(base):
        return False
    total = 0
    for i, digit in enumerate(num_str[::-1]):
        total += int(digit) * (base ** i)
    return total

def is_valid_base(base, expr):
    a, op, b, _, c = expr.split()
    a_val = base_to_int(a, base)
    b_val = base_to_int(b, base)
    if c != 'X':
        c_val = base_to_int(c, base)
        if a_val is False or b_val is False or c_val is False:
            return False
        return (op == '+' and a_val + b_val == c_val) or (op == '-' and a_val - b_val == c_val)
    else:
        return a_val is not False and b_val is not False

def solve_unknown(bases, expr):
    a, op, b, _, c = expr.split()
    results = set()
    for base in bases:
        a_val = base_to_int(a, base)
        b_val = base_to_int(b, base)
        if a_val is False or b_val is False:
            continue
        res = a_val + b_val if op == '+' else a_val - b_val
        if res < 0:
            continue
        res_str = int_to_base(res, base)
        results.add(res_str)
    if len(results) == 1:
        return f"{a} {op} {b} = {results.pop()}"
    else:
        return f"{a} {op} {b} = ?"

def solution(expressions):
    valid_bases = [b for b in range(2, 10) if all(is_valid_base(b, e) for e in expressions)]

    answers = []
    for expr in expressions:
        if expr.endswith('X'):
            answers.append(solve_unknown(valid_bases, expr))
    return answers
