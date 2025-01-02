import sys
input = sys.stdin.readline
def rank(scores,taesu):
    scores.sort(reverse=True)
    ranks = {}
    rank = 1
    for i, score in enumerate(scores):
        if score not in ranks:
            ranks[score] = rank
        rank+=1
    return ranks[taesu]
n,taesu, p = map(int,input().split())
if n==0:
    print(1)
else:
    scores = list(map(int,input().split()))
    scores.append(taesu)
    res = rank(scores,taesu)
    if n==p and taesu<=scores[-1]:
        print(-1)
    else:
        print(res)