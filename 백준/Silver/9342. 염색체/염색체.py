import re

pattern = re.compile(r'^[A-F]?A+F+C+[A-F]?$')

t = int(input())
for _ in range(t):
    s = input().strip()
    if pattern.fullmatch(s):
        print("Infected!")
    else:
        print("Good")
