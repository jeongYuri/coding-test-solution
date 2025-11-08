def solution(park, routes):
    answer = []
    directions = {'N':(-1,0),'S':(1,0),'W':(0,-1),'E':(0,1)}
    h,w = 0,0
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j]=='S':
                h,w = i,j
    for route in routes:
        d,n = route.split()
        n = int(n)
        dh,dw = directions[d]
        nh,nw = h,w
        sucess = True
        for _ in range(n):
            nh+=dh
            nw+=dw
            if not(0<=nh<len(park) and 0<=nw<len(park[0])):
                sucess = False
                break
            if park[nh][nw]=='X':
                sucess = False
                break
        if sucess:
            h,w = nh,nw
    return [h,w]
        
    return answer