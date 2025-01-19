import sys
input = sys.stdin.readline
s = input().strip()
pikachu = ['pi', 'ka', 'chu']

for p in pikachu:
    s = s.replace(p, ' ')

if s.strip() == '':
    print("YES")
else:
    print("NO")