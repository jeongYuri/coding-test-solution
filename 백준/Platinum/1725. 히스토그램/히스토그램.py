import sys
input = sys.stdin.readline

n = int(input())
hist = [int(input()) for _ in range(n)] + [0] 
stack = [-1]
max_area = 0

for i in range(n+1):
    while stack[-1] != -1 and hist[stack[-1]] >= hist[i]:
        idx = stack.pop()
        h = hist[idx]
        width = i-stack[-1]-1
        max_area  = max(max_area,h*width)
    stack.append(i)
print(max_area)