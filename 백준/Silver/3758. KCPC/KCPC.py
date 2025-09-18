import sys
from collections import defaultdict
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n,k,id,m = map(int,input().split())
    infos = defaultdict(list)
    score = defaultdict(dict)
    submits = defaultdict(int)
    last = defaultdict(int)
    for idx in range(1,m+1):
        i,j,s = map(int,input().split())
        infos[i].append((j,s))
        submits[i]+=1
        last[i] = idx
        if j not in score[i] or s>score[i][j]:
            score[i][j] = s
    res = {}
    for i in range(1, n + 1):
        temp = sum(score[i].values()) if i in score else 0
        res[i] = temp
    teams = []
    for i in range(1, n + 1):
        teams.append((-res[i], submits[i], last[i], i))
    teams.sort()
    for rank, (_, _, _, team_id) in enumerate(teams, start=1):
        if team_id == id:
            print(rank)
            break