import sys
input = sys.stdin.readline

word = input().strip()
total = 10
for i in range(1, len(word)):
    if word[i] == word[i-1]:
        total += 5
    else:
        total += 10
print(total)