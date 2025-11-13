def solution(n):
    arr = [[0]*(i+1) for i in range(n)]
    x,y = -1,0
    num = 1
    for step in range(n):
        for _ in range(step,n):
            if step%3==0: #아래
                x+=1
            elif step%3==1: #오른쪽
                y+=1
            else: #왼쪽 위
                x-=1
                y-=1
            arr[x][y] = num
            num+=1
        
    return sum(arr,[])