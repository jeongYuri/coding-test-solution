import sys
from itertools import combinations

input = sys.stdin.readline
n,m = map(int,input().split())

town = [list(map(int, input().split())) for _ in range(n)]
result = 999999
home = []
chick = []

for i in range(n):
    for j in range(n):
        if town[i][j] == 1:
            home.append([i, j])
        elif town[i][j] == 2:
            chick.append([i, j])

for selected_chickens in combinations(chick, m):
    dis = 0
    for t in home:
        chicken_distance = min([abs(t[0] - chi[0]) + abs(t[1] - chi[1]) for chi in selected_chickens])
        dis += chicken_distance
    result = min(result, dis)

print(result)