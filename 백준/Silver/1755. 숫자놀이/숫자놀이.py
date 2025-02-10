import sys
input = sys.stdin.readline
def number_to_word(num):
    digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    return " ".join(digits[int(d)]for d in str(num))
def sort_numbers(m,n):
    numbers = list(range(m,n+1))
    numbers.sort(key=number_to_word)
    return numbers

m,n = map(int,input().split())
res = sort_numbers(m,n)
for i, num in enumerate(res):
    print(num, end=" " if (i + 1) % 10 != 0 else "\n")