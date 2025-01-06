import sys
input = sys.stdin.readline
n = int(input())
dasom = int(input())
candi = [int(input()) for _ in range(n-1)]
res= 0
if not candi:
    print(0)
    exit()

while max(candi) >=dasom:
    candi.sort(reverse=True)
    candi[0]-=1
    dasom +=1
    res +=1
print(res)
