import sys
input = sys.stdin.readline

n = int(input())
straw = [int(input())for _ in range(n)]
straw.sort(reverse = True)

res = -1

for i in range(n-2):
    if straw[i]<straw[i+1]+straw[i+2]:
        res = straw[i]+straw[i+1]+straw[i+2]
        break
print(res)
