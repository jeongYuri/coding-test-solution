import sys

input = sys.stdin.readline

word = [input().strip() for _ in range(5)]
res = ''
for i in range(len(max(word, key=len))):
    for j in range(5):
        if i < len(word[j]):
            res += word[j][i]
print(res)
