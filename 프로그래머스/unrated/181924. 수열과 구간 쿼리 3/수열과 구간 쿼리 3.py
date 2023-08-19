def solution(arr, queries):
    answer = []
    for ry in queries:
        s, e = ry        
        arr[s], arr[e] = arr[e], arr[s]
    return arr