def findcount(array, n):
    count = 0
    for i in range(len(array)):
        for j in range(len(array)-n+1):
            if array[i][j:j+n] == array[i][j:j+n][::-1]:
                 count += 1
    return count

for tc in range(1, 11):
    n = int(input())
    array = [list(input())for _ in range(8)]
    array90 = list(zip(*array))
    count = findcount(array, n) + findcount(array90, n)

    print(f'#{tc} {count}')