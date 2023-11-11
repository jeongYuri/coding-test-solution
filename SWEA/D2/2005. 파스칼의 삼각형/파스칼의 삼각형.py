t = int(input())
for tc in range(1,t+1):
    n = int(input())
    pascal = [[1]]
    for i in range(1,n):
        row =[1]
        for j in range(1,i):
            num = pascal[i-1][j-1]+pascal[i-1][j]
            row.append(num)
        row.append(1)
        pascal.append(row)
    print(f'#{tc}')
    for row in pascal:
        for num in row:
            print(num, end=' ')
        print()