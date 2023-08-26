def solution(n):
    nums = [n]
    r = ((0,1),(1,0),(0,-1),(-1,0))
    answer = [[0 for i in range(n)] for j in range(n)] 
    count ,x,y = 0,-1,0
    
    while n>1:
        n -=1
        nums.append(n)
        nums.append(n)
        
    for i in range(len(nums)):
        for j in range(nums[i]):
            y+=r[i%4][0]
            x+=r[i%4][1]
            count +=1
            answer[y][x]=count
    return answer