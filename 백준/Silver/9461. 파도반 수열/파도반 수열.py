import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    arr = []
    for i in range(1,n+1):
        if i<=3:
            arr.append(1)
        elif i>3:
            num = arr[i-3]+arr[i-4]
            arr.append(num)
    print(arr[-1])