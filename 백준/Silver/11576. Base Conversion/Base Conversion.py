import sys
input = sys.stdin.readline
def to_decimal(a_base, digits):
    decimal = 0
    power = len(digits)-1
    for digit in digits:
        decimal += digit*(a_base**power)
        power -=1
    return decimal
def from_decimal(b_base, decimal):
    result = []
    while decimal>0:
        result.append(decimal%b_base)
        decimal//=b_base
    return result[::-1]
a,b = map(int,input().split())
m= int(input())
digits = list(map(int, input().split()))

decimal_value = to_decimal(a, digits)
res = from_decimal(b,decimal_value)
print(*res)