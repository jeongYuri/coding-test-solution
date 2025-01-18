import sys
input = sys.stdin.readline

n, game = map(str,input().split())
n = int(n)
players = set(input().rstrip() for _ in range(n))
p = len(players)
if game=='Y':
    print(p)
elif game=='F':
    print(p//2)
else:
    print(p//3)
