import sys
input = sys.stdin.readline

text = input().rstrip()
cnt = 0
n = len(text)
substring = set()
for start in range(n):
    for end in range(start+1, n+1):
        substring.add(text[start:end])
print(len(substring))