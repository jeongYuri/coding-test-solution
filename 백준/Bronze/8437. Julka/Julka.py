import sys
input = sys.stdin.readline

S = int(input())  
D = int(input()) 
N = (S - D) // 2 
K = N + D       

print(K)  
print(N) 