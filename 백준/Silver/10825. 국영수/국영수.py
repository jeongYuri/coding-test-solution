import sys
input = sys.stdin.readline

n = int(input())
scores = []
for _ in range(n):
    data = input().split()
    name = data[0]
    ko, en, math = map(int,data[1:])
    scores.append((name, ko, en, math))
scores.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
for score in scores:
    print(score[0])