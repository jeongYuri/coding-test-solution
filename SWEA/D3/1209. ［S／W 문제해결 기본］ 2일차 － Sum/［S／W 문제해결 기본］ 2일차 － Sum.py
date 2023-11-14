for tc in range(1, 11):
    m = int(input())
    n = 100  # 변경된 코드: n을 직접 지정
    nums = [list(map(int, input().split())) for _ in range(n)]
    first_sum = 0
    second_sum = 0
    result = []

    for i in range(n):
        col = 0
        row = 0
        first_sum += nums[i][i]
        second_sum += nums[i][n - 1 - i]
        for j in range(n):
            col += nums[i][j]
            row += nums[j][i]
        result.extend([col, row])

    result.extend([first_sum, second_sum])
    print(f'#{tc} {max(result)}')