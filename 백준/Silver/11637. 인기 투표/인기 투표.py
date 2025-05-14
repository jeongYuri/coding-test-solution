def popularity_vote():
    n = int(input())
    votes = [int(input()) for _ in range(n)]
    max_vote = max(votes)
    if votes.count(max_vote) > 1:
        print("no winner")
        return
    idx = votes.index(max_vote) + 1  
    if max_vote > sum(votes) // 2:
        print(f"majority winner {idx}")
    else:
        print(f"minority winner {idx}")

T = int(input())
for _ in range(T):
    popularity_vote()
