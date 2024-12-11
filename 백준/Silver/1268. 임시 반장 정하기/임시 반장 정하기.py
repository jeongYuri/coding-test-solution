n = int(input())
clas = [list(map(int, input().split())) for _ in range(n)]
same = [[0] * n for _ in range(n)]

for i in range(5):  
    for j in range(n):  
        for k in range(j + 1, n):  
            if clas[j][i] == clas[k][i]:  
                same[j][k] = 1
                same[k][j] = 1


cnt = [sum(row) for row in same]
print(cnt.index(max(cnt)) + 1)
