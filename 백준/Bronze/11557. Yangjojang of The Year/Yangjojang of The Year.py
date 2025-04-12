import sys
input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    n = int(input())
    arr = {}
    for _ in range(n):
        name,liter = map(str,input().split())
        if name not in arr:
            arr[name] = []
        arr[name].append(int(liter))
    winner = max(sum(liter) for liter in arr.values())
    for name in arr:
        if sum(arr[name])== winner:
            print(name)
            break

