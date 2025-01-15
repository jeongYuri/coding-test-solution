import sys

input = sys.stdin.readline

x,y = map(int,input().split()) #가로와 세로
k = int(input()) #칼로 잘라야하는 점선의 개수
x_cut = [0,x]
y_cut = [0,y]
for _ in range(k):
    a,b = map(int,input().split())
    if a==0:
        y_cut.append(b)
    elif a==1:
        x_cut.append(b)
x_cut.sort()
y_cut.sort()

sub_x = []
sub_y = []
for i in range(len(x_cut)-1):
    sub_x.append(x_cut[i+1]-x_cut[i])
for i in range(len(y_cut)-1):
    sub_y.append(y_cut[i+1]-y_cut[i])
print(max(sub_x)*max(sub_y))
