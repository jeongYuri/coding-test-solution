import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    candy, box = map(int,input().split())
    box_list = []
    for _ in range(box):
        r,c = map(int,input().split())
        box_list.append(r*c)
    box_list.sort(reverse = True)
    cnt = 0
    for v in box_list:
        candy -= v
        cnt +=1
        if candy<=0:
            break
    print(cnt)
