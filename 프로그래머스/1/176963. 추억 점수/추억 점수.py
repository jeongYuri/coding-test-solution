from collections import defaultdict
def solution(name, yearning, photo):
    answer = []
    temp = {}
    for n, y in zip(name,yearning):
        temp[n] = y
    for picture in photo:
        score = 0
        for pic in picture:
            if pic in temp:
                score += temp[pic]
        answer.append(score)
    return answer