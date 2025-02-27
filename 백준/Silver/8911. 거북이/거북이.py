import sys
input = sys.stdin.readline

dx = [0,1,0,-1]
dy = [1,0,-1,0]
def control(tc):
    x,y = 0,0
    direction = 0
    min_x, max_x = 0,0
    min_y, max_y = 0,0
    for cmd in tc:
        if cmd == 'F':
            x += dx[direction]
            y += dy[direction]
        elif cmd == 'B':
            x -= dx[direction]
            y -= dy[direction]
        elif cmd == 'L':  # 왼쪽으로 90도 회전
            direction = (direction - 1) % 4
        elif cmd == 'R':  # 오른쪽으로 90도 회전
            direction = (direction + 1) % 4

        min_x, max_x = min(min_x, x), max(max_x, x)
        min_y, max_y = min(min_y, y), max(max_y, y)

    return (max_x - min_x) * (max_y - min_y)
t = int(input())
for _ in range(t):
    tc = input().strip()
    res = control(tc)
    print(res)
