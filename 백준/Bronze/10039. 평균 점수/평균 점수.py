import sys
input = sys.stdin.readline

score = []
for _ in range(5):
    score.append(int(input()))
for i in range(5):
    if score[i]<40:
        score[i] = 40
print(sum(score)//5)
