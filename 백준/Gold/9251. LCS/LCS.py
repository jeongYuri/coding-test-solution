import sys
input = sys.stdin.readline
a = list(map(str, input().rstrip()))
b = list(map(str, input().rstrip()))
LCS = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
max_row = [0] * len(a)
max_col = [0] * len(b)

for i in range(1, len(a) + 1):
    for j in range(1, len(b) + 1):
        if a[i - 1] == b[j - 1]:
            LCS[i][j] = LCS[i - 1][j - 1] + 1
        else:
            LCS[i][j] = max(LCS[i - 1][j], LCS[i][j - 1])


        max_row[i - 1] = max(max_row[i - 1], LCS[i][j])


for j in range(1, len(b) + 1):
    max_col[j - 1] = max(row[j] for row in LCS)


print(max(max(max_row), max(max_col)))