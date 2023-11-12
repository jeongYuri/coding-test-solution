t = int(input())
grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
for tc in range(1,t+1):
    n, k = map(int,input().split())
    rank = []
    for _ in range(n):
        mid,final,hws = map(int,input().split())
        total = (mid * 0.35) + (final * 0.45) + (hws*0.2)
        rank.append(total)
    k_score = rank[k-1]
    rank.sort(reverse=True)
    div = n//10
    final_score = rank.index(k_score)//div
    print(f'#{tc} {grades[final_score]}')