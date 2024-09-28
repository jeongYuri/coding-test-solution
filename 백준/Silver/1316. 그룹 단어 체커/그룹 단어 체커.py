import sys
input = sys.stdin.readline

n = int(input())
words = [input().rstrip() for _ in range(n)]
cnt = 0
for text in words:
    is_group = True
    for i in range(len(text) - 1):  
        if text[i] != text[i + 1]:
            if text[i + 1] in text[:i + 1]:
                is_group = False
                break
    if is_group:
        cnt += 1

print(cnt)

