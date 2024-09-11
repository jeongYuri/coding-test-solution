for _ in range(3):
    yut = list(map(int, input().split()))
    sum_yut = sum(yut)
    if sum_yut == 0:
        print('D')
    elif sum_yut == 1:
        print('C')
    elif sum_yut == 2:
        print('B')
    elif sum_yut == 3:
        print('A')
    else:
        print('E')