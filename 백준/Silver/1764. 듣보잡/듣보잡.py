import sys
input = sys.stdin.readline

n,m = map(int,input().split())
names = [input().strip() for _ in range(1,n+m+1)]
result = []

see = set(names[0:n])
listen = set(names[n:])
result = sorted(list(see&listen))
print(len(result))

for p in result:
    print(p)