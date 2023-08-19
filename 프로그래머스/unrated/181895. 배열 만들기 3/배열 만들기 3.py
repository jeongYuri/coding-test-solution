def solution(arr, intervals):
    first = intervals[0]
    second = intervals[1]
    new = arr[first[0]:first[1]+1] + arr[second[0]:second[1]+1]
    return new