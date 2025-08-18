import sys
input = sys.stdin.readline

n,b = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]

def multi(arr1,arr2):
    res = [[0]*n for _ in range(n)]
    for row in range(n):
        for col in range(n):
            s = sum(arr1[row][i]*arr2[i][col] for i in range(n))
            res[row][col] = s%10000
    return res
def power(n,a): #분할정복함수
    if n==1:
        return a
    if n%2==0:
        half = power(n//2,a)
        return multi(half,half)
    else: #홀수일경우
        return multi(a,power(n-1,a))

for row in power(b,a):
    print(*[r%1000 for r in row])