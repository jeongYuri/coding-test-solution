from collections import Counter
for _ in range(1,11):
    tc = int(input())
    find = str(input())
    setence = list(str(input()))
    n= len(find)
    word = []
    for i in range(len(setence)-n+1):
        word.append("".join(setence[i:i+n]))
    if find in word:
        count = word.count(find)
    print(f'#{tc} {count}')