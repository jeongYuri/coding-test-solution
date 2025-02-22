import sys
from collections import defaultdict
input = sys.stdin.readline

n,m = map(int,input().split()) #입력 받을 걸그룹의 수, 맞혀야 할 문제의 수
members = defaultdict(list)
member_to_team = {}

for _ in range(n):
    team_name = input().strip()
    num = int(input().rstrip())
    for i in range(num):
        member_name = input().strip()
        members[team_name].append(member_name)
        member_to_team[member_name] = team_name  # 멤버 -> 팀 매핑
for team in members:
    members[team].sort()

for i in range(m):
    name = input().strip()
    quiz = int(input().rstrip())
    if quiz==0:
        for member in members[name]:
            print(member)
    else:
        print(member_to_team[name])

