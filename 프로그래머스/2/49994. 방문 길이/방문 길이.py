def solution(dirs):
    udrl = {'U':(0,1),'D':(0,-1),'R':(1,0),'L':(-1,0)}
    x,y = 0,0
    ans = set()
    for d in dirs:
        dx,dy = udrl[d]
        nx, ny = x+dx, y+dy
        if abs(nx)<=5 and abs(ny)<=5:
            ans.add((x,y,nx,ny))
            ans.add((nx,ny,x,y))
            x = nx
            y = ny
    return len(ans)//2