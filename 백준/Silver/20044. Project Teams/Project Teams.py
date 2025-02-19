n = int(input())
skills = sorted(map(int, input().split()))

teams = [skills[i] + skills[-(i+1)] for i in range(n)]
print(min(teams))