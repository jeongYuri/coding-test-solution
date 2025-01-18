import sys
from collections import Counter
input = sys.stdin.readline


n  = int(input())
students = []
for _ in range(n):
    country, num, score = map(int, input().split())
    students.append((country, num, score))
students.sort(key=lambda x: x[2], reverse=True)
medals = {}
win = []
for country, num, score in students:
    if len(win)==3:
        break
    if medals.get(country,0)<2:
        win.append((country, num))
        medals[country] = medals.get(country,0)+1
for winner in win:
    print(winner[0],winner[1])