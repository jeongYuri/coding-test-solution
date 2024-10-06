import sys
input = sys.stdin.readline

def three_split(word):
    n = len(word)
    splits =[]
    for i in range(1,n-1):
        for j in range(i+1,n):
            part1 = word[:i]
            part2 = word[i:j]
            part3 = word[j:]
            splits.append((part1, part2, part3))
    return splits
def reverse_word(ans1):
    reverse_parts = [''.join(part[::-1])for part in ans1]
    return reverse_parts
def hab(ans):
    return (''.join(ans))

word = input().strip()
split_words = three_split(word)
results = []
for parts in split_words:
    reverse_part = reverse_word(parts)
    res = hab(reverse_part)
    results.append(res)
results = sorted(results)
print(results[0])