def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        arr=bin(arr1[i]|arr2[i])[2:].zfill(n)
        a= arr.replace("1","#").replace("0"," ")
        answer.append(a)
    return answer