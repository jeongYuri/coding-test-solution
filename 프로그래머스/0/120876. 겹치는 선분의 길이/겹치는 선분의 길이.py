def solution(lines):
    arr = [0]*201
    for s,e in lines:
        s += 100
        e += 100
        for i in range(s,e):
            arr[i]+=1
    return sum(1 for x in arr if x>1)