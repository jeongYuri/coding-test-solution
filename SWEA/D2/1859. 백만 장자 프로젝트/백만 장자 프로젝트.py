t = int(input())
for tc in range(1,t+1):
    n = int(input())
    cost = list(map(int,input().split()))
    max_num = 0
    result = 0
    for i in range(len(cost)-1,-1,-1):
        if cost[i]>max_num:
            max_num = cost[i]
        else:
            result += max_num-cost[i]
    print(f'#{tc} {result}')