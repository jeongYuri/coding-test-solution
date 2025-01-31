import sys
from collections import Counter

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    number = list(map(int, input().split()))
    team = []
    for i in range(n):
        team.append((i + 1, number[i]))

    team_cnt = Counter(number)

    final = []
    for idx, team_num in team:
        if team_cnt[team_num] >= 6:
            final.append((idx, team_num))


    final.sort(key=lambda x: x[0])
    re_ranked = []
    new_rank = 1
    for old_idx, team_num in final:
        re_ranked.append((new_rank, team_num))
        new_rank += 1

    ranking = {}
    for rnk, tnum in re_ranked:
        if tnum not in ranking:
            ranking[tnum] = []
        ranking[tnum].append(rnk)

    ans = {}
    for k, v in ranking.items():
        ans[k] = sum(v[:4])

    min_score = min(ans.values())
    candidates = [k for k, v in ans.items() if v == min_score]

    if len(candidates) > 1:
        plus = {}
        for c in candidates:
            plus[c] = ranking[c][4]
        m = min(plus.values())
        candidates = [k for k, v in plus.items() if v == m]

    if len(candidates) > 1:
        plus = {}
        for c in candidates:
            plus[c] = ranking[c][5]
        m = min(plus.values())
        candidates = [k for k, v in plus.items() if v == m]
    print(min(candidates))
