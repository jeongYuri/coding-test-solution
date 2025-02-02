import sys
input = sys.stdin.readline

cnt = 1
while True:
    name = []
    goods = set()
    n = int(input().strip())
    if n == 0:
        break
    else:
        for i in range(n):
            name.append(input().strip())

        for i in range(2*n-1):
            num, type = input().split()
            num = int(num)
            if num in goods:
                goods.remove(num)
            else:
                goods.add(num)

    print(cnt, name[goods.pop()-1])  
    cnt += 1
