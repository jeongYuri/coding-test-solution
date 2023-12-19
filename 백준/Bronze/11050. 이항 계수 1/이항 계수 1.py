def coef_factorial(n,k):
    if k==0 or n==k:
        return 1
    return coef_factorial(n-1,k)+coef_factorial(n-1,k-1)

n,k = map(int,input().split())
result = coef_factorial(n,k)
print(result)