import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    arr = list(input().split())
    num = float(arr[0])
    for i in arr[1:]:
        if i=='@':
            num*=3
        elif i=='%':
            num+=5
        else:
            num-=7
    print(f"{num:.2f}")

