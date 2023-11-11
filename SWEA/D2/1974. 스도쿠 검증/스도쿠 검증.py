t = int(input())
for tc in range(1, t + 1):
    board = [list(map(int, input().split())) for _ in range(9)]
    result = 1
    for row in board:
        check = []
        for r in row:
            check.append(r)
            if len(set(check))!=len(check):
                result = 0
                break

    for i in range(9):
        check=[]
        for j in range(9):
            check.append(board[j][i])
        if len(set(check))!=len(check):
            result = 0
            break

    for i in range(0,9,3):
        for j in range(0,9,3):
            check = []
            for x in range(3):
                for y in range(3):
                    check.append(board[i + x][j + y])
            if len(set(check)) != len(check):
                result = 0
                break

    print(f'#{tc} {result}')



