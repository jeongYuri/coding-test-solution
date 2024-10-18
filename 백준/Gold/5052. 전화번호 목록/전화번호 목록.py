import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input()) #전화번호의 수
    numbers = [input().strip() for _ in range(n)]
    numbers.sort()
    is_consistent = True
    for i in range(n - 1):

        if numbers[i + 1].startswith(numbers[i]):
            is_consistent = False
            break

    if is_consistent:
        print('YES')
    else:
        print('NO')