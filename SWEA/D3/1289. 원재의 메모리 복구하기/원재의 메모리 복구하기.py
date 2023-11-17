t = int(input())
for tc in range(1,t+1):
    arr = list(input())
    n = ['0']*len(arr)
    cnt = 0
    for i in range(len(arr)):
        if n[i]!=arr[i]:
            n[i:]= arr[i]*len(n[i:])
            cnt +=1
    print('#{} {}'.format(tc, cnt))