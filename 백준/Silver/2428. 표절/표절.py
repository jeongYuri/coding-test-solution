import sys
input = sys.stdin.readline

n = int(input())
file = list(map(int,input().split()))
file.sort(reverse=True)
cnt = 0

for i in range(n-1):
    if file[i]*0.9<=file[-1]:
        cnt+= n-i-1
        continue
    s,e = i+1, n-1
    while s<=e:
        m = (s+e)//2
        if file[m]>=file[i]*0.9:
            s = m+1
        else:
            e = m-1
    cnt+= e-i
print(cnt)