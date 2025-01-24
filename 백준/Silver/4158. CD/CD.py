import sys
input = sys.stdin.readline
while True:
    n,m = map(int,input().split())
    if n==0 and m==0:
        break
    sang = list(int(input()) for _ in range(n))
    sun = list(int(input()) for _ in range(m))
    idx_n, idx_m = 0,0
    cnt = 0
    while idx_n<n and idx_m<m:
        if sang[idx_n]==sun[idx_m]:
            cnt +=1
            idx_n +=1
            idx_m +=1
        elif sang[idx_n]<sun[idx_m]:
            idx_n+=1
        else:
            idx_m+=1
    print(cnt)
