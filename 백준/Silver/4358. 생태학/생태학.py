import sys
from collections import Counter

input = sys.stdin.read
trees = input().split("\n")[:-1]
cnt = len(trees)

freq = Counter(trees)

for name in sorted(freq):
    print(f"{name} {freq[name] / cnt * 100:.4f}")