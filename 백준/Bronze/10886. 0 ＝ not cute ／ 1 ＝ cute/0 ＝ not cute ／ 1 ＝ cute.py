import sys
input = sys.stdin.readline

n = int(input())
z = sum(1 for _ in range(n) if int(input()) == 0)  
c = n - z
print("Junhee is not cute!" if z > c else "Junhee is cute!")
