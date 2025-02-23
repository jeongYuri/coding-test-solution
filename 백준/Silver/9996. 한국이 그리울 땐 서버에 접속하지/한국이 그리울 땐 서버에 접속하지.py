import sys
input = sys.stdin.readline

n = int(input())
pattern = str(input().strip())
files = [input().strip() for _ in range(n)]

prefix, suffix = pattern.split('*')

for file in files:
    if len(file)<len(prefix) + len(suffix):
        print("NE")
    elif file.startswith(prefix) and file.endswith(suffix):
        print("DA")
    else:
        print("NE")


