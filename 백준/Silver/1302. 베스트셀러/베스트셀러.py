import sys
from collections import Counter
input = sys.stdin.readline
n = int(input())
data = [input().strip() for _ in range(n)]
counter = Counter(data)
max_count = max(counter.values())
max_words = [word for word, count in counter.items() if count == max_count]
max_words.sort()

print(max_words[0])