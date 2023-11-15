def findcount(array, k):
    for i in range(k//2):
        if array[i]!=array[-1-i]:
            return False
    return True

for _ in range(1, 11):
    n = int(input())
    m = 100
    array = [list(input())for _ in range(100)]
    res = 1
    flag = False
    array90 = list(zip(*array))
    for k in range(100,1,-1):
        for i in range(m):
            for j in range(m-k+1):
                if findcount(array[i][j:j+k],k)or findcount(array90[i][j:j+k],k):
                    res,flag = k,True
                    break
            if flag:
                break
        if flag:
            break

    print(f'#{n} {res}')