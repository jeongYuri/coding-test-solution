def solution(n, s):
    if s < n:
        return [-1]

    q = s // n
    r = s % n
    answer = [q + 1 if i < r else q for i in range(n)]
    answer.sort()
    return answer