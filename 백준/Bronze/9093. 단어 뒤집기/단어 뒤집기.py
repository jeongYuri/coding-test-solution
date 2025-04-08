import sys
input = sys.stdin.readline
n = int(input())

for _ in range(n):
    str = input().rstrip()
    words = list(str.split())
    reverse_words = []

    for word in words:
        reverse_words.append(word[::-1])

    answer = " ".join(reverse_words)
    print(answer)