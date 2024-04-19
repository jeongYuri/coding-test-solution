def solution(arr1, arr2):
    row = len(arr1)
    col1 = len(arr1[0])
    col2 = len(arr2[0])
    answer = [[0]*col2 for _ in range(row)]
    for i in range(row):
        for j in range(col2):
            for k in range(col1):
                answer[i][j] += arr1[i][k]*arr2[k][j]
    return answer