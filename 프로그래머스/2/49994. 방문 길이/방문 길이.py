def solution(dirs):
    answer = 0
    Map = []
    x,y = 5,5
    move = {'U':(0,-1),'D':(0,1),'R':(1,0),'L':(-1,0)}
    for i in range(len(dirs)):
        (dx,dy) = move[dirs[i]]
        if not(0<=x+dx and x+dx<=10 and 0<=y+dy and y+dy<=10):
            continue
        Map.append((x,y,x+dx,y+dy))
        Map.append((x+dx,y+dy,x,y))
        x = x + dx
        y = y + dy
        Mapset = set(Map)
        answer = len(Mapset)//2
    return answer