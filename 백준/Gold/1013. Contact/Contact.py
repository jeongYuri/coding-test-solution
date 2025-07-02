import sys
input = sys.stdin.readline
import re
t = int(input())
check = re.compile('(100+1+|01)+')

for i in range(t):
    a = check.fullmatch(input().rstrip())
    if  a==None:
        print("NO")
    else:
        print("YES")
