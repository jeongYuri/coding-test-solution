from collections import deque
def solution(queue1, queue2):

    q1 = deque(queue1)
    q2 = deque(queue2)
    sum1, sum2 = sum(q1), sum(q2)

    target = (sum1 + sum2) // 2
    max_operations = len(q1) * 3 
    
    cnt = 0
    while cnt < max_operations:
        if sum1 == target:
            return cnt
        
        if sum1 > target:
            value = q1.popleft()
            q2.append(value)
            sum1 -= value
            sum2 += value
        else:
            value = q2.popleft()
            q1.append(value)
            sum2 -= value
            sum1 += value
        
        cnt += 1
    
    return -1