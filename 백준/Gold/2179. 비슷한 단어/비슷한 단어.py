import sys
input = sys.stdin.readline

n = int(input())
words = [(input().strip(), i) for i in range(n)]
res = ''
answer = float('inf')

words.sort()
for i in range(n - 1):
    if words[i][0] == words[i + 1][0]:  #중복 단어 제거
        continue

    min_len = min(len(words[i][0]), len(words[i + 1][0]))
    min_idx = min(words[i][1], words[i + 1][1])

    j = 0
    while j < min_len and words[i][0][j] == words[i + 1][0][j]:
        j += 1

    if len(res) < j or (len(res) == j and min_idx < answer):
        res = words[i][0][:j]
        answer = min_idx 

answer_list = []
if res:
    for word, idx in words:
        if word[:len(res)] == res:
            answer_list.append((word, idx))
answer_list.sort(key=lambda x: x[1])
for word, _ in answer_list[:2]:
    print(word)
