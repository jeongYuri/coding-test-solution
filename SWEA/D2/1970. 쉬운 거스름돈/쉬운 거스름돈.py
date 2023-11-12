t = int(input())
for tc in range(1,t+1):
    n = int(input())
    cost = [50000,10000,5000,1000,500,100,50,10]
    result = []
    for i in range(len(cost)):
        if cost[i]>n:
            result.append(0)
        elif n>=cost[i]:
            result.append(n//cost[i])
        n%=cost[i]

    print(f'#{tc}')
    print(f'{" ".join(map(str, result))}')