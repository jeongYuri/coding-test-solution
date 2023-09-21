def solution(priorities, location):
    answer = 0
    queue = [(p, idx) for idx, p in enumerate(priorities)]
    while queue:
        front = queue.pop(0)
        priority, idx = front
        if any(priority<p for p, _ in queue):
            queue.append(front)
        else:
            answer +=1
            if idx == location:
                return answer
    return answer