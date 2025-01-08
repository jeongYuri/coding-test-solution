import sys
input = sys.stdin.readline

k = int(input())
for _ in range(k):
    arr = list(map(int,input().split()))
    n = arr[0]
    scores = arr[1:]
    max_score = max(scores)
    min_score = min(scores)
    score = sorted(scores,reverse=True)
    gap = 0
    for i in range(n-1):
        gap = max(gap, score[i] - score[i + 1])

    print(f"Class {_+1}")
    print(f"Max {max_score}, Min {min_score}, Largest gap {gap}")