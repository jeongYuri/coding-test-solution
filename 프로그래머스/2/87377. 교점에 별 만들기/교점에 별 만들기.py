def solution(line):
    points = []
    min_x, min_y = float('inf'), float('inf')
    max_x, max_y = float('-inf'), float('-inf')   
    n = len(line)
    for i in range(n):
        for j in range(i + 1, n):
            A, B, E = line[i]
            C, D, F = line[j]
            d = A * D - B * C
            if d == 0:  
                continue

            x_n = B * F - E * D
            y_n = E * C - A * F
            
            if x_n % d == 0 and y_n % d == 0: 
                x = x_n // d
                y = y_n // d
                points.append((x, y))
                min_x, min_y = min(min_x, x), min(min_y, y)
                max_x, max_y = max(max_x, x), max(max_y, y)

    width = max_x - min_x + 1
    height = max_y - min_y + 1
    grid = [['.'] * width for _ in range(height)]

    for x, y in points:
        grid[max_y - y][x - min_x] = '*'

    return [''.join(row) for row in grid]