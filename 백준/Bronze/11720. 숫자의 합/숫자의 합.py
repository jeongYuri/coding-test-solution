import sys
input = sys.stdin.readline
n = int(input().strip())  
num = input().strip()    
total = sum(int(digit) for digit in num)  
print(total)