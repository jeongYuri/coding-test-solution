import sys
input = sys.stdin.readline

n = int(input())
x_nums = []
y_nums = []

for _ in range(n):
    x,y = map(int,input().split())
    x_nums.append(x)
    y_nums.append(y)

res_x = max(x_nums)-min(x_nums)
res_y = max(y_nums)-min(y_nums)
print(res_x*res_y)