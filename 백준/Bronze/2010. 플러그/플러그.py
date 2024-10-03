import sys
input = sys.stdin.readline

n = int(input())
multi = []
con = 1
for i in range(n):
    multi.append(int(input()))
    con+= multi[i]-1
print(con)