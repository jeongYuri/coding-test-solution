s,e = map(int,input().split())
arr = []
for i in range(1,e+1):
    for j in range(i):
        arr.append(i)
print(sum(arr[s-1:e]))