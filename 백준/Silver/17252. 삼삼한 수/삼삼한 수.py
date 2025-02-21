import sys
input = sys.stdin.readline

n = int(input())
if n==0:
    print("NO")
    sys.exit(0)
while n>0:
    if n%3==2:
        print("NO")
        sys.exit(0)
    n//=3

print("YES")