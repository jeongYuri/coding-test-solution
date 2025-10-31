def solution(sizes):
    answer = 0
    for i in range(len(sizes)):
        sizes[i].sort()
    col = max(w for w,h in sizes)
    row = max(h for w,h in sizes)
    return col*row