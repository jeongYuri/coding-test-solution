import sys
input = sys.stdin.readline
a,b,c,d,e,f = map(int,input().split())

x,y =  0,0

print((c*e-b*f)//(a*e-b*d),(a*f-d*c)//(a*e-b*d))