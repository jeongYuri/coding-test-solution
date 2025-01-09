
import sys
input=sys.stdin.readline

a,b=map(int,input().split())
ac=set(map(int,input().split()))
bc=set(map(int,input().split()))
ans = ac - bc
print(len(ans))
print(*sorted(ans))