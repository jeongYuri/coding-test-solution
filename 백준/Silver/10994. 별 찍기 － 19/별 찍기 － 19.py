import sys
input = sys.stdin.readline


def draw_star(n, x, y):
    if n == 1:
        arr[x][y] = '*'
        return

    length = 4 * n - 3

    for i in range(length):
        arr[x][y + i] = '*'  # 위쪽
        arr[x + i][y] = '*'  # 왼쪽
        arr[x + length - 1][y + i] = '*'  # 아래쪽
        arr[x + i][y + length - 1] = '*'  # 오른쪽

    draw_star(n - 1, x + 2, y + 2)


N = int(input())
size = 4 * N - 3
arr = [[' '] * size for _ in range(size)]

draw_star(N, 0, 0)

for row in arr:
    print(''.join(row))