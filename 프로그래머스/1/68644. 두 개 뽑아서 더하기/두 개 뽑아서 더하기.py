from itertools import combinations
def solution(numbers):
    answer = set()
    hu = list(combinations(numbers,2))
    for ch in hu:
        answer.add(sum(ch))
    return sorted(list(answer))