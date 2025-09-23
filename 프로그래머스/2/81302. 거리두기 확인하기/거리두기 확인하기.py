from collections import deque

def bfs(p):
    start = []
    
    for i in range(5): 
        for j in range(5):
            if p[i][j] == 'P':
                start.append([i, j])
    
    for s in start:
        q = deque([s])  
        visited = [[0]*5 for i in range(5)]   
        dist = [[0]*5 for i in range(5)]  
        visited[s[0]][s[1]] = 1
        
        while q:
            y, x = q.popleft()
            dx = [-1, 1, 0, 0]  
            dy = [0, 0, -1, 1]  

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0<=nx<5 and 0<=ny<5 and visited[ny][nx] == 0:
                    
                    if p[ny][nx] == 'O':
                        q.append([ny, nx])
                        visited[ny][nx] = 1
                        dist[ny][nx] = dist[y][x] + 1
                    
                    if p[ny][nx] == 'P' and dist[y][x] <= 1:
                        return 0
    return 1


def solution(places):
    ans = []
    
    for i in places:
        ans.append(bfs(i))
    
    return ans