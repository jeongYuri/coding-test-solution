import sys
input = sys.stdin.readline
def split_digits(n):
    if n<10:
        n = f"{n:02d}"
    return[int(digit) for digit in str(n)]
n = int(input().strip())
start = n
cycle = 0
while True:
    numbers = split_digits(n)
    new = sum(numbers)
    n = (numbers[1]*10) + (new%10)
    cycle +=1
    if n==start:
        break
print(cycle)
