import sys
from math import gcd, sqrt
input = sys.stdin.readline
def divisors(numbers):
    value = numbers[0]
    for num in numbers[1:]:
        value = gcd(value, num)
    div = set()
    for i in range(1,int(sqrt(value))+1):
        if value % i==0:
            div.add(i)
            div.add(value//i)
    return sorted(div)
n = int(input())
numbers = list(map(int,input().split()))
res = divisors(numbers)
for r in res:
    print(r)
