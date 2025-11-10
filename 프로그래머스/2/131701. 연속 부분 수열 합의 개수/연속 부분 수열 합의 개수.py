def solution(elements):
    n = len(elements)
    elements = elements*2
    sums = set()
    for leng in range(1,n+1):
        for start in range(n):
            part_sum = sum(elements[start:start+leng])
            sums.add(part_sum)
    return len(sums)