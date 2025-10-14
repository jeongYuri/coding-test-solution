import sys
input = sys.stdin.readline

n,r = map(int,input().split())
volunteers = set(map(int,input().split()))

all_volunteer = set(range(1,n+1))
missing = all_volunteer.difference(volunteers)
res = sorted(list(missing))
if not res:
    print("*")
else:
    ans = ' '.join(map(str,res))+ ' '
    print(ans)