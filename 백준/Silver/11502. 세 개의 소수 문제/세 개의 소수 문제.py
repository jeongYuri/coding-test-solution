import sys
input = sys.stdin.readline
def ans(x, sosu):
    for i in sosu:
        for j in sosu:
            for k in sosu:
                if i+j+k == x:
                    print(i,j,k)
                    return
n = 997
sosu =[] 
arr = [False, False]+([True]*(n-1)) #인덱스 0,1은 False(소수가 아님!!), 나머지는 True
for i in range(2,n+1):
    if arr[i]:
        sosu.append(i)
    for j in range(i*2,n,i): #i의 배수를 모두 false로 만들어...
        arr[j]  = False
t = int(input())
for _ in range(t):
    k = int(input())
    ans(k,sosu)
