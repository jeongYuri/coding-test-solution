import sys
input = sys.stdin.readline

n = int(input())
infor = []
for _ in range(n):
    name, dd, mm, yyyy = input().split()
    infor.append((name, int(dd), int(mm), int(yyyy)))
infor.sort(key=lambda x: (x[3], x[2], x[1]))
print(infor[-1][0])
print(infor[0][0])