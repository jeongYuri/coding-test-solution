import sys
from collections import Counter
input = sys.stdin.readline

n,c = map(int,input().split())
message = list(map(int,input().split()))
freq = Counter(message)
sorted_message = sorted(message, key=lambda x: (-freq[x], message.index(x)))
print(*sorted_message)