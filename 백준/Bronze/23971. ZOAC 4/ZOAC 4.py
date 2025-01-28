import sys
input = sys.stdin.readline

h,w,n,m = map(int,input().split())
seats = ((h+n) // (n+1)) * ((w+m) // (m+1))
print(seats)

