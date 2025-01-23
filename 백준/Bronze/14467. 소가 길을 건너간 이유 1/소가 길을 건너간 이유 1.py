import sys
input = sys.stdin.readline
n = int(input())
cow = {}
cnt = 0
for i in range(n):
    num, position = map(int,input().split())
    if num in cow:
        if cow[num]!=position:
            cnt +=1
    cow[num] = position
print(cnt)