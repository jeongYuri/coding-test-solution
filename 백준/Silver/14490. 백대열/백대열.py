import sys
input = sys.stdin.readline
import math
n,m = map(int,input().split(':'))
g = math.gcd(n, m)
n =n//g
m =m//g
print(f"{n}:{m}")

