import sys
input = sys.stdin.readline
a,b,c = map(int,input().split())
d = int(input())
current_time = a*3600 + b*60 + c
end_time = current_time + d
h = (end_time//3600)%24
m = (end_time%3600)//60
s = (end_time%60)
print(h,m,s)