import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    cnt= {}
    all_char = []
    words = input().split()
    for word in words:
        all_char.extend(list(word))

    for char in all_char:
        if char in cnt:
            cnt[char] += 1
        else:
            cnt[char] = 1

    max_f = max(cnt.values())
    most_chars = [char for char, count in cnt.items() if count == max_f]

    if len(most_chars) == 1:
        print(most_chars[0])
    else:
        print('?')