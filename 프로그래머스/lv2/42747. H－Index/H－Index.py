def solution(citations):
    h = 0
    citations.sort(reverse=True)
    for i, cita in enumerate(citations):
        if cita>=i+1:
            h = i+1
        else:
            break
    return h