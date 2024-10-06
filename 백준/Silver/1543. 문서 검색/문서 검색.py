import sys
input = sys.stdin.readline

text = input().strip()
find_word = input().strip()

cnt = 0
idx = 0
while idx<=len(text)-len(find_word):
    if text[idx:idx+len(find_word)] == find_word:
        cnt +=1
        idx += len(find_word)
    else:
        idx +=1
print(cnt)