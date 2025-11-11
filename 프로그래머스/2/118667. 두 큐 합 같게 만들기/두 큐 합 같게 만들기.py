from collections import deque
def solution(queue1, queue2):
    q1, q2 = deque(queue1), deque(queue2)
    sum1, sum2 = sum(q1), sum(q2)
    total = sum1 + sum2
    cnt = 0
    limit = len(q1) * 3 

    while cnt <= limit:
        if sum1 == sum2:
            return cnt
        if sum1 > sum2:
            val = q1.popleft()
            q2.append(val)
            sum1 -= val
            sum2 += val
        else:
            val = q2.popleft()
            q1.append(val)
            sum2 -= val
            sum1 += val
        cnt += 1

    return -1
