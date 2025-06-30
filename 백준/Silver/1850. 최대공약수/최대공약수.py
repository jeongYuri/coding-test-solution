import sys
import math
input = sys.stdin.readline

a,b = map(int,input().split())

gcd_len = math.gcd(a,b)
print("1" * gcd_len)