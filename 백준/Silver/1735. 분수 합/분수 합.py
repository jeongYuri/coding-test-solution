import sys
import math
input = sys.stdin.readline

a, b = map(int, input().split())
c, d = map(int, input().split())
numerator = a * d + b * c
denominator = b * d
gcd = math.gcd(numerator, denominator)
numerator //= gcd
denominator //= gcd

print(numerator, denominator)