def solution(progresses, speeds):
    answer = []
    while progresses:
        remain = (100 - progresses[0] + speeds[0] - 1) // speeds[0]
        count = 0
        while progresses and progresses[0] + speeds[0] * remain >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count +=1
        answer.append(count)
    return answer