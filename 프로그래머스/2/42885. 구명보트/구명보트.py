from collections import deque

def solution(people, limit):
    people.sort()
    people = deque(people)
    cnt = 0
    
    while people:
        if len(people) == 1:
            cnt += 1
            break

        if people[0] + people[-1] <= limit:
            people.popleft()
        
        people.pop()
        cnt += 1
    
    return cnt