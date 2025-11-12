def solution(operations):
    q = []
    for op in operations:
        c, n = op.split()
        n = int(n)
        if c == 'I':
            q.append(n)
        elif c == 'D':
            if not q:
                continue
            if n == 1:
                q.remove(max(q))
            elif n == -1:
                q.remove(min(q))
    return [max(q), min(q)] if q else [0, 0]