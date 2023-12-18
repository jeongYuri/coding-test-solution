t = int(input())
def solv(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    elif n==3:
        return 4
    else:
        return solv(n-1)+solv(n-2)+solv(n-3)
for _ in range(t):
    n = int(input())
    result = solv(n)
    print(result)