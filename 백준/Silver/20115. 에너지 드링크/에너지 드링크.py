import sys
input = sys.stdin.readline

n = int(input())
energy = list(map(int,input().split()))
energy.sort()

while len(energy)>1:
    smallest = energy.pop(0)  
    energy[-1] += smallest / 2
result = energy[-1]
print(int(result) if result.is_integer() else result)

