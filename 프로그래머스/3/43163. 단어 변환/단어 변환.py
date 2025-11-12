from collections import deque
def solution(begin, target, words):
    visited = set()
    q  = deque([(begin,0)])
    while q:
        word, step = q.popleft()
        if word==target:
            return step
        for w in words:
            if w not in visited and sum(a!=b for a,b in zip(word, w))==1:
                visited.add(w)
                q.append((w,step+1))
                
        
    return 0