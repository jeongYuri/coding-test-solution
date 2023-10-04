def solution(msg):
    answer = []
    mydic = dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', range(1, 27)))
    start, end = 0, 0
    while True:
        end += 1
        if end == len(msg):
            answer.append(mydic[msg[start:end]])
            break
        if msg[start:end + 1] not in mydic:
            mydic[msg[start:end + 1]] = len(mydic) + 1
            answer.append(mydic[msg[start:end]])
            start = end
    return answer