import sys
input = sys.stdin.readline

t = int(input())
office = set()
for _ in range(t):
    name,state = map(str,input().split())
    if state =='enter':
        office.add(name)
    else:
        office.discard(name)
office = sorted(office,reverse = True)
for name in office:
    print(name)