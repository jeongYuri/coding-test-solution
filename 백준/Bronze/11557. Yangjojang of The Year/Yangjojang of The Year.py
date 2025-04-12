import sys
input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    n = int(input())
    arr = {}
    for _ in range(n):
        name, liter = input().split()
        liter = int(liter)  
        arr.setdefault(name, []).append(liter)  

    winner = max(map(lambda x: sum(x), arr.values()))
    
    for name, liters in arr.items():
        if sum(liters) == winner:
            print(name)
            break
