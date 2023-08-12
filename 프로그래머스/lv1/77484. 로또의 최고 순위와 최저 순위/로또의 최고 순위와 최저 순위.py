def solution(lottos, win_nums):
    max = 0
    min = 0
    win={6:1,5:2,4:3,3:4,2:5,1:6,0:6}
    for i in lottos:
        if i==0:
            max+=1
        else:
            if i in win_nums:
                max+=1
                min+=1
                
    return [win.get(max),win.get(min)]