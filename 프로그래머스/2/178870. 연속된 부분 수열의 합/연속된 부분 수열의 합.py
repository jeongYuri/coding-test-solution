def solution(sequence, k):
    n = len(sequence)
    start, end = 0,0
    total = sequence[0]
    res = [0,n-1]
    while start<n and end<n:
        if total==k:
            if (end-start)<(res[1]-res[0]):
                res=[start, end]
            start +=1
            if start<n:
                total -= sequence[start-1]
        elif total<k:
            end+=1
            if end<n:
                total += sequence[end]
        else:
            total -= sequence[start]
            start+=1
    return res