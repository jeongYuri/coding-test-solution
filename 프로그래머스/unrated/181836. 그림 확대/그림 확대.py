def solution(picture, k):
    answer = []
    for row in picture:
        big = ''
        for pixel in row:
            big += pixel *k
        for _ in range(k):
            answer.append(big)
    return answer