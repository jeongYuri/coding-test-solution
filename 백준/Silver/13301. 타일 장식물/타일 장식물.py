import sys
input = sys.stdin.readline
n = int(input())
p = [0] * 81
p[0] = 4
p[1] = 6
for i in range(2,n+1):
    p[i] = p[i-1]+p[i-2]
print(p[n-1])