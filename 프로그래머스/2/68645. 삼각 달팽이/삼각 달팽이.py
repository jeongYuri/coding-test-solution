def solution(n):
    triangle = [[0] * n for _ in range(n)]
    directions = [(1, 0), (0, 1), (-1, -1)]  
    num = 1
    x, y = -1, 0
    direction_idx = 0
    for i in range(n):
        for j in range(i, n):
            dx, dy = directions[direction_idx]
            x, y = x + dx, y + dy
            triangle[x][y] = num
            num += 1
        direction_idx = (direction_idx + 1) % 3
    answer = []
    for row in triangle:
        for num in row:
            if num != 0:
                answer.append(num)
    return answer