from collections import Counter
def solution(want, number, discount):
    answer = 0
    want_dict = dict(zip(want, number))
    for i in range(len(discount)-9):
        days = discount[i:i+10]
        temp = Counter(days)
        if temp == want_dict:
            answer+=1
    return answer