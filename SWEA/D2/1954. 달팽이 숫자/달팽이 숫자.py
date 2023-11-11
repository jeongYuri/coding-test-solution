t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = [[0] * n for _ in range(n)]
    d = 1
    x, y = -1, 0
    num = 1
    size = n
    while size > 0:
        for _ in range(size):
            x += d
            arr[y][x] = num
            num +=1
        size -= 1
        for _ in range(size):
            y += d
            arr[y][x] = num
            num +=1
        d *= -1
    print(f'#{tc}')
    for i in range(len(arr)):
        print(*arr[i])