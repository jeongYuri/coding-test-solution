import sys
input = sys.stdin.readline

t = int(input())
plager = [list(map(int,input().split())) for _ in range(t)]

scores = [0]*t

for game in range(3):
    current_game = [plager[i][game] for i in range(t)]
    freq = {}

    for num in current_game:
        freq[num] = freq.get(num,0)+1
    for i in range(t):
        num = plager[i][game]
        if freq[num]==1:
            scores[i]+= num
for score in scores:
    print(score)


