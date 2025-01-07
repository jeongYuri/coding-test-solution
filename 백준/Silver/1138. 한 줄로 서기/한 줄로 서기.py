import sys
input = sys.stdin.readline

n = int(input())
people = list(map(int,input().split()))
res = [0]*n
for i in range(n):
    cnt = 0
    for j in range(n):
        if res[j]==0:
            cnt +=1
        if cnt == people[i]+1:
            res[j] = i+1
            break
print(*res)