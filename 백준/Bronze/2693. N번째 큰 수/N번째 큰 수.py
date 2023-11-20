t = int(input())
for tc in range(1,t+1):
    arr = list(map(int,input().split()))
    arr.sort(reverse=True)
    print(arr[2])