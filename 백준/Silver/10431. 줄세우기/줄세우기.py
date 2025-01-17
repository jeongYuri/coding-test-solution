import sys
input = sys.stdin.readline
t = int(input())
tall = []
for _ in range(t):
    tall= list(map(int,input().split()))
    total = 0
    for i in range(1,len(tall)-1):
        for j in range(i+1, len(tall)):
            if tall[i]>tall[j]:
                tall[i],tall[j] = tall[j],tall[i]
                total+=1
    print(tall[0], total)

