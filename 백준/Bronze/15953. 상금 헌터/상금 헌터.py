import sys
input = sys.stdin.readline

t = int(input())

def cal(rank17,rank18):
    prize17 = [500,300,200,50,30,10]
    count17 = [1, 2, 3, 4, 5, 6]

    prize18 = [512, 256, 128, 64, 32]
    count18 = [1, 2, 4, 8, 16]
    res = 0

    if rank17>0:
        position  = 0
        while position<len(count17) and rank17>count17[position]:
            rank17-= count17[position]
            position+=1
        if position<len(prize17):
            res+= prize17[position]
    if rank18>0:
        position= 0
        while position<len(count18) and rank18>count18[position]:
            rank18 -= count18[position]
            position+=1
        if position< len(prize18):
            res+= prize18[position]
    return res*10000
for _ in range(t):
    a,b = map(int,input().split())
    print(cal(a,b))
