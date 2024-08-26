import sys
input = sys.stdin.readline

a = input().rstrip()
b = input().rstrip()
c = input().rstrip()
result1 = int(a) + int(b) - int(c)
combined_number = int(a + b)
result2 = combined_number - int(c)

print(result1)
print(result2)  