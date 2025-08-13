import sys
input = sys.stdin.readline

x_s = []
y_s = []
for i in range(3):
    x,y = map(int,input().split())
    x_s.append(x)
    y_s.append(y)

for i in range(3):
    if x_s.count(x_s[i])==1:
        x4 = x_s[i]
    if y_s.count(y_s[i])==1:
        y4 = y_s[i]
print(x4,y4)