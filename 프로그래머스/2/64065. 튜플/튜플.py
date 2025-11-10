def solution(s):
    answer = []
    s = s[2:-2].split("},{")
    s = sorted([list(map(int, x.split(','))) for x in s], key=len)
    for i in s:
        for num in i:
            if num not in answer:
                answer.append(num)
    return answer