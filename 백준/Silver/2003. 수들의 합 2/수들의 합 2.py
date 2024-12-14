def solve(n, m, arr):
    s, e = 0, 0 
    total = arr[0]  
    cnt = 0  

    while e < n:
        if total < m:  
            e += 1
            if e < n:  
                total += arr[e]
        elif total == m:  
            cnt += 1
            total -= arr[s]
            s += 1
        else:  
            total -= arr[s]
            s += 1

    return cnt


n, m = map(int, input().split())
arr = list(map(int, input().split()))
print(solve(n, m, arr))