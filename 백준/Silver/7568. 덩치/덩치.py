def calculate_rank(n, people):
    ranks = []
    for i in range(n):
        rank = 1
        for j in range(n):
            if i != j and people[i][0] < people[j][0] and people[i][1] < people[j][1]:
                rank += 1

        ranks.append(rank)

    return ranks

n = int(input())
people = []

for i in range(n):
    weight, height = map(int, input().split())
    people.append((weight, height))

ranks = calculate_rank(n, people)

# 결과 출력
for i in range(n):
    print(ranks[i],end=" ")
