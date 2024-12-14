import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = set(input().strip() for _ in range(n))  
test = [input().strip() for _ in range(m)]

cnt = sum(1 for word in test if word in s)

print(cnt)