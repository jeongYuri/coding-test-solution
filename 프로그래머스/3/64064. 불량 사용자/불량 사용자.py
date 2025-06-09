import re
from itertools import permutations

def solution(user_id, banned_id):
    matches = []
    
    for b in banned_id:
        pattern = '^' + b.replace('*', '.') + '$'
        candidates = [u for u in user_id if re.match(pattern, u)]
        matches.append(candidates)
    res = set()
    
    def dfs(depth, path):
        if depth == len(banned_id):
            if len(set(path)) == len(banned_id):
                res.add(tuple(sorted(path)))
            return
        for user in matches[depth]:
            if user not in path:
                dfs(depth+1,path+[user])
    dfs(0, [])
    return len(res)