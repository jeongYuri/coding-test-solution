n = int(input())
no = [3, 6, 9]
result = []

for number in range(1, n + 1):
    numbers = []
    temp = number
    while temp > 0:
        digit = temp % 10
        if digit in no:
            numbers.append('-')
        temp //= 10

    if numbers:  
        result.append(''.join(reversed(numbers)))
    else:
        result.append(str(number)) 

print(" ".join(result))
