import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    r,e,c = map(int,input().split())
    if(r+c<e):
        print('advertise')
    elif (r+c==e):
        print('does not matter')
    else:
        print('do not advertise')