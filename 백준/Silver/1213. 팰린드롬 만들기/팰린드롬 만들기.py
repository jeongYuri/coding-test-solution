from collections import Counter
import sys

word = sys.stdin.readline().strip()
char_count = Counter(word)

odd_chars = [char for char, count in char_count.items() if count % 2 == 1]
if len(odd_chars) > 1:
    print("I'm Sorry Hansoo")
else:
    mid = odd_chars[0] if odd_chars else ''

    half_palindrome = ''.join(char * (count // 2) for char, count in sorted(char_count.items()))

    print(half_palindrome + mid + half_palindrome[::-1])