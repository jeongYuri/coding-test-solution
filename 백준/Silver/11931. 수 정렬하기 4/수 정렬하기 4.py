import sys
input = sys.stdin.readline

n = int(input().strip())  #
numbers = [int(input().strip()) for _ in range(n)]
numbers.sort(reverse=True)

print("\n".join(map(str, numbers)))