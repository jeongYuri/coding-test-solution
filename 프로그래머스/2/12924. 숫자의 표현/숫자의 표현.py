def solution(n):
    cnt = 0
    i = 1
    while i*i<=n:
        if n%i==0:
            j = n//i
            if i%2==1:
                cnt+=1
            if j!=i and j%2==1:
                cnt+=1
        i+=1
    return cnt
                