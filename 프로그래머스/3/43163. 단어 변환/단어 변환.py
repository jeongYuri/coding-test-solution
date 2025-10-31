from collections import deque
def solution(begin, target, words):
    if target not in words:
        return 0
    q = deque([(begin,0)])
    visited = set()
    while q:
        word, step = q.popleft()
        if word==target:
            return step
        for w in words:
            if w not in visited and sum(a!=b for a,b in zip(word, w))==1:
                visited.add(w)
                q.append((w,step+1))
    return 0
    
